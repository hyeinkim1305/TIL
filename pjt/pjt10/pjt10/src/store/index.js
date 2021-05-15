import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    myMovies: [],
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
    ADD_MY_MOVIE: function (state, movie) {
      state.myMovies.push(movie)
    },
    DELETE_MY_MOVIE: function (state, movie) {
      const index = state.myMovies.indexOf(movie)
      state.myMovies.splice(index, 1)
    }
  },
  actions: {
    getMovies: function({commit}, movies) {
      commit('GET_MOVIES', movies)
    },
    addMyMovie: function({commit}, movie) {
      commit('ADD_MY_MOVIE', movie)
    },
    deleteMyMovie: function({commit}, movie) {
      commit('DELETE_MY_MOVIE', movie)
    }
  },
  modules: {
  }
})
