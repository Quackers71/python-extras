#!/bin/bash

age=17

if [ "$age" -lt 18 -o "$age" -lt 40 ]
then
        echo "The Age $age is correct"
else
        echo "The Age $age is not correct"
fi
