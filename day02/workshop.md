# Workshop - Day02

## Problem 1

```python
n = 5
m = 9 

for i in range(m):
    for j in range(n):
        print('*', end='')
    print()
```



## Problem 2

```python
student = {
    'python': 80,
    'algorithm': 99,
    'django': 89,
    'flask': 83,
}

score_sum = 0
for value in student.values():
    score_sum += value

print(score_sum / len(student))
```

```python
score_sum = sum(student.values())
print(score_sum / len(student))
```



## Problem 3

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'A', 'B', 'O', 'B', 'AB']
blood = {}

for blood_type in blood_types:
    if blood_type in blood:
        blood[blood_type] += 1
    else : 
        blood[blood_type] = 1
        
print(blood)
```

