1. To retrieve data with Rest API(pulling from the default mongo db), just run the following command line,
replace X's with your API key which can be find in the setting page of the server:
curl -X GET http://184.173.18.156/api/session/?api_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX&limit=10

	PS: 184.173.18.156 is my server IP, replace that with your own.
	More details about the APIs should be found here:
	https://github.com/threatstream/mhn/wiki/MHN-REST-APIs



	you should see something like:
		{ 
		"destination_ip" : "1.2.3.4", 
		"protocol" : "TCP", 
		"hpfeed_id" : ObjectId("XXXXXXXXXXXXXXXXXXXX"), 
		"timestamp" : ISODate("2015-04-29T06:25:55.712Z"), 
		"source_ip" : "5.6.7.8", 
		"snort" : { 
			"priority" : 2, 
			"header" : "1:2001219:19", 
			"classification" : 4, 
			"signature" : "ET SCAN Potential SSH Scan" 
		}, 
		"source_port" : 54015, 
		"honeypot" : "snort", 
		"identifier" : "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX", 
		"sensor" : "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX", 
		"destination_port" : 22 
		}

2. The above command line retrive data for session. There are 9 differet kinds of data can be retrieved. Please refers to
https://github.com/threatstream/mhn/wiki/MHN's-MongoDB-Collections


3. You can dump the mongo db data in command line too. on your server, enter:
mongoexport --db mnemosyne --collection session > session.json
More info can be found in
https://github.com/threatstream/mhn/wiki/Exporting-Honeypot-Data-from-MHN
