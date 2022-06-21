#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=10)); do
        sleep 0.5
        echo $i
    done
} | whiptail --gauge "Please wait while we are sleeping..." 6 50 0