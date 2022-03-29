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
import re
import sys
import os
import time
import colorama
import random
import json
import threading
import itertools
import requests
import traceback
from captcha2upload import CaptchaUpload
from twocaptcha import TwoCaptcha
import shutil
from telethon.errors import FloodWaitError
from telethon.errors import ChannelsTooMuchError
from telethon.errors import UserBannedInChannelError

with open("cfg.json", "r") as fh:
  json_str = fh.read()
  json_value = json.loads(json_str)
  gruptuyul = json_value["gruptuyulku"]
  targetbot = json_value["targetbotnya"]
  keyword = json_value["katakunci"]
  keyword2 = json_value["katakunci2"]
  curr = json_value["matauang"]


def mengetik(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random()*0.1)


def tunggu(x):
		sys.stdout.write("\r")
		sys.stdout.write(
		    "                                                               ")
		for remaining in range(x, 0, -1):
			 sys.stdout.write("\r")
			 sys.stdout.write(
			     "\x1b[1;35mSTATUS VISIT    \x1b[39m: \x1b[1;36mWait \x1b[1;32m{:2d} \x1b[1;36mseconds ".format(remaining))
			 sys.stdout.flush()
			 sleep(1)


banner = "INI BANNER"
os.system("clear")
print(banner)
print("\x1b[94mCONFIGURATION SETTING \x1b[39m: \x1b[93mAUTO JOIN, VISIT & WD CLICKBOT")


def password():
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

		pwin = input(
		    "\x1b[1;35mLINK PASSWORD         \x1b[1;36m: https://bit.ly/2UQHGfo\n\x1b[1;35mINPUT PASSWORD        \x1b[1;36m: ")
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
currency = "doge"
if (currency == "doge") or (currency == "ltc") or (currency == "btc"):
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
else:
	print("\x1b[1;35mSTATUS                \x1b[1;36m: Wrong Input \n")
	sys.exit()
print(colorama.ansi.clear_screen())
done = False

if not os.path.exists("session"):
	os.makedirs("session")

os.system("clear")
ua = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'


def View():
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mView Channel Dulu Bentar\n")
	channel = "https://t.me/InfoAirdrop1001"
	posts = client(GetHistoryRequest(peer=channel, limit=3, offset_date=None,
	               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
	msg_id = posts.messages[0].id
	result = client(functions.messages.GetMessagesViewsRequest(
    peer=channel,
    id=[msg_id],
    increment=True
))


def View1():
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mView Channel Dulu Bentar\n")
	channel = "https://t.me/InfoAirdrop1001"
	posts = client(GetHistoryRequest(peer=channel, limit=3, offset_date=None,
	               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
	msg_id = posts.messages[1].id
	result = client(functions.messages.GetMessagesViewsRequest(
    peer=channel,
    id=[msg_id],
    increment=True
))


def Join1():
	channel = 'https://t.me/PlayArcadeLand'
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))
	


def Join2():
	channel = 'https://t.me/PlayArcadeLandAnn'
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))
	


def Join3():
	channel = 'https://t.me/GiveawayInspector'
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))


def Join4():
	channel = 'http://t.me/airdropinspector'
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoin {channel}\n")
	client(JoinChannelRequest(channel))


def Start():
	client.send_message(entity=bot, message=key2)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{bot}: {key2}\n")


def Button():
	messages = client.get_messages(bot)
	messages[0].click()
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")


def Button2():
	messages = client.get_messages(bot, limit=1)
	messages[0].click(1, 0)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mClick Button\n")


def Captcha():
	for i in range(50):
		client.send_message(entity=bot, message=key2)
		sys.stdout.write(
		    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mStart Bot: {bot}, Ref: {key2}\n")
		sleep(3)
		posts = client(GetHistoryRequest(peer=bot, limit=1, offset_date=None,
		               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
		media = posts.messages[0].media
		photo = posts.messages[0].photo
		if media is not None:
			client.download_media(media, 'img.jpg')
			sys.stdout.write(
			    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mStart Bypass Captcha\n")
		posts = client(GetHistoryRequest(peer=bot, limit=2, offset_date=None,
		               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
		if posts.messages[0].message.find("Hi") != -1:
			sys.stdout.write(
			    f"\r\x1b[32;1m[\x1b[32;1m-\x1b[32;1m] \x1b[32;1mCaptcha Passed\n")
			break
		else:
			solver = TwoCaptcha('e48fde3e1ad2efc81dd62363fe0')
			result = solver.normal('img.jpg')
			cap = result.get('code')
			sys.stdout.write(
			    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mSending Captcha: {cap}\n")
			client.send_message(entity=bot, message=cap)
			sleep(2)
			posts = client(GetHistoryRequest(peer=bot, limit=2, offset_date=None,
			               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
			posts.messages[1].message.find("Wrong captcha")
			sys.stdout.write(f"\r\x1b[31;1m[\x1b[31;1m-\x1b[31;1m] \x1b[31;1mDone\n")


def Msg1():
	msg = 'Continue'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot, message=msg)


def Msg2():
	msg = 'Submit Details'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot, message=msg)


def Msg3():
	msg = '✅Done'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot, message=msg)


def Msg4():
	msg = '✅Yes'
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{msg}\n")
	client.send_message(entity=bot, message=msg)


def Wallet():
	client.send_message(entity=bot, message=wallet)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mWallet: {wallet}\n")


def Wallet2():
	client.send_message(entity=bot, message=wallet2)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mWallet: {wallet2}\n")


def Email():
	client.send_message(entity=bot, message=myself.username+"@gmail.com")
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mEmail: {email}\n")


def UsernameTelegram():
	usernametelegram = "@"+myself.username
	client.send_message(entity=bot, message=usernametelegram)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mUsername Telegram: {usernametelegram}\n")


def UsernameTwitter():
	usernametwitter = "@"+myself.username+twt
	client.send_message(entity=bot, message=usernametwitter)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mTwitter: {usernametwitter}\n")


def Twitter():
	twitter = "https://twitter.com/"+myself.username+twt
	client.send_message(entity=bot, message=twitter)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mTwitter: {twitter}\n")


def Retweet():
	s = "012345678912345678"
	sr = ''.join(random.sample(s, len(s)))
	retweet = "https://twitter.com/"+myself.username+twt+"/status/1"+sr+"?s=19"
	client.send_message(entity=bot, message=retweet)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mRetweet: {retweet}\n")


def Retweet2():
	s = "012345678912345678"
	sr = ''.join(random.sample(s, len(s)))
	retweet2 = "https://twitter.com/"+myself.username+twt+"/status/1"+sr+"?s=19"
	client.send_message(entity=bot, message=retweet2)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mRetweet: {retweet2}\n")


def Medium():
	s = "109"
	sr = ''.join(random.sample(s, len(s)))
	medium = "https://www.medium.com/@"+myself.username+sr
	client.send_message(entity=bot, message=medium)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mMedium: {medium}\n")


def Youtube():
	huruf = "abdefghijkNOPQRSTVWXYZ"
	yt = ''.join(random.sample(huruf, len(huruf)))
	client.send_message(
	    entity=bot, message="https://www.youtube.com/channel/UC"+yt)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mYoutube: https://www.youtube.com/channel/UC{yt}\n")


def Discord():
	s = "1478"
	sr = ''.join(random.sample(s, len(s)))
	discord = myself.username+"#"+sr
	client.send_message(entity=bot, message=discord)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mDiscord: {discord}\n")


def Linkedin():
	linkedin = "https://www.linkedin.com/company/"+myself.username
	client.send_message(entity=bot, message=linkedin)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mLinkedin: {linkedin}\n")


def Reddit():
	reddit = "https://www.reddit.com/user/"+myself.username+"/"
	client.send_message(entity=bot, message=reddit)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mReddit: {reddit}\n")


def Facebook():
	s = "1234567890"
	sr = ''.join(random.sample(s, len(s)))
	facebook = "https://facebook.com/"+sr
	sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mFacebook\n")
	client.send_message(entity=bot, message=facebook)


def Instagram():
	instagram = "https://www.instagram.com/"+myself.username
	client.send_message(entity=bot, message=instagram)
	sys.stdout.write(
	    f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mInstagram: {instagram}\n")


def Lapor():
	posts = client(GetHistoryRequest(peer=bot, limit=1, offset_date=None,
	               offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
	if posts.messages[0].message.find("Thank you") != -1:
		sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mLaporan\n")
		client.send_message(entity=tuyulku, message=bot+" "+wallet)


f = open("list_active.txt")
baris = len(f.readlines())
f.close()

g1 = open("0xwallet.txt")
barisg2 = len(g1.readlines())
g1.close()

g2 = open("solwallet.txt")
baris22 = len(g2.readlines())
g2.close()

h = open("email.txt")
baris3 = len(h.readlines())
h.close()

for i in range(baris):
	f = open("list_active.txt")
	phone_number = f.readlines()[i].strip()
	f.close()
	g1 = open("0xwallet.txt")
	wallet = g1.readlines()[i].strip()
	g1.close()
	g2 = open("trxwallet.txt")
	wallet2 = g2.readlines()[i].strip()
	g2.close()
	h = open("email.txt")
	email = h.readlines()[i].strip()
	h.close()
	mengetik("============[ YOUR DATA ]============")
	print(f"\x1b[34mYOUR NUMBER     : \x1b[1;36m{phone_number}\n")
	client = TelegramClient('session/'+phone_number, api_id, api_hash)
	client.connect()
	if not client.is_user_authorized():
		try:
			client.send_code_request(phone_number)
			me = client.sign_in(phone_number, input(
			    "\x1b[1;35mVERIF CODE      \x1b[39m: \x1b[1;36m"))
		except SessionPasswordNeededError:
			passw = input("\x1b[1;35m2FA CODE        \x1b[39m: \x1b[1;36m")
			me = client.start(phone_number, passw)
		except Exception:
			sleep(3)
	myself = client.get_me()
	try:
		if currency == "doge":
			tuyulku = gruptuyul
			t = "012"
			twt = ''.join(random.sample(t, len(t)))
			bot = "@ArcadeLand_bot"
			key = keyword
			key2 = keyword2
			Captcha()
			sleep(3)
			Join1()
			sleep(3)
			Join2()
			sleep(3)
			Join3()
			sleep(3)
			Msg1()
			sleep(3)
			Msg2()
			sleep(3)
			Msg3()
			sleep(3)
			Twitter()
			sleep(3)
			Msg3()
			sleep(3)
			Msg4()
			sleep(3)
			Wallet()
			sleep(3)
			Lapor()
			
			
	except ChannelsTooMuchError as e:
	    sys.stdout.write(
	        "\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mChannel/Group Terlalu Banyak, Harus Leave!\n\n")
	    client.send_message(
	        entity=tuyulku, message="NEED LEAVE CHANNEL UDAH PENUH "+phone_number)
	except FloodWaitError as e:
         waktu = e.seconds
         sys.stdout.write(
            "\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mAkun Kena Flood Harap Tunggu Selama {waktu} detik\n\n")
	except UserBannedInChannelError:
		sys.stdout.write("\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mUser Banned Channel !\n\n")
	except Exception:
		sys.stdout.write("\r\x1b[1;35mSTATUS AKUN     \x1b[39m: \x1b[1;36mSomething Wrong happened !\n\n")
	finally:
		client.disconnect()
		sleep(3)
