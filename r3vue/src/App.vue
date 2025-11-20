<script setup lang="ts">
import { onMounted, ref, watch } from "vue"
import One from "./components/One.vue"
import Two from "./components/Two.vue"
import Requests from "./requests"
import {type Video, type VideoContext} from "./types"

const ipAddress = import.meta.env.VITE_IP_ADDRESS
// Two lists are necessary for the search function to work.
const videos = ref<Video[]>([])
const videoSearchList = ref<Video[]>([])
const video = ref<Video | null>(null)
const videoContext = ref<VideoContext | null>(null)

const search = ref("")

onMounted(async () => {
    const vids = await Requests.getVideos(ipAddress)
    const context = await Requests.getVideoContext(ipAddress)

    videos.value = vids
    videoSearchList.value = vids

    if (context) {
        videoContext.value = context
        video.value = context.current_video
    }
})

watch(search, () => {
    videos.value = videoSearchList.value.filter((video: Video) =>
        video.title.toLowerCase().includes(search.value.toLowerCase()),
    )
})
</script>

<template>
    <div class="container">
        <One
            v-model:search="search"
            :video-context="videoContext"
            v-model:video="video"
            :ipAddress="ipAddress"
            v-model:videos="videos" />

        <Two
            :ipAddress="ipAddress"
            v-model:videos="videos"
            v-model:video="video" />
    </div>
</template>

<style scoped>
.container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
</style>
