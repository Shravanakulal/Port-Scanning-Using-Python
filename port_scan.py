import socket

ip = "localhost"
port_list = [20, 80, 8080, 139, 445, 23, 21, 22]


for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result =s.connect_ex((ip, port))


    if result == 0:
        print('-' * 60)
        print("port:" , port, "open")
        print('-' * 60)
    else:
        print("port:" , port, "closed")
