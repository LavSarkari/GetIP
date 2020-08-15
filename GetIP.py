#python 3.7.1
#do not copy..
#give an star
import socket
import time

#Take the server name
#Some Samples:
    #www.google.com
    #www.facebook.com
    #www.brazzers.com
    #www.wikipedia.com

print("Welcome to getip")
time.sleep(2)
print("Created by lav_sarkari")
print("Enter the website")
host = input()

try:
  #know the ip address of the website
  addr = socket.gethostbyname(host)
  print(f"IP ADDRESS : {addr}")
  print("See you later")

except socket.gaierror:
  print("The website does not exits!")
