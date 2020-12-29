import socket
import sys

try:
    host = input("[+]enter the host: ")
except KeyboardInterrupt:
    print("\n\nyou close the program")
    exit()

print("-"*50)
print("scanning host",)
print("-"*50)

def scan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        return True
    except KeyboardInterrupt:
        print("you exit the program")
        exit()
    except:
        return False

for port in range(1,1000):
    if scan(port):
        print("port {} open".format(port))
    else:
        pass

print("\nscanning complete")
