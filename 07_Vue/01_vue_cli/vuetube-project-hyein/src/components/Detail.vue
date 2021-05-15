<template>
  <div>
    <iframe :src="youtubeVideoSrc" frameborder="0"></iframe>
    <p>{{ targetVideo.snippet.title }}</p>
    <p>{{ targetVideo.snippet.description }}</p>
  </div>
</template>

<script>
// import _ from 'lodash'

export default {
  name:'Detail',
  props: {
    targetVideo: {
      type: Object,
      required: true
    }
  },
  computed: {
    youtubeVideoSrc: function () {
      const videoId = this.targetVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  // filters: {
  //   stringUnescape: function ()
  // }
}
</script>

<style>

</style>