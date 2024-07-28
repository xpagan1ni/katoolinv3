#!/usr/bin/python3

import os
import sys, traceback


if os.getuid() != 0:
	print ("Sorry. This script requires sudo privledges")
	sys.exit()
def main():
	try:
		print ('''

\033[1;35m		 
██╗  ██╗ █████╗ ████████╗ ██████╗  ██████╗ ██╗     ██╗███╗   ██╗
██║ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║████╗  ██║
█████╔╝ ███████║   ██║   ██║   ██║██║   ██║██║     ██║██╔██╗ ██║
██╔═██╗ ██╔══██║   ██║   ██║   ██║██║   ██║██║     ██║██║╚██╗██║
██║  ██╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ V3.0\033[1;m
                                                                
                                                                       

\033[1;35m~~~~~~~~~~~~~~+  Upgraded by Pagan1ni  +~~~~~~~~~~~~~~\033[1;m
		 
\033[1;32m~~~~~~~~~~~~~~+  352 Tools  +~~~~~~~~~~~~~~\033[1;m


\033[1;91m!!! Before using the Katoolin tool, please note that you need to have Python3 on your system. If not, you can download Python3 with option 'P' before starting to install the tools. .\033[1;m		 

		''')
		def inicio1():
			while True:
				print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
6) About

			''')

				opcion0 = input("\033[1;36mkat > \033[1;m")
			

				while opcion0 == "1":
					print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

					''')
					repo = input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
					repo = input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu -y")
				elif opcion0 == "5":
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		''')
				elif opcion0 == "6":
					print('''
****************** + About Katoolin V3.0 + ******************
		   
Automatically install all Kali linux tools.

\033[1;35mUpgrade by pagan1ni\033[1;m
		   
\033[1;32mDeveloped by LionSec\033[1;m		   

	
		   ''')

				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 ''')
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Information Gathering\033[1;m

1) acccheck                 30) lbd
2) ace-voip                 31) Maltego Teeth
3) Amap                     32) masscan
4) Automater                33) Metagoofil
5) bing-ip2hosts            34) Miranda
6) braa                     35) Netdiscover
7) CaseFile                 36) Netmask
8) CDPSnarf                 37) Nmap
9) cisco-torch              38) p0f
10) Cookie Cadger           39) Parsero
11) copy-router-config      40) Recon-ng
12) DMitry                  41) SET
13) dnmap                   42) smtp-user-enum
14) dnsenum                 43) snmpcheck
15) dnsmap                  44) sslcaudit
16) DNSRecon                45) SSLsplit
17) dnstracer               46) sslstrip
18) dnswalk                 47) SSLyze
19) DotDotPwn               48) THC-IPV6
20) enum4linux              49) theHarvester
21) enumIAX                 50) TLSSLed
22) exploitdb               51) twofi
23) Fierce                  52) URLCrazy
24) Firewalk                53) Wafw00f
25) fragroute               54) Wireshark
26) fragrouter              55) WOL-E
27) Ghost Phisher           56) Xplico
28) GoLismero               57) iSMTP
29) goofile                 58) InTrace
                            59) hping3
                           

0) Install all Information Gathering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck -y")
							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install amap -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install automater -y")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install casefile -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install cdpsnarf -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cookie-cadger -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dmitry -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install dnsrecon -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install dotdotpwn -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux -y")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumiax -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install fierce -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install firewalk -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter -y")
							elif opcion2 == "27":
								cmd = os.system("apt-get install ghost-phisher -y")
							elif opcion2 == "28":
								cmd = os.system("apt-get install golismero -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install maltego-teeth -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan -y")
							elif opcion2 == "33":
								cmd = os.system("apt-get install metagoofil -y")
							elif opcion2 == "34":
								cmd = os.system("apt-get install miranda -y")
							elif opcion2 == "35":
								cmd = os.system("apt-get install netdiscover -y")
							elif opcion2 == "36":
								cmd = os.system("apt-get install netmask -y")
							elif opcion2 == "37":
								cmd = os.system("apt-get install nmap -y")
							elif opcion2 == "38":
								cmd = os.system("apt-get install p0f -y")
							elif opcion2 == "39":
								cmd = os.system("apt-get install parsero -y")
							elif opcion2 == "40":
								cmd = os.system("apt-get install recon-ng -y")
							elif opcion2 == "41":
								cmd = os.system("apt-get install set -y")
							elif opcion2 == "42":
								cmd = os.system("apt-get install smtp-user-enum-y")
							elif opcion2 == "43":
								cmd = os.system("apt-get install snmpcheck -y")
							elif opcion2 == "44":
								cmd = os.system("apt-get install sslcaudit -y")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslsplit -y")
							elif opcion2 == "46":
								cmd = os.system("apt-get install sslstrip -y")
							elif opcion2 == "47":
								cmd = os.system("apt-get install sslyze -y")
							elif opcion2 == "48":
								cmd = os.system("apt-get install thc-ipv6 -y")
							elif opcion2 == "49":
								cmd = os.system("apt-get install theharvester -y")
							elif opcion2 == "50":
								cmd = os.system("apt-get install tlssled -y")
							elif opcion2 == "51":
								cmd = os.system("apt-get install twofi -y")
							elif opcion2 == "52":
								cmd = os.system("apt-get install urlcrazy -y")
							elif opcion2 == "53":
								cmd = os.system("apt-get install wafw00f -y")
							elif opcion2 == "54":
								cmd = os.system("apt-get install wireshark -y")
							elif opcion2 == "55":
								cmd = os.system("apt-get install wol-e -y")
							elif opcion2 == "56":
								cmd = os.system("apt-get install xplico -y")
							elif opcion2 == "57":
								cmd = os.system("apt-get install ismtp -y")
							elif opcion2 == "58":
								cmd = os.system("apt-get install intrace -y")
							elif opcion2 == "59":
								cmd = os.system("apt-get install hping3 -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

1) afl++                           20) Nmap
2) BBQSQL                          21) ohrwurm
3) BED                             22) openvas-administrator
4) cisco-auditing-tool             23) openvas-cli	
5) cisco-global-exploiter          24) openvas-manager
6) cisco-ocs                       25) openvas-scanner
7) cisco-torch                     26) Oscanner
8 copy-router-config               27) Peass
9 commix                           28) Powerfuzzer
10) DBPwAudit                      29) sfuzz
11) DoonaDot                       30) SidGuesser
12) DotPwn                         31) SIPArmyKnife
13) Greenbone Security Assistant   32) Spike
14) GSD                            33) sqlmap
15) HexorBase                      34) Sqlninja
16) Inguma                         35) sqlsus
17) inviteflood                    36) THC-IPV6
18) jSQL                           37) tnscmd10g			
19) Lynis                          38) unix-privesc-check			
                                   39) Yersinia

0) Install all Vulnerability Analysis tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install af++ -y")
							if opcion2 == "2":
								cmd = os.system("apt-get install bbqsql -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install bed -y")

							elif opcion2 == "4":
								cmd = os.system("apt-get install cisco-auditing-tool -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-global-exploiter -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cisco-ocs -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install cisco-torch -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install copy-router-config -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "10":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "11":
								cmd = os.system("apt-get install doona -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dotdotpwn -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install greenbone-security-assistant -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "15":
								cmd = os.system("apt-get install hexorbase -y")
							elif opcion2 == "16":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif opcion2 == "17":
								cmd = os.system("apt-get install inviteflood -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install jsql -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install lynis -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install nmap -y")
							elif opcion2 == "21":
								cmd = os.system("apt-get install ohrwurm -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install openvas-administrator -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install openvas-cli -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install openvas-manager -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install openvas-scanner -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install oscanner -y")
							elif opcion2 == "27":
								cmd = os.system("apt-get install peass -y")
							elif opcion2 == "28":
								cmd = os.system("apt-get install powerfuzzer -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install sfuzz -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install sidguesser -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install siparmyknife -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install spike -y")
							elif opcion2 == "33":
								cmd = os.system("apt-get install sqlmap -y")
							elif opcion2 == "34":
								cmd = os.system("apt-get install sqlninja -y")
							elif opcion2 == "35":
								cmd = os.system("apt-get install sqlsus -y")
							elif opcion2 == "36":
								cmd = os.system("apt-get install thc-ipv6 -y")
							elif opcion2 == "37":
								cmd = os.system("apt-get install tnscmd10g -y")
							elif opcion2 == "38":
								cmd = os.system("apt-get install unix-privesc-check -y")
							elif opcion2 == "39":
								cmd = os.system("apt-get install yersinia -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print ('''
		\033[1;36m=+[ Wireless Attacks\033[1;m

1) Aircrack-ng          17) kalibrate-rtl
2) Airgeddon            18) KillerBee			  				
2) Asleap               19) Kismet				
3) Bluelog              20) mdk3				
4) BlueMaho             21) mfcuk			
5) Bluepot              22) mfoc				
6) BlueRanger           23) mfterm				
7) Bluesnarfer          24) Multimon-NG	 			
8) Bully                25) PixieWPS				
9) coWPAtty             26) Reaver			
10) crackle             27) redfang				
11) eapmd5pass          28) RTLSDR Scanner           				
12) Fern Wifi Cracker   29) Spooftooph			
13) Ghost Phisher       30) Wifi Honey			
14) GISKismet           31) Wifitap
16) gr-scan             32) Wifite 

0) Install all Wireless Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install aircrack-ng -y")
							elif opcion2 == "2":
								cmd = os.system("apt-get install airgeddon -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install asleap -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install bluelog -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "6":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "7":
								cmd = os.system("apt-get install blueranger -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install bluesnarfer -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install bully -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cowpatty -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install crackle -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install eapmd5pass -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install fern-wifi-cracker -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install ghost-phisher -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install giskismet -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "18":
								cmd = os.system("apt-get install kalibrate-rt -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install killerbee -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install kismet -y")
							elif opcion2 == "21":
								cmd = os.system("apt-get install mdk3 -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install mfcuk -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install mfoc -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install mfterm -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install multimon-ng -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install pixiewps -y")
							elif opcion2 == "27":
								cmd = os.system("apt-get install reaver -y")
							elif opcion2 == "28":
								cmd = os.system("apt-get install redfang -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install rtlsdr-scanner -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install spooftooph -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install wifi-honey -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install wifitap -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install wifite -y")
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Web Applications\033[1;m

1) apache2              24) Maltego Teeth
2) apache-users         25) PadBuster		
3) Arachni              26) Paros			
4) BBQSQL               27) Parsero
5) beef-xss             28) plecost					
6) BlindElephant        29) Powerfuzzer				
7) Burp Suite           30) ProxyStrike				
8) commix               31) Recon-ng				
9) CutyCapt             32) Skipfish				
10) DAVTest             33) sqlmap				
11) deblaze             34) Sqlninja	 			
12) DIRB                35) sqlsus				
13) DirBuster           36) ua-tester
14) feroxbuster         37) Uniscan			
15) fimap               38) Vega				
16) FunkLoad            39) w3af				
17) Grabber             40) WebScarab
18) Httpx               41) WebSlayer
19) Hydra               42) WebSploit 	
20) Katana              43) Wfuzz	     
21) jboss-autopwn       44) WPScan			
22) joomscan            45) XSSer		
23) jSQL                46) zaproxy
                        	
				
				
					

0) Install all Web Applications tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apache2 -y")
							if opcion2 == "2":
								cmd = os.system("apt-get install apache-users -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install arachni -y")

							elif opcion2 == "4":
								cmd = os.system("apt-get install bbqsql -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install beef-xss -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install blindelephant -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install burpsuite -y")
							elif opcion2 == "8":
								
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cutycapt -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install davtest -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install deblaze -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dirb -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dirbuster -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install feroxbuster -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install fimap -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install funkload -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install grabber -")
							elif opcion2 == "18":
								cmd = os.system("apt-get install httpx-toolkit -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install hydra -y")
							elif opcion2 == "20":
								print("Please download katana from: https://github.com/PowerScript/KatanaFramework")
							elif opcion2 == "21":
								cmd = os.system("apt-get install jboss-autopwn -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install joomscan -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install jsql -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install maltego-teeth -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install padbuster -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install paros -y")
							elif opcion2 == "27":
								cmd = os.system("apt-get install parsero -y")
							elif opcion2 == "28":
								cmd = os.system("apt-get install plecost -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install powerfuzzer -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install proxystrike -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install recon-ng -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install skipfish -y")
							elif opcion2 == "33":
								cmd = os.system("apt-get install sqlmap -y")
							elif opcion2 == "34":
								cmd = os.system("apt-get install sqlninja -y")
							elif opcion2 == "35":
								cmd = os.system("apt-get install sqlsus -y")
							elif opcion2 == "36":
								cmd = os.system("apt-get install ua-tester -y")
							elif opcion2 == "37":
								cmd = os.system("apt-get install uniscan -y")
							elif opcion2 == "38":
								cmd = os.system("apt-get install vega -y")
							elif opcion2 == "39":
								cmd = os.system("apt-get install w3af -y")
							elif opcion2 == "40":
								cmd = os.system("apt-get install webscarab -y")
							elif opcion2 == "41":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
							elif opcion2 == "42":
								cmd = os.system("apt-get install websploit -y")
							elif opcion2 == "43":
								cmd = os.system("apt-get install wfuzz -y")
							elif opcion2 == "44":
								cmd = os.system("apt-get install wpscan -y")
							elif opcion2 == "45":
								cmd = os.system("apt-get install xsser -y")
							elif opcion2 == "46":
								cmd = os.system("apt-get install zaproxy -y")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

1) Bettercap             19) rtpbreak             
2) Burp Suite            20) rtpinsertsound				 	
3) DNSChef               21) rtpmixsound
4) ettercap-graphical    22) sctpscan	
5) fiked                 23) SIPArmyKnife
6) hamster-sidejack      24) SIPp
7) HexInject             25) SIPVicious
8) iaxflood              26) SniffJoke
9) inviteflood           27) SSLsplit
10) iSMTP                28) sslstrip
11) isr-evilgrade        29) THC-IPV6
12) macchanger           30) VoIPHopper
13) mitmproxy            31) WebScarab
14) netsniff-ng          32) Wifi Honey
15) ohrwurm              33) Wireshark
16) protos-sip           34) xspy
17) rebind               35) Yersinia
18) responder            36) zaproxy 
				
			
0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install bettercap -y")
							if opcion2 == "2":
								cmd = os.system("apt-get install burpsuite -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install dnschef -")
							elif opcion2 == "4":
								cmd = os.system("apt-get install ettercap-graphical -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install fiked -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install hamster-sidejack -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install hexinject -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install iaxflood -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install inviteflood -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install ismtp -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "12":
								cmd = os.system("apt-get install macchanger -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install mitmproxy -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install netsniff-ng -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install ohrwurm -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install protos-sip -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install rebind -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install responder -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install rtpbreak -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install rtpinsertsound -y")
							elif opcion2 == "21":
								cmd = os.system("apt-get install rtpmixsound -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install sctpscan -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install siparmyknife -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install sipp -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install sipvicious -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install sniffjoke -y")
							elif opcion2 == "27":
								cmd = os.system("apt-get install sslsplit -y")
							elif opcion2 == "28":
								cmd = os.system("apt-get install sslstrip -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install thc-ipv6 -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install voiphopper -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install webscarab -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install wifi-honey -y")
							elif opcion2 == "33":
								cmd = os.system("apt-get install wireshark -y")
							elif opcion2 == "34":
								cmd = os.system("apt-get install xspy -y")
							elif opcion2 == "35":
								cmd = os.system("apt-get install yersinia -y")
							elif opcion2 == "36":
								cmd = os.system("apt-get install zaproxy -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "6":
							print ('''
\033[1;36m=+[ Maintaining Access\033[1;m

1) CryptCat
2) Cymothoa
3) dbd
4) dns2tcp
5) http-tunnel	
6) HTTPTunnel
7) Intersect
8) metasploit-framework
9) Nishang
10) polenum
11) PowerSploit
12) pwnat
13) RidEnum
14) sbd
15) U3-Pwn
16) Webshells
17) Weevely

0) Install all Maintaining Access tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install cryptcat -y")

							elif opcion2 == "2":
								cmd = os.system("apt-get install cymothoa -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dbd -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dns2tcp -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install http-tunnel -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install httptunnel -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install intersect -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install metasploit-framework -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install nishang -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install polenum -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install powersploit -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install pwnat -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install ridenum -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install sbd -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install u3-pwn -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install webshells -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install weevely -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "7":
							print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote	
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Install all Reporting Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install casefile -y")

							elif opcion2 == "2":
								cmd = os.system("apt-get install cutycapt -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dos2unix -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dradis -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install keepnote -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install magictree -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install metagoofil -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install nipper-ng -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install pipal -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

1) Armitage
2) Backdoor Factory
3) BeEF
4) cisco-auditing-tool
5) cisco-global-exploiter	
6) cisco-ocs
7) cisco-torch
8) commix
9) crackle
10) Fatrat
11) jboss-autopwn
12) Linux Exploit Suggester
13) Maltego Teeth
14) metasploit-framework
15) SET
16) ShellNoob
17) sqlmap
18) THC-IPV6
19) Yersinia

0) Install all Exploitation Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install armitage -y")
							elif opcion2 == "2":
								cmd = os.system("apt-get install backdoor-factory -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install beef-xss -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install cisco-auditing-tool -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-global-exploiter -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cisco-ocs -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install cisco-torch -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("apt-get install crackle -y")
							elif opcion2 == "10":
								cmd = os.system("git clone https://github.com/Screetsec/TheFatRat.git && cd TheFatRat && chmod +x setup.sh && ./setup.sh")
							elif opcion2 == "11":
								cmd = os.system("apt-get install jboss-autopwn -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install linux-exploit-suggester -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install maltego-teeth -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install metasploit-framework -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install set -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install shellnoob -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install sqlmap -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install thc-ipv6 -y")
							elif opcion2 == "":
								cmd = os.system("apt-get install yersinia -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "9":
							print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

1) Binwalk             12) Galleta				
2) bulk-extractor      13) Guymager			
3) Capstone            14) iPhone Backup Analyzer				
4) chntpw              15) p0f				
5) Cuckoo              16) pdf-parser				
6) dc3dd               17) pdfid				
7) ddrescue            18) pdgmail				
8) diStorm3            19) peepdf					
9) Dumpzilla           20) Volatility	
10) extundelete        21) Xplico			
11) Foremost        			
					
					

0) Install all Forensics Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install binwalk -y")
							elif opcion2 == "2":
								cmd = os.system("apt-get install bulk-extractor -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cuckoo -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install dc3dd -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install ddrescue -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "9":
								cmd = os.system("apt-get install dumpzilla -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install extundelete -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install foremost -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install galleta -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install guymager -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install iphone-backup-analyzer -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install p0f -y")
							elif opcion2 == "16":
								cmd = os.system("apt-get install pdf-parser -y")
							elif opcion2 == "17":
								cmd = os.system("apt-get install pdfid -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install pdgmail -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install peepdf -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install volatility")
							elif opcion2 == "21":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10":
							print ('''
\033[1;36m=+[ Stress Testing\033[1;m

1) DHCPig
2) FunkLoad
3) iaxflood
4) Inundator
5) inviteflood	
6) ipv6-toolkit
7) mdk3
8) Reaver
9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		

0) Install all Stress Testing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install dhcpig -y")

							elif opcion2 == "2":
								cmd = os.system("apt-get install funkload -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install iaxflood -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/inundator.git")
							elif opcion2 == "5":
								cmd = os.system("apt-get install inviteflood -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install ipv6-toolkit -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install mdk3 -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install reaver -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install rtpflood -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install slowhttptest -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install t50 -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install termineter -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install thc-ipv6 -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install thc-ssl-dos -y")    				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11":
							print ('''
\033[1;36m=+[ Password Attacks\033[1;m

1) acccheck               21) Maskprocessor
2) Burp Suite             22) multiforcer
3) CeWL                   23) Ncrack	
4) chntpw                 24) oclgausscrack
5) cisco-auditing-tool    25) PACK
6) CmosPwd                26) patator
7) creddump               27) phrasendrescher
8) crunch                 28) polenum
9) DBPwAudit              29) RainbowCrack	
10) findmyhash            30) rcracki-mt
11) gpp-decrypt           31) RSMangler
12) Hashcat               32) seclists
13) hashcat-utils         33) Statsprocessor		
14) hash-identifier       34) THC-pptp-bruter		
15) HexorBase             35) TrueCrack
16) THC-Hydra             36) WebScarab 
17) John the Ripper       37) wordlists 
18) Johnny                38) zaproxy
19) keimpx                 
20) Maltego Teeth    
			

0) Install all Password Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck -y")

							elif opcion2 == "2":
								cmd = os.system("apt-get install burpsuite -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install cewl -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-auditing-tool -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cmospwd -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install creddump -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install crunch -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install findmyhash -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install gpp-decrypt -y")
							elif opcion2 == "12":
								cmd = os.system("apt-get install hashcat -y")
							elif opcion2 == "13":
								cmd = os.system("apt-get install hashcat-utils -y")
							elif opcion2 == "14":
								cmd = os.system("apt-get install hash-identifier -y")
							elif opcion2 == "15":
								cmd = os.system("apt-get install hexorbase -y")
							elif opcion2 == "16":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "17":
								cmd = os.system("apt-get install john -y")
							elif opcion2 == "18":
								cmd = os.system("apt-get install johnny -y")
							elif opcion2 == "19":
								cmd = os.system("apt-get install keimpx -y")
							elif opcion2 == "20":
								cmd = os.system("apt-get install maltego-teeth -y")
							elif opcion2 == "21":
								cmd = os.system("apt-get install maskprocessor -y")
							elif opcion2 == "22":
								cmd = os.system("apt-get install multiforcer -y")
							elif opcion2 == "23":
								cmd = os.system("apt-get install ncrack -y")
							elif opcion2 == "24":
								cmd = os.system("apt-get install oclgausscrack -y")
							elif opcion2 == "25":
								cmd = os.system("apt-get install pack -y")
							elif opcion2 == "26":
								cmd = os.system("apt-get install patator -y")
							elif opcion2 == "27":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "28":
								cmd = os.system("apt-get install polenum -y")
							elif opcion2 == "29":
								cmd = os.system("apt-get install rainbowcrack -y")
							elif opcion2 == "30":
								cmd = os.system("apt-get install rcracki-mt -y")
							elif opcion2 == "31":
								cmd = os.system("apt-get install rsmangler -y")
							elif opcion2 == "32":
								cmd = os.system("apt-get install seclists -y")
							elif opcion2 == "33":
								cmd = os.system("apt-get install statsprocessor -y")
							elif opcion2 == "34":
								cmd = os.system("apt-get install thc-pptp-bruter -y")
							elif opcion2 == "35":
								cmd = os.system("apt-get install truecrack -y")
							elif opcion2 == "36":
								cmd = os.system("apt-get install webscarab -y")
							elif opcion2 == "37":
								cmd = os.system("apt-get install wordlists -y")
							elif opcion2 == "38":
								cmd = os.system("apt-get install zaproxy -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
							print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

1) apktool
2) dex2jar
3) diStorm3
4) edb-debugger
5) jad	
6) javasnoop
7) JD-GUI
8) OllyDbg
9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apktool -y")
							elif opcion2 == "2":
								cmd = os.system("apt-get install dex2jar -y")
							elif opcion2 == "3":
								cmd = os.system("apt-get install python3-diStorm3")
							elif opcion2 == "4":
								cmd = os.system("apt-get install edb-debugger -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install jad -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install javasnoop -y")
							elif opcion2 == "7":
								cmd = os.system("apt-get install JD -y")
							elif opcion2 == "8":
								cmd = os.system("apt-get install OllyDbg -y")
							elif opcion2 == "9":
								cmd = os.system("apt-get install smali -y")
							elif opcion2 == "10":
								cmd = os.system("apt-get install Valgrind -y")
							elif opcion2 == "11":
								cmd = os.system("apt-get install YARA -y")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apktool dex2jar python3-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

1) android-sdk
2) apktool
3) Arduino
4) dex2jar
5) Sakis3G	
6) smali

0) Install all Hardware Hacking tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install android-sdk -y")

							elif opcion2 == "2":
								cmd = os.system("apt-get install apktool -y")

							elif opcion2 == "3":
								cmd = os.system("apt-get install arduino -y")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dex2jar -y")
							elif opcion2 == "5":
								cmd = os.system("apt-get install sakis3g -y")
							elif opcion2 == "6":
								cmd = os.system("apt-get install smali -y")

							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3 -y")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
