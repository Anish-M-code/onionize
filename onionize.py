import os
import time
import platform
import sys
import subprocess

if platform.system().lower() == 'windows':
    print('Platform not supported!')
    sys.exit(1)

def download_eotk():
    print('Downloading Enterprise Onion Toolkit....\n')
    x = subprocess.run(['git','clone','https://github.com/alecmuffett/eotk.git'])
    os.chdir('eotk')

def get_domains():
    domain = []
    while 1:
        x = input('Enter domain of clearnet website:')
        choice = input('\nDo you want enter more domains?(y/n):')
        domain.append(x)
        if choice.lower() != 'y':
            break
    return domain

print('\n    --- ONIONIZE: CREATE ONION MIRROR FOR WEBSITES --- ')
while 1:

    print('\n Select os to install :-')
    print('\n1) Raspbian ')
    print('2) Ubuntu 20.04LTS ')
    print('3) Ubuntu 18.04LTS ')
    print('4) CentOS 8.2.2004 ')
    print('5) macOS Mojave ')
    print('6) FreeBSD 12.1')
    choice = input('\n\nEnter choice:')
    print()

    if choice == '1':
        print('Installing git...\n')
        x = subprocess.run(['sudo','apt-get','install','-y','git'])
        download_eotk()
        x = subprocess.run(['sudo','./opt.d/build-raspbian-stretch.sh'])
        break

    elif choice == '2':
        download_eotk()
        x = subprocess.run(['sudo','./opt.d/build-ubuntu-20.04.sh'])
        break

    elif choice == '3':
        download_eotk()
        x = subprocess.run(['sudo','./opt.d/build-ubuntu-18.04.sh'])
        break

    elif choice == '4':
        print('Installing git ...\n')
        x = subprocess.run(['sudo','yum','-y','install','git'])
        download_eotk()
        x = subprocess.run(['sudo','./opt.d/build-centos-8.2.2004.sh'])
        break

    elif choice == '5':
        download_eotk()
        x = subprocess.run(['./opt.d/build-macos-mojave.sh'])
        break

    elif choice == '6':
        print('Installing git ...\n')
        x = subprocess.run(['pkg','install','git'])
        download_eotk()
        x = subprocess.run(['./opt.d/build-freebsd-12.1.sh'])
        break

    else:
        print("Invalid choice!!!")

domainlist = get_domains()
with open("tor_server.tconf",'w') as f:
    f.write("set project tor_server\n")
    for domain in domainlist:
        f.write("hardmap %NEW_V3_ONION% "+domain+"\n")
    
x = subprocess.run(['sudo','./eotk','config','tor_server.tconf'])
x = subprocess.run(['sudo','./eotk','config','tor_server.conf'])
x = subprocess.run(['sudo','./eotk','start','tor_server'])
print('\nPlease wait ...\n')
time.sleep(10)
x = subprocess.run(['sudo','./eotk','status','tor_server'])
