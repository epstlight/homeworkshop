# Workshop - Day15

## Problem 1

- 다음은 ‘Base is everywhere!’이라는 문자를 공유하는 서로 다른 2개의 View를 나타낸
  것이다. 템플릿 확장(Template Extending)을 활용하여 아래와 같이 보여지는 3개의
  html 파일을 작성하시오. (단, ‘base.html’ 파일은 앱 폴더 안의 templates 폴더 안에
  있다고 가정한다.)
  
  - base.html
  
  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <h1>Base is everywhere!</h1>
    {% block content %}
    {% endblock %}
  </body>
  </html>
  ```
  
  - one.html
  
  ```HTML
  {% extends 'base.html' %}
  
  {% block content %}
  <h2>I am ONE!</h2>
  {% endblock %}
  ```
  
  - two.html
  
  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h2>I am TWO!</h2>
  {% endblock %}
  ```
  
  



