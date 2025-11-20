<script setup lang="ts">
import Requests from "../requests"
import VideoCard from "./VideoCard.vue"

const props = defineProps<{ ipAddress: string }>()
const videos = defineModel("videos")
const video = defineModel('video')

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
    overflow: hidden;
    height: 90vh;
    display: flex;
    justify-content: center;
}

ul {
    overflow: scroll;
}
</style>
