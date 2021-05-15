# 04_vue_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. - => `F`
- mutation은 반드시 state를 수정하기 위해서만 사용되어야 한다. -  => `T`
- mutation은 store.dispatch로, action은 store.commit으로 호출할 수 있다. - => `F`
- state는 data와 동일하고, getters는 computed와 동일한 동작을 한다  => `T`



### 2. Vuex에서 action과 mutation의 역할과, 두 함수의 차이를 서술하시오

[역할]

action

- state를 직접 변경하지 않고 mutations에 정의된 메서드를 호출해서 변경한다.

mutations

- state를 변경한다.

[차이]

action은 데이터 fetch 및 처리 & 가공, 비동기 작업을 한다. mutations는 동기적인 작업을 수행한다. 

actions는 첫번째 인자로 항상 context를 받고 dispatch로 mutations의 메서드를 호출한다. 반면 mutations는 첫 번째 인자로 항상 state를 받고 commit을 통해 호출한다.

