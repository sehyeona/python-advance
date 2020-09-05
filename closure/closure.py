b = 1
def func_v1(a):
    print(a)
    print(b)

func_v1(5)

def func_v2(a):
    print(a)
    print(b)
    b = 2

# func_v1(5)

from dis import dis
print(dis(func_v2))

class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        return sum(self._series) / len(self._series)
avg_cls = Averager()
print(avg_cls(10))
print(avg_cls(60))
print(avg_cls(20))

def closure_avg1():
    # Free variable region
    series = []
    # closure 영역
    def average(v):
        series.append(v)
        return sum(series) / len(series)
    return average

avg_closure1 = closure_avg1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(60))

print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)
print("closure:", dir(avg_closure1.__closure__))
print("closure:", avg_closure1.__closure__[0].cell_contents)


def closure_avg2():
    #free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager





