# Workshop - Day04

## Problem 1

- 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요.

```python
def sqrt(x):
    lnum = 1
    rnum = (lnum + x ) /2

    while(round(rnum, 3) != round(lnum, 3)):
        mnum = (lnum + rnum) / 2
        if mnum ** 2 > x:
            rnum = mnum
        else:
            lnum = mnum
            
    return round(rnum, 3)
        
print(sqrt(int(input('양의 정수: '))))
```



