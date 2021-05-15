<template>
  <div>
    <ul>
      <VideoListItem 
      v-for="(video, idx) in videos" 
      :key="idx"
      :video="video" 
      @get-video="getVideo"
      />

    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'
export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    getVideo: function (object) {
      this.$emit('get-video', object)
    }
  }
}
</script>

<style>

</style>