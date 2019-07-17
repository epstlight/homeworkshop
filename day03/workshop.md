# Workshop - Day03

## Problem 1

- Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다.
  따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.
- 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는
  함수 palindrome(word)를 만들어보세요.

```python
def palindrome(word):
    word_list = list(word)
    word_reverse = ('').join(reversed(word_list))
    
    return True if word == word_reverse else False

print(palindrome(input('단어를 입력하세요.:')))
```



