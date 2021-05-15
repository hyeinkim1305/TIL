<template>
  <div>
    <h2>Child</h2>
    <input type="text" @input="childChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
  },
  methods: {
    childChange: function (event) {
      this.$emit('child-change', event.target.value)
    }
  }
}
</script>

<style>

</style>