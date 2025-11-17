<script lang="ts" setup>
import { ref } from "vue"
import type { Video } from "../types"
import Requests from "../requests"
import Controls from "./Controls.vue"
import Modal from "./Modal.vue"

const props = defineProps<{ ipAddress: string }>()
const emits = defineEmits([
    "getRandomVideo",
    "search",
    "selectionOption",
    "videos",
    "resetVideoStatus",
])

const video = defineModel<Video | null>("video")
const videos = defineModel<Video[] | null>("videos")

const currentPlayTime = ref(0)
const showModal = ref(false)

const videoRef = ref<HTMLVideoElement | null>(null)
const selectionOption = ref()

const handleInput = (e: any) => {
    emits("search", e.target.value)
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
</script>
<template>
    <div class="one">
        <video
            ref="videoRef"
            :src="video?.url"
            controls
            @pause="onPause"
            @timeupdate="getTime"
            @loadedmetadata="onMetadataLoaded" />
        <h2>
            {{ video?.title || "Click the RV button or click a video card." }}
        </h2>
        <Controls
            @reset-video-status="emits('resetVideoStatus', videos)"
            v-model:selectionOption="selectionOption"
            :emit="emits"
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
    height: 100%;
    margin-left: 30px;
}

.one {
    margin-left: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
