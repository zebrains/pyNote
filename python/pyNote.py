import json, urllib2

def Balance():
	jsondata = {"jsonrpc": "2.0", "method": "getbalance", "params": {} }
	jsondata = json.dumps(jsondata)
	response = urllib2.urlopen("http://localhost:8082/json_rpc", jsondata)
	print response.read()

Balance()
