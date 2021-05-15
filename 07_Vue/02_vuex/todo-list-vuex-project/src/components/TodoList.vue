<template>
  <div>
    <!-- <TodoListItem v-for="(todo, idx) in $store.state.todos" :key="idx"/> -->
    <TodoListItem 
      v-for="(todo, idx) in todos" 
      :key="idx"
      :todo="todo"
    />
    <!-- :todo="todo" 에서 props에서 받는 이름은 왼쪽 todo 인것 -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'


export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // },
    // mapstate의 역할 : computed와 state를 연결, 매핑
    // mapGetters의 역할 : Computed와 getters 매핑
    ...mapState ([
      'todos',
    ])
  }

}

// Component
// 1. 불러온다
// 2. 불러온 걸 등록한다
// 3. 등록한 걸 사용한다.

</script>

<style>

</style>

