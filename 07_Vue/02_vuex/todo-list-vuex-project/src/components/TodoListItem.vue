<template>
  <div>
    <!-- this.todo 때문에 todo가 들어가야함 -->
    <span 
    @click="updateTodo(todo)"
    :class="{ completed: todo.completed }"
    >{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
    <!-- completed class 값을 todo의 completed 값에 따라서 속성부여한다.(False면 안들어가게) -->
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    // deleteTodo: function () {
    //   // console.log('Todo 삭제')
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo: function () {
    //   // console.log('수정!')    // console에 나오는지 확인
    //   this.$store.dispatch('updateTodo', this.todo)
    // }
    ...mapActions([
      'deleteTodo',
      'updateTodo',
    ])
  }
}
</script>

<style>
  .completed {
    text-decoration: line-through;
  }
</style>