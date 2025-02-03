#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    setmeup.main([])

    tabs = ["https://fastapi.tiangolo.com/tutorial/path-params/", "https://github.com/fastapi/fastapi/tree/master/docs_src/path_params/", "https://github.com/pflagerd/fastapi_learn_tutorial_user_guide/tree/main/path_params/tutorial001.py"]

    launcher = "chromium-browser"
    if not setmeup.spawn('which chromium-browser').returncode:
        subprocess.Popen([launcher, "--user-data-dir=/tmp/fastapi_learn_tutorial_user_guide", "--new-window"] + tabs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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

