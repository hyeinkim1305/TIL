# 04_js_homework

### 1. 

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하 는 역할을 한다. => `T`
- XMLHttpRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드 로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다.  => `T`
- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다. => `T`



### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```
'Hello SSAFY가 Call Stack에 들어가고 출력이 되고 setTimeout 함수는 Call Stack을 거쳐 Web API에 들어간다. 그 다움에 Bye SSAFY가 Call stack에 들어가고 출력된다. setTiemout의 function은 Task Queue에 들어갔다가 Event Loop에 의해 Call stack으로 push된 후 출력된다. 
```



### 3. 

- Concurrency : 병행성

  동시에 실행되는 것처럼 보이는 것이다. 물리적으로 병렬이 아니 순차적으로 동작하며 실제로는 Time-Sharing으로 CPU를 나눠 사용한다. 

- Parallelism : 병렬성

  실제로 동시에 작업이 처리되는 것으로 오직 Multi core에서만 가능하다. 

paralelism은 하나의 작업 응답시간을 줄일 수 있다. 내부 하위 작업들을 동시에 수행하기 때문이다. 반면, Concurrency는 단일 작업에 대한 응답시간은 줄일 수 없다. 하지만 한 번에 여러 작업을 처리해서 Throughput을 늘리는 데에 의미가 있다.

