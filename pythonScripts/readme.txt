
1. detectJrxml.py is used to check if search strings are working as intended, complex searches might require regex instead
    a. search results are sorted and shown in jasper_search_results.csv

2. in detectJrxml.py, you can edit the following:
    a. search_strings
    b. moveFiles, if set to True, files with positive searches are moved to forEditing for the editJrxml.py
    c. the search logic loop

3. For editJrxml.py, its search_strings and logic should be updated according to the needs, edit logic loop are recommended to be adjusted depending on need
    a. to check if it worked, check jasper_search_results.csv for the specific line of the file you want to check
    b. visit edited, open the file, and check the line, further investigate accordingly if there are unintended edits


4. Now you have edited jrxml files, you can compile it in the java program.