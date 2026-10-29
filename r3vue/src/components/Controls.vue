<script setup lang="ts">
import { convertToPlayTime } from "../utils.ts"
import type { Video } from "../types.ts"
import { onMounted, watch } from "vue"
import Requests from "../requests.ts"

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

const handleResetPlayTime = async () => {
    const updatedVideo = {
        ...video.value!,
        video_status: {
            ...video.value!.video_status,
            current_play_time: 0,
        },
    }
    await Requests.updateVideo(props.ipAddress, updatedVideo)
    video.value = updatedVideo
    window.location.reload()
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
        <button @click="handlePlayToggle">
            <img src="/Play.svg" alt="" />
        </button>
        <h3 class="time">
            {{ convertToPlayTime(currentPlayTime as number) }}
        </h3>
        <input
            type="range"
            name="test"
            id=""
            @change="handleCurrentPlayTime"
            v-model="currentPlayTime"
            min="0"
            :max="video?.duration" />
        <h3 class="time">
            {{
                convertToPlayTime((video?.duration as number) - currentPlayTime)
            }}
        </h3>
        <button @click="handleMuteToggle">
            <img src="/volume-2.svg" alt="" />
        </button>
        <button @click="handleFullScreenToggle">
            <img src="/maximize.svg" />
        </button>
        <button @click="handleResetPlayTime">
            <img src="/rotate-ccw.svg" />
        </button>
    </div>
</template>

<style scoped>
.name {
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    width: 100%;
    margin-left: 20px;
}

h2 {
    font-size: 50px;
    margin-right: 20px;
}

.time {
    display: flex;
    width: 100%;
}

button {
  justify-items: center;
}

input[type="range"] {
    appearance: none;
    width: 150%;
    margin: 20px;
}

input[type="range"]::-webkit-slider-runnable-track {
    height: 30px;
    //background-color: #c92a6f;
    background-image: linear-gradient(#432995, #c92a6f 80%);
}

input[type="range"]::-moz-range-track {
    border: 2px solid #00be88;
    height: 5px;
    background-color: #b19849;
    margin: 0 5px;
}

input[type="range"]::-moz-range-thumb {
    appearance: none;
    border: 2px solid #00be88;
    height: 30px;
    width: 5%;
    border-radius: 20px;
    background-color: #00be88;
    cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    height: 30px;
    width: 30px;
    border-radius: 20px;
    background-color: #00be88;
    background-image: linear-gradient(#432995, #00be88 80%);
}

@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    .name {
        width: 100%;
    }

    h2 {
        font-size: 25px;
        width: 100%;
    }

    button {
        padding: 3px;
        margin: 5px;
        font-size: 25px;
    }

    input[type="range"] {
        width: 200%;
        height: 20px;
    }

    input[type="range"]::-webkit-slider-runnable-track {
        height: 10px;
        background-color: #c92a6f;
    }

    input[type="range"]::-webkit-slider-thumb {
        appearance: none;
        border: 5px solid #ffdb60;
        height: 10px;
        width: 10px;
        border-radius: 20px;
        background-color: #432995;
    }
}
</style>
