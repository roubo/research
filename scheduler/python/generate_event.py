#!/usr/bin/env python
# encoding: utf-8
from time import sleep

event_listeners = {}

def fire_event(name):
    event_listeners[name]()

def use_event(func):
    """python 函数修饰符"""
    def call(*args, **kwargs):
        generator = func(*args, **kwargs)
        # 执行到yield，返回所谓的事件名称
        event_name = next(generator)
        def resume():
            try:
                next(generator)
            except StopIteration:
                pass
        event_listeners[event_name] = resume
    return call

@use_event
def test_work():
    print("=" * 50)
    print("waiting click")
    yield "click"
    print("clicked !!")

if __name__ == "__main__":
    test_work()
    sleep(3)
    # 触发事件
    fire_event("click")
