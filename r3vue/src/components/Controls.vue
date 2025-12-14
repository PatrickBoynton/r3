<script setup lang="ts">
import { convertToPlayTime } from "../utils.ts"
import { ref } from "vue"

const currentPlayTime = ref(0)
const videoRef = defineModel("videoRef")
const video = defineModel("video")
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
        <button @click="handlePlayToggle">Play</button>
        <h2>
            {{ !video?.duration ? "" : convertToPlayTime(currentPlayTime) }}
        </h2>
        <h2>
            {{ video?.title || "Click the RV button or click a video card." }}
        </h2>
        <h2>
            {{
                currentPlayTime
                    ? convertToPlayTime(
                          (video?.duration as number) - currentPlayTime,
                      )
                    : ""
            }}
        </h2>
        <button @click="handleMuteToggle">Mute</button>
        <button @click="handleFullScreenToggle">FS</button>
    </div>
</template>

<style scoped></style>
