#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    launcher = "chromium-browser"
    if setmeup.spawn('which chromium-browser').returncode:
        raise RuntimeError("This script requires chromium-browser to be installed")

    if os.path.exists("./main.py"):
        subprocess.Popen([launcher, "--user-data-dir=" + os.getcwd() + "/.chromium-browser", "--new-window"] + args[1:], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.execvp(".venv/bin/fastapi", [".venv/bin/fastapi", "dev", "main.py"])
    else:
        os.execvp(launcher, [launcher, "--user-data-dir=" + os.getcwd() + "/.chromium-browser", "--new-window"] + args[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

