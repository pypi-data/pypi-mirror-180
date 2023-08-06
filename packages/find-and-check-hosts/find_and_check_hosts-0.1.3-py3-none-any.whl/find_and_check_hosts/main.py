import argparse
import csv
import logging
import os
import traceback
from typing import Any
#  local files
from .checker import FileChecker
from .rules import load_rule_file
from .patterns import IP_REGEX, CSV_HEADER, HOSTNAME_REGEX, should_check_file, determine_statuses_to_show


def parse_cli_arguments() -> Any:
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="enable additional debugging outpust (like the used regexes)")
    # subcommands = ap.add_subparsers(dest="cmd", required=True)

    # search = subcommands.add_parser("search", description="search files for the IP addresses and hostnames")
    search = ap
    search.add_argument("root_dir", help="directory that will be recursively searched for files containing IPv4 addresses and hostnames")
    search.add_argument("-c", "--config", help="the config file with the rules, that will be used for the IPv4 and hostname classification")
    search.add_argument("--csv", metavar="output_file", help="write the results as a CSV to the given file")
    group_status = search.add_argument_group("Filter by status")
    group_show_hide = group_status.add_mutually_exclusive_group()
    group_show_hide.add_argument("-s", "--show", help="only shows entries with the given statuses. Multiple values can be passed using comas (example: 'warn,bad')")
    group_show_hide.add_argument("-S", "--hide", help="shows all entries that do NOT match the given statuses. Multiple values can be passed using comas (example: 'ok,warn')")
    group_exit_pretty = search.add_argument_group("Exit code")
    group_exit = group_exit_pretty.add_mutually_exclusive_group()
    group_exit.add_argument("-r", "--assert-results", action="store_true", help="exit with an error status if no results are returned")
    group_exit.add_argument("-R", "--assert-no-results", action="store_true", help="exit with an error status if any results are returned")

    # replace = subcommands.add_parser("replace", description="search and replace IP addresses and hostnames")
    # replace.add_argument("root_dir", help="directory that will be recursively searched for files containing potential leaks")
    # replace.add_argument("-c", "--config", required=True, help="the config file with the rules, that will be used for the IP and hostname classification")


    return ap.parse_args()



def main():
    args = parse_cli_arguments()

    if args.debug:
        logging.basicConfig(format="[%(levelname)s] %(message)s",level=logging.DEBUG)

    logging.debug("IP search regex: %s", IP_REGEX.pattern)
    logging.debug("Hostname search regex: %s", HOSTNAME_REGEX.pattern)

    _main_search(args)
    # if args.cmd == "search":
    #     _main_search(args)
    # elif args.cmd == "replace":
    #      _main_replace(args)


def _main_search(args):
    if args.config:
        config_path = args.config
    else:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(script_dir, "example-config.yaml")
    config = load_rule_file(config_path)

    show_status_list = determine_statuses_to_show(args.show, args.hide)

    file_checker = FileChecker(config, show_status_list, bool(args.csv))

    root_dir = args.root_dir
    if not os.path.isdir(root_dir):
        raise Exception(f"'{root_dir}' is not an existing directory")
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for name in file_names:
            path = os.path.join(dir_path, name)
            if should_check_file(path):
                try:
                    file_checker.check_file(path)
                except Exception:
                    print(f"[ERROR] Error while checking '{path}'")
                    traceback.print_exc()
    
    file_checker.print_summary()

    if args.csv:
        with open(args.csv, 'w') as csvfile: 
            writer = csv.writer(csvfile) 

            writer.writerow(CSV_HEADER)                
            for row in file_checker.csv_data:
                writer.writerow(row)
        print(f"Written results as CSV to '{args.csv}'")

    has_results = file_checker.has_results()
    if args.assert_results and not has_results:
        # Expected results but got none
        exit(1)
    elif args.assert_no_results and has_results:
        # Expected to find nothing, but found something
        exit(1)


def _main_replace(args):
    pass
