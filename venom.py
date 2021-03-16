#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import random

white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
cyan = Fore.CYAN

colors = (white, green, red, yellow, cyan)
color = random.choice(colors)

banner = """
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗       ██████╗ ██████╗  ██████╗ ██████╗ ██╗  ██╗     ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔════╝ ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║  ███╗██║  ██║██║   ██║██████╔╝█████╔╝█████╗██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║   ██║██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ╚██████╔╝██████╔╝╚██████╔╝██║  ██║██║  ██╗     ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝       ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

"""
author = 'Venom 🐍 (Gaurav Chaudhary)'
team = 'From Team Venom 🐍'
facebook = 'https://facebook.com/venomgrills'
insta = 'https://instagram.com/i.m.gauravchaudhary'
github = 'https://github.com/venomsec-Dev/'
print(color + banner + color)
print(color + '   Author: ' + color + green + author + green)
print(color + '   Team: ' + color + red + team + red)
print(color + '   Facebook: ' + color + yellow + facebook + yellow)
print(color + '   Insta: ' + color + cyan + insta + cyan)
print(color + '   Github: ' + color + white + github + white)
print('\n')
links = []
titles = []
dorks = []
url = 'https://cxsecurity.com/dorks/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
for i in soup.findAll('a'):
    link = i.get('href')
    if link.startswith('https://cxsecurity.com/issue/') is True:
        title = i.get('title')
        titles.append(title)
        links.append(link)
    else:
        pass
for i in soup.findAll('font', color="#FCFCFC"):
    dork = i.text
    dorks.append(dork)
x = 0
while x <= 19:
    print(white + '     [' + color + str(x) + white + '] ' + color + 'Title: ' + green + titles[x])
    print(white + '     [' + color + '+' + white + ']  ' + green + dorks[x])
    print('\n')
    x +=1
num = int(input(white +'     [' + color + '+' + white + '] ' + color + 'Enter a number to continue: '))
def exploit(number):
    _response = requests.get(links[number])
    _soup = BeautifulSoup(_response.content, 'html.parser')
    read = _soup.find('div', class_="well well-sm premex")
    print('\n')
    print(white + '[+]' + color + '----------------- ' + green + titles[number] + color + ' ---------------------' + white + '[+]')
    print('\n')
    print(green + read.text)
exploit(num)
new_dork = dorks[num]
venom = new_dork.replace('Dork:', ' ')
useragents = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
headers = {'user-agent': random.choice(useragents)}
new_url = 'https://www.google.com/search?q='+venom
new_response = requests.get(url=new_url, headers=headers)
new_soup = BeautifulSoup(new_response.content, 'html.parser')
print('\n')
print(white + '     [+]' + color + '-------------------' + green + 'Vulnerable urls' + color + '---------------------------' + white + '[+]')
print('\n')
for i in new_soup('a'):
    hf = i.get('href')
    if hf.startswith('/url?q=') is True:
        new_link = hf[7:-88]
        if (new_link.startswith('https://support.google.com') or new_link.startswith('https://accounts.google.com')) is False:
            vuln_link = new_link.replace('%3D', '=')
            final_link = vuln_link.replace('%3F','?')
            print(white + '     [' + color + '+' + white + '] ' + green + final_link)
        else:
            pass
    else:
        pass

