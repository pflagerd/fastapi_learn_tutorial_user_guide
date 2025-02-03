#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    setmeup.main([])

    tabs = ["http://127.0.0.1:8000", "http://127.0.0.1:8000/docs", "http://127.0.0.1:8000/redoc", "http://127.0.0.1:8000/openapi.json"]

    launcher = "chromium-browser"
    if not setmeup.spawn('which chromium-browser').returncode:
        subprocess.Popen([launcher, "--user-data-dir=" + os.getcwd() + "/.chromium-browser", "--new-window"] + tabs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        if not setmeup.spawn('which open').returncode:
            launcher = "open"
        elif not setmeup.spawn('which gio').returncode:
            launcher = "gio"
        else:
            print('Neither chromium-browser, open nor gio is available in your PATH, cannot launch default browser', file=sys.stderr)

        for tab in tabs:
            subprocess.Popen([launcher, tab], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    os.execvp(".venv/bin/fastapi", [".venv/bin/fastapi", "dev", "main.py"])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

