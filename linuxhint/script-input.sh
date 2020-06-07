#!/bin/bash

: '
echo $0 $1 $2 $3 # ./script-input Yo BMW Quality
# ouput: ./script-input Yo BMW Quality'


args=("$@")

# echo ${args[0]} ${args[1]} ${args[2]}

# unlimited array until you press [CR]
echo $@

# this will print out the left of the array
echo $# 

