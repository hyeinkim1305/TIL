<template>
  <div class="container">
    <h1>Random</h1>
    <button @click="randomMovie">Pick</button>
    <div class="card mb-3" v-if="movie.title" id="imagesize">
      <img :src="movieImage" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import _ from 'lodash'

export default {
  name: 'Random',
  data: function () {
    return {
      movie: {},
    }
  },
  computed: {
    ...mapState([
      'movies'
    ]),
    movieImage: function() {
      return 'https://image.tmdb.org/t/p/w500'+ this.movie.poster_path
    }
  },
  methods: {
    randomMovie: function () {
      const movie = _.sample(this.movies)
      this.movie = movie
    }
  }

}
</script>

<style>
#imagesize {
  width: 400px;
  height: 500px;
}
  

</style>