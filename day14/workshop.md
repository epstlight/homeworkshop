# Workshop - Day14

## Problem 1

- 다음은 임의의 숫자를 입력할 수 있는 Form과, 해당 Form으로부터 넘어온 숫자를 받아
  보여주는 2개의 View를 나타낸 것이다. 아래 이미지를 참고하여 ‘urls.py’, ‘views.py’,
  ‘templates(html)’를 작성하시오.
- urls.py

```python
urlpatterns = [
    path('num/push/', views.num_push),
    path('num/pull/', views.num_pull),
]
```

  - views.py

    ```python
    def num_push(request):
        return render(request, 'num_push.html')
    
    def num_pull(request):
        num = request.GET.get('num')
    context = {
            'num': num,
        }
        return render(request, 'num_pull.html', context)
    ```
    
- templates(html) - num_push.html

  ```html
  <h1>Push Number</h1>
    <form action="/num/pull/">
      <input type="number" name="num">
      <button type="submit">Push!</button>
    </form>
  ```

- templates(html) - num_pull.html

  ```html
  <h1>Pull Number</h1>
  <h2>Pull 해보니 {{ num }}입니다!</h2>
  ```

  



