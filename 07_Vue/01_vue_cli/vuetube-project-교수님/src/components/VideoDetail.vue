<template>
  <div class="video-detail" v-if="video">
    <div class="video-container">
      <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
    <p>{{ video.snippet.title | stringUnescape }}</p>
    <hr>
    <p>{{ video.snippet.description | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: [String, Object],
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.video-detail {
  width: 70%;
  padding-right: 1rem;
}

.video-container {
  position: relative;
  padding-top: 56%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>