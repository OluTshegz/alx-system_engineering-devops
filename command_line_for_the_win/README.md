Command line for the win
========================

- Weight: 1

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/324/06AChAO.png)

Background Context
------------------

[CMD CHALLENGE](https://alx-intranet.hbtn.io/rltoken/a83_NOBEtXgFr1Yqej0HYA "CMD CHALLENGE") is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It's a good training to improve your command line skills!

**This project is NOT mandatory** at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won't get hurt if you don't do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

Requirements
------------

## General

- A `README.md` file, at the root of the folder of the project, is mandatory
- This project will be manually reviewed.
- As each task is completed, the name of that task will turn green
- Create a screenshot, showing that you completed the required levels
- Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

### Specific

In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

#### References

SFTP Guide
SFTP File Transfer Tutorial

#### Here are the steps to follow

- Take the screenshots of the completed levels as mentioned in the general requirements.
- Open a terminal or command prompt on your local machine.
- Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
- Once connected, navigate to the directory where you want to upload the screenshots.
- Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
- Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
- Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
- Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.


# SFTP Usage Guide

## Overview

SFTP (Secure File Transfer Protocol) is a secure and encrypted file transfer protocol that provides a secure way to transfer files between hosts over a network. This guide outlines basic SFTP commands and usage.

## Table of Contents

- [Connecting to SFTP Server](#connecting-to-sftp-server)
- [Navigating Remote Directory](#navigating-remote-directory)
- [Uploading Files](#uploading-files)
- [Downloading Files](#downloading-files)
- [Closing SFTP Session](#closing-sftp-session)

## Connecting to SFTP Server

To connect to an SFTP server, use the following command:

```bash
sftp username@hostname
```

Replace `username` with your SFTP username and `hostname` with the server's hostname or IP address. You will be prompted to enter your password.

## Navigating Remote Directory

Once connected, you can navigate through the remote directory using the following commands:

- Change remote directory: `cd remote_directory`
- Change local directory: `lcd local_directory`
- Print current remote directory: `pwd`
- List remote directory contents: `ls`

## Uploading Files

To upload files from the local machine to the remote server, use the following command:

```bash
put local_file [remote_path]
```

Replace `local_file` with the name of the local file you want to upload. Optionally, you can specify a `remote_path` to define the destination directory on the remote server.

## Downloading Files

To download files from the remote server to the local machine, use the following command:

```bash
get remote_file [local_path]
```

Replace `remote_file` with the name of the remote file you want to download. Optionally, you can specify a `local_path` to define the destination directory on the local machine.

## Closing SFTP Session

To close the SFTP session and disconnect from the server, use the following command:

```bash
exit
```

Alternatively, you can use the shortcut:

```bash
bye
```

## Conclusion

This guide provides basic commands for using SFTP to transfer files securely between a local machine and a remote server. Refer to the [official documentation](https://www.openssh.com/manual.html) for more advanced options and features.


### NOTE :
The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/

More Info
---------

### Manual QA Review

**It is your responsibility to request a review for this project from a peer. If no peers have been reviewed, you should request a review from a TA or staff member.**

Tasks
-----

### 0\. First 九 tasks

# advanced

Complete the first 9 tasks.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `command_line_for_the_win`
- File: `0-first_9_tasks.jpg,0-first_9_tasks.png`

 Done? Help

### 1\. Reach חי completed tasks

# advanced

Complete the 9 next tasks, getting to 18 total.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `command_line_for_the_win`
- File: `1-next_9_tasks.jpg,1-next_9_tasks.png`

 Done? Help

### 2\. Reach the perfect cube, 27

# advanced

Complete the 9 next tasks, getting to 27 total.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `command_line_for_the_win`
- File: `2-next_9_tasks.jpg,2-next_9_tasks.png`

Your first challenge is to print `“hello world”` on the terminal in a single command. Hint: There are many ways to print text on the command line, one way is with the `‘echo’` command. Try it below and good luck!

```
echo "hello world"
```

Print the current working directory.

```
pwd
```

List names of all the files in the current directory, one file per line.

```
ls
```

There is a file named `access.log` in the current directory. Print the contents.

```
cat access.log
```

Print the last 5 lines of `“access.log”`.

```
cat access.log | tail -n 5
```

Create an empty file named `take-the-command-challenge` in the current working directory.

```
touch take-the-command-challenge
```

Create a directory named `tmp/files` in the current working directory. Hint: The directory `"tmp/"` doesn't exist, with one command you need to create both `"tmp/"` and `"tmp/file"`.

```
mkdir tmp tmp/files
```

Copy the file named `take-the-command-challenge` to the directory `tmp/files`

```
cp take-the-command-challenge tmp/files/
```

Move the file named `take-the-command-challenge` to the directory `tmp/files`

```
mv take-the-command-challenge tmp/files/take-the-command-challenge
```

A symbolic link is a type of file that is a reference to another file. Create a symbolic link named `take-the-command-challenge` that points to the file `tmp/files/take-the-command-challenge`.

```
ln -s tmp/files/take-the-command-challenge "take-the-command-challenge"
```

Delete all of the files in this challenge directory including all subdirectories and their contents. Hint: There are files and directories that start with a dot `"."`, `"rm -rf *"` won't work here!

```
rm -r * .*
```

There are files in this challenge with different file extensions. Remove all files with the `.doc` extension recursively in the current working directory.
The command rm -r **/*.doc is used to delete all files with the .doc extension in the current directory and its subdirectories recursively. The -r option stands for recursive, which means it will delete files and directories within subdirectories as well.

```
rm -r **/*.doc
```

There is a file named `access.log` in the current working directory. Print all lines in this file that contains the string `"GET"`.

```
cat access.log | grep "GET"
```

Print all files in the current directory, one per line (not the path, just the filename) that contain the string `“500”`.

```
ls | grep -l "500" *
```

Print the relative file paths, one path per line for all filenames that start with `“access.log”` in the current directory. `%P for file path`

```
`find . -type f -name "access.log*" -printf "%P\n"` or `ls -F | grep "access.log*"` or just `ls access.log*`
```

Print all matching lines (without the filename or the file path) in all files under the current directory that start with `“access.log”` that contain the string `“500”`. Note that there are no files named `access.log` in the current directory, you will need to search recursively.

```
`cat **/access.log* | grep "500"` or `grep -h -r "500" --include="access.log*" .`
```

Extract all IP addresses from files that start with `“access.log”` printing one IP address per line.

```
`cat **/access.log* | grep -ro ^[0-9.]*` or `grep -E -r -h -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' --include "access.log*"`
```

Count the number of files in the current working directory. Print the number of files as a single integer.

```
`find . -type f | wc -l` or `ls -l | wc -l`
```

Print the contents of access.log sorted.

```
`sort access.log` or `cat access.log | sort`
```

Print the number of lines in `access.log` that contain the string `“GET”`.

```
`grep GET access.log | wc -l` or `cat access.log | grep -e "GET" | wc --lines`
```

The file `split-me.txt` contains a list of numbers separated by a `;` character. Split the numbers on the `;` character, one number per line.

```
`cat split-me.txt | tr ";" "\n"` or `tr ';' '\n' < split-me.txt`
```

Print the numbers 1 to 100 separated by spaces.

```
`echo {1..100}` or `for i in {1..100}; do echo -n "$i "; done` or `for ((i=1; i<=100; i++)); do echo -n "$i "; done`
```

This challenge has text files (with a `.txt` extension) that contain the phrase `“challenges are difficult”`. Delete this phrase from all text files recursively. Note that some files are in subdirectories so you will need to search for them.

```
`sed -i "challenge are difficult/d" **/*.txt` or `find . -type f -name "*.txt" -exec sed -i "/challenges are difficult/d" {} \;`
```

The file `sum-me.txt` has a list of numbers, one per line. Print the sum of these numbers.

```
`let sum=0; for num in $(cat sum-me.txt); do let sum+=$num; done; echo $sum` or `a=0; for x in $(cat sum-me.txt); do a=$((a+x)); done; echo $a`
```

Print all files in the current directory recursively without the leading directory path. `%f for filename`

```
find . -type f -printf "%f\n"
```

Rename all files removing the extension from them in the current directory recursively.

```
`mv * .*` or `rm -rf ** .*`
```

The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a ‘.’ character.

```
`ls | tr ' ' '.'` or `ls | tr " " "."`
```
