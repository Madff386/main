import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #yellow
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #green
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #grey

#switches
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #purple
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #orange
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #brown
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #blue



def start_discord_bot(channel):
	if channel == 17:
		with open('token.txt', 'r') as f:
			TOKEN = f.read()
		os.popen(f'python covidbot.py {TOKEN}')

GPIO.add_event_detect(17, GPIO.RISING, callback=start_discord_bot)
