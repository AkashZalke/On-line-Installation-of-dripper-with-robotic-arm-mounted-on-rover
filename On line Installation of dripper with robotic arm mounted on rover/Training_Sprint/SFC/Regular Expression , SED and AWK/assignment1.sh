#!/bin/bash

#take the input file name which is passed as an argument

#find the number of lines with one or more digits present in the input file

#print the number of line with one or more digits found

#find the digits present in the input file

#print the digits found
result=()
var=0
flag=0
while read p
do 

    arr1=(${p//","/ }) 
    arr2=(${p//";"/ }) 
    for word in ${arr1[@]} 
    do
        if [[ $word =~ ^[0-9]*$ ]]; then
        if [[ $flag == 0 ]];then
        var=$(( var + 1 ))
        flag=1
        fi
        result+=($word)
        fi
    done
    
    flag=0

    for word in ${arr2[@]}
    do
        if [[ $word =~ ^[0-9]*$ ]]; then
        if [[ ! " ${result[*]} " =~ " ${word} " ]]; then
            result+=($word)
        fi
        fi
    done

done < $1
echo "Number of lines having one or more digits are: $var"
echo "Digits found:"
for word in ${result[@]}
    do
        echo "$word" 
    done