# Homework - Day01



## 1번문제

```python
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



## 2번문제

```python
a = round(0.1 * 3, 1)
b = 0.3 
print(a == b)
```
```
import math
a = 0.1 * 3
b = 0.3 
print(math.isclose(a, b))
```



## 3번문제

1) 줄바꿈

```
print('\n')
```

2) 탭

```
print('\t')
```

3) \

```
print('\\')
```



## 4번문제

```
name = '철수'
print(f'"안녕, {name}야"')
```



## 5번문제

5) int('3.5')

String 변수인 3.5를 int로 변환할 수 없다.

