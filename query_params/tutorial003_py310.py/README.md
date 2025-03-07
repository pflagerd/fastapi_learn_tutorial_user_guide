# fastapi_learn_tutorial_user_guide/query_params/tutorial003_py310.py/README.md

This repository contains artifacts generated when David and Dan (D&D) executed the tutorial at [FastAPI > Learn > Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial).

<br>

## TODO
   DONE

<br>

## Setup
You must have python3 and git.

| OS | git | python3 |
| -------- | -------- | -------- |
| kubuntu 24.04.1 LTS   | 2.43.0, 2.45.2   | Python 3.12.3   |
| kubuntu 24.10   | 2.45.2   | Python 3.12.7   |
| macOS Sequoia 15.1.1   | 2.39.5 (Apple Git-154)   | Python 3.12.7   |

Git clone current repo to your local machine

​	`git clone https://github.com/pflagerd/fastapi_learn_tutorial_user_guide.git`

Change your working directory to fastapi_learn_tutorial_user_guide repository

​	`cd path/to/fastapi_learn_tutorial_user_guide/query_params/tutorial003_py310.py`

Type

 ```commandline
./RUNME
```

In the shell from which you just executed `./RUNME` you should see something like:
```
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from
             /home/oy753c/desktops/neon-algorithms/david-and-dan/fastapi_learn_tutorial_user_guide/query_params/tutorial003_py310.py

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories:
             ['/home/oy753c/desktops/neon-algorithms/david-and-dan/fastapi_learn_tutorial_user_guide/query_params/tutorial003_py310.py
             ']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [44912] using WatchFiles
      INFO   Started server process [45525]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
      INFO   127.0.0.1:58876 - "GET /items/foo?short=0 HTTP/1.1" 200
      INFO   127.0.0.1:58876 - "GET /favicon.ico HTTP/1.1" 404
```

In a new browser window or tab, you should see something like this:

![Image](https://github.com/user-attachments/assets/723074cd-a57a-4b8e-b97a-45b0b7b6078e)
