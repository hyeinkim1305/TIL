# 05_django_homework

1) 

```
동일한 레벨에 작성되어야 유효하지 않다고 판단된 form이 들어왔을 때 실행될 수 있다. request.POST된 데이터를 가지고 create로 가게 된다. 동일한 레벨에 들어가지 않으면 valueerror가 나오게 된다. 
```

2)

```
method가 POST일 때 create.html에서 입력된 데이터가 넘어온 것임을 확인할 수 있기 때문이다. 즉 POST를 먼저 확인해야 새로 입력하겠다는 것인지, 입력된 데이터를 저장해야 하는것인지를 구분할 수 있으며 redirect 혹은 return 해줄 수 있다. 
```

정답 : 

```
Post말고도 다양한 메서드(PUT, DELETE)들이 있기 때문에, POST방식이 왔을 때 이것을 하고 그 외에는 밑에 코드들을 실행해라는 의미
```



