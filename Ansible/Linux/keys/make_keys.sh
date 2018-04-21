#!/bin/bash
mv id_rsa id_rsa.old
mv id_rsa.pub id_rsa.pub.old
ssh-keygen -b 2048 -t rsa -f "./$1" -q -N ""
chmod 400 "./$1"
