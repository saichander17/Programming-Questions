import csv
import itertools

import zmq
# import random
import sys
import time
# import threading
import datetime
# from threading import Thread

print(datetime.datetime.now())
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


def broadcast_and_fetch_next_item(item, item_line, book, time_column_number):
  while (item is not None and int(item[time_column_number])<=int(cur_time)):
    broadcast(item)
    item_line+=1
    item = fetch_next_item(book, item_line)
  return [item, item_line]


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
    aa = broadcast_and_fetch_next_item(orders, order_line, order_book, time_column_number)
    orders = aa[0]
    order_line = aa[1]

    aa = broadcast_and_fetch_next_item(trade, trade_line, trades_book, time_column_number)
    trade = aa[0]
    trade_line = aa[1]
    
    if (trade is None and orders is None):
      print(datetime.datetime.now())
      return
    sleep_time =((1.0/speed) - ((int(round(time.time() * 1000))) - prev_time))/1000.0
    if sleep_time>0:
      time.sleep( sleep_time)
    cur_time = int(cur_time) + 1
  

  return


main('/Users/saichander/Downloads/BTC-USD.csv', '/Users/saichander/Downloads/2-BTC-USD.csv', 'qs_send_time', 1)