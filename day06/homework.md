# Homework - Day06



## Problem 1

- Python은 객체 지향 프로그래밍 언어입니다. Python에서 기본적으로 정의되어
  있는 클래스 5가지만 작성하시오.

  **int, range, list, dict, tuple**



## Problem 2

- 다음 매직 메서드의 역할을 간단하게 작성하시오.

  - `__init__`

    => 객체 인스턴스를 생성할 때 자동적으로 호출되는 method

  -  `__del__`

    => 객체 인스턴스 삭제 시 자동적으로 호출되는 method

  - `__str__`

    => 객체 인스턴스명을 print시 자동적으로 호출되는 method

  - `__repr__`

    => 객체 인스턴스명을 호출 시 자동적으로 호출되는 method



## Problem 3

- 아래 코드의 ‘.sort()’와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때
  사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트,
  딕셔너리 등을 조작하는 메서드 3가지를 그 역할과 함께 작성하시오.

  ```python
  numbers = [5, 1, 2]
  numbers.sort()
  print(numbers) #[1, 2, 5]
  ```

- `.append`(x)

  list에 element(x)를 list 마지막에 추가하는 method

  ```
  numbers = [5, 1, 2]
  numbers.append(3)
  print(numbers) #[5, 1, 2, 3]
  ```

  

- `.update()`

  dictionary에 값을 제공하는 key, value로 덮어 쓰거나 존재하지 않을 시 추가합니다.

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
  my_dict.update(apple='사과아')
  print(my_dict) # {'apple': '사과아', 'banana': '바나나', 'melon': '멜론'}
  my_dict.update(orange='오렌지')
  print(my_dict) # {'apple': '사과아', 'banana': '바나나', 'melon': '멜론', 'orange': '오렌지'}
  ```

  

- `.insert(i, x)`

  list에 정해진 위치 i에 element(x)를 추가합니다.

  길이를 넘어서는 인덱스의 경우 마지막에 추가합니다.

  ```python
  numbers = [5, 1, 2]
  numbers.insert(1, 2)
  print(numbers) #[5, 2, 2]
  numbers.insert(100, 4)
  print(numbers) #[5, 2, 2, 5]
  ```

  