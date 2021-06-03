import psutil
import platform
from datetime import datetime
print('\033[1;36;40mGive some seconds to collect the info.....')
print()
print('\033[1;36;40mDISCLAIMER: WE ARE NOT RESPONSIBLE FOR ANY OF YOUR MISUSE OF THIS CONTENT...')
print()
print('COPYRIGHT to ipinfo.io api')
print()
print('\033[1;36;40mTHE INFO GIVEN HERE IS NOT ACCURATE AND ONLY YOUR ISP CAN TRACK YOUR LIVE LOCATION AND ALSO  SOME OF YOUR APPS CAN..OOH.. ')
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

text="I PYRATE"
cprint(figlet_format(text, font="slant"), "blue")

import requests
import json
import socket as s

res=requests.get("https://ipinfo.io/")
data=res.json()
#print(data)
IP_address=data['ip']
print("\033[1;32;40mIP_ADDRESS :",IP_address)
print()
org=data['org']
print('ORGANIZATION :',org)
print()
tz=data['timezone']
print('TIME ZONE :',tz)
print()
con=data['country']
print('COUNTRY :',con)
print()
region=data['region']
print('REGION :',region)
print()
city=data['city']
print('CITY :',city)
print()
pc=data['postal']
print('POSTAL CODE :',pc)
print()
location=data['loc'].split("," )
lat=float(location[0])
lon=float(location[1])
print('LATITUDE :',lat)
print()
print('LONGITUDE :',lon)
print()
print()
print('\033[1;33;40mCopy and Paste this in GOOGLE MAPS to see the location map :')
print()

a_list=[lat,lon]
converted_list = [str(element) for element in a_list]
joined_string = ",".join(converted_list)
print(joined_string)
print()
print()

sw=0
while sw <= 3:
	print()
	print("\033[1;33;40m[1]- YOUR SYSTEM INFO.")
	print("[2]- YOUR NETWORK INFO.")
	print("[3]- YOUR MEMORY INFO.")
	print("[4]- EXIT LOOP.")
	print()
	sw=int(input('ENTER THE NUMBER : '))
	print()
	if sw == 1:
	   	print("\033[1;32;40m""_"*20, "SYSTEM INFORMATION", "_"*20)
	   	print()
	   	uname = platform.uname()
	   	print(f"System: {uname.system}")
	   	print()
	   	print(f"Node Name: {uname.node}")
	   	print()
	   	print(f"Release: {uname.release}")
	   	print()
	   	print(f"Version: {uname.version}")
	   	print()
	   	print(f"Machine: {uname.machine}")
	   	print()
	   	print(f"Processor: {uname.processor}")
	   	print()
	elif sw == 2:
	   	print("\033[1;35;40m""_"*20, "NETWORK INFORMATION", "_"*19)
	   	if_addrs = psutil.net_if_addrs()
	   	for interface_name, interface_addresses in if_addrs.items():
	   	   		for address in interface_addresses:
	   	   			print()
	   	   			print()
	   	   			print(f"Interface: {interface_name}/n")
	   	   			print()
	   	   			print()
	   	   			if str(address.family) == 'AddressFamily.AF_INET':
	   	   			 print()
	   	   			 print(f"  IP Address: {address.address}")
	   	   			 print()
	   	   			 print(f"  Netmask: {address.netmask}")
	   	   			 print()
	   	   			 print(f"  Broadcast IP: {address.broadcast}")
	   	   			elif str(address.family) == 'AddressFamily.AF_PACKET':
	   	   			 print()
	   	   			 print(f"  MAC Address: {address.address}")
	   	   			 print()
	   	   			 print(f"  Netmask: {address.netmask}")
	   	   			 print()
	   	   			 print(f"  Broadcast MAC: {address.broadcast}")
	elif sw == 3:
		  print("\033[1;34;40m""_"*20,"MEMORY INFORMATION","_"*20)
		  svmem=psutil.virtual_memory()
		  print()
		  #print(f"Memory :{psutil.virtual_memory()}")
		  print()
		  print(f"Total Memory Usage: ",svmem[0])
		  print()
		  print(f"Availabe memory: ",svmem[1])
		  print()
		  print(f"Percent: ",svmem[2])
		  print()
		  print(f"Used: ",svmem[3])
		  print()
		  print(f"Free: ",svmem[4])
		  print()
		  print(f"Active: ",svmem[5])
		  print()
		  print(f"Inactive: ",svmem[6])
		  print()
		  print(f"Buffers: ",svmem[7])
		  print()
		  print(f"Cached: ",svmem[8])
		  print()
		  print(f"Shared: ",svmem[9])
		  print()
		  print(f"Slab: ",svmem[10])
		  print()
	elif sw <= 0 or sw > 4:
	  	print()
	  	print('\033[1;31;40mINVALID OPTION')
	  	sw=1
	  	print()
	 
	 	



print('\033[1;36;40mNOTE : DO NOT PUT HTTPS...Try entering simply\ndoimain.com or simple ip address without ports')
print()

ip=str(input("\033[1;31;40mEnter the target website URL or IP address : \033[1;36;40m "))
a=ip.replace('.','')
#print(a)
if a.isnumeric() == False:
	targetip=s.gethostbyname(ip)
	print()
	print('\033[1;32;40mIP_ADRESS :',targetip)
	str1="https://ipinfo.io/"
	targetip1=str1+str(targetip)
elif a.isnumeric() == True:
   str1="https://ipinfo.io/"
   targetip1=str1+str(ip)
res1=requests.get(targetip1)
data1=res1.json()
#IP_address1=data1['ip']
#print('\033[1;32;40mIP_ADDRESS :',IP_address1)
print()
if 'org' in data1:
	org1=data1['org']
	print('ORGANIZATION :',org1)
	print()
else:
	print()
tz1=data1['timezone']
print('TIME ZONE :',tz1)
print()
con1=data1['country']
print('COUNTRY :',con1)
print()
region1=data1['region']
print('REGION :',region1)
print()
city1=data1['city']
print('CITY :',city1)
print()
location1=data1['loc'].split("," )
lat1=float(location1[0])
lon1=float(location1[1])
print('LATITUDE :',lat1)
print()
print('LONGITUDE :',lon1)
print()
print()
print('\033[1;33;40mCopy and Paste this in GOOGLE MAPS to see the location map :')
print()

a_list1=[lat1,lon1]
converted_list1 = [str(element) for element in a_list1]
joined_string1 = ",".join(converted_list1)
print(joined_string1)
print()
print()

print('\033[1;36;40mCODED BY Love_3i')



