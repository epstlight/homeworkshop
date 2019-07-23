# Homework - Day05



## Problem 1

- 아래와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를
  실행할 수 있도록 하는 import 구문을 (A), (B), (C)를 채워 넣어 완성하시오



- **fibo,py**

```python
	def fibo_recursion(n):
        if n < 2:
            return n
        else: 
            return fibo_recursion(n-1) + fibo_recursion(n-2)
```



```python
from fibo import fibo_recursion as recursion
recursion(4)
```



## Problem 2

- 다음 에러들이 어떠한 경우에 발생하는지 간단하게 작성하시오.

  - ZeroDivisionError

    => 어떤한 수를 0으로 나눌 때 발생하는 오류

  -  NameError

    => 정의되지 않은 변수를 호출할 경우 발생하는 오류

  -  TypeError

    => 연산이나 함수가 부적절한 type의 객체에 적용될 때 발생하는 오류

  -  IndexError

    => index 범위에서 벗어날 때 발생하는 오류

  -  KeyError

    => dictionary의 key가 기존 키 집합에서 발견되지 않을 때 발생하는 오류

  -  ModuleNotFoundError

    => import한 module을 찾을 수 없을 때 발생하는 오류 

  -  ImportError

    => import문이 모듈을 로드하는데 문제가 있을 때 발생하는 오류, 

