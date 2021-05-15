<template>
  <div>
    <p>{{ todo }}</p>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  props: {
    todo: {
      type: String,
    }
  }
}
</script>

<style>

</style>