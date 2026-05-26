<script setup lang="ts">
import { convertToPlayTime } from "../utils.ts"
import Requests from "../requests.ts"
import type { Video } from "../types.ts"
import { onMounted, watch } from "vue"

const props = defineProps<{ ipAddress: string }>()
const videoRef = defineModel("videoRef")
const video = defineModel<Video>("video")
let currentPlayTime = defineModel("currentPlayTime")
let currentTime = defineModel("currentTime")

const handlePlayToggle = () => {
    if (videoRef.value?.paused) {
        videoRef.value.play()
    } else {
        videoRef.value?.pause()
    }
}

const handleFullScreenToggle = () => {
    videoRef.value?.requestFullscreen()
}
const handleMuteToggle = () => {
    videoRef.value.muted = !videoRef.value?.muted
}

const handleResetPlayTime = () => {
    const updatedVideo = {
        ...video.value!,
        video_status: {
            ...video.value!.video_status,
            current_play_time: 0,
        },
    }
    Requests.updateVideo(props.ipAddress, updatedVideo)
    video.value = updatedVideo
    Requests.getVideos(props.ipAddress)
}
onMounted(() => {
    currentTime = videoRef.value?.currentTime
})

watch(currentTime, () => {
    currentTime = videoRef.value?.currentTime
    currentPlayTime = videoRef.value?.currentTime
})

const handleCurrentPlayTime = () => {
    if (videoRef.value) {
        currentTime = videoRef.value?.currentTime
        currentPlayTime = videoRef.value?.currentTime
    }
}
</script>

<template>
    <div class="name">
        <h2>
            {{ video?.title || "Click the RV button or click a video card." }}
        </h2>
        <button @click="handlePlayToggle">P</button>
        <h2 class="time">
            {{ convertToPlayTime(currentPlayTime as number) }}
        </h2>
        <input
            type="range"
            name="test"
            id=""
            @change="handleCurrentPlayTime"
            v-model="currentPlayTime"
            min="0"
            :max="video?.duration" />
        <h2 class="time">
            {{
                convertToPlayTime((video?.duration as number) - currentPlayTime)
            }}
        </h2>
        <button @click="handleMuteToggle">M</button>
        <button @click="handleFullScreenToggle">FS</button>
        <button @click="handleResetPlayTime">RS</button>
    </div>
</template>

<style scoped>
.name {
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    width: 90%;
}

.time {
    width: 100%;
}

input[type="range"] {
    appearance: none;
    width: 150%;
}

input[type="range"]::-webkit-slider-runnable-track {
    border: 2px solid #ffdb60;
    height: 5px;
    background-color: #b19849;
    margin: 0 5px;
}

input[type="range"]::-moz-range-track {
    border: 2px solid #ffdb60;
    height: 5px;
    background-color: #b19849;
    margin: 0 5px;
}

input[type="range"]::-moz-range-thumb {
    appearance: none;
    border: 2px solid #ffdb60;
    height: 20px;
    width: 5%;
    border-radius: 20px;
    background-color: #201449;
    cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    border: 2px solid #ffdb60;
    height: 20px;
    width: 20px;
    border-radius: 20px;
    background-color: #201449;
}
</style>
