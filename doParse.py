import json

load_profile = open('openvpn-status.log', "r")
read_it = load_profile.read().splitlines()

route_table_index = read_it.index("ROUTING TABLE")

client_list = []
routing_list = []
#client_list starts from 4th row(3 index)
for i in range(3,route_table_index):
    line = read_it[i].split(',')
    client = {}
    client["common_name"] = line[0]
    client["real_address"] = line[1]
    client["bytes_received"] = line[2]
    client["bytes_sent"] = line[3]
    client["connected_since"] = line[4]
    client_list.append(client)

    #route_table starts from route_table_index+2
    j = (route_table_index-3)+2+i
    line = read_it[j].split(',')
    print line
    route = {}
    route["virtual_address"] = line[0]
    route["common_name"] = line[1]
    route["real_address"] = line[2]
    route["last_ref"] = line[3]
    routing_list.append(route)


f = open("parseOutput.txt","a+")
for i in range(0,len(client_list)):
    for j in range(0, len(routing_list)):
        if client_list[i]["real_address"] == routing_list[j]["real_address"] :
            client_list[i]["virtual_address"] = routing_list[j]["virtual_address"]

    # write to file
    line_to_write = json.dumps(client_list[i])
    print line_to_write
    f.write(line_to_write)
    f.write("\n")

f.close()

 
