#!/usr/bin/env python3

import requests
import json
import time

StartIndex = 710
StopIndex = 770

payload = {
	"settings": {
		"number_of_shards": 1,
		"number_of_replicas": 1
	}
}

for i in range( StartIndex, StopIndex + 1 ):
	response = requests.put( 'http://localhost:9200/test-index-{:06d}'.format( i ), json=payload )
	if response.status_code == 200:
		print( response.content )
	else:
		print( f'Something wrong : {response.status_code}' )
		print( f'{response.content}' )
	
	time.sleep( 0.1 )