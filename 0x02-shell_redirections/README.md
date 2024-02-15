This is a README.md file describing what each script is doing in this repository

**File `0-hello_world`:** Prints "Hello, World", followed by a new line to the standard output.  

**File `1-confused_smiley`:** Displays a confused smiley `"(Ôo)'`.  

**File `2-hellofile`:** Display the content of the `/etc/passwd` file.  

**File `3-twofiles`:** Display the content of `/etc/passwd` and `/etc/hosts`.  

**File `4-lastlines`:** Display the last 10 lines of `/etc/passwd`.  

**File `5-firstlines`:** Display the first 10 lines of `/etc/passwd`.  

**File `6-third_line`:** Displays the third line of the file `iacta`.  

**File  `7-file`:** Creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.  
**File:  `8-cwd_state`:** Writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.  

**File `9-duplicate_last_line`:** Duplicates the last line of the file `iacta`.  

**File `10-no_more_js`:** Deletes all the regular files (not the directories) with a  `.js`  extension that are present in the current directory and all its subfolders.  

**File `11-directories`:** Counts the number of directories and sub-directories in the current directory.

-   The current and parent directories should not be taken into account  
    
-   Hidden directories should be counted

**File `12-newest_files`:** Displays the 10 newest files in the current directory.

Requirements:

-   One file per line
-   Sorted from the newest to the oldest

**File `13-unique`:** Takes a list of words as input and prints only words that appear exactly once.

-   Input format: One line, one word
-   Output format: One line, one word
-   Words should be sorted

**File `14-findthatword`:** Display lines containing the pattern "root" from the file `/etc/passwd`.  

**File `15-countthatword`:** Display the number of lines that contain the pattern "bin" in the file `/etc/passwd`.  

**File `16-whatsnext`:** Display lines containing the pattern "root" and 3 lines after them in the file `/etc/passwd`.  

**File `17-hidethisword`:** Display all the lines in the file `/etc/passwd` that do not contain the pattern "bin".  

**File `18-letteronly`:** Display all lines of the file `/etc/ssh/sshd_config` starting with a letter.  

**File `19-AZ`:** Replace all characters `A` and `c` from input to `Z` and `e` respectively.

**File `20-hiago`:** Create a script that removes all letters `c` and `C` from input.

**File `21-reverse`:** Reverses its input.  

**File `22-users_and_homes`:** Displays all users and their home directories, sorted by users.

-   Based on the the  `/etc/passwd`  file

**File `100-empty_casks`:** Finds all empty files and directories in the current directory and all sub-directories.

-   Only the names of the files and directories should be displayed (not the entire path)  
    
-   Hidden files should be listed
-   One file name per line  
    
-   The listing should end with a new line
