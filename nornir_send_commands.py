#!/usr/bin/env python3
'''
This script will ask for a list of commands to be executed against all hosts defined in ./inventory/hosts.csv (no filtering).

Since there is no filtering, to successfully run commands against all hosts in hosts.csv the hosts must all:
1) use the same credentials (user is interviewed for credentials at runtime)
2) the commands input must be valid across all devices

The output will be displayed in the shell as well as written to files (one file per command, per device) in the ./output directory (which need be present).
'''

from nornir import InitNornir
from nornir_csv.plugins.inventory import CsvInventory
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file
from getpass import getpass
from datetime import datetime

def send_command(task):
	for c in cmd_list:
		task.run(
    		task=netmiko_send_command,
    		command_string=c
		)

def write_output(task):
	x = len(cmd_list)
	y = 1
	z = 0
	while y < x + 1:
		key = str(task.host)
		dt = datetime.now().strftime("%m%d%Y-%H%M%S-%f")
		_cmd = cmd_list[z]
		task.run(
			task=write_file,
			filename=f"output/{task.host}-{_cmd.replace(' ','_')}-{dt}.txt",
			content=f"Command Output From: {_cmd} \n \n {r[key][y].result}"
	)
		y = y + 1
		z = z + 1


def transform_func(host):
	host.password = password
	host.username = username

def main():
	InventoryPluginRegister.register("CsvInventoryPlugin", CsvInventory)
	global r, cmd, username, password, cmd_list
	cmd=input("Enter a Command, or a list of comma separated commands: ")
	cmd_list=cmd.split(',')
	username=input("Username: ")
	password= getpass()
	nr = InitNornir(config_file='sample_config.yaml')
	for host in nr.inventory.hosts.values():
	    transform_func(host)
	r = nr.run(task=send_command)
	print_result(r) 
	w = nr.run(task=write_output)
	#print_result(w)

if __name__ == "__main__":
    main()

