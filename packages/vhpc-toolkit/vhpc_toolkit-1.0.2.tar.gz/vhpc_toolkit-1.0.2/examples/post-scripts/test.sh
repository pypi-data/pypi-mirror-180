#!/bin/bash

echo "hello world 1" >> test1.log 

# Environment variables
# [FRONTEND]
# Check FRONTEND\'s Network
export DNS1="10.142.7.1"
export DNS2="10.132.7.2"

echo "nameserver ${DNS1}" >> test1.log 
echo "nameserver ${DNS2}" >> test1.log