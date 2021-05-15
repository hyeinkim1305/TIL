<template>
  <div class="search-bar" :style="{ margin: videosLength ? '0' : '40vh 0' }">
    <input @keyup.enter="onInputChange" type="text" placeholder="Search" autofocus>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    videosLength: {
      type: Number
    }
  },
  methods: {
    onInputChange: function (event) {
      // console.log(event)
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>
.search-bar {
  transition: margin 0.5s;
}

.search-bar > input {
  width: 100%;
  padding: 0.5rem;
  font-size: 2rem;
}
</style>