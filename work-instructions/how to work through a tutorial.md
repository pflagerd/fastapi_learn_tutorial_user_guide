1. From Chromium Instance 2, Tab 1, navigate to the next tutorial or the next chunk of the current tutorial (based on the existence of the sub-title font).
     <br><br>e.g. the sub-title font will look something like this (different text)

     ![Image](https://github.com/user-attachments/assets/87a516aa-6cf3-4bd5-a5a3-f9e01148cadb)

2. Hover over the icon to the right of the title as shown:

   ![image](https://github.com/user-attachments/assets/d0c091d0-896d-4da8-86fc-cbdf74ef3ecd)

3. Right click, and choose "Copy Link Address" to capture a link which can be used to update fastapi_learn_tutorial_user_guide/RUNME to show the correct tutorial in Chromium Instance 2, Tab 1.

   ![image](https://github.com/user-attachments/assets/c0e91164-3fb3-404e-8c75-0231a503e352)

   Notice that in this case the link copied was `https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-more-validations`

4. Using Kate (or another editor) Tab 2 edit `fastapi_learn_tutorial_user_guide/RUNME`, replacing the first link on line 11 with the copied link:

   ![image](https://github.com/user-attachments/assets/da7f2b20-b8ce-4584-88f4-3982b54f4575)
   
5. Look at Chromium Instance 2, Tab 1 again and observe the portion of the URL preceding the "#". e.g.
   ![image](https://github.com/user-attachments/assets/c56a6bcc-e8bc-42fc-82ce-3b0f641607e5)

     In this example that would be `query-params-str-validations`.
6. Let's create a kind of mental variable name which we will call *new-tutorial-directory*. We will use this variable name to refer to this portion (e.g. `query-params-str-validations`) later in this work instruction.
7. Read the tutorial until we encounter some code. Here's an old example:

     ![Image](https://github.com/user-attachments/assets/eab3c212-b07c-4818-a331-6033fd0af548)

8. In Chromium Instance 2, Tab 2, make a mental note of the part of the URL following `fastapi/docs_src`. e.g.
   ![image](https://github.com/user-attachments/assets/d66aaa2f-588b-4d68-85aa-65545b894325)

9. In this example that part is `query_params_str_validations/tutorial001_py310.py`.  Let's create another mental variable name called *old-tutorial-name* to refer to that part of the URL (in this case `query_params_str_validations/tutorial001_py310.py`)
10. From Chromium Instance 2, Tab 2, navigate to *new-tutorial-directory*. (e.g. `.../query_params_str_validations`).  Observe some .py filenames whose contents might be the code we see above. Find the filename whose contents match the code in the tutorial. Let's create yet another mental variable name to contain the filename we found: *new-tutorial-name*.  e.g. *new-tutorial-name* contains `query_params_str_validations/tutorial002_an_py310.py`

10. NOTE: both *old-tutorial-name* and *new-tutorial-name* should contain two path elements: `query_params_str_validations/tutorial002_an_py310.py` `query_params_str_validations` and `tutorial002_an_py310.py`
    
11.  From Konsole tab 3, press Ctrl-C to terminate the currently running *old-tutorial-name*
12.  Execute the following:
   ``` bash
     cd ../../ # fastapi_learn_tutorial_user_guide
     ./clone-tutorial *old-tutorial-name* *new-tutorial-name*
     cd *new-tutorial-name*
     ./RUNME
   ```
13. Observe that a new Chromium window appears with several tabs open:

     ![image](https://github.com/user-attachments/assets/b5097f1c-88b4-43a7-b31f-c56b0d0917ae)

14. Observe in konsole tab 3 that *new-tutorial-name* is running:

     ![image](https://github.com/user-attachments/assets/da4811c9-3576-47e0-9b4b-015b23fe2bfb)

15. From another konsole tab or from a kate terminal pane execute the following:
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
16. Terminate the konsole session. This will close all the open windows.
17. Rerun in a new konsole session as follows:
    ```
    cd .../david-and-dan
    ./RUNME
    ```
18. Observe that there are three Chromium instances as before, and a Konsole instance now with three tabs.
19. Observe that Konsole tab 3 is running *new-tutorial-name*
20. Observe that Chromium instance 2, Tab 1 is showing the new tutorial page.
21. Observe that Chromium instance 2, Tab 2 is showing *new-tutorial-name* under the fastapi repo directory [`fastapi/docs_src/`](https://github.com/fastapi/fastapi/blob/master/docs_src/).
22. Observe that Chromium instance 2, Tab 3 is showing *new-tutorial-name* under the `[fastapi_learn_tutorial_user_guide/](https://github.com/pflagerd/fastapi_learn_tutorial_user_guide/tree/master/)` directory
23. Observe that Chromium instance 3, Tab 2, shows `127.0.0.1:8000/docs` and when fully expanded shows the expected Parameters as defined in the tutorial's code.
24. Decide how to test the statements made in the tutorial. One test case is implied by the tutorial text:

     ![Image](https://github.com/user-attachments/assets/606eb18d-4328-40dd-94ea-e976e1aede61)

25. Now continue with Step 1 above.
