from openstack import connection
conn = connection.Connection(auth_url="http://10.85.140.143:5000/v2.0",
                             project_name="Capsule_Corp",
                             username="jamah",
                             password="Cisco123")
def list_images(i_name):

    for image in conn.compute.images():
	i_name = image["name"]

def create_network(net_name, sub_ip, gate_ip):
    print("Create Network:")

    network = conn.network.create_network(
        name=net_name) 

    print(network)

    subnet = conn.network.create_subnet(
        name=net_name,
        network_id=network.id,
        ip_version='4',
        cidr=sub_ip,
        gateway_ip=gate_ip) 

    print(subnet)

def create_server(IMAGE_NAME, FLAVOR_NAME, NETWORK_NAME, SERVER_NAME):
    print("Create Server:")

    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)
    #keypair = create_keypair(conn)

    server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}])
        #, key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

    print("ssh -i root@{ip}".format(
        #key=PRIVATE_KEYPAIR_FILE,
        ip=server.access_ipv4))

def create_router(ROUTER_NAME):
	print("Create Router:")

    	network = conn.network.find_network("public")
	print (network.id)
	router = conn.network.create_router(name=ROUTER_NAME,
	external_gateway_info={"network_id": network.id})
		
	print(router)

#def add_router_interfaces()
	

"""	
im_name = "cirros"
vm_name = "VM1"
fl_name = "m1.tiny"

create_network(net_name=vm_name, sub_ip="192.168.1.0/24", gate_ip="192.168.1.1")
create_server(IMAGE_NAME=im_name, FLAVOR_NAME=fl_name, NETWORK_NAME=vm_name, SERVER_NAME=vm_name)  


vm_name = "VM2"
create_network(net_name=vm_name, sub_ip="10.1.1.0/24", gate_ip="10.1.1.1")
create_server(IMAGE_NAME=im_name, FLAVOR_NAME=fl_name, NETWORK_NAME=vm_name, SERVER_NAME=vm_name)  
"""

r_name = "HFR2"
create_router(r_name)

