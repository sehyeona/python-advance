def coroutine1():
    print('>>> coroutine start')
    i = yield
    print('>>> coroutine received : {}'.format(i))

c1 = coroutine1()
print("type of coroutine", type(c1))
next(c1)
# 기본으로 none값을 전달
# next(c1)
# c1.send(100)

def coroutine2(x):
    print(f"return: {x}")
    y = yield x
    print(f"received: {y}")
    z = yield x + y
    print(f"received: {z}")

from inspect import getgeneratorstate
c2 = coroutine2(30)
print(f"status1 : {getgeneratorstate(c2)}")
next(c2)
print(f"status1 : {getgeneratorstate(c2)}")
c2.send(20)
print(f"status1 : {getgeneratorstate(c2)}")
# c2.send(50)

from functools import wraps

def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def sumer():
    total = 0
    number = 0
    while True :
        number =  yield total
        total += number

su = sumer()
print(su.send(1))
print(su.send(2))
print(su.send(3))

class SampleException(Exception):
    '''설명에 사용할 예외 유형'''

def coroutine_except():
    print(">> corutine started")
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print("-> SampleException handled, Continuing...")
            else:
                print(f"-> coroutine received : {x}")
    finally:
        print("-> corutine ending")

exe_co = coroutine_except()
print(next(exe_co))
print(exe_co.send(100))
print(exe_co.send(20))
print(exe_co.throw(SampleException))
print(exe_co.close())

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total/cnt
    return f"Averager : {avg}"

avger = averager_re()
next(avger)
avger.send(10)
avger.send(49)
avger.send(70)
try:
    avger.send(None)
except StopIteration as e:
    print(e.value)

def gen1():
    for i in "AB":
        yield i
    for i in range(1,4):
        yield i

def gen2():
    yield from "AB"
    yield from range(1, 4)

test1 = gen1()
test2 = gen2()
print(next(test1), next(test1), next(test1))
print(next(test2), next(test2), next(test2))

def gen3_sub():
    print("Sub coroutine")
    x = yield 10
    print("Recv :", str(x))
    x = yield 100
    print("Recv :", str(x))
    return "Finish"

def gen4_main():
    yield from gen3_sub()
test3 = gen4_main()
print(next(test3), test3.send(17))
try :
    test3.send("hello")
except StopIteration as e:
    print(e.value)
