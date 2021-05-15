<template>
  <div>
    <h1>TodoList.vue</h1>
    <!-- <Todo /> -->
    <!-- <Todo v-for="(todo, idx) in todos" :key="idx" :todo="todo"/> -->
    <TodoListItem />
  </div>
  
  
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // data: function () {
  //   return {
  //     todos: ["Todo.vue", "Todo.vue", "Todo.vue" ]
  //   }
  // }
}
</script>

<style>

</style>