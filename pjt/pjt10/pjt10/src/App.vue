<template>
  <div id="app">
    <!-- <button @click="getMovies">Click</button> -->
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/mymovielist">MyMovieList</router-link>
    </div>
    <router-view/>

  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
// import { mapState } from 'vuex'

const URL = 'https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json'

export default {
  name: 'App',
  created: function () {
    axios.get(URL)
    .then(response => {
      this.$store.dispatch('getMovies', response.data)
      // console.log(response.data)
    })
  },


}

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
