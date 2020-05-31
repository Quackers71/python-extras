#!/bin/bash

function printFunc() {
        echo $1 $2 $3 $4 $5 $6
}

printFunc Hi, this is a New Function

function funcCheck() {
        returningValue="Using the funcCheck Function right now"
        echo "$returningValue"
}

funcCheck

returningValue="Changing the rV variable outside of the funcCheck Function"
echo "$returningValue"

funcCheck

## 1st example
: '
function printFunc() {
        echo "This is a New Function"
}

printFunc'
