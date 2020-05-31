#!/bin/bash

read -p "Enter the file name to create :" fileName

if [[ -f "$fileName" ]]
then
        echo "The File $fileName exists"
        exit 0
else
        echo "The File $fileName doesn't exist"
        read -p "Would you like to create that File? [Y/N]: " prompt
        if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" || $prompt == "YES" ]]
        then
                echo "Creating the $directory File"
                touch $fileName
                #echo `ll $fileName`
                exit 0

        elif [[ $prompt == "n" || $prompt == "N" || $prompt == "no" || $prompt == "No" || $prompt == "NO" ]]
        then
                echo "We didn't create the $directory File, so see you l8rz"
                exit 0
        else
                echo "Wrong Input"
        fi
        touch $fileName
fi
