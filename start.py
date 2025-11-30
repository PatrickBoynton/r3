import socket
import os

#  Run this file first.
r3vids = "/home/mymar101/r3vids/.env"
r3vids_mac = "/Users/patrick/r3/.env"
r3vue = "/home/mymar101/r3vids/r3vue/.env"
r3vue_mac = "/Users/patrick/r3/r3vue/.env"
data_folder = "/home/mymar101/r3vids/data"
data_folder_mac = "/Users/patrick/r3/data"

hostname = socket.gethostname()


def get_ip_address():
    ip_list = socket.gethostbyname_ex(hostname)[2]
    print(f"ip list: {ip_list}")
    if "192" in ip_list[0]:
        return  ip_list[0]
    else:
        return "localhost"


try:
    ip_address = get_ip_address()
except:
    ip_address = "localhost"

print(f"Ip address: {ip_address}")
print(f"Current host: {hostname}")

with open (r3vids or r3vids_mac, "w") as file:
    file.write(f"IP_ADDRESS={ip_address}\n")
    file.write(f"CURRENT_OS={hostname}\n")

with open(r3vue or r3vue_mac, "w") as file2:
    file2.write(f"VITE_IP_ADDRESS={ip_address}\n")

if not data_folder:
    os.mkdir(data_folder)
else:
    print("Data folder already exists.")
