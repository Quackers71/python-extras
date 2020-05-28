#!/bin/bash

echo "hello bash"

echo "Type something: "
# now output using cat
cat > output.txt

echo "Type some more: "
cat >> output.txt

: '
now output using cat
now output using cat
now output using cat'

echo "we're all done"
