#!/usr/bin/env python3

import sys

import requests
import json

import pprint

response = requests.get( 'http://localhost:9200' )
if response.status_code == 200:
	dataDict = json.loads( response.content )
else:
	print( f'Something wrong. [{response.status_code}]' )
	sys.exit( 1 )


#	Cat shard
print( '\n\n#######################################\n\n' )
print( '** Cat shards **\n' )
response = requests.get( 'http://localhost:9200/_cat/shards?v=true' )
if response.status_code == 200:
	print( response.content.decode() )

print( '\n\n#######################################\n\n' )

print( '** Cluster health **\n' )
response = requests.get( 'http://localhost:9200/_cluster/health' )
if response.status_code == 200:
	pprint.pprint( json.loads( response.content ) )


print( '\n\n#######################################\n\n' )

print( '** Cluster stats **\n' )
response = requests.get( 'http://localhost:9200/_cluster/stats?filter_path=indices.shards.*' )
if response.status_code == 200:
	pprint.pprint( json.loads( response.content ) )

print( '\n\n#######################################\n\n' )

allIndex = 0
openIndex = 0
closeIndex = 0

#	Get cluster state
response = requests.get( 'http://localhost:9200/_cluster/state?filter_path=metadata.indices.*.settings.index.number_of*,metadata.indices.*.state' )
if response.status_code == 200:
	dataDict = json.loads( response.content )
	for indexName, infoDict in dataDict['metadata']['indices'].items():
		allIndex += 1
		if infoDict[ 'state' ] == 'open':
			openIndex += int( infoDict['settings'][ 'index' ][ 'number_of_shards' ] )
		else:
			closeIndex += int( infoDict['settings'][ 'index' ][ 'number_of_shards' ] )

print( 'Index status: ' )
print( f'Num open index = {openIndex}' )
print( f'Num close index = {closeIndex}' )
print( f'All index = {allIndex}' )

print( '\n\n#######################################\n\n' )
