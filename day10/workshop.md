

# Workshop - Day10

## Problem 1

- 아래의 코드를 작성하여 몇 번째 단락이 빨간색으로 변하는지 확인해보자.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>ex</title>
  <style>
    .ssafy > p:nth-child(2) {
      color: red;
    }
  </style>
</head>
<body>
  <div class="ssafy">
    <h2>어떻게 선택될까?</h2>
    <P>첫번째 단락</P>
    <P>두번째 단락</P>
    <P>세번째 단락</P>
    <P>네번째 단락</P>
  </div>
</body>
</html>
```

생각하는 대로 선택되는가? 

=> **첫번째 단락이 빨간색으로 변한다.**

이번에는 nth-child 대신 nth-of-type를 사용해보고 몇 번째 단락이 파란색으로 변하는지 확인해보자.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>ex</title>
  <style>
    .ssafy > p:nth-of-type(2) {
      color: blue;
    }
  </style>
</head>
<body>
  <div class="ssafy">
    <h2>어떻게 선택될까?</h2>
    <P>첫번째 단락</P>
    <P>두번째 단락</P>
    <P>세번째 단락</P>
    <P>네번째 단락</P>
  </div>
</body>
</html>
```

=> **두번째 단락이 파란색으로 변한다.**


