# 01_vue_homework



### 1. 

- SPA는 Single Pattern Application의 약자이다. => `F, single page aplication이다. `
- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이 지 갱신에 필요한 데이터만 전달받는다. => `F`
- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업 데이트되는 것을 의미한다 => `T`



### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시 오

Model, View, View Model의 약자이다. 

- Model : Vue Instance 내부에서 data로 사용되는데 이 값이 바뀌면 View가 반응한다.
- View : data의 변화에 따라서 바뀌는 대상
- ViewModel : View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리



### 3. 

(a) : message

(b) : new Vue

(c) : #app



### 4. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

- 동일한 요소에 v-for와 v-if 두 디렉티브가 함께 작성된 경우,  매 반복 시에 v-if의 조건문으로 요소의 렌더링 여부를 결정한다. => `F`
- v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다. => `F`
- v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다. => `F`



### 5. computed와 watch의 개념과 그 차이에 대해서 간단히 서술하시오.

- computed : 함수의 형태로 정의하지만 함수가 아닌 함수의 반환 값이 바인딩 된다. 

- watch : 특정 데이터의 변화 상황에 맞춰 다른 data등이 바뀌어야 할 때 주로 사용한다.

  computed는 종속된 대상이 변경될 때만 함수를 실행한다. 하지만 watch는 데이터에 변화가 일어났을 때 실행된다. 

  

### 6. 다음은 홀수 데이터만 렌더링하는 Vue Application의 예시이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오

(a) : v-for

(b) : index 

(c) : nums