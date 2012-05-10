import commands

a,b = commands.getstatusoutput(" curl --insecure -X PUT -H \"Content-Type: text/pson\" -d \"{}\" https://172.16.0.11:8139/production/run/no_key ")
print b
