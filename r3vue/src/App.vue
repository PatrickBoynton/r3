<script setup lang="ts">
import { onMounted, ref, watch } from "vue"
import One from "./components/One.vue"
import Two from "./components/Two.vue"
import Requests from "./requests"
import { type Video } from "./types"

const ipAddress = import.meta.env.VITE_IP_ADDRESS
// Two lists are necessary for the search function to work.
const videos = ref<Video[]>([])
const videoSearchList = ref<Video[]>([])
const video = ref<Video | null>(null)

const search = ref("")

onMounted(async () => {
    const vids = await Requests.getVideos(ipAddress)
    const context = await Requests.getVideoContext(ipAddress)

    videos.value = vids
    videoSearchList.value = vids

    if (context) {
        video.value = context
    }
})

watch(search, () => {
    videos.value = videoSearchList.value.filter((video: Video) =>
        video.title.toLowerCase().includes(search.value.toLowerCase()),
    )
})

// Emitters
const handleRandomVideo = (rv: Video) => {
    video.value = rv
}

const handlePickedVideo = (pv: Video | null) => {
    video.value = pv
}

const handleSearch = (st: any) => {
    search.value = st
}
</script>

<template>
    <div class="container">
        <One
            :video="video"
            :search="search"
            @getRandomVideo="handleRandomVideo"
            @search="handleSearch"
            :ipAddress="ipAddress" />

        <Two
            :ipAddress="ipAddress"
            :videos="videos"
            :video="video"
            @getVideo="handlePickedVideo" />
        <!-- Modal -->
        <Three />
    </div>
</template>

<style scoped>
.container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
</style>
