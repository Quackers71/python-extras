#!/bin/bash

# for i in 1 2 3 4 5 # specific numbers

# for i in {1..30} # {start..end}

# for i in {0..32..4} # {start..end..increment}

for (( i=1; i<6; i++ ))
do
        echo $i
done
