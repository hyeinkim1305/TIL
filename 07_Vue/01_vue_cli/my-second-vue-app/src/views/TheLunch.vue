<template>
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneLunchMenu">메뉴추천!</button>
    <p>오늘의 점심 메뉴 추천 : {{ selectedLunchMenu }}</p>
    <!-- v-model로만 하면 string으로 넘어가니까 .number추가 -->
    <!-- v-model은 HTML form 요소의 값과 data를 양방향 바인딩 -->
    <input v-model.number = "lottoNum" type="text" placeholder="추천받을 번호의 갯수를 입력하시오">
    <button @click="setLottoNum">Get my Lotto!</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['간장계란밥', '볶음밥', '치킨'],
      selectedLunchMenu: '',
      lottoNum: '',
    }
  },
  methods: {
    pickOneLunchMenu: function () {
      this.selectedLunchMenu = _.sample(this.lunch)
      
    },
    setLottoNum: function () {
      this.$router.push({ name: 'TheLotto' , params: { lottoNum: this.lottoNum }})
    }

  }
}
</script>

<style>

</style>