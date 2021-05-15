<template>
  <div>
    <h1>MyMovieList</h1>
    <MyListForm/>
    <ul>
    <MyList
    v-for="(myMovie, idx) in myMovies" 
    :key="idx"
    :myMovie="myMovie"
    />
    </ul>
  </div>
</template>

<script>
import MyList from '@/components/MyList.vue'
import MyListForm from '@/components/MyListForm.vue'
import { mapState } from 'vuex'

export default {
  name: 'MyMovieList',
  components: {
    MyList,
    MyListForm,
  },
  computed: {
    ...mapState([
      'myMovies'
    ])
  }

}
</script>

<style>

</style>