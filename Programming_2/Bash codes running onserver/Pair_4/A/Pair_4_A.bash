#!/bin/bash


#Pair_1_A 

from=planetlab-3.cmcl.cs.cmu.edu
to=plonk.cs.uwaterloo.ca

pingingfile="rajat_ping_"$from"_to_$to.txt"
traceroute_file="rajat_traceroute_"$from"_to_$to.txt"

while true; do

	date=$(date +"%m-%d-%Y")
	time=$(date +"%H:%M")
	
	echo "Date: $date (MM/DD/YYYY), Time: $time, from: $from, to: $to " >> $pingingfile
	echo "Date: $date (MM/DD/YYYY), Time: $time, from: $from, to: $to " >> $traceroute_file
	echo "" >> $pingingfile
	echo "" >> $traceroute_file
	
    ping $to -c 20 >> $pingingfile
    traceroute $to 2>> $traceroute_file >> $traceroute_file
    
    echo "" >> $pingingfile
	echo "" >> $traceroute_file

    sleep 3600
done