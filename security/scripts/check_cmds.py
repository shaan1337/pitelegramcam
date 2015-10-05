#!/bin/python

import sys
import telegram
import time
import myconfig

def main(argv):
        bot = telegram.Bot(token=myconfig.token)
	offset = 0

	while True:
		updates = bot.getUpdates(offset=offset)
		for u in updates:
			if(u.message.chat_id==myconfig.chat_id):
				offset = max(offset,u.update_id+1)

				cmd = u.message.text
				if cmd=="/status":
					bot.sendMessage(chat_id=myconfig.chat_id,text=u"Online")
				elif cmd=="/activate":
					state_file = open("states/active", "w")
					state_file.write("1")
					state_file.close()
                                        bot.sendMessage(chat_id=myconfig.chat_id,text=u"Sending of pictures/videos activated")
				elif cmd=="/deactivate":
                                        state_file = open("states/active", "w")
                                        state_file.write("0")
                                        state_file.close()
                                        bot.sendMessage(chat_id=myconfig.chat_id,text=u"Sending of pictures/videos deactivated")
		time.sleep(10)

if __name__ == "__main__":
   main(sys.argv[1:])

