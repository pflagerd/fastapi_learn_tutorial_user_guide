#!/usr/bin/env python3
import distro
import os
import os.path
import platform
import subprocess
import sys
import time
from types import SimpleNamespace


def has_apt():
    return not spawn("which apt").returncode


def if_package_not_installed_install_it_now(package):
    if not has_apt():
        raise RuntimeError("This script has only been tested on systems with the apt package manager.")

    # is package installed?
    # Do something like this bash command: sudo apt list --installed | grep python3-venv3
    if package in spawn("sudo apt list --installed").stdout:
        return

    response = spawn(f"sudo apt install {package} -y")
    if response.returncode:
        raise RuntimeError("Something went wrong: " + response.stderr)


def main(args, debug=False):
    supported_python_versions = [(3, 11, 2), (3, 12, 3), (3, 12, 7), (3, 13, 0)]
    if (sys.version_info.major, sys.version_info.minor, sys.version_info.micro) not in supported_python_versions:
        print("Current version " + sys.version.split()[0] + " not tested.  Must be one of " + version_info_tuple_to_str(supported_python_versions), file=sys.stderr)
        sys.exit(1)

    if debug:
        print(__file__)
        print(os.path.abspath(__file__))

    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    if debug:
        print(script_directory)  # Does script_directory contain a trailing '/'?  No.

    if_package_not_installed_install_it_now("python3-pip")
    if_package_not_installed_install_it_now("python3-venv")

    if not os.path.exists(script_directory + "/.venv"):  # if
        spawn_result = spawn("python3 -m venv .venv")
        if spawn_result.returncode:
            raise RuntimeError("python3 -m venv .venv failed: " + spawn_result.stderr)
        if debug:
            print(spawn_result)

    stdout = spawn(".venv/bin/pip freeze").stdout
    if debug:
        print(f'stdout == {stdout}')

    if not stdout:
        spawn_result = spawn(".venv/bin/pip install -r requirements.txt")
        if debug:
            print(spawn_result)


def spawn(command_line):
    process = subprocess.run(
        command_line.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return SimpleNamespace(
        stdout=process.stdout.decode('utf-8'),
        stderr=process.stderr.decode('utf-8'),
        returncode=process.returncode
    )


def version_info_tuple_to_str(version_info_tuple):
    s = ""
    for version_info in version_info_tuple:
        if s:
            s += ", "
        s += str(version_info[0]) + "." + str(version_info[1]) + "." + str(version_info[2])
    return s


if __name__ == "__main__":
    sys.exit(main(sys.argv))

