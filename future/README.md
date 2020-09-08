# concurrent future
* 장점
1. 동시성 개념
2. 비동기 작업
3. TreadPool
4. ProcessPool
5. Block / Non-Block 개념

### netword I/O 관련 작업 동시성 활용 권장
적합한 작업일 경우 순차 진행보다 압도적으로 성능향상  
하지만 파이썬의 GIL로 인해 오히려 순차 실행에서가 더 성능이 좋을 수 있다.


# GIL (global interpreter lock)
CPython에서의 GIL은 Python 코드(bytecode)를 실행할 때에 여러 thread를 사용할 경우, 단 하나의 thread만이 Python object에 접근할 수 있도록 제한하는 mutex 이다.   
그리고 이 lock이 필요한 이유는 CPython이 메모리를 관리하는 방법이 thread-safe하지 않기 때문이다.

* mutex, thread-safe의 개념
* CPython이 메모리를 관리하는 방법  
에 대해서 알아보자

```
import threading
x = 0 # A shared value

def foo(): 
    global x 
    for i in range(100000000): 
        x += 1 
def bar(): 
    global x 
    for i in range(100000000): 
        x -= 1 
t1 = threading.Thread(target=foo) 
t2 = threading.Thread(target=bar) 
t1.start() 
t2.start() 
t1.join() 
t2.join() # Wait for completion

print(x)
```
제대로 작동했다면 0 반환되는 것이 맞아보인다. 하지만 어느 한 thread의 결과가 무시당했기 때문에 의외의 결과가 반환된다.  
이와 같은 오류를 race condition이라고 한다.  
즉 thread-safe 하다는 것은 각각의 thread가 race condition을 일으키지 않고 자신의 일을 잘 수행하는 것을 의미한다.

## mutex   
tread safe 한 코드를 작성하기 위한 방법중 하나가 mutex이다. mutual exclusion  
어떤 thread 가 특정 메모리에서 작업하고 있다면 다른 thread들이 접근할 수 없도록 문을 걸어잠근다. 

어느 한 thread가 최초로 mutex를 가져갔다면 (pthread_mutex_lock을 성공했다면), 그 thread는 그 다음 코드를 계속 진행할 수 있다. 반면, 그 순간 이후로 다른 thread가 mutex를 가져가려고 한다면, 첫 번째로 mutex를 가져간 thread가 그 잠금을 풀 때까지 (pthread_mutex_unlock를 실행할 때까지) 기다려야 한다. 그렇게 mutex의 잠금이 해제되면, 이제서야 두 번째 thread가 mutex를 받아서 다음 코드를 진행할 수 있게 된다.

이렇게 mutex가 보호하고자 하는 변수는 dotstr.sum으로, thread들이 각자의 합을 계산해서 모두 합치는 자리인데, 여기서 race condition이 발생한다면 제대로 총합이 더해질 수 없기 때문에, mutex를 이용해서 이 변수에 동시적인 접근을 막는 것이다.

POSIX thread에 대한 정리는 여기서 그만한다. 
https://computing.llnl.gov/tutorials/pthreads/

출처 : https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython

위와 같은 race condition이 발생하지 않도록 하기 위해 파이썬은 어느한 쓰레드가 특정 메모리에서 작업한다면 다른 쓰레드의 접근을 막는다. 이 것이 GIL

## multiThreading
파이썬의 멀티쓰레딩은 비동기적으로 문제를 아주 빠르게 해결할 수 있는 좋은 솔루션이지만 GIL의 영향을 받기 때문에 몇몇 문제에서는 sequential 보다 더 낮은 성능을 보인다. 
sequential.py 과 threading.py 를 비교해보자

## future
파이썬에서 제공하는 구수준의 쓰레딩 프로세싱 모듈

submit: callable 객체 스케쥴링(실행 얘약) -> future
future: future.result(), future.done(), as_completed(future_list) , future.cancelled 주로 사용