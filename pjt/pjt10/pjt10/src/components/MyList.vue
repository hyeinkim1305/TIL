<template>
  <li>
    {{ myMovie }}
    <button @click="deleteMyMovie(myMovie)">X</button>
  </li>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MyList',
  props: {
    myMovie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions([
      'deleteMyMovie',
    ])
  }

  

}
</script>

<style>

</style>