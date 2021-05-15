<template>
  <div>
    <h2>Parent</h2>
    <input type="text" v-model="parentInputData" @input="parentChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child 
    :appData="appData"
    :parentData="parentInputData"
    @child-change="onchildData"
    />
  </div>
</template>

<script>
import Child from './Child'

export default {
  name: 'Parent',
  components: {
    Child,
  },
  data: function() {
    return { 
      parentInputData: '',
      childData: '',
    }
  },
  props: {
    appData: {
      type: String,
      required: true
    }
  },
  methods: {
    onchildData: function (text) {
      this.childData = text 
      this.$emit('child-change', text)
    },
    parentChange: function(event) {
      this.$emit('parent-change', event.target.value)
    }
  }
}
</script>

<style>

</style>