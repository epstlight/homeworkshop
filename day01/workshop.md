# Workshop - Day01

## Problem 1

```
n = 5
m = 9
print(('*' * n + '\n') * m, end='')
```



## Problem 2

```
print(print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\''))
```



## Problem 3

```
import math
def equation_calc(a, b, c):
    clac = math.sqrt(b ** 2 - 4 * a * c) 
    X1 = (-b + clac) / (2 * a)
    X2 = (-b - clac) / (2 * a)
    print(f'해는 {X1}, {X2} 입니다.')

equation_calc(1, 4, -21)
```

