#!/usr/bin/env python3

import requests
import time

import datetime

def sendData():

	while True:	
		timeStamp = time.time()
		message = f'Send data on {timeStamp}'		
		timeStamp_int = int( timeStamp * 1000 )
		print( message )

		payLoad = {
			"message" : message,
			"@timestamp" : timeStamp_int
		}

		#	Send data
		response = requests.post( 'http://localhost:9200/test-logs-atlv/_doc', json=payLoad )

		if response.status_code == 200 or response.status_code == 201:
			print( response.content )
		else:
			print( f'Something wrong {response.status_code}' )
			print( response.content )	

		time.sleep(1)

try:
	sendData()
except KeyboardInterrupt:
	print( 'exit' )
