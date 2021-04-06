## Problem Description

Some websites were stored in a old server (since 2007). When this server was disabled, a backup was made. However, when the files were written, special carachters were losted, then a lot of unicode codes appear on the files. Thus, when the websites were put online again, they were full of "?" in place of special carachters;

## Solution

Instead to open each file to correct this problem (there were hundreds of files), I develop a simple python script that read each file, changing the codes to the letters (with special carachters).

## Technologies

Python 3.8
