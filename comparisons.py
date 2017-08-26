# Program to do comparisons in number of attacks

# IDs for SL VS 
id_ibm = [ 
"3003b20c-67ae-11e7-9428-0654b098fe83",  
"4968a73e-67ae-11e7-9428-0654b098fe83",
"b04a1fee-67b0-11e7-9428-0654b098fe83",
"cf0febe8-67b0-11e7-9428-0654b098fe83",
"4fbc59f6-67b2-11e7-9428-0654b098fe83"
]

# IDs for AWS VS
id_aws = [ 
"dc8ac93c-7813-11e7-9428-0654b098fe83",
"08a40324-782a-11e7-9428-0654b098fe83",
"c276c020-782a-11e7-9428-0654b098fe83",
"5a3cc8a0-782b-11e7-9428-0654b098fe83",
"3c186e46-782c-11e7-9428-0654b098fe83"
]


# Import libraries
import pymongo
from pymongo import MongoClient
import pprint
import datetime
import numpy as np
import scipy.stats as stats
import math

# Define Mongo DB access
client = MongoClient()
db = client.mnemosyne
collection = db.hpfeed

# Define json template for hpfeed
hpfeed = {
	"_id" : "59673e953167c67ef223f2a8",
	"ident" : "4968a73e-67ae-11e7-9428-0654b098fe83",
	"timestamp" : "2017-07-13T09:34:12.999Z",
	"normalized" : "true",
	"payload" : { 
		"local_host" : "169.50.175.2",
		"connection_type" : "reject",
		"connection_protocol" : "pcap",
		"remote_port" : 60111,
		"local_port" : 23,
		"remote_hostname" : "",
		"connection_transport" : "tcp",
		"remote_host" : "177.40.229.135"
	 },
	"channel" : "dionaea.connections"
}


print "-"*78
print "Comparing SL and AWS Vulnerability"
print "-"*78

# Total number of records in database
hpfeeds = db.hpfeed
print "\nTotal number of records in database is %d." %hpfeeds.count()

# Define time period to be studied

start = datetime.datetime(2017,7,31,12,0,0)
end = datetime.datetime(2017,8,14,12,0,0) # Two weeks later

num1 = hpfeeds.find({"timestamp": {"$lt": end, "$gte": start}}).count()
print "Total number of attacks for period under study (2 weeks) is %d. " %num1

# Count number of attacks and run test

ibm = np.arange(5)
for i in range(1,6):
  ibm[i-1] = hpfeeds.find({
	"timestamp": {"$lt": end, "$gte": start},
	"ident": id_ibm[i-1]}).count()
print "Total number of attacks on 5 SL machines is %d."  %ibm.sum()
print "Average number of attacks per machine is %.2f." %ibm.mean()

aws = np.arange(5)
for i in range(1,6):
  aws[i-1] = hpfeeds.find({
	"timestamp": {"$lt": end, "$gte": start},
	"ident": id_aws[i-1]}).count()
print "Total number of attacks on 5 AWS machines is %d." %aws.sum()
print "Average number of attacks per machine is %.2f." %aws.mean()
print "2 Tailed T-Test:"

# Two sample t-test
two_sample = stats.ttest_ind(ibm,aws)

print "The t-statistic is %.3f and the p-value is %.3f" %two_sample

two_sample_diff_var = stats.ttest_ind(ibm, aws, equal_var=False)

print "If we assume unequal variances than the t-statistic is %.3f and the p-value is %.3f." % two_sample_diff_var







