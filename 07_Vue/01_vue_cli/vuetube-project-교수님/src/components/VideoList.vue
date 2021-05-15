<template>
  <ul class="video-list list-group">
    <VideoListItem 
    v-for="(video, idx) in videos" 
    :key="idx" 
    :video="video"
    @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import _ from 'lodash'
import VideoListItem from './VideoListItem'

export default {
  name: 'VideoList',
  components:{
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
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
.video-list {
  padding: 0;
  margin: 0;
  list-style-type: none;

  width: 30%;
}
</style>