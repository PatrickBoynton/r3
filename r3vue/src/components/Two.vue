<script setup lang="ts">
import Requests from "../requests"
import VideoCard from "./VideoCard.vue"

const props = defineProps<{ ipAddress: string }>()
const videos = defineModel("videos")
const video = defineModel("video")

const handlePickedVideo = async (vid: any) => {
    video.value = await Requests.getVideo(props.ipAddress, vid)
    videos.value = await Requests.getVideos(props.ipAddress)
}
</script>
<template>
    <div class="two">
        <ul>
            <VideoCard
                :ipAddress="ipAddress"
                @click="handlePickedVideo(video)"
                v-for="video in videos"
                :video="video"
                :key="video.id" />
        </ul>
    </div>
</template>
<style scoped>
.two {
    margin-left: 33%;
}

ul {
    height: 92vh;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
}
li:first-child {
  margin-top: 0;
}

@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    ul {
      height: 89vh;
      width: 100%;
    }
    .two {
        width: 40%;
        margin-left: 340px;
    }
}
</style>
