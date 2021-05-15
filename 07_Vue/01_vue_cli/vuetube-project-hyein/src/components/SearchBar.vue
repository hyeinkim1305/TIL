<template>
  <div>
    <input @keyup.enter="onInputChange" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputChange: function (event) {
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>


</style>