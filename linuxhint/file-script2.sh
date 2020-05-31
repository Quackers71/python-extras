#!/bin/bash

read -p "Enter the file name to create : " fileName

if [[ -f "$fileName" ]]
then
        echo "The File \"$fileName\" exists"
        exit 0
else
        echo "The File \"$fileName\" doesn't exist"
fi
