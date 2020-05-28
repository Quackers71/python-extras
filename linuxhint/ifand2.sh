#!/bin/bash

age=17

if [[ "$age" -gt 18 && "$age" -lt 40 ]]
then
        echo "The Age $age is correct"
else
        echo "The Age $age is not correct"
fi
