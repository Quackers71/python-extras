#!/bin/bash

#      stdout      stderr
#ls -al 1>file1.txt 2>file2.txt

#      stdout      stderr
#ls +al 1>file1.txt 2>file2.txt

#ls -al >file1.txt
#ls +al >file1.txt

#ls -al >file1.txt 2>&1 #will produce stderr on an error i.e.
#ls +al >file1.txt 2>&1 # shorter version:
ls +al >&file1.txt
