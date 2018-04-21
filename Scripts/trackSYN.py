#!/usr/bin/env python3

# File: trackSYN.py
#
# Description:  Listens on a given interface for incoming TCP segments with
#               the SYN flag set. Ignores segments with both SYN and ACK flags
#               set.

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # supress IPv6 error
try:
  from scapy.all import *
except Exception as e:
  print("scapy is required for this script to work")
  print("Install:\n\tapt install python3-pip\n\tpip3 install scapy-python3")
  sys.exit(1)

#### print TCP SYN segment ####
def print_seg(seg):
  flags = seg[TCP].flags
  if (flags & 0x02 and (not flags & 0x10)):  # 0x02 = SYN    0x10 = ACK
    if (seg.src != mac):	# if not outgoing packet
      print(str(seg[IP].src)+' ---> '+str(seg.dport))



#### get command line arguments ####
intf="eth0"
# get MAC address and validate interface
try:
  mac = get_if_hwaddr(intf)
except:
  sys.exit("Invalid interface name")


#### sniff packets ####
sniff(filter="tcp", iface=intf, prn=(lambda x: print_seg(x)))


