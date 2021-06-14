#! /usr/bin/python3

from readcsv import readcsv
from readcsv import printline
from ssh_connect import cssh_connect
from ssh_connect import jssh_connect
from ssh_connect import assh_connect
import os
from os import path
import sys
import time
import getpass
import logging

line = printline()

#Start logging
logging.basicConfig(filename= "test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


# Check if any transfer file given as input
if len(sys.argv) < 2:
    print("No file input......Please try again and input a file to copy")
    sys.exit()

# Check if the transfer exists 
sourc_file = sys.argv[1]
if not path.exists(sourc_file):
    print("File '{}' does not exists.    Try again.....".format(sourc_file))
    sys.exit()

# Opening file
cmd = []
with open(sourc_file, 'r') as c:
    cmdlist = c.readlines()
    for i in cmdlist:
        cmd.append(i.strip("\n"))

vendor = input("Select the vendor you wish to push the configs on : 1. Cisco  2. Juniper  3. Arista : ")
venlow = vendor.lower()
print(line)
# getting IP list
ip_list = readcsv()
print(line)
print("\nPlease, confirm the below config commands you want to push : ")
for i in cmd:
    print("\n{}".format(i))

gett = input("\nProceed? [n]y: ")

if gett == 'n':
    sys.exit()

print(line)

print("\nPlease, confirm if you want to push config commands on: ")
for ip in ip_list:
    print("\n{}".format(ip))
# Getting confirmation to proceed or abort
gett = input("\nProceed? [n]y: ")

if gett == 'n':
    sys.exit()

cmd_file = sourc_file
# Prompting for username and password
print(line)
username = input('''\nPlease enter your username : ''')

passwd = getpass.getpass('''\nAnd your password : ''')

print("\n" + line)

if vendor == '1' or venlow == 'cisco':

    # Starting time count
    start = time.time()

    for ip in ip_list:
        username = username
        passwd = passwd
        cssh_connect(ip, username, passwd, cmd_file)
        print(line)
    # Stoping time count
    stop = time.time()

    # Getting total time
    consume = stop - start
    # Printing the upload time
    print("Task completed in {} seconds.".format(consume))
    print(line)

elif vendor == '2' or venlow == 'juniper':
    # Starting time count
    start = time.time()

    for ip in ip_list:
        username = username
        passwd = passwd
        jssh_connect(ip, username, passwd, cmd)
        print(line)
    # Stoping time count
    stop = time.time()

    # Getting total time
    consume = stop - start
    # Printing the upload time
    print("Task completed in {} seconds.".format(consume))
    print(line)

else:
    # Starting time count
    start = time.time()

    for ip in ip_list:
        username = username
        passwd = passwd
        assh_connect(ip, username, passwd, cmd_file)
        print(line)
    # Stoping time count
    stop = time.time()

    # Getting total time
    consume = stop - start
    # Printing the upload time
    print("Task completed in {} seconds.".format(consume))
    print(line)
