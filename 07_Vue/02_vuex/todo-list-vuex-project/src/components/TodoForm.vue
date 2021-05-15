<template>
  <div>
    <!-- 엔터누르거나 클릭 누를 때 할일이 추가됨 -->
    <input type="text" v-model="todoTitle" @keyup.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem ={
        title: this.todoTitle,
        completed: false,
      }
      // todoItem의 제목을 공백제거했을 떄도 있다면
      if (todoItem.title.trim()) {
      // this.$store.commit('CREATE_TODO', todoItem)
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = ''
      // console.log('Todo생성')
    }
  }
}
</script>

<style>

</style>