#! /usr/bin/python3
#Importing necesaary modules to call functions
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from readcsv import printline
from time import sleep

#Prompting for username and password
line = printline()
print(line)

def jssh_connect(ip, username, passwd, cmd):
    try:
       global line

       print('\nGetting into: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'cisco', 
                      'device_type':'juniper',
               }
       connection = ConnectHandler(**Device)
       connection.enable()
       confsnmp = connection.send_config_set(config_commands=cmd, delay_factor=10, max_loops=500, exit_config_mode= False)
       print(confsnmp)
       connection.commit()
       connection.exit_config_mode()
#Disconnecting from the current device
       connection.disconnect() 
       print("\nAll the configurations have been pushed into '{}' successfully".format(ip))
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")

def assh_connect(ip, username, passwd, cmd):
    try:
       global line

       print('\nGetting into: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'cisco', 
                      'device_type':'arista_eos',
               }
       connection = ConnectHandler(**Device)
       connection.enable()
       confsnmp = connection.send_config_set(config_commands=cmd, delay_factor=10, max_loops=500)
       print(confsnmp)
       connection.save_config()
#Disconnecting from the current device
       connection.disconnect() 
       print("\nAll the configurations have been pushed into '{}' successfully".format(ip))
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")


def cssh_connect(ip, username, passwd, cmd):
    try:
       global line

       print('\nGetting into: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'cisco', 
                      'device_type':'cisco_ios',
               }
       connection = ConnectHandler(**Device)
       connection.enable()
       confsnmp = connection.send_config_set(config_commands=cmd, delay_factor=10, max_loops=500)
       print(confsnmp)
       connection.save_config()
#Disconnecting from the current device
       connection.disconnect() 
       print("\nAll the configurations have been pushed into '{}' successfully".format(ip))
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")
