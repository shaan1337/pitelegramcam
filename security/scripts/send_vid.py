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
	video = sys.argv[1]
	bot.sendDocument(chat_id=myconfig.chat_id, document=open(video,'rb'))

if __name__ == "__main__":
   main(sys.argv[1:])
