#!python
# Licensed under the MIT License

import argparse
import re
import fileinput
import os

def main():
    print("Auto NMAP IPs by Reboot-Codes v1.0.0")

    parser = argparse.ArgumentParser(description="Automatically run NMAP on a list of IP addresses from a file")
    parser.add_argument("filename", nargs='?', type=str, help="The path (relative to CWD) to the file containing IP addresses, or will read from STDIN")

    args = parser.parse_args()
    filename = args.filename
    ips = []

    if filename and len(filename) > 0:
        if os.path.isfile(filename):
            try:
                with open(filename, "r") as file:
                    for line in file.read().splitlines():
                        ips.append(line.strip())
            except:
                print(f"Error reading: {filename}, exiting...")
    else:
        for line in fileinput.input():
            line
            ips.append(line.strip())

    for ipaddr in ips:
        os.system(f"nmap -sC -sV {ipaddr} -oN {ipaddr}.txt --unprivileged")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")

