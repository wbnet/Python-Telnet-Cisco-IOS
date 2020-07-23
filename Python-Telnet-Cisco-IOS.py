
#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST = "10.0.90.103"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("TempPass\n")

tn.write("show version | include uptime\n")

# tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()

