#!/bin/bash

ansible-playbook Linux/null_route_linux.yml -i hosts.inv --ask-become-pass --extra-vars "bad_ip=$1"
ansible-playbook Windows/null_route_windows.yml -i hosts.inv --extra-vars "bad_ip=$1"
