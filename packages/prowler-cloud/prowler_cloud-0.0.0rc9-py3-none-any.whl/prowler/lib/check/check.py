import functools
import importlib
import os
import sys
from pkgutil import walk_packages
from types import ModuleType

from alive_progress import alive_bar
from colorama import Fore, Style
from lib.check.compliance_models import load_compliance_framework
from lib.check.models import Check, Output_From_Options, load_check_metadata
from lib.logger import logger
from lib.outputs.outputs import report
from lib.utils.utils import open_file, parse_json_file
from providers.aws.lib.audit_info.models import AWS_Audit_Info

from config.config import compliance_specification_dir, orange_color


# Load all checks metadata
def bulk_load_checks_metadata(provider: str) -> dict:
    bulk_check_metadata = {}
    checks = recover_checks_from_provider(provider)
    # Build list of check's metadata files
    for check_name in checks:
        # Build check path name
        check_path_name = check_name.replace(".", "/")
        # Append metadata file extension
        metadata_file = f"prowler/{check_path_name}.metadata.json"
        # Load metadata
        check_metadata = load_check_metadata(metadata_file)
        bulk_check_metadata[check_metadata.CheckID] = check_metadata

    return bulk_check_metadata


# Bulk load all compliance frameworks specification
def bulk_load_compliance_frameworks(provider: str) -> dict:
    """Bulk load all compliance frameworks specification into a dict"""
    bulk_compliance_frameworks = {}
    compliance_specification_dir_path = f"{compliance_specification_dir}/{provider}"
    try:
        for filename in os.listdir(compliance_specification_dir_path):
            file_path = os.path.join(compliance_specification_dir_path, filename)
            # Check if it is a file
            if os.path.isfile(file_path):
                # Open Compliance file in JSON
                # cis_v1.4_aws.json --> cis_v1.4_aws
                compliance_framework_name = filename.split(".json")[0]
                # Store the compliance info
                bulk_compliance_frameworks[
                    compliance_framework_name
                ] = load_compliance_framework(file_path)
    except Exception as e:
        logger.error(f"{e.__class__.__name__} -- {e}")

    return bulk_compliance_frameworks


# Exclude checks to run
def exclude_checks_to_run(checks_to_execute: set, excluded_checks: list) -> set:
    for check in excluded_checks:
        checks_to_execute.discard(check)
    return checks_to_execute


# Exclude services to run
def exclude_services_to_run(
    checks_to_execute: set, excluded_services: list, provider: str
) -> set:
    # Recover checks from the input services
    for service in excluded_services:
        modules = recover_checks_from_provider(provider, service)
        if not modules:
            logger.error(f"Service '{service}' was not found for the AWS provider")
        else:
            for check_module in modules:
                # Recover check name and module name from import path
                # Format: "providers.{provider}.services.{service}.{check_name}.{check_name}"
                check_name = check_module.split(".")[-1]
                # Exclude checks from the input services
                checks_to_execute.discard(check_name)
    return checks_to_execute


# Load checks from checklist.json
def parse_checks_from_file(input_file: str, provider: str) -> set:
    checks_to_execute = set()
    f = open_file(input_file)
    json_file = parse_json_file(f)

    for check_name in json_file[provider]:
        checks_to_execute.add(check_name)

    return checks_to_execute


def list_services(provider: str) -> set():
    available_services = set()
    checks = recover_checks_from_provider(provider)
    for check_name in checks:
        # Format: "providers.{provider}.services.{service}.{check_name}.{check_name}"
        service_name = check_name.split(".")[3]
        available_services.add(service_name)
    return sorted(available_services)


def list_categories(provider: str, bulk_checks_metadata: dict) -> set():
    available_categories = set()
    for check in bulk_checks_metadata.values():
        for cat in check.Categories:
            available_categories.add(cat)
    return available_categories


def print_categories(categories: set):
    print(
        f"There are {Fore.YELLOW}{len(categories)}{Style.RESET_ALL} available categories: \n"
    )
    for category in categories:
        print(f"- {category}")


def print_services(service_list: set):
    print(
        f"There are {Fore.YELLOW}{len(service_list)}{Style.RESET_ALL} available services: \n"
    )
    for service in service_list:
        print(f"- {service}")


def print_compliance_frameworks(
    bulk_compliance_frameworks: dict,
):
    print(
        f"There are {Fore.YELLOW}{len(bulk_compliance_frameworks.keys())}{Style.RESET_ALL} available Compliance Frameworks: \n"
    )
    for framework in bulk_compliance_frameworks.keys():
        print(f"\t- {Fore.YELLOW}{framework}{Style.RESET_ALL}")


def print_compliance_requirements(
    bulk_compliance_frameworks: dict, compliance_framework: str
):
    for compliance in bulk_compliance_frameworks.values():
        # Workaround until we have more Compliance Frameworks
        split_compliance = compliance_framework.split("_")
        framework = split_compliance[0].upper()
        version = split_compliance[1].upper()
        provider = split_compliance[2].upper()
        if compliance.Framework == framework and compliance.Version == version:
            print(
                f"Listing {framework} {version} {provider} Compliance Requirements:\n"
            )
            for requirement in compliance.Requirements:
                checks = ""
                for check in requirement.Checks:
                    checks += f" {Fore.YELLOW}\t\t{check}\n{Style.RESET_ALL}"
                print(
                    f"Requirement Id: {Fore.MAGENTA}{requirement.Id}{Style.RESET_ALL}\n\t- Description: {requirement.Description}\n\t- Checks:\n{checks}"
                )


def print_checks(
    provider: str,
    check_list: set,
    bulk_checks_metadata: dict,
):
    for check in check_list:
        try:
            print(
                f"[{bulk_checks_metadata[check].CheckID}] {bulk_checks_metadata[check].CheckTitle} - {Fore.MAGENTA}{bulk_checks_metadata[check].ServiceName} {Fore.YELLOW}[{bulk_checks_metadata[check].Severity}]{Style.RESET_ALL}"
            )
        except KeyError as error:
            logger.critical(
                f"Check {error} was not found for the {provider.upper()} provider"
            )
            sys.exit()

    print(
        f"\nThere are {Fore.YELLOW}{len(check_list)}{Style.RESET_ALL} available checks.\n"
    )


# Parse checks from compliance frameworks specification
def parse_checks_from_compliance_framework(
    compliance_frameworks: list, bulk_compliance_frameworks: dict
) -> list:
    """Parse checks from compliance frameworks specification"""
    checks_to_execute = set()
    try:
        for framework in compliance_frameworks:
            # compliance_framework_json["Requirements"][*]["Checks"]
            compliance_framework_checks_list = [
                requirement.Checks
                for requirement in bulk_compliance_frameworks[framework].Requirements
            ]
            # Reduce nested list into a list
            # Pythonic functional magic
            compliance_framework_checks = functools.reduce(
                lambda x, y: x + y, compliance_framework_checks_list
            )
            # Then union this list of checks with the initial one
            checks_to_execute = checks_to_execute.union(compliance_framework_checks)
    except Exception as e:
        logger.error(f"{e.__class__.__name__}[{e.__traceback__.tb_lineno}] -- {e}")

    return checks_to_execute


# Recover all checks from the selected provider and service
def recover_checks_from_provider(provider: str, service: str = None) -> list:
    try:
        checks = []
        modules = list_modules(provider, service)
        for module_name in modules:
            # Format: "providers.{provider}.services.{service}.{check_name}.{check_name}"
            check_name = module_name.name
            # We need to exclude common shared libraries in services
            if (
                check_name.count(".") == 5
                and "lib" not in check_name
                and "test" not in check_name
            ):
                checks.append(check_name)
        return checks
    except Exception as e:
        logger.critical(f"{e.__class__.__name__}[{e.__traceback__.tb_lineno}]: {e}")
        sys.exit()


# List all available modules in the selected provider and service
def list_modules(provider: str, service: str):
    module_path = f"providers.{provider}.services"
    if service:
        module_path += f".{service}"
    return walk_packages(
        importlib.import_module(module_path).__path__,
        importlib.import_module(module_path).__name__ + ".",
    )


# Import an input check using its path
def import_check(check_path: str) -> ModuleType:
    lib = importlib.import_module(f"{check_path}")
    return lib


# Sets the Output_From_Options to be used in the output modes
def set_output_options(
    quiet: bool,
    output_modes: list,
    input_output_directory: str,
    security_hub_enabled: bool,
    output_filename: str,
    allowlist_file: str,
    bulk_checks_metadata: dict,
    verbose: bool,
):
    """Sets the Output_From_Options to be used in the output modes"""
    global output_options
    output_options = Output_From_Options(
        is_quiet=quiet,
        output_modes=output_modes,
        output_directory=input_output_directory,
        security_hub_enabled=security_hub_enabled,
        output_filename=output_filename,
        allowlist_file=allowlist_file,
        bulk_checks_metadata=bulk_checks_metadata,
        verbose=verbose,
        # set input options here
    )
    return output_options


def run_check(check: Check, output_options: Output_From_Options) -> list:
    findings = []
    if output_options.verbose or output_options.is_quiet:
        print(
            f"\nCheck ID: {check.CheckID} - {Fore.MAGENTA}{check.ServiceName}{Fore.YELLOW} [{check.Severity}]{Style.RESET_ALL}"
        )
    logger.debug(f"Executing check: {check.CheckID}")
    try:
        findings = check.execute()
    except Exception as error:
        print(f"Something went wrong in {check.CheckID}, please use --log-level ERROR")
        logger.error(
            f"{check.CheckID} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
        )
    finally:
        return findings


def execute_checks(
    checks_to_execute: list,
    provider: str,
    audit_info: AWS_Audit_Info,
    audit_output_options: Output_From_Options,
) -> list:
    all_findings = []
    print(
        f"{Style.BRIGHT}Executing {len(checks_to_execute)} checks, please wait...{Style.RESET_ALL}\n"
    )
    with alive_bar(
        total=len(checks_to_execute),
        ctrl_c=False,
        bar="blocks",
        spinner="classic",
        stats=False,
        enrich_print=False,
    ) as bar:
        for check_name in checks_to_execute:
            # Recover service from check name
            service = check_name.split("_")[0]
            bar.title = f"-> Scanning {orange_color}{service}{Style.RESET_ALL} service"
            try:
                # Import check module
                check_module_path = (
                    f"providers.{provider}.services.{service}.{check_name}.{check_name}"
                )
                lib = import_check(check_module_path)
                # Recover functions from check
                check_to_execute = getattr(lib, check_name)
                c = check_to_execute()
                # Run check
                check_findings = run_check(c, audit_output_options)
                all_findings.extend(check_findings)
                report(check_findings, audit_output_options, audit_info)
                bar()

            # If check does not exists in the provider or is from another provider
            except ModuleNotFoundError:
                logger.critical(
                    f"Check '{check_name}' was not found for the {provider.upper()} provider"
                )
                bar.title = f"-> {Fore.RED}Scan was aborted!{Style.RESET_ALL}"
                sys.exit()
            except Exception as error:
                logger.error(
                    f"{error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
                )
        bar.title = f"-> {Fore.GREEN}Scan is completed!{Style.RESET_ALL}"
    return all_findings
