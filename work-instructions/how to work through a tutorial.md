1. From Chromium Instance 2, Tab 1, navigate to the next tutorial or the next chunk of the current tutorial (sometimes based on the existence of the sub-title font).
     <br><br>e.g. the sub-title font will look something like this (different text)

     ![Image](https://github.com/user-attachments/assets/87a516aa-6cf3-4bd5-a5a3-f9e01148cadb)

2. Hover over the icon to the right of the title as shown, right click, and choose "Copy Link Address" to capture a link which we will later use to update fastapi_learn_tutorial_user_guide/RUNME to show the correct tutorial in Chromium Instance 2, Tab 1.

   ![image](https://github.com/user-attachments/assets/c0e91164-3fb3-404e-8c75-0231a503e352)

   Notice that in this case the link copied was `https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-more-validations`
   
3. Using Kate (or another editor) Tab 2 edit `fastapi_learn_tutorial_user_guide/RUNME`, replacing the first link on line 11 with the copied link:

   ![image](https://github.com/user-attachments/assets/da7f2b20-b8ce-4584-88f4-3982b54f4575)
   

4. Paste the same link and a screen shot of the next tutorial or next chunk of the current tutorial into the issue associated with working through the tutorial. e.g. [#64](https://github.com/pflagerd/fastapi_learn_tutorial_user_guide/issues/64)

   Rationale: This step is intended to give us a visual cue as to what the copied link will look like when put into a browser.

5. From the link just pasted make a variable called *new-tutorial-directory* containing the portion of the URL following the `https://fastapi.tiangolo.com/tutorial/` AND preceding the `/#`(e.g. `query-params-str-validations`)
    
   Rationale: We will use this variable name to refer to this portion later in this work instruction.

6. Read the tutorial until we encounter some code. Here's an old example:

     ![Image](https://github.com/user-attachments/assets/eab3c212-b07c-4818-a331-6033fd0af548)

7. In Chromium Instance 2, Tab 2, copy the part of the URL following `https://github.com/fastapi/fastapi/blob/master/docs_src/` to another variable name called *old-tutorial-name*.

   ![image](https://github.com/user-attachments/assets/ea32c411-6a78-4b1e-a790-41132a96a468)

8. From Chromium Instance 2, Tab 2, navigate to *new-tutorial-directory*. (e.g. `.../query_params_str_validations`).  Observe some .py filenames whose contents might be the code we see above.
9. Find the filename whose contents match the code in the tutorial.
10. Let's create yet another mental variable name to contain the filename we found: *new-tutorial-name*.  e.g. *new-tutorial-name* contains `query_params_str_validations/tutorial002_an_py310.py`
11. NOTE: both *old-tutorial-name* and *new-tutorial-name* should contain two path elements (a sort of directory and a sort of filename): `query_params_str_validations/tutorial002_an_py310.py` `query_params_str_validations` and `tutorial002_an_py310.py`    
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
20. Observe that Konsole tab 3 is running *new-tutorial-name*
21. Observe that Chromium instance 2, Tab 1 is showing the new tutorial page.
22. Observe that Chromium instance 2, Tab 2 is showing *new-tutorial-name* under the fastapi repo directory `https://github.com/fastapi/fastapi/blob/master/docs_src/`.
23. Observe that Chromium instance 2, Tab 3 is showing *new-tutorial-name* under the `https://github.com/pflagerd/fastapi_learn_tutorial_user_guide/tree/master/`.
24. Observe that Chromium instance 3, Tab 2, shows `127.0.0.1:8000/docs` and when fully expanded shows the expected Parameters as defined in the tutorial's code.
25. Decide how to test the statements made in the tutorial and the code in the tutorial. Here is an example similar to the code you'll be testing.:

     ![Image](https://github.com/user-attachments/assets/606eb18d-4328-40dd-94ea-e976e1aede61)

26. Now continue with Step 1 above.
