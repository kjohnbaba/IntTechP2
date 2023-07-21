import threading
import time
import random
import socket


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # testmessage = "hello"

    f = open("PROJ2-HNS.txt", "r")
    for item in f:
        cs.send(item.encode())

    # testmessage.split('\n')
    f.close()

    # Receive data from the server
    data_from_server = cs.recv(512)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    serveroutput = data_from_server.decode('utf-8')

    f = open("RESOLVED.txt", "a")
    f.write(serveroutput)
    f.write('\n')
    f.close()

    # close the client socket
    cs.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    print("Done.")
