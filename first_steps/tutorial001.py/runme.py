#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    setmeup.main([])

    import tempfile
    user_data_dir=tempfile.mktemp()

    launcher = "chromium-browser"
    if not setmeup.spawn('which chromium-browser').returncode:
        print(f"user_data_dir == \"{user_data_dir}\"")
        subprocess.Popen([launcher, "--user-data-dir=/tmp/" + user_data_dir, "--new-window", "http://127.0.0.1:8000", "http://127.0.0.1:8000/docs", "http://127.0.0.1:8000/redoc", "http://127.0.0.1:8000/openapi.json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        if not setmeup.spawn('which open').returncode:
            launcher = "open"
        elif not setmeup.spawn('which gio').returncode:
            launcher = "gio"
        else:
            print('Neither chromium-browser, open nor gio is available in your PATH, cannot launch default browser', file=sys.stderr)

        subprocess.Popen([launcher, "http://127.0.0.1:8000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    os.execvp(".venv/bin/fastapi", [".venv/bin/fastapi", "dev", "main.py"])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

