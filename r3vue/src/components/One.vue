<script lang="ts" setup>
import { onMounted, onUnmounted, ref } from "vue"
import type { Video, VideoContext } from "../types"
import Requests from "../requests"
import Modal from "./Modal.vue"
import Controls from "./Controls.vue"
import Filters from "./Filters.vue"

const props = defineProps<{
    ipAddress: string
    videoContext: VideoContext | null
}>()

let video = defineModel<Video | null>("video")
const videos = defineModel<Video[] | null>("videos")
const search = defineModel("search")
const selectionOption = defineModel("selectionOption")
const currentPlayTime = ref(0)

const showModal = ref(false)

const videoRef = ref<HTMLVideoElement | null>(null)

const handleInput = (e: any) => {
    search.value = e.target.value
}

const getTime = () => {
    if (videoRef.value) {
        currentPlayTime.value = videoRef.value.currentTime
        if (videoRef.value.paused && video.value) {
            video.value.video_status.current_play_time =
                currentPlayTime.value as number
        }
    }
}

const onMetadataLoaded = () => {
    if (videoRef.value) {
        videoRef.value.currentTime = video.value?.video_status
            .current_play_time as number
    }
}

const onPause = async () => {
    if (videoRef.value && video.value) {
        await Requests.updateVideo(props.ipAddress, video.value)
    }
}

let timerId: number | null = null

const setTimer = () => {
    timerId = setInterval(() => {
        if (
            video.value &&
            videoRef.value &&
            videoRef.value.currentTime > 0 &&
            !videoRef.value?.paused
        ) {
            video.value.video_status.current_play_time =
                videoRef.value?.currentTime
            Requests.updateVideo(props.ipAddress, video.value)
        }
    }, 60)
}
onMounted(() => {
    setTimer()
})

onUnmounted(() => {
    if (timerId) {
        clearInterval(timerId)
    }
})
const handleKeyEvents = (event: any) => {
    if (event.key === "p") {
        if (videoRef.value?.paused) {
            videoRef.value.play()
        } else {
            videoRef.value?.pause()
        }
    }

    if (event.key === "f") {
        videoRef.value?.requestFullscreen()
    }

    if (event.key === "m" && videoRef.value) {
        videoRef.value.muted = !videoRef.value?.muted
    }
}
const handleEnded = () => {
    const rv = Requests.getRandomVideo(props.ipAddress, "")
    video = rv
}

const onMouse = () => {
    if (videoRef.value?.paused) {
        videoRef.value.play()
    } else {
        videoRef.value?.pause()
    }
}

const handleDouble = () => {
  if(document.fullscreenElement) {
    document.exitFullscreen()
  } else {
    videoRef.value?.requestFullscreen()
  }
}
</script>
<template>
    <div class="one">
        <video
            ref="videoRef"
            :src="video?.url"
            @pause="onPause"
            @keydown="(e: any) => handleKeyEvents(e)"
            @mousedown="onMouse"
            @timeupdate="getTime"
            @loadedmetadata="onMetadataLoaded"
            @dblclick="handleDouble"
            @ended="handleEnded" />
        <Controls
            v-model:video="video as Video"
            v-model:videoRef="videoRef"
            :ipAddress="ipAddress"
            v-model:currentPlayTime="currentPlayTime" />
        <Filters
            v-model:selectionOption="selectionOption"
            :ipAddress="ipAddress"
            :handleInput="handleInput"
            v-model:showModal="showModal"
            v-model:video="video"
            v-model:videos="videos" />
    </div>
    <Modal v-model:showModal="showModal" />
</template>
<style scoped>
video {
    width: 100%;
    height: 500px;
    margin-left: 30px;
}

.one {
    margin-left: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.name {
    display: flex;
}

.name h2 {
    margin: 10px;
}
</style>
