# Workshop - Day13

## Problem 1

- 이름이 'classroom' 인 프로젝트를 생성하시오
  - VS Code Extensions 에서 `Python` 과 `Django` 설치
  - .vscode/settings.json 수정을 통한 환경세팅

```python
{
    // 파이썬 환경 선택 => 자동으로 해줌
    "python.pythonPath": "venv\\Scripts\\python.exe",

    // Django 에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    // django-html 에서도 html emmet 을 적용
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html 에서 tab size 를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    }
}
```

  - 프로젝트 생성

    ```bash
    (venv)
    $ django-admin startproject django_intro .
    
    $ python manage.py runserver
    ```

    

## Problem 2

- ‘/info' 의 주소로 접속했을 때 , 다음과 같이 반의 정보를 보여주는 페이지를 만드시오

  - application 생성 

  ```bash
  (venv)
  $ python manage.py startapp pages
  ```

  - urls.py에서 path 추가

   ```python
  urlpatterns = [
      path('info/', views.info),
  ]
   ```
  
  - application에 views.py에 info 모듈 추가 
  
  ```python
  def info(request):
  	return render(request, 'info.html')
  ```
  
  - info.html 생성 및 작성
  
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
    <h1>우리반 정보</h1>
    <h2>Teacher</h2>
    <ul>
     <li>NAME</li>
    </ul>
    <h2>Student</h2>
    <ul>
     <li>홍길동</li>
     <li>김길동</li>
     <li>박길동</li>
    </ul> 
  </body>
  </html>
  ```
  
  

## Problem 3

- ‘/student/<학생이름>' 의 주소로 접속했을 때 , 다음과 같이 학생의 이름과 나이를
  보여주는 페이지를 만들어 주세요

  - urls.py 작성

  ```
  urlpatterns = [
      path('student/<str:name>/<int:old>', views.student),
  ]
  ```

  - application에 views.py에 student 모듈 추가 

  ```python
  def student(request, name, old):
      context = {
          'name': name,
          'old': old,
      }
  	return render(request, 'student.html', context)
  ```

  - info.html 생성 및 작성

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
    <h1>이름 : {{ name }}</h1>
    <h2>나이 : {{ old }}</h2>
  </body>
  </html>
  ```

  

