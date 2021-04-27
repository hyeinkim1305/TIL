# 16_django_homework



### 1. 

```
T
F -> PUT과 DELETE도 있다.
T
F -> CREATE는 HTTP METHOD로 정의한다.
```



### 2. 

```
200 : 요청이 성공적으로 수행됨
400 : Bad request, 사용자의 잘못된 요청 처리 불가
401 : Unauthorized 인증이 필요한 페이지 요청 (너가 누군지 모르겠다)
403 : Forbidden 접근 금지라서 차단 (너가 누군지는 아는데 여기 차단됨)
404 : Not found 요청한 페이지 없음
500 : Internal server error 내부 서버 오류
```



### 3. 

```python
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'
```



### 4. 

```
serializer 는 queryset과 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 또는 다른 콘텐츠 유형으로 쉽게 변환할 수 있다. 
Serializers 는 QuerySet 과 Model 같은 복잡한 데이터를 Python 데이터 타입으로 변환하여 준다.
```



