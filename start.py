import os
import socket

#  Run this file first.
r3vids = "/home/mymar101/r3vids/.env"
r3vue = "/home/mymar101/r3vids/r3vue/.env"
data_folder = "/home/mymar101/r3vids/data"

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

if "192" in ip_address:
    print(f"hostname: {hostname}")
    print(f"ip_address: {ip_address}")

    with open(r3vids, "w") as file, open(r3vue, "w") as file2:
        file.write(f"IP_ADDRESS={ip_address}")
        file2.write(f"VITE_IP_ADDRESS={ip_address}")

else:
    print("localhost")
    with open(r3vids, "w") as file, open(r3vue, "w") as file2:
        file.write(f"IP_ADDRESS=localhost")
        file2.write(f"VITE_IP_ADDRESS=localhost")

if not os.path.exists(data_folder):
    os.makedirs(data_folder)
else:
    print("Data folder exists.")
