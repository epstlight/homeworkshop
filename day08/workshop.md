

# Workshop - Day8

## Problem 1

- Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’ 페
  이지를 만들어보세요.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    work_book = {
        'apple': 'apple은(는) 사과',
        'banana': 'banana은(는) 바나나',
    }
    
    if word in work_book:
        result = work_book[word]
    else:
        result = f'{word}은(는) 나만의 단어장에 없는 단어입니다!'
        
    return result

if __name__ == "__main__":
    app.run(debug=True)
```



