<template>
  <div id="app">
    <div class="container">
      <h1>My First Youtube Project</h1>
      <SearchBar 
      @input-change="onInputChange"
      />
      <Detail
      :targetVideo="targetVideo"
      />
      <!-- 추가 -->
      <VideoList
      :videos="videos"
      @get-video="getVideo"
      />
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import Detail from './components/Detail.vue'
import VideoList from './components/VideoList.vue'


const API_KEY = process.env.VUE_APP_VUETUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    Detail,
  },
  data: function () {
    return {
      inputValue: '',
      videos: [],
      targetVideo: '',
    }
  },
  methods: {
    onInputChange: function (inputText) {
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios.get(API_URL, { params })
      // axios({
      //   method: 'get',
      //   url: API_URL,
      //   params,
      // })
      .then(res => {
        // console.log(res.data.items)
        // 추가
        this.videos = res.data.items
        // console.log(this.videoList)
        // this.videoList.forEach(element => {
        //   console.log(element.snippet.title)
        // });
      })
      .catch(err => {
        console.log(err)
      })
    },
    getVideo: function(object) {
      this.targetVideo = object
      console.log(this.targetVideo)
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
