#!/bin/bash

: '
-rwxr-xr-x 1 pi pi    14 May 28 12:31 bashTemplate.sh
-rwxr-xr-x 1 pi pi   341 May 29 08:46 case.sh
-rwxr-xr-x 1 pi pi   211 May 28 12:23 elifScript.sh
-rwxr-xr-x 1 pi pi    56 May 30 08:48 forloop.sh
-rwxr-xr-x 1 pi pi   156 May 28 12:32 ifand2.sh
-rwxr-xr-x 1 pi pi   154 May 29 08:25 ifand3.sh
-rwxr-xr-x 1 pi pi   158 May 28 12:29 ifand.sh
-rwxr-xr-x 1 pi pi   156 May 29 08:33 ifor2.sh
-rwxr-xr-x 1 pi pi   154 May 29 08:32 ifor.sh
-rw-r--r-- 1 pi pi  3553 May 30 08:41 notes.txt
-rw-r--r-- 1 pi pi    46 May 28 08:25 output.txt
-rwxr-xr-x 1 pi pi    72 May 28 22:08 tree-cron2.sh
-rwxr-xr-x 1 pi pi   132 May 28 22:10 tree-cron.sh
-rw-r--r-- 1 pi pi 17069 May 28 21:58 tree.txt
-rwxr-xr-x 1 pi pi   102 May 30 08:44 untilloop.sh
-rwxr-xr-x 1 pi pi   102 May 29 13:16 whileloop.sh'

# single line comment

for i in 1 2 3 4 5
do
        echo $i
done
