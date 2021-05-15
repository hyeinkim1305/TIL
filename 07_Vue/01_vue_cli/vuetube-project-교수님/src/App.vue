<template>
  <div id="app">
    <h1>My First Vuetube Project</h1>
    <header>    
      <SearchBar @input-change="onInputChange" :videos-length="videos.length" />
    </header>
    <section>
      <VideoDetail :video="selectVideo" />
      <VideoList :videos="videos" @select-video="onSelectVideo" />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

const API_KEY = process.env.VUE_APP_VUETUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      selectVideo: '',
      videos: [],
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

      axios.get(API_URL, { params } )
      // axios({
      //   method: 'get',
      //   url: API_URL,
      //   params,
      // })
      .then(res => {
        // console.log(res)
        // console.log(res.data.items)
        this.videos = res.data.items
        this.selectVideo = this.videos[0]
      })
      .catch(err => {
        console.log(err)
      })
    },
    onSelectVideo: function (video) {
      this.selectVideo = video
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
section,
header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex;
}
</style>
