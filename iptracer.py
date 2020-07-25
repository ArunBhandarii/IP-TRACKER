# Print out the IP details from hackertarget


banner = '''  
  _____ _____    ______ _____ _   _ _____  ______ _____  
 |_   _|  __ \  |  ____|_   _| \ | |  __ \|  ____|  __ \ 
   | | | |__) | | |__    | | |  \| | |  | | |__  | |__) |
   | | |  ___/  |  __|   | | | . ` | |  | |  __| |  _  / 
  _| |_| |      | |     _| |_| |\  | |__| | |____| | \ \ 
 |_____|_|      |_|    |_____|_| \_|_____/|______|_|  \_\
                                                         
                                                                                                                                                      
Coded by Arun Bhandari
Twitter : @ArunBhandarii'''
print(banner)

print("[+]Find the Geo Location and details of an IP address.")

import requests
site=''
while not site:
  print("[+] Please Enter the IP Address of the target:")
  site=input()
  break
x = requests.get("https://api.hackertarget.com/geoip/?q="+site)
print(x.text)

# Prints out ip location details in the terminal. 
