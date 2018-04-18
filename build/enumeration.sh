#!/bin/bash

search_dir=$2
curr_part=$1

echo "Using Directory: $search_dir"

use_dir="$search_dir/*"
tmp_dir="/usr/tmp/iKnowdeDiscovery/enum"

fileNames=$(ls -al $search_dir | grep '^-')
count=${#fileNames[@]}
declare -a inodes=()
declare -A files=()

mkdir -p $tmp_dir;

#for entry in "$search_dir"/*
#do
#	  echo "$entry"
#done

echo $fileNames

#for ((i=0; i<$count; i++)); do
#	echo ${fileNames[$i]}
#	printf "%s\n" "${fileNames[$i]}" > "$tmp_dir/$i.txt"
#	printf "%s\n" "$(ls -i ${fileNames[$i]} | awk '{print $1}')" >> "$tmp_dir/$i.txt"
#done

#for ((i=0; i<$count; i++)); do
#	curr_ival="$(sed '2q;d' $tmp_dir/$i.txt)"
#	printf "%s\n" "$(debugfs -R 'ncheck '$curr_ival $curr_part 2>/dev/null)" > "$tmp_dir/$i.txt"
#done
