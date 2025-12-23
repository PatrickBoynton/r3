<script setup lang="ts">
import { convertToPlayTime } from "../utils.ts"

const videoRef = defineModel("videoRef")
const video = defineModel("video")
const currentPlayTime = defineModel("currentPlayTime")

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
</script>

<template>
    <div class="name">
        <h2>
            {{ video?.title || "Click the RV button or click a video card." }}
        </h2>
        <button @click="handlePlayToggle">P</button>
        <h2 class="time">
            {{ convertToPlayTime(currentPlayTime) }}
        </h2>
        <input type="range" name="test" id="" />
        <h2 class="time">
            {{
                convertToPlayTime((video?.duration as number) - currentPlayTime)
            }}
        </h2>
        <button @click="handleMuteToggle">M</button>
        <button @click="handleFullScreenToggle">FS</button>
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
