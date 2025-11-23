import os
import socket

#  Run this file first.
r3vids = "/home/mymar101/r3vids/.env"
r3vids_mac = "/Users/patrick/r3/.env"
r3vue = "/home/mymar101/r3vids/r3vue/.env"
r3vue_mac = "/Users/patrick/r3/r3vue/.env"
data_folder = "/home/mymar101/r3vids/data"
data_folder_mac = "/Users/patrick/r3/data"

hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    return ip
try:
    ip_address = get_ip_address()
except:
    ip_address = 'localhost'

if "192" in ip_address:
    print(f"hostname: {hostname}")
    print(f"ip_address: {ip_address}")
    if "Mac" in hostname:
        with open(r3vids_mac, "w") as file, open(r3vue_mac, "w") as file2:
            file.write(f"IP_ADDRESS={ip_address}")
            file2.write(f"VITE_IP_ADDRESS={ip_address}")
    else:
        with open(r3vids, "w") as file, open(r3vue, "w") as file2:
            file.write(f"IP_ADDRESS={ip_address}")
            file2.write(f"VITE_IP_ADDRESS={ip_address}")

else:
    print("localhost")
    with open(r3vids_mac, "w") as file, open(r3vue_mac, "w") as file2:
        file.write(f"IP_ADDRESS=localhost")
        file2.write(f"VITE_IP_ADDRESS=localhost")

if not os.path.exists(data_folder_mac):
    os.makedirs(data_folder_mac)
else:
    print("Data folder exists.")
