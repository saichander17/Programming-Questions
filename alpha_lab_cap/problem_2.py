import csv
import itertools

import zmq
import random
import sys
import time
import threading
import datetime
print(datetime.datetime.now())
def broadcast(arr):
  port = "5556"
  context = zmq.Context()
  socket = context.socket(zmq.PAIR)
  socket.connect("tcp://localhost:%s" % port)
  # msg = socket.recv()
  # print msg
  socket.send(''.join(arr))
  # socket.send("client message to server2")
  # time.sleep(1)

cur_time = 0
def startTimer(speed):
  global cur_time
  cur_time = int(cur_time)+(0.0001*speed)
  # print("speed: ")
  # print(speed)
  threading.Timer(0.0000001, startTimer, [speed]).start()

def rebroadcast_from_files(order_book_name, trades_book_name, column_name_for_time, speed):
  # order_book_name = '/Users/saichander/Downloads/BTC-USD.csv'
  # trades_book_name = '/Users/saichander/Downloads/2-BTC-USD.csv'
  column_name_number_map = {
    "qs_send_time": 0,
    "recorder_recv_time": 1,
    "exch_time": 2
  }
  order_book = open(order_book_name)

  trades_book = open(trades_book_name)
  time_column_number = 0
  time_column_number = column_name_number_map[column_name_for_time]
  with open(order_book_name, 'r') as order_book:
      # N = int(input('What line do you need? > '))
      trades_done=0
      orders_done=0
      order_line = 2
      with open(trades_book_name, 'r') as trade_book:
        trade_line = 2
        # import code; code.interact(local=dict(globals(), **locals()))
        orders = next(itertools.islice(csv.reader(order_book), order_line, None))
        trade = next(itertools.islice(csv.reader(trade_book), trade_line, None))
        cur_time = orders[time_column_number]
        startTimer(speed)
        while True:
          # print("Trade Line No:")
          # print(trade_line)
          # print("Time= ")
          # print(cur_time)
          if (orders[time_column_number] > trade[time_column_number]):
            if (int(trade[time_column_number])>int(cur_time)):
              # print("Program sleeping for ")
              # print(int(trade[time_column_number])-int(cur_time))
              time.sleep((int(trade[time_column_number])-int(cur_time))/(1000.0*speed))
              # print("Awaken")
            broadcast(trade)
            trade_line+=1
            try:
              trade = next(itertools.islice(csv.reader(trade_book), trade_line, None))
            except StopIteration:
              trades_done=1
              break
          else :
            if (orders[time_column_number]<cur_time):
              # print("Program sleeping for ")
              # print(int(trade[time_column_number])-int(cur_time))
              time.sleep((cur_time-orders[time_column_number])/(1000.0*speed))
              # print("Awaken")

            broadcast(orders)
            order_line+=1
            try:
              orders = next(itertools.islice(csv.reader(order_book), order_line, None))
            except StopIteration:
              orders_done=1
              break
        if (trades_done==0):
          while trade:
            # print("Time = ")
            # print(cur_time)
            if (int(trade[time_column_number])>int(cur_time)):
              time.sleep((int(trade[time_column_number])-int(cur_time))/(1000.0*speed))

            broadcast(trade)
            trade_line+=1
            try:
              trade = next(itertools.islice(csv.reader(trade_book), trade_line, None))
            except StopIteration:
              trades_done=1
              break

        if (orders_done==0):
          while orders:
            # print("Time.       =     ")
            # print(cur_time)
            if (int(orders[time_column_number])>int(cur_time)):
              time.sleep((int(orders[time_column_number])-int(cur_time))/(1000.0*speed))

            broadcast(orders)
            # order_line+=1
            # print("Before Try")
            try:
              # print("In Try")
              orders = next(itertools.islice(csv.reader(order_book), order_line, None))
              # print("In Try After orders")
              order_line+=1
            except StopIteration:
              # print("In catch")
              orders_done=1
              break
  print(datetime.datetime.now())
  sys.exit(0)


rebroadcast_from_files('/Users/saichander/Downloads/BTC-USD.csv', '/Users/saichander/Downloads/2-BTC-USD.csv', 'qs_send_time', 10000000)