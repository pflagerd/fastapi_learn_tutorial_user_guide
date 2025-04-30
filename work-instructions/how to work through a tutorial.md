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

6. In this example that would be `query-params-str-validations`.
7. Let's create a kind of mental variable name which we will call *new-tutorial-directory*. We will use this variable name to refer to this "suffix" (e.g. `query-params-str-validations`) later in this work instruction.
8. Read the tutorial until we encounter some code. Here's an old example:

     ![Image](https://github.com/user-attachments/assets/eab3c212-b07c-4818-a331-6033fd0af548)

9. In Chromium Instance 2, Tab 2, make a mental note of the part of the URL following `fastapi/docs_src`. e.g.
   ![image](https://github.com/user-attachments/assets/d66aaa2f-588b-4d68-85aa-65545b894325)

10. In this example that part is `query_params_str_validations/tutorial001_py310.py`.  Let's create another mental variable name called *old-tutorial-name* to refer to that part of the URL (in this case `query_params_str_validations/tutorial001_py310.py`)
11. From Chromium Instance 2, Tab 1, navigate to the *new-tutorial-directory* portion of *old-tutorial-name*. (e.g. `.../query_params_str_validations`).  Observe some .py files which might be the code we see above. Based on the number in name of the last directory (.e.g. tutorial003_py310.py contains the number 003), look for another with the next number in sequence (e.g. 004 in this case). Find the filename whose file contents match the code in the tutorial. Let's create yet another mental variable name to contain the filename we found: *new-tutorial-name*.  e.g. *new-tutorial-name* contains `query_params_str_validations/tutorial002_an_py310.py`
12.  From Konsole tab 3, press Ctrl-C to terminate the currently running *old-tutorial-name*
13.  Execute the following:
   ``` bash
     cd ../../ # fastapi_learn_tutorial_user_guide
     ./clone-tutorial *old-tutorial-name* *new-tutorial-name*
     cd *new-tutorial-name*
     ./RUNME
   ```
14. Observe that a new Chromium window appears with several tabs open:

     ![image](https://github.com/user-attachments/assets/b5097f1c-88b4-43a7-b31f-c56b0d0917ae)

15. Observe in konsole tab 3 that *new-tutorial-name* is running:

     ![image](https://github.com/user-attachments/assets/da4811c9-3576-47e0-9b4b-015b23fe2bfb)

16. From another konsole tab or from a kate terminal pane execute the following:
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
17. Terminate the konsole session. This will close all the open windows.
18. Rerun in a new konsole session as follows:
    ```
    cd .../david-and-dan
    ./RUNME
    ```
19. Observe that there are three Chromium instances as before, and a Konsole instance now with three tabs.
20. Observe that Konsole tab 3 is running *new-tutorial_name*
21. Observe that Chromium instance 2, Tab 1 is showing the new tutorial page.
22. Observe that Chromium instance 2, Tab 2 is showing *new-tutorial-name* under the fastapi repo directory `fastapi/docs_src/`.
23. Observe that Chromium instance 2, Tab 3 is showing *new-tutorial-name* under the `fastapi_learn_tutorial_user_guide/` directory
24. Observe that Chromium instance 3, Tab 2, shows `127.0.0.1:8000/docs` and when fully expanded shows the expected Parameters as defined in the tutorial's code.
25. Decide how to test the statements made in the tutorial. One test case is implied by the tutorial text:

     ![Image](https://github.com/user-attachments/assets/606eb18d-4328-40dd-94ea-e976e1aede61)

26. Now continue with Step 1 above.
