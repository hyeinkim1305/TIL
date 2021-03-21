# 05_django_workshop

### Django Model Form

##### 1)

```
class ReservationForm(forms.ModelForm)
class Meta:
```

2) 

```
else:
	form이하에 context부터가 else문 밖으로 나와있어야한다. 그래야 is_valid()에 걸리지 않은 것들이 context이하 문에 걸리게 된다.
```

3) 

```
(a) : form = ReservationForm(request.POST, instance=reservation)
(b) : form = ReservationForm(instance=reservation)
```

4) 

```
{{ form.as_p }}
```

