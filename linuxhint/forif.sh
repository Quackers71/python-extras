#!/bin/bash

for (( i=1; i<11; i++ ))
do
        if [ $i -eq 3 ] || [ $i -eq 7 ]
        then
            continue
        fi
        echo $i
done
