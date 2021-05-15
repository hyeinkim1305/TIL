<template>
  <!-- getVideo 추가 -->
  <li @click="getVideo">
    <img :src="youtubeImageSrc" alt="youtube-thumbnail">
    {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    getVideo: function () {
      this.$emit('get-video', this.video)
      // console.log(this.video.snippet)
    }
  }
}
</script>

<style>

</style>