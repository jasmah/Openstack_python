import json
from openstack import connection
conn = connection.Connection(auth_url="http://10.85.140.143:5000/v2.0",
                             project_name="GVE",
                             username="jamah",
                             password="Cisco123")


print("List Images:")

for image in conn.compute.images():
	keys = image.keys()
	for x, index in enumerate(keys): 
		if index == "name":
			print "%s | %s\n" % (keys[x], image[index])

print("List Servers:")
for server in conn.compute.servers():
	keys = server.keys()
	for x, index in enumerate(keys): 
		print "%s | %s\n" % (keys[x], server[index])



