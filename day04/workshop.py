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