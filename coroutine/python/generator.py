#/usr/bin/env python
#encoding: utf-8
import random

def get_data() :
  return random.sample(range(10), 3)

def consume() :
  data_sum = 0
  data_item_len = 0
  while True :
    data = yield
    data_item_len += len(data)
    data_sum += sum(data)
    print("The average is {}".format(data_sum/data_item_len))

def produce(consumer) :
  """产生序列集合，传递给消费函数（consumer）"""
  while True :
    data = get_data()
    print("producer data {}".format(data))
    consumer.send(data)
    yield

if __name__ == '__main__' :
  """消费者总是习惯先被创建，然后将消费者告诉给生产者。触发总是由生产者完成"""
  consumer = consume()
  consumer.send(None)
  producer = produce(consumer)

  for _ in range(10) :
    next(producer)

