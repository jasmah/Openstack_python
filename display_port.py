from openstack import connection
conn = connection.Connection(auth_url="http://10.85.140.143:5000/v2.0",
                             project_name="Capsule_Corp",
                             username="jamah",
                             password="Cisco123")

def delete_port(NAME):
        print("Port:")

        port = conn.network.find_port(NAME)
        print(port)


port_id = raw_input("Enter port ID: ")
delete_port(port_id)

