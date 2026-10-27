<script lang="ts" setup>
import { onMounted, ref } from "vue"
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
    console.log(video)
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
const handleEnded = async () => {
    video.value = await Requests.getRandomVideo(props.ipAddress, "")
    await Requests.getVideos(props.ipAddress)
}

const onMouse = () => {
    if (videoRef.value?.paused) {
        videoRef.value.play()
    } else {
        videoRef.value?.pause()
    }
    if (document.fullscreenElement) {
        if (videoRef.value?.paused) {
            videoRef.value.play()
        } else {
            videoRef.value?.pause()
        }
    }
}

const handleDouble = () => {
    if (document.fullscreenElement) {
        document.exitFullscreen()
    } else {
        videoRef.value?.requestFullscreen()
    }
}
</script>
<template>
    <div class="one">
        <div class="section">
            <button>Videos</button>
            <button>Tutorials</button>
            <button>Movies</button>
            <button>Tags</button>
        </div>
        <video
            ref="videoRef"
            :src="video?.url"
            preload="metadata"
            muted
            :key="video?.id"
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
    <Modal v-model:showModal="showModal" :ip-address="ipAddress" />
</template>
<style scoped>
video {
    padding: 0;
    margin: 0;
    height: 100%;
    width: 100%;
    object-fit: contain;
    aspect-ratio: 16 / 9;
}

.one {
    height: 98vh;
    width: 61vw;
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

.section {
    //background-color: #00be88;
    background-image: linear-gradient(#2c725f 2%, #00be88 40%);
    width: 100%;
    display: flex;
    justify-content: center;
}

.section button {
    background-color: #180f36;
    font-size: 40px;
    padding: 20px;
}

.section button:hover {
    background-color: #d04c82;
    border: 2px solid #180f36;
}

@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    .section {
        height: 90px;
        width: 100%;
        justify-content: space-around;
    }

    .section button {
        font-size: 20px;
    }

    .one {
    }

    video {
        height: 100%;
    }
}
</style>
