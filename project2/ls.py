import threading
import time
import random
import socket
import select


def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # todo bunun aynisini server()'de cs1 ve cs2'yle yap
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    msg = " Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))



    dictionary = {}
    with open("PROJ2-DNSTS1.txt", "r") as f:
        for line in f:
            splitLine = line.split()
            dictionary[(splitLine[0])] = ",".join(splitLine[1:])


    while True:
        everything = csockid.recv(4000)
        if not everything:
            break
        parts = everything.decode()

        #todo THIS PARTTTT
        #print(parts)   # this prints everything properly
        for key, value in dictionary.items():
            if parts.lower() in dictionary:
                # print(dictionary[searchstring])
                d2 = key + " " + dictionary[parts.lower()]
                d3 = d2.replace(",", " ")
                # d3 = d3 + " IN"    do this in ls
                # change top part maybe? it has 1 ,
                print(d3)  # todo THIS DOESNT PRINT   (Q_Q)
                # send response here with cs.send(d2.encode())
                break
            else:
                break




    # Close the server socket
    ss.close()
    exit()


# todo bottom part is test might delete later



if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    print("Done.")
