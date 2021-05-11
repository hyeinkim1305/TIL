<template>
  <div>
    <h1>this is about page</h1>
    <NewComponent my-message="this is prop data" @child-input-change="paraengGetChange"/>
  </div>
</template>

<script>
import NewComponent from '@/components/NewComponent.vue'
// import NewComponent from '../components/NewComponent.vue'  
// @ === '/src' 와 같은 것

export default {
  name: 'About',
  components: {
    NewComponent
  },
  methods: {
    parengGetChange: function (textInput) {
      console.log(`이것은 하위 컴포넌트 NewComponent로 부터 받은 ${textInput}이다.`)
    }
  }
}
</script>

<style>

</style>