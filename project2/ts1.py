import threading
import time
import random
import socket
import re


# todo change server() to server (ip,port) or something and make it runnable with terminal commands in hw instructions.

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50008)
    ss.bind(server_binding)
    ss.listen(1)

    # todo accept connection from host in a loop (test stuff below)

    host = socket.gethostname()
    localhost_ip = (socket.gethostbyname(host))


    dictionary = {}
    with open("PROJ2-DNSTS1.txt", "r") as f:
        for line in f:
            splitLine = line.split()
            dictionary[(splitLine[0])] = ",".join(splitLine[1:])

    csockid, addr = ss.accept()

    while True:
        receivedQuery = csockid.recv(1000)  # might lower this instead of taking stuff in bulk
        if not receivedQuery:
            break
    decodedQuery = receivedQuery.decode()

    for key, value in dictionary.items():
        if decodedQuery.lower() in dictionary:
            # print(dictionary[searchstring])
            d2 = key + " " + dictionary[decodedQuery.lower()]
            d3 = d2.replace(",", " ")
            # d3 = d3 + " IN"    do this in ls
            print(d3)
            csockid.send(d3.encode())

            break
        else:
            break

    # todo check stuff below gives error 'decodedQuery' referenced before assignment

    ss.close()
    exit()


# todo this code below might be changed later on (?)

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
