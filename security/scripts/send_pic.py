#!/usr/bin/python

import sys
import telegram
import myconfig

def main(argv):
	with open ("states/active", "r") as myfile:
    		data=myfile.read()
		if data!="1":
			sys.exit(0)

	bot = telegram.Bot(token=myconfig.token)
	picture = sys.argv[1]
	bot.sendPhoto(chat_id=myconfig.chat_id, photo=open(picture,'rb'))

if __name__ == "__main__":
   main(sys.argv[1:])
