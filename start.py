import socket
import os

#  Run this file first.
r3vids = "/home/mymar101/r3vids/.env"
r3vue = "/home/mymar101/r3vids/.env"
data_folder = "/home/mymar101/r3vids/data"

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

if "192" in ip_address:
    print(f"hostname: {hostname}")
    print(f"ip_address: {ip_address}")

    with open(r3vids, "w") as file:
        file.write(f"IP_ADDRESS={ip_address}")

    with open(r3vue, "w") as file:
        file.write(f"VITE_IP_ADDRESS={ip_address}")
else:
    print("localhost")
    with open(r3vids, "w") as file:
        file.write(f"IP_ADDRESS=localhost")

    with open(r3vue, "w") as file:
        file.write(f"VITE_IP_ADDRESS=localhost")

if not os.path.exists(data_folder):
    os.makedirs(data_folder)
else:
    print("Data folder exists.")

print(f"FINISHED ADDING IP ADDRESS {ip_address}")
