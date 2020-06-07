#!/bin/bash

car=$1

echo $1

case $car in 
        "BMW" )
                echo "It's a BMW" ;;
        "MERCEDES" )
                echo "It's a Mercedes" ;;
        "TOYOTA" )
                echo "It's a Toyota" ;;
        "HONDA" )
                echo "It's a Honda" ;;
        * )
                echo "Unknown vehicle type" ;;
esac

