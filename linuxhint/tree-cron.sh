#!/bin/bash

cd ~/
echo `tree` >> tree.txt
echo `df -h /` >> tree.txt
echo `date` >> tree.txt
echo `ls -lah ~/tree.txt` >> tree.txt
