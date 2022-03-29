from telethon import TelegramClient, sync, events
from telethon import functions, types
from telethon.tl import types
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import SessionPasswordNeededError
from time import sleep
from bs4 import BeautifulSoup
import re,sys,os,time,colorama,random,json,threading,itertools,requests,traceback
from telethon.errors import FloodWaitError
from telethon.errors import ChannelsTooMuchError

with open ("cfg.json", "r") as fh:
  json_str = fh.read()
  json_value = json.loads(json_str)
  gruptuyul = json_value["gruptuyulku"]
  keyword = json_value["katakunci"]
 

def mengetik(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random()*0.1)


def tunggu(x):
		sys.stdout.write("\r")
		sys.stdout.write("                                                               ")
		for remaining in range(x, 0, -1):
			 sys.stdout.write("\r")
			 sys.stdout.write("\x1b[1;35mSTATUS VISIT    \x1b[39m: \x1b[1;36mWait \x1b[1;32m{:2d} \x1b[1;36mseconds ".format(remaining))
			 sys.stdout.flush()
			 sleep(1)

banner = "INI BANNER"
os.system("clear")
print(banner)
print ("\x1b[94mCONFIGURATION SETTING \x1b[39m: \x1b[93mAUTO JOIN, VISIT & WD CLICKBOT")

def password ():
	c = requests.Session()
	if not os.path.exists(".password"):
		os.makedirs(".password")
	pw = "nomen"
	if not os.path.exists(".password/password.txt"):
		f = open(".password/password.txt", "w+")
		f.write("File_Ready")
		f.close()
	for i in range(99):
		f = open(".password/password.txt", "r")
		if f.readlines()[0] == pw:
			break
		
		pwin = input("\x1b[1;35mLINK PASSWORD         \x1b[1;36m: https://bit.ly/2UQHGfo\n\x1b[1;35mINPUT PASSWORD        \x1b[1;36m: ")
		if pwin == pw:
			f = open(".password/password.txt", "w+")
			f.write(pwin)
			f.close()
			print("\x1b[1;35mSTATUS                \x1b[1;36m: Correct Password")
			break
		else:
			print("\x1b[1;35mSTATUS                \x1b[1;36m: Wrong Password\n")
			sys.exit()

password()
currency= "doge"
if (currency=="doge") or (currency=="ltc") or (currency=="btc"):
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
else:
	print("\x1b[1;35mSTATUS                \x1b[1;36m: Wrong Input \n")
	sys.exit()
print(colorama.ansi.clear_screen())
done = False

if not os.path.exists("session"):
	os.makedirs("session")

os.system("clear")
ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

def View():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mView Channel Dulu Guys\n")
	channel = "https://t.me/"
	posts = client(GetHistoryRequest(peer=channel,limit=3,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	result = client(functions.messages.GetMessagesViewsRequest(
    peer=channel,
    id=[msg_id],
    increment=True
))

def View1():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mView Channel Dulu Guys\n")
	channel = "https://t.me/"
	posts = client(GetHistoryRequest(peer=channel,limit=3,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[1].id
	result = client(functions.messages.GetMessagesViewsRequest(
    peer=channel,
    id=[msg_id],
    increment=True
))


def Join1():
	channel = 'https://t.me/polkawar'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))
	
def Join2():
	channel = 'https://t.me/polkawarchat'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))
	
def Join3():
	channel = 'https://t.me/AirdropRampage'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))
	
def Start():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mBot {bot}\n")
	client.send_message(entity=bot,message=key)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{key}\n")
	
def Button():
	messages = client.get_messages(bot)
	messages[0].click()
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Button2():
	messages = client.get_messages(bot)
	messages[0].click(2, 0)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Button3():
	messages = client.get_messages(bot)
	messages[0].click(3, 0)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Button4():
	messages = client.get_messages(bot)
	messages[0].click(4, 0)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Button5():
	messages = client.get_messages(bot)
	messages[0].click(5, 0)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Button6():
	messages = client.get_messages(bot)
	messages[0].click(6, 0)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")

def Captcha():
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	message = posts.messages[0].message
	awal = posts.messages[0].message.find(": ")
	akhir = posts.messages[0].message.find("=")
	a = posts.messages[0].message[111:113]
	c = posts.messages[0].message[114]
	b = posts.messages[0].message[116]
	acb = posts.messages[0].message[awal+1:akhir-1]
	client.send_message(entity='@CalcuBot',message=acb)
	posts = client(GetHistoryRequest(peer='@CalcuBot',limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	message = posts.messages[0].message
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mCaptcha: {acb}\n")

def Captcha2():
	sleep(3)
	posts = client(GetHistoryRequest(peer=bot,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	message = posts.messages[0].message
	awal = posts.messages[0].message.find(":")
	akhir = posts.messages[0].message.find("]")
	emoji = posts.messages[0].message[awal+2]
	messages = client.get_messages(bot)
	messages[0].click(text=emoji)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mCaptcha Emoji: {emoji}\n")

def Jawaban():
	posts = client(GetHistoryRequest(peer='@CalcuBot',limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	jwb = posts.messages[0].message.find("=")
	message = posts.messages[0].message
	jawaban = posts.messages[0].message[0:jwb-1]
	client.send_message(entity=bot,message=jawaban)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJawaban: {jawaban}\n")

def Check1():
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	if posts.messages[0].message.find("Thats correct!") != -1:
		sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mCaptcha Done\n")

def Check2():
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	if posts.messages[0].message.find("Wrong answer!") != -1:
		sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mWrong Captcha!\n")
		posts = client(GetHistoryRequest(peer='@CalcuBot',limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
		message = posts.messages[0].message
		answ = posts.messages[0].message[0:3]
		client.send_message(entity=bot,message=answ)


def English():
	msg = '🇫🇰 English'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot,message=msg)

def Home():
	msg = '🌐 Home'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot,message=msg)

def Msg2():
	msg = '✅ Check'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot,message=msg)

def Msg3():
	msg = '☑️ Done'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot,message=msg)





def Wallet():
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	client.send_message(entity=bot,message=wallet,reply_to=msg_id)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mWallet: {wallet}\n")
	
def TrxWallet():
	client.send_message(entity=bot,message=trxwallet)
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mWallet: {trxwallet}\n")
	

	
def Email():
	client.send_message(entity=bot,message=myself.username+"@gmail.com")
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mEmail: {email}\n")
	
	
def UsernameTelegram():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mUsername Telegram\n")
	client.send_message(entity=bot,message="@"+myself.username)
	
def UsernameTwitter():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mTwitter\n")
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	client.send_message(entity=bot,message="@"+myself.username+"69",reply_to=msg_id)
	
def Twitter():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mTwitter\n")
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	client.send_message(entity=bot,message="https://twitter.com/"+myself.username+"69", reply_to=msg_id)
	
def Retweet():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mRetweet\n")
	s = "012345678912345678"
	sr = ''.join(random.sample(s, len(s)))
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	client.send_message(entity=bot,message="https://twitter.com/"+myself.username+"69/status/1"+sr+"?s=19",reply_to=msg_id)
	
def Retweet2():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mRetweet\n")
	s = "012345678912345678"
	sr = ''.join(random.sample(s, len(s)))
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	msg_id = posts.messages[0].id
	client.send_message(entity=bot,message="https://twitter.com/"+myself.username+"69/status/1"+sr+"?s=19",reply_to=msg_id)
	
def Medium():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mMedium\n")
	client.send_message(entity=bot,message="https://www.medium.com/@"+myself.username+"999")
	
def Youtube():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mYoutube\n")
	client.send_message(entity=bot,message="https://www.youtube.com/channel/"+myself.username)
	
def Discord():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mDiscord\n")
	s = "1478"
	sr = ''.join(random.sample(s, len(s)))
	client.send_message(entity=bot,message=myself.username+"#"+sr)
	
def Linkedin():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mLinkedin\n")
	client.send_message(entity=bot,message="https://www.linkedin.com/company/"+myself.username)
	
def Reddit():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mReddit\n")
	client.send_message(entity=bot,message="https://www.reddit.com/user/"+myself.username)
	
def Facebook():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mFacebook\n")
	client.send_message(entity=bot,message="https://www.facebook.com/"+myself.username)
	
def Instagram():
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mInstagram\n")
	client.send_message(entity=bot,message="https://www.instagram.com/"+myself.username)
	
def Lapor():
	posts = client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	if posts.messages[0].message.find("Your referral link ") != -1:
		sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mLaporan\n")
		client.send_message(entity=tuyulku,message=bot+" "+wallet)
	

f= open("list_active.txt")
baris = len (f.readlines())
f.close()

g1= open("0xwallet.txt")
barisg2 = len (g1.readlines())
g1.close()

g2= open("trxwallet.txt")
baris22 = len (g2.readlines())
g2.close()

for i in range(baris):
	f= open("list_active.txt")
	phone_number = f.readlines()[i].strip()
	f.close()
	g1= open("0xwallet.txt")
	wallet = g1.readlines()[i].strip()
	g1.close()
	g2= open("trxwallet.txt")
	trxwallet = g2.readlines()[i].strip()
	g2.close()
	mengetik("INFO AKUN")
	print(f"\x1b[34mYOUR NUMBER     : \x1b[1;36m{phone_number}\n")
	client = TelegramClient('session/'+phone_number, api_id, api_hash)
	client.connect()
	if not client.is_user_authorized():
		try:
			client.send_code_request(phone_number)
			me = client.sign_in(phone_number, input("\x1b[1;35mVERIF CODE      \x1b[39m: \x1b[1;36m"))
		except SessionPasswordNeededError:
			passw = input("\x1b[1;35m2FA CODE        \x1b[39m: \x1b[1;36m")
			me = client.start(phone_number,passw)
		except Exception:
			sleep(3)
	myself = client.get_me()
	try:
		if currency=="doge" :
			channel_entity=client.get_entity("@cctip_bot")
			bot="@PolkawarAirdrop_Bot"
			tuyulku=gruptuyul
			key=keyword
			Start()
			sleep(2)
			Button()
			sleep(2)
			Captcha2()
			sleep(2)
			Button2()
			sleep(2)
			Button2()
			sleep(2)
			UsernameTwitter()
			sleep(2)
			Button()
			sleep(2)
			Retweet()
			sleep(2)
			Button()
			sleep(2)
			Retweet2()
			sleep(2)
			Button()
			sleep(4)
			Wallet()
			sleep(2)
			Button()
			sleep(2)
			Lapor()
			sleep(2)
			Join1()
			Join2()

	except ChannelsTooMuchError as e:
	    sys.stdout.write(
	        "\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mChannel/Group Terlalu Banyak, Harus Leave!\n\n")
	    client.send_message(
	        entity=tuyulku, message="NEED LEAVE CHANNEL UDAH PENUH "+phone_number)
	except FloodWaitError as e:
         waktu = e.seconds
         sys.stdout.write(
            "\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mAkun Kena Flood Harap Tunggu Selama {waktu} detik\n\n")
	except Exception:
		sys.stdout.write("\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mSomething Wrong happened !\n\n")
	finally:
		client.disconnect()
		sleep(3)
