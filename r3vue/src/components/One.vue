<script lang="ts" setup>
import {  ref } from "vue"
import type {Video, VideoContext} from "../types"
import Requests from "../requests"
import Controls from "./Controls.vue"
import Modal from "./Modal.vue"
import { convertToPlayTime } from "../utils.ts"

const props = defineProps<{ ipAddress: string, videoContext: VideoContext | null }>()

const video = defineModel<Video | null>("video")
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
        videoRef.value.currentTime = video.value?.video_status.current_play_time as number
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
        <div class="name">
            <h2>{{ videoContext?.total_videos + ' videos' || 'NOTHING. '}}</h2>
            <h2>
                {{
                    currentPlayTime
                        ? convertToPlayTime(video?.duration as number - currentPlayTime)
                        : ""
                }}
            </h2>
            <h2>
                {{
                    video?.title || "Click the RV button or click a video card."
                }}
            </h2>
            <h2>
                {{ video?.duration ? convertToPlayTime(video?.duration) : "" }}
            </h2>
        </div>
        <Controls
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

.name {
    display: flex;
}

.name h2 {
    margin: 10px;
}
</style>
