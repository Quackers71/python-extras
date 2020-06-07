#!/bin/bash

fileName="tree.txt"

cd ~/
if [[ -f "$fileName" ]]
then
        echo `tree` >> $fileName
        echo `df -h /` >> $fileName
        echo `date` >> $fileName
        echo `ls -lah ~/$fileName` >> $fileName 
else
        touch $fileName
        cp ~/tree-template.txt ~/$fileName
fi
