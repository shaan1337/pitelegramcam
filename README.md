# pitelegramcam
Security camera built on Raspberry Pi using:
* Raspbian
* Motion-MMAL
* Telegram Bot API
* python-telegram-bot

Hardware required:
* Raspberry Pi
* Pi NoIR camera
* Infrared illuminator (preferably 48 infrared LED or more)

#Dependencies
* sudo apt-get update
* sudo apt-get install python-pip
* sudo pip install python-telegram-bot
* sudo apt-get install motion
* sudo apt-get remove motion  
* sudo apt-get install libjpeg62

#Setup
* cd /home/pi/
* git clone https://github.com/shaan1337/pitelegramcam.git
* chmod +x pitelegramcam/security/*.sh
* chmod +x pitelegramcam/security/scripts/*.py
* chmod +x pitelegramcam/security/motion
* Using a text editor (e.g. nano) edit the file ./pitelegramcam/security/scripts/myconfig.py and put your Telegram bot token and user chat id
* ./pitelegramcam/security/start.sh
