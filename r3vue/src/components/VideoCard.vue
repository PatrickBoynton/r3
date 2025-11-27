<script setup lang="ts">
import { convertToPlayTime, formatDate } from "../utils"

defineProps<{ ipAddress: string }>()
const video = defineModel("video")
</script>
<template>
    <li>
        <h1>{{ video.title }}</h1>
        <hr />
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
    </li>
</template>
<style scoped>
hr {
    border: 2px solid #ffdb60;
    width: 113%;
}

h4:first-of-type {
    margin-top: 20px;
}

span {
    font-weight: bold;
    font-size: 18px;
    color: #ffdb60;
}
</style>
