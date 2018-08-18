import csv
import itertools

import zmq
# import random
import sys
import time
# import threading
import datetime
# from threading import Thread

# print(datetime.datetime.now())
def broadcast(arr):
  port = "5556"
  context = zmq.Context()
  socket = context.socket(zmq.PAIR)
  socket.connect("tcp://localhost:%s" % port)
  # msg = socket.recv()
  # print msg
  socket.send(''.join(arr))



cur_time = 0

def fetch_next_item(book, line):
  try:
    aa = next(itertools.islice(csv.reader(book), line, None))
    return aa
  except StopIteration:
    orders = None

def main(order_book_name, trades_book_name, column_name_for_time, speed):
  # order_book = open(order_book_name)
  # trades_book = open(trades_book_name)
  column_name_number_map = {
    "qs_send_time": 0,
    "recorder_recv_time": 1,
    "exch_time": 2
  }
  order_line = 2
  trade_line = 2
  time_column_number = column_name_number_map[column_name_for_time]
  with open(order_book_name, 'r') as order_book:
    with open(trades_book_name, 'r') as trades_book:
      startBroadcast(order_book, trades_book, time_column_number, trade_line, order_line, speed)


def startBroadcast(order_book, trades_book, time_column_number, trade_line, order_line, speed):
  
  global cur_time
  orders = fetch_next_item(order_book, order_line)
  trade = fetch_next_item(trades_book, trade_line)
  # if cur_time==1:
  if int(orders[time_column_number])<int(trade[time_column_number]):
    cur_time = int(orders[time_column_number])
  else:
    cur_time = int(trade[time_column_number])

  while True:
    prev_time = int(round(time.time() * 1000))
    
    while (orders is not None and int(orders[time_column_number])<=int(cur_time)):
      broadcast(orders)
      order_line+=1
      orders = fetch_next_item(order_book, order_line)

    

    while (trade is not None and int(trade[time_column_number])<=int(cur_time)):
      broadcast(trade)
      trade_line+=1
      trade = fetch_next_item(trades_book, trade_line)
    
    # print(order_line)
    # print(trade_line)
    # print("------")
    if (trade is None and orders is None):
      import code; code.interact(local=dict(globals(), **locals()))
      # print(datetime.datetime.now())
      return
    sleep_time =((1/speed) - ((int(round(time.time() * 1000))) - prev_time))/1000
    
    if sleep_time>0:
      # print(sleep_time)
      time.sleep( sleep_time)
    cur_time = int(cur_time) + 1
  

  return


main('/Users/saichander/Downloads/BTC-USD.csv', '/Users/saichander/Downloads/2-BTC-USD.csv', 'qs_send_time', 500)