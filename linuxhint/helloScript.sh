#!/bin/bash

cat << kreativ
some creative text
and another line
kreativ

cat << EOF
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
