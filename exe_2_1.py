from telnetlib import Telnet
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>Select Options>>>>>>>>>>>>>>>>>")
print("1: Telnet To server")
print("2: SSH To server")
print("3: Check the Dick Usage")
print("4: Inode Usage")
print("5: Get the list offiles from the path")
print("6: Copy files")
print(":::::::::::::::::::::::::::")
ch = input("Enter Choice: ")
server = input("Enter the server IP: ")
port = int(input("Enter the port: "))
with Telnet(server, port) as tn:
    tn.interact()

