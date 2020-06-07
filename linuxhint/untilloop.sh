#!/bin/bash

number=1
until [ $number -ge 11 ]
do
    echo "$number"
    number=$(( number+1 ))

done
