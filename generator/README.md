# python generator
### 마치 발전기로 생산해내듯이 next가 호출 되었을때 마다 하나씩 호출해서 사용
### 하나를 실행하고 다음 상태를 snapshot!! 다음 상태 저장하고 기다림

1. 지능형 리스트, 딕셔너리, 집합 등의 iter 가능한 객체의 데이터 셋이 증가할 경우 메모리 사용량도 같이 증가한다.
이것을 완화하기 위해 사용됨
2. 단위 실행가능한 코루틴을 사용하기 위해
3. 딕셔너리 리스트 를 호출 할때 아주 작은 하나의 값만을 호출

\+ iter 객체인지 확인하는 방법
1. hasattr(object, '__iter__')
2. isInstance(object, collection.abc)

\+ underscore
* 인터프리터(Interpreter)에서 마지막 값을 저장할 때
    1. 파이썬 인터프리터에서 마지막으로 반환된 결과값이 _에 저장된다. 
* 값을 무시하고 싶을 때 (흔히 “I don’t care"라고 부른다.)
* 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
    1. _single_leading_underscore : 하나의 객체 안에서만 사용되는 함수, 메서드, 필드등을 지정할때
    2. single_tailing_underscore_ : 파이썬 예약어나 키워드와의 충돌을 피하기 위하여
    3. __double_leading_underscore : 이는 컨벤션이 아닌 하나의 문법적인 요소로서, 하나의 속성명을 맹글링하여 클래스 속성명간의 충돌을 방지한다
    4. \_\_double_leading_tailing_underscore\__ : 파이썬에서 매직 메서드 등 문법적으로 특별한 기능을 수행
* 국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
* 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때

```
def generator_ex1():
    print("start")
    yield "aaa"
    print("continue")
    yield "BBB"
    print("end")
temp1 = iter(generator_ex1())
temp2 = [x*2 for x in generator_ex1()]
temp3 = (x*2 for x in generator_ex1())
```
temp1 과 temp2 같은 방식으로 제네레이터를 만들어 줄 수 있고 for 문을 돌리거나 next 를 이용하여 인자를 하나하나 뽑아 낼 수 있다.
실제로 빅데이터를 다뤄야하는 상황에 정말 많이 사용됨. pyspark / hadoop등 빅데이터 프레임워크에서 사용됨
```
from itertools
gen1 = itertools.count(1, 2.5)
gen2 = itertools.takewhile(lambda n : n < 1000, intertools.count(1, 2.5))
gen3 = itertools.filterfalse(lambda n : n< 3, [1, 2, 3, 4, 5])
gen4 = itertools.accumulate([x for range(1, 101)])
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
gen6 = itertools.chain(enumerate("ABCDE"))
gen7 = itertools.product("ABCDE", repeat=2)
gen9 = itertools.groupby("AAABBCCCDDDEEE")
```
1. 카운트 제네레이터
2. 특정 조건을 걸어, 조건에 맞을때 까지 진행되는 제네레이터
3. false인 것만 반환하는 재네레이터
4. 특정한 값들의 축적
5. iterable한 데이터를 합친 제네레이터
7. 카르테시안 곱
8. 같은 문자이용 그룹바이



