#!/bin/bash
mv id_rsa id_rsa.old
mv id_rsa.pub id_rsa.pub.old
ssh-keygen -b 2048 -t rsa -f -q ./$1 -N ""
#cp ./id_rsa ~/.ssh/id_rsa
#cp ./id_rsa.pub ~/.ssh/id_rsa.pub
