import threading
import time
import random
import socket
import select


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # todo change port etc numbers for adding ts2 as well below (its currently only connecting to ts1)

    # Define the port on which you want to connect to the server
    port = 50008
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    f = open("PROJ2-HNS.txt", "r")
    for item in f:
        cs.send(item.encode())
    f.close()

    # Receive data from the server
    data_from_server = cs.recv(512)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))


    # todo add stuff like Select() and timeout(5) here, also obviously cs.recv(200) stuff

    # todo probably create extra function to forward response we got from ts12 servers here to the client.py client

    cs.close()
    exit()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    print("Done.")
