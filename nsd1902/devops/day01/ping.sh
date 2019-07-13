#!/bin/bash

date
for ip in 172.40.58.{1..254}
do
    ping -c2 $ip &> /dev/null && echo "$ip:up" || echo "$ip:down"
done
date
