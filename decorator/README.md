# Decorator
* 장점
1. 중복 제거, 코드 간결
2. 파이썬에서는 클로저 보다 문법 간결
3. 조합해서 사용 용이
* 단점
1. 디버깅 어려움
2. 에러의 모호함

```
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
```
인자로 받은 func은 free variable 영역에 존재하며, perfomance_clocked 이 클로저로서 작동하며 func을 끌고와 사용한다.

