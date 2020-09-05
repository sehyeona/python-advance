import time

def perfomance_clock(func):
    # free variable region 
    # func 만 존재
    def perfomance_clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        name = func.__name__
        args_str = ','.join(repr(arg) for arg in args)
        print('[%0.5fs] %s(%s) -> %r'%(end, name, args_str, result))
        return result
    return perfomance_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

@perfomance_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)

# decorator X
non_deco1 = perfomance_clock(time_func)
print(non_deco1)
print(non_deco1.__code__.co_freevars)

# decorator O
print(fact_func(30))