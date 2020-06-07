#!/bin/bash

car=('BMW' 'Toyota' 'Honda' 'Mercedes' 'VW')


echo "${car[@]}"

echo "${car[0]}"

echo "${!car[@]}"

echo "${#car[@]}"

echo "removing: ${car[2]}"
unset car[2]
car[2]="Fiat"
echo "and replacing it with: ${car[2]}"
echo "The New List is now: ${car[@]}"
