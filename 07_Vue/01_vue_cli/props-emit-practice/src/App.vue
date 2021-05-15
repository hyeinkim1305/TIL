<template>
  <div id="app">
    <h2>App</h2>
    <input type="text" v-model="appInputData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <Parent 
    :appData="appInputData"
    @child-change="onchildData"
    @parent-change="onparentData"
    />
  </div>
</template>

<script>
import Parent from './components/Parent'

export default {
  name: 'App',
  components: {
    Parent
  },
  data: function() {
    return {
      appInputData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onparentData: function (text) {
      this.parentData = text 
    },
    onchildData: function (text) {
      this.childData = text 
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
