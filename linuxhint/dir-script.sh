#!/bin/bash

: '
direc="Directory2"

if [ -d "$direc" ]
then
        echo "The $direc exists!"
else
        echo "Creating the $direc directory!"
        mkdir -p Directory2
fi'

function checkMakeDir() {

echo "If the Directory exists we won't re-make it but if it doesn't we will create it"
echo "Enter directory name to check: "
read directory

if [ -d "$directory" ]
then
        echo "The $directory Directory exists"
else
        read -p "Are you sure you'd like to create that Directory [Y/N]: " prompt
        if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" || $prompt == "YES" ]]
        then
                echo "Creating the $directory directory"
                mkdir $directory
                echo `ls`
                exit 0

        elif [[ $prompt == "n" || $prompt == "N" || $prompt == "no" || $prompt == "No" || $prompt == "NO" ]]
        then
                echo "We didn't create the $directory directory, so see you l8rz"
                exit 0
        else
                echo "Wrong Input"
        fi
fi
}


function startUp() {
read -p "Would you like to create a Directory [Y/N]: " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" || $prompt == "YES" ]]
then
        checkMakeDir
elif [[ $prompt == "n" || $prompt == "N" || $prompt == "no" || $prompt == "No" || $prompt == "NO" ]]
then
        echo "Ok, see you l8rz"
        exit 0
else
        echo "Wrong Input"
fi
}


startUp
