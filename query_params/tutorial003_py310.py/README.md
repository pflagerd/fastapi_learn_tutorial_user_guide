# fastapi_learn_tutorial_user_guide/query_params/tutorial002_py310.pyREADME.md

This repository contains artifacts generated when David and Dan (D&D) executed the tutorial at [FastAPI > Learn > Tutorial - User Guide > First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/).

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

​	`cd path/to/fastapi_learn_tutorial_user_guide/query_params/tutorial002_py310.py`

Type

 ```commandline
./RUNME
```

In the shell from which you just executed `./RUNME` you should see something like:
```
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from
             /home/oy753c/desktops/neon-algorithms/fastapi_learn_tutorial_user_guide/path_params/tutorial004.py

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories:
             ['/home/oy753c/desktops/neon-algorithms/fastapi_learn_tutorial_user_guide/path_params/tutorial004.py']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [137565] using WatchFiles
      INFO   Started server process [137787]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
      INFO   127.0.0.1:35806 - "GET /items/3 HTTP/1.1" 404
      INFO   127.0.0.1:35806 - "GET /favicon.ico HTTP/1.1" 404
      INFO   127.0.0.1:35816 - "GET / HTTP/1.1" 404
      INFO   127.0.0.1:35816 - "GET /docs HTTP/1.1" 200
      INFO   127.0.0.1:35816 - "GET /openapi.json HTTP/1.1" 200
      INFO   127.0.0.1:42600 - "GET /redoc HTTP/1.1" 200
      INFO   127.0.0.1:42600 - "GET /openapi.json HTTP/1.1" 200
      INFO   127.0.0.1:42600 - "GET /openapi.json HTTP/1.1" 200
```

In a new browser window or tab, you should see something like this:

![Image](https://github.com/user-attachments/assets/24e4f39a-13ba-4e21-b738-b3db2cc9c834)
