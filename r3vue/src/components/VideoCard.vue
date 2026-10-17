<script setup lang="ts">
import { convertToPlayTime, formatDate } from "../utils"

defineProps<{ ipAddress: string }>()
const video = defineModel("video")
</script>
<template>
    <li>
        <h1>{{ video?.title }}</h1>
        <div class="details">
          <h4>{{ "tags: " + video?.tags?.name }}</h4>
          <h4>{{ "Category: " + video?.category?.name }}</h4>
          <h4>{{ "video length - " + convertToPlayTime(video.duration) }}</h4>
          <h4>
              <span>uploaded date - </span> {{ formatDate(video.uploaded_date) }}
          </h4>
          <h4>
              <span>number of times picked - </span>
              {{ video.video_status.selection_count }}
          </h4>
         <h4>
              <span>current play time - </span>
              {{ convertToPlayTime(video.video_status.current_play_time) }}
          </h4>
        </div>
    </li>
</template>
<style scoped>
h1 {
    font-size: 50px;
    background-color: #c92a6f;;
    width: 100%;
    color: #201449;
   font-weight: bold;
    height: 5vh;
    text-align: center;
}

h4:first-of-type {
    margin-top: 20px;
}

span {
    font-weight: bold;
    font-size: 20px;
    color: #ffdb60;
}
.details {
  width: 100%;
  text-align: center;
  background-color: #180f36;
}
@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
  li {
    height: 30%;
    padding-right: 20px;
  }
  h1 {
    font-size: 30px;
  }
}
</style>
