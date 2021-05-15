<template>
  <li class="list-group-item" @click="selectVideo">
    <img v-bind:src="youtubeImageSrc" alt="youtube-thumbnail-image">
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
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
.list-group .list-group-item {
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
}

.list-group .list-group-item:hover {
  background: #eee;
}

.list-group .list-group-item img {
  height: fit-content;
  margin-right: 0.5rem;
}
</style>