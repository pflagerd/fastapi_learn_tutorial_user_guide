[Required Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters)


1. From Chromium Instance 2, Tab 1, navigate to the next tutorial or the next chunk of the current tutorial (based on the existence of the sub-title font).
     <br><br>e.g. the sub-title font looks like this (different text)

     ![Image](https://github.com/user-attachments/assets/87a516aa-6cf3-4bd5-a5a3-f9e01148cadb)

2. Update fastapi_learn_tutorial_user_guide/RUNME to show the correct tutorial in Chromium Instance 2, Tab 1.
3. Read the tutorial until we encounter some code:

     ![Image](https://github.com/user-attachments/assets/eab3c212-b07c-4818-a331-6033fd0af548)

4. In Chromium Instance 2, Tab2, navigate to https://github.com/fastapi/fastapi/blob/master/docs_src/query_params.  Observe some .py files which might be the code we see above. By inspection we determine that the file we want is tutorial005.py
5.  From Konsole tab 3, press Ctrl-C to terminate the currently running app: tutorial004_py310.py
6.  Execute the following:
   ``` bash
     cd ../../ # fastapi_learn_tutorial_user_guide
     ./clone-tutorial query_params/tutorial004_py310.py query_params/tutorial005.py
     cd query_params/tutorial005.py
     ./RUNME
   ```
7. Observe that a new Chrome window appears with several tabs open:

     ![image](https://github.com/user-attachments/assets/b5097f1c-88b4-43a7-b31f-c56b0d0917ae)

8. Observe in konsole tab 3 that `query_params/tutorial005.py` is running:

     ![image](https://github.com/user-attachments/assets/da4811c9-3576-47e0-9b4b-015b23fe2bfb)

9. Decide how to test the statements made in the tutorial. One test case is implied by the tutorial text:

     ![Image](https://github.com/user-attachments/assets/606eb18d-4328-40dd-94ea-e976e1aede61)

10. From another konsole tab, or from a kate terminal pane execute the following:
    ```bash
     cd ../ # david-and-dan
     git add .
     git commit -m "new tutorial"
     git push
     cd fastapi_learn_tutorial_user_guide
     git add .
     git commit -m "new tutorial"
     git push
    ```
11. Terminate the konsole session. This will close all the open windows.
12. Rerun in a new konsole session as follows:
    ```
    cd .../david-and-dan
    ./RUNME
    ```
13. If there are any missing things, fix them.
14. Now continue with Step 1 above.
