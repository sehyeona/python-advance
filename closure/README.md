# Closure
1. 파이썬 범수 범위
2. 여러가지 클로저 구현
3. 클로저 속성

## 파이썬 범수 범위
```
b = 1
def func_v1(a):
    print(a)
    print(b)

func_v1(5)
```
함수 안에 없기 때문에 전역 영역을 확인해서 b = 1인 것 확인 후 함수 안에서 사용


```
b = 1
def func_v2(a):
    print(a)
    print(b)
    b = 2

func_v1(5)
```
예외 발생함, 로컬 변수 b 는 할당전에 참조되기 때문에 즉 b를 출력하려고 하는데 지역범위 안에 있음이 check됨   
근데 변수 할당 되기 전에 출력으로 참조되기 때문에 예외가 발생  
밖에 전역변수로 b가 존재하지만, 지역범위 안에 b가 있기 때문에 예외가 발생한다.   
* 같은변수가 있을때 지역변수가 우선
* 어떤 범위에 어떤 변수가 있는지 런타임에 먼저 체크한 다음에 위에서 부터 확인하면서 변수 할당

```
from dis import dis
dis(func_v2)
```
dis 모듈을 이용하면 바이트 코드의 흐름을 확인할 수 있음,  
파이썬 인터프리터 엔진이 우리가 짠 코드를 바이트 바꿔서 라인별로 실행하는데 흐름을 확인할 수 있다. 
```
  9           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP

 10           8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                1 (b)
             12 CALL_FUNCTION            1
             14 POP_TOP

 11          16 LOAD_CONST               1 (2)
             18 STORE_FAST               1 (b)
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE
```
와 같은 결과확인 가능  b의 load가 store보다 우선으로 작동하기 때문에 예외가 발생한다. 

# Closuer(클로저)
### 반환되는 내부 함수에 대해서 선언된 연결 정보를 가지고 참조하는 방식
### 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다. 
```
a = 10
print(a + 10) # 20
print(a + 100) # 110
```
선언된 a 는 print문에서 독립적으로 사용된다.   
결과를 누적할 수 있을까?
```
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        return sum(self._series)/ len(self._series)
avg_cls = Averager()
print(avg_cls(10))
print(avg_cls(60))
```
위의 클래스를 이용해서 누적이 가능한데, 클래스의 인스턴스 변수안에 우리가 추가하는 값을 계속 넣어주고 있기 때문  
하지만 클로저를 이용해서도 똑같은 기능을 구현할 수 있다.

```
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
print(avg_closure1(20))
```
avg_closure1 = closure_avg1() 로 반환된 것은 average 함수임. 반환된 average함수의 유효범위를 벗어난 변수는 즉 series가 된다.   
print(avg_closure(10))과 같은 함수의 사용이 끝나도, 유효범위를 벗어난 변수인 series는 소멸되지 않는다!
#### closure의 이점
1. 전역변수 사용 감소
2. 디자인 패턴 적용
3. 외부에서 보이지 않게 은닉화 가능
```
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)
```
확인해보면 avg_closure1.\_\_code_\_.cofreevarse 를 확인해보면 자기 영역안이 아닌데도, sereies 를 물고 다니는 것을 확인할 수 있다.

```
print("closure:", dir(avg_closure1.__closure__))
print("closure:", avg_closure1.__closure__[0].cell_contents)
```
closure 객체(튜플 형태)와 closure의 첫번째 변수 (즉 series) 안에 컨텐츠 확인가능

### closure 사용 주의점
```
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
```
free variable: 파이썬에서 자유변수는 코드 블럭 안에서 사용은 되었지만, 그 코드블럭에서 정의되지 안흔 변수를 의미한다.

에러 발생 averager 영역에서 cnt+=1 을 한다는 것은 cnt를 선언하고 cnt 에 1을 더한다는 의미 
하지만 averager 에서는 cnt 가 할당 즉 변수에 어떤 값이 할당된 적이 없다.   
따라서 파이썬이 할당전에 참조한다고 판단하여 예외처리를 함.  
위의 series 는 아예 averager 영역에서 아예 할당하려는 움직임이 없었다. 따라서 자연스럽게 바로 위이 영역에서 찾았지만   
cnt += 1 같은 경우는 averager에서 할당하려고 하기때문에 문제가 발생한다. 이 경우 cnt 가 average 영역에서 할당하지 않고 밖에서 찾겠다고 nonlocal을 이용해 선언해 주자

* 추가
```
cnt += 1
``` 
1. cnt 에 1을 더한다.
2. cnt에 cnt + 1 을 선언한다 (할당한다.)
즉 파이썬 인터프리터는 "음... avearge변수 안에 cnt가 할당되긴하는데... 참조한 뒤에 할당이 되는구만?" 으로 이해하고 예외를 내뱉는다.


