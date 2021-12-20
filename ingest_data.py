#!/usr/bin/env python3

import requests
import json
import time

payload = {
	"settings": {
		"number_of_shards": 1,
		"number_of_replicas": 0
	}
}

for i in range( 981, 992 ):
	response = requests.put( 'http://localhost:9200/test-index-{:06d}'.format( i ), json=payload )
	if response.status_code == 200:
		print( response.content )
	else:
		print( f'Something wrong : {response.status_code}' )
		print( f'{response.content}' )
	
	time.sleep( 0.1 )