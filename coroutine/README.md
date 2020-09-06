# python coroutine
1. 코루틴 개념
2. 제네레이터 vs 코루틴
3. 코루틴 기초 실습
4. 코루틴 예외 처리
5. yield from 

* yield : 메인 루틴 과 서브 루틴 간의 통신을 가능하게 해준다
* 하나하나 값을 반환해준다. yield 키워드를 만나면 멈춰있다가 다시 next 를 만나면 값을 반환한다.
* 코루틴 제어, 코루틴 상태, 양방향 값 전송
* yield from

## 메인루틴
하나의 흐름, 제일 위부터 차례로 내려오면서 코드를 해석
## 서브루틴 
함수나 클래스등 메인루틴의 흐름에 벗어난 진행되는 코드의 흐름, 예를 들어 메인루틴이 실행되다가 함수를 만나면
서브루틴으로 그 함수를 실행하고 리턴값이 있으면 받아와 다시 메인루틴을 실행한다. 즉 원래라면 return을 통해서 메인루틴으로 돌아온다.  
### 이런 서브루틴을 여러개 실행할 수 있게 하는 것이 yield 함수
왜냐? next를 만난 순간 하나의 값을 반환하고, 그 상태를 유지한체 메인 루틴을 실행한다.   
그러다가 또 next를 만나면 저장되어 있는 서브루틴의 상태를 확인한 후 다음 yield 값 반환   
__즉 yield를 통해 서브루틴의 상태를 보존한채로 메인루틴을 실행할 수 있다__
이런 서브루틴의 상태를 코루틴이라고 한다.
* 서브루틴: 메인루틴에서 잠시 서브루틴으로 갔다가, 리턴에 의해 호출 부분을 돌아와 다시 프로세스
* 코루틴: 루틴 실행중 멈춤 가능, 특정 위치로 돌아갔다가, 다시 원래 위치로 돌아와 수행가능. __동시성 프로그래밍 가능하게함__, 가독성이 매우 낮음  
    코루틴은 스케줄링 오버해드가 매우적다. (하나의 쓰레드에서 적용하기 때문에) 매우 적은 메모리로 왔다갔다
* 쓰레드: 공유되는 자원에 대한 교착 상태가 발생할 가능성이 있기때문에 주의 해야함. 컨텍스트 스위칭 비용발생, 자원이 많이 사용됨.

1. GEN_CREATED: 제네레이터가 만들어진 상태
2. GEN_RUNNING: 현재 활동중
3. GEN_SUSPEND: 제네레이터 정지 상태
4. GEN_CLOSED: 제네레이터 종료
```
from inspect import generatorstatus
```
를 이용하여 상태 확인 가능
```
def coroutine2(x):
    print(f"return: {x}")
    y = yield x
    print(f"received: {y}")
    z = yield x + y
    print(f"received: {z}")
c2 = coroutine2(30)
next(c2)
c2.send(20)
c2.send(30)
```
1. 처음에 코루틴으로 사용할 제네레이터 생성 GEN_CREATED 단계 이때 next를 사용안하면 시작안됨
2. next로 인해 제네레이터 시작 yield x 한 후에 y 값을 받기 위해 대기
3. send(20) 하면 y값을 받고 yield x + y 까지 실행하고  z 값을 받기 위해 대기
4. send(30) 으로 z 값 30을 받고 stopexcetion 적용
```
@coroutine
def sumer():
    total = 0
    number = 0
    while True :
        number =  yield total
        total += number
```
매번 next로 생성된 제네레이터를 실행시켜주는 것이 귀찮기 때문에 데코레이터로 처리해주자

\+ try, except, else, finally
1) else: try 문에서 예외 발생 안하면
2) finally: try 문에서 예외 발생 여부와 상관없이 실행

### 코루틴 제어 관련 메소드들 
1. coroutine.throw(error) : 를 이용해 코루틴에 에러를 던질 수 있음
2. coroutine.close() : 를 이용해 코루틴 종료 가능 GEN_CLOSED 상태로
3. coroutine 에 StopIteration을 except 로 잡아 value를 확인하면 coroutine 안에 넣은 return 값을 받을 수 있다.

### await(yield from)
await에게 코루틴의 흐름을 위임한다. 예제 코드 참고


