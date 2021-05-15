import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
// 위에 거는 새로고침 했을 때 사라지는 거 안하게끔 하는 코드 + plugins 넣기 (로컬스토리지저장됨)

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [
      {
        title: '할일1',
        completed: false,
      },
      {
        title: '할일2',
        completed: false,
      }
    ]
  },
  // mutations는 데이터 조작 역할, 첫번째 인자로 항상 state를 받음  + actions의 commit으로 mutation을 호출하게됨
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      // console.log(state)
      // 1. todoitem이 첫번째로 만나는 요소의 인덱스를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 인덱스 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1)    // 이렇게만 해도 새로운 배열이 생성됨
    },
    UPDATE_TODO: function (state, todoItem) {
      // console.log(state)
      // console.log(todoItem)
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          // return {title: todoItem.title, completed: !todo.completed}
          return { ...todo, completed: !todo.completed}
        }
        return todo
      })
       
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
      // context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
    // crateTodo: function (context, todoItem) {
    //   context.commit('CREATE_TODO', todoItem)
    // }
  },
  // 완료된 투두개수, 진행중인 투두개수 위함
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
    TodosCount: function (state) {
      return state.todos.length
    }
  },
  modules: {
  }
})
