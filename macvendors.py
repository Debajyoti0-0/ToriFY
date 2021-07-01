from colorizor import COLOR,STYLE
import os
import random
import string

random_chars = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)

def mac_samsung():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 94:51:03:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 94:51:03:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 94:51:03:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_apple():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:03:93:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:03:93:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:03:93:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_huawei():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:18:82:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:18:82:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:18:82:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_nokia():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:19:2D:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:19:2D:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:19:2D:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_blackberry():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:1C:CC:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:1C:CC:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:1C:CC:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_motorola():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:0A:28:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:0A:28:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:0A:28:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_htc():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:23:76:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:23:76:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:23:76:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_google():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:1A:11:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:1A:11:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:1A:11:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_asus():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 9C:5C:8E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 9C:5C:8E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 9C:5C:8E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_FUJITSU():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:00:0E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:00:0E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:00:0E:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_toshiba():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:00:39:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:00:39:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:00:39:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)


def mac_acer():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m C0:98:79:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m C0:98:79:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m C0:98:79:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_hp():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:0B:CD:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:0B:CD:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:0B:CD:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def mac_dell():
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -m 00:06:5B:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98)))
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -m 00:06:5B:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars,random.randint(10,99),random.randint(55,98)))
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {3} -m 00:06:5B:{0}:{1}:{2} >/dev/null 2>&1'.format(random_chars
                                                                                   ,random.randint(10,99),random.randint(55,98),interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

