#!/bin/bash

select car in BMW MERCEDES TESLA VW AUDI EXIT
do
        case $car in
        BMW)
                echo "BMW selected";;
        MERCEDES)
                echo "MERCEDES selected";;
        TESLA)
                echo "TESLA selected";;
        VW)
                echo "VW selected";;
        AUDI)
                echo "AUDI selected";; 
        *)
                echo "Error! Please select between 1..5";;
        esac
done
