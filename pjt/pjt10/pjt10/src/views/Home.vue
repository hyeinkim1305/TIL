<template>
  <div class="container">
    <h1>Home</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCard 
      v-for="(movie, idx) in movies"
      :key="idx"
      :movie="movie"
      />
    </div>
  </div>
  
</template>

<script>
import { mapState } from 'vuex'
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  computed: {
    ...mapState ([
      'movies',
    ])
  }

}
</script>

<style>

</style>