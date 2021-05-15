<template>
  <div>
    <input type="text" @keyup.enter="addMyMovie" v-model.trim="textInput" list="datalistOptions">
    <datalist id="datalistOptions">
      <option v-for="(movie, idx) in movies" :key="idx" v-bind:value="movie.title"></option>
    </datalist>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyListForm',
  data: function () {
    return {
      textInput: '',
    }
  },
  methods: {
    addMyMovie: function() {
      const text = this.movies.filter(movie => {
        return this.textInput === movie.title
      })
      console.log(text)
      if (text[0].title.length) {
        this.$store.dispatch('addMyMovie', text[0].title)
      }
      this.textInput=''
    }
  },
  computed: {
    ...mapState([
      'movies'
    ])
  }
}
</script>

<style>

</style>