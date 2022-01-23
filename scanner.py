#!/usr/bin/env python3

from sys import path
from plyer import notification
from time import sleep
import argparse
import os


def check_and_notify(args, path_to_compare):
    os.system('sudo ./checkDiff.sh ' + path_to_compare)
    services_list = []
    ports_started = False

    input_file = open('scans/ndiffresults.txt', "rt")
    output_file = open('unwated_open_ports.txt', 'wt')

    for lin in input_file:
        line = lin.split()
        if not len(line):
            continue
        if line[0] == "PORT" or line[0] == "+PORT" or line[0] == "-PORT":
            ports_started = True
            services_list.append(line)
        if ports_started:
            if line[0][0] == '+':
                services_list.append(line)
                output_file.write(lin)
            elif line[0] == "-PORT" or line[0] == "PORT":
                output_file.write(lin)

    input_file.close()
    output_file.close()

    if len(services_list) > 1:
        notification.notify(
            title = "Otworzono porty niezgodne z zestawem wzorcowym!",
            message = "Sprawdź plik unwated_open_ports.txt",
            app_icon = "icons/warning-icon.png", 
            timeout = args.time
        )


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-c",
        "--continuous",
        action = "store_true",
        dest = "continuous",
        help = "Continuous working" 
    )
    arg_parser.add_argument(
        "-s",
        "--sleep",
        type = int,
        default = 60,
        dest = "sleep",
        help = "Time between checks" 
    )
    arg_parser.add_argument(
        "-t",
        "--time",
        type = int,
        default = 20,
        dest = "time",
        help = "Time of notification visible" 
    )
    arg_parser.add_argument(
        "-p",
        "--path",
        type = str,
        default = 'scans/testscan.xml',
        dest = "path",
        help = "Path to compare file" 
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    if args.continuous:
        while(True):
            check_and_notify(args, args.path)
            sleep(args.sleep)
    else:
        check_and_notify(args, args.path)

