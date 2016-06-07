from openstack import connection
conn = connection.Connection(auth_url="http://10.85.140.143:5000/v2.0",
                             project_name="Capsule_Corp",
                             username="jamah",
                             password="Cisco123")

def create_network(name, sub_ip, gate_ip):
    print("Create Network:")

    network = conn.network.create_network(
        name=name) 

    print(network)

    subnet = conn.network.create_subnet(
        name=name,
        network_id=network.id,
        ip_version='4',
        cidr=sub_ip,
        gateway_ip=gate_ip) 

    print(subnet)

def create_server(conn):
    print("Create Server:")

    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)
    keypair = create_keypair(conn)

    server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

    print("ssh -i {key} root@{ip}".format(
        key=PRIVATE_KEYPAIR_FILE,
        ip=server.access_ipv4))







create_network(name="VM1", sub_ip="192.168.1.0/24", gate_ip="192.168.1.1")
create_network(name="VM2", sub_ip="10.1.1.0/24", gate_ip="10.1.1.1")



