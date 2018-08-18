import time
import datetime
cur_time = 0
def startTimer():
  prev_time = int(round(time.time() * 1000))
  global cur_time
  cur_time = int(cur_time)+1
  # print("speed: ")
  # print(speed)
  # threading.Timer(0.0000001, startTimer, [speed]).start()
  # import code; code.interact(local=dict(globals(), **locals()))
  time.sleep(1 - (int(round(time.time() * 1000)) - prev_time))
  # print (datetime.datetime.now() + prev_time)
  startTimer()

startTimer()




# startBroadcast(order_book, trades_book, time_column_number, trade_line, order_line, speed)
  # threading.Timer(0.001/speed, startBroadcast, [order_book_name, trades_book_name, time_column_number, trade_line, order_line, speed]).start()
  # startBroadcast(order_book, trades_book, time_column_number, trade_line, order_line, speed)
  

  # thread = Thread(target=startBroadcast, args=(order_book, trades_book, time_column_number, trade_line, order_line, speed))
  # thread.start()
  # while thread.isAlive() is True:
  #   1+1