node bigdatanode {
	include repos
	include python26
	include cassandra
#hadoop
}

node "centos56-4.novalocal" inherits bigdatanode {
}
