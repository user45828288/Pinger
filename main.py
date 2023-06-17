import os

ip = ""
while True:
    p = os.system(f"ping {ip}")
    print(p)
