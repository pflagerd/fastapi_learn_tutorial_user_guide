[Required Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters)


1. From Chromium Instance 2, Tab 1, navigate to the next tutorial or the next chunk of the current tutorial (based on the existence of the sub-title font).
     <br><br>e.g. the sub-title font will look something like this (different text)

     ![Image](https://github.com/user-attachments/assets/87a516aa-6cf3-4bd5-a5a3-f9e01148cadb)

2. Observe that the name of the URL for the current tutorial has a "suffix". e.g.
   ![image](https://github.com/user-attachments/assets/ab2f3d0c-4f49-4513-a528-653dda557eea)

3. In this example, the "suffix" is `query-params-str-validations`.
4. Let's create a kind of mental variable name which we will call *new-tutorial-directory*. We will use this variable name to refer to this "suffix" (e.g. `query-params-str-validations`) later in this work instruction.
5. Update fastapi_learn_tutorial_user_guide/RUNME to show the correct tutorial in Chromium Instance 2, Tab 1.
6. Read the tutorial until we encounter some code. Here's an old example:

     ![Image](https://github.com/user-attachments/assets/eab3c212-b07c-4818-a331-6033fd0af548)

7. In Chromium Instance 2, Tab 2, make a mental note of the part of the URL following `fastapi/docs_src`. e.g.
   ![image](https://github.com/user-attachments/assets/d66aaa2f-588b-4d68-85aa-65545b894325)

8. In this example that part is `query_params_str_validations/tutorial001_py310.py`.  Let's create another mental variable name called *old-tutorial-name* to refer to that part of the URL (in this case `query_params_str_validations/tutorial001_py310.py`)
9. TODO (FIX THIS STEP). From Chromium Instance 2, Tab 1, navigate to the top-level directory portion of *old-tutorial-name*. (e.g. `.../query_params_str_validations`).  Observe some .py files which might be the code we see above. Based on the number in name of the last directory (.e.g. tutorial003_py310.py contains the number 003), look for another with the next number in sequence (e.g. 004 in this case). Find the filename whose file contents match the code in the tutorial. Let's create yet another mental variable name to contain the filename we found: *new-tutorial-name*.  e.g. *new-tutorial-name* contains `query_params_str_validations/tutorial002_an_py310.py`
10.  From Konsole tab 3, press Ctrl-C to terminate the currently running *old-tutorial-name*
11.  Execute the following:
   ``` bash
     cd ../../ # fastapi_learn_tutorial_user_guide
     ./clone-tutorial *old-tutorial-name* *new-tutorial-name*
     cd query_params/tutorial005.py
     ./RUNME
   ```
11. Observe that a new Chrome window appears with several tabs open:

     ![image](https://github.com/user-attachments/assets/b5097f1c-88b4-43a7-b31f-c56b0d0917ae)

12. Observe in konsole tab 3 that *new-tutorial-name* is running:

     ![image](https://github.com/user-attachments/assets/da4811c9-3576-47e0-9b4b-015b23fe2bfb)

13. From another konsole tab or from a kate terminal pane execute the following:
    ```bash
     cd ../../../ # david-and-dan
     git add .
     git commit -m "new tutorial"
     git push
     cd fastapi_learn_tutorial_user_guide
     git add .
     git commit -m "new tutorial"
     git push
    ```
14. Terminate the konsole session. This will close all the open windows.
15. Rerun in a new konsole session as follows:
    ```
    cd .../david-and-dan
    ./RUNME
    ```
16. Observe that there are three Chromium instances as before, and a Konsole instance now with three tabs.
17. Observe that Konsole tab 3 is running *new-tutorial_name*
18. Observe that Chromium instance 2, Tab 1 is showing the new tutorial page.
19. Observe that Chromium instance 2, Tab 2 is showing *new-tutorial-name* under the fastapi repo directory `fastapi/docs_src/`.
20. Observe that Chromium instance 2, Tab 3 is showing *new-tutorial-name* under the `fastapi_learn_tutorial_user_guide/` directory
21. Observe that Chromium instance 3, Tab 2, shows `127.0.0.1:8000/docs` and when fully expanded shows the expected Parameters as defined in the tutorial's code.
22. Decide how to test the statements made in the tutorial. One test case is implied by the tutorial text:

     ![Image](https://github.com/user-attachments/assets/606eb18d-4328-40dd-94ea-e976e1aede61)

23. Now continue with Step 1 above.
