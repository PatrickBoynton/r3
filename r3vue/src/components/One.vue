<script lang="ts" setup>
import { ref } from "vue"
import type { Video } from "../types"
import Requests from "../requests"

const props = defineProps<{ ipAddress: string }>()
const emit = defineEmits(["getRandomVideo", "search", "selectionOption"])

const video = defineModel<Video | null>("video")
const currentPlayTime = ref(0)
const showModal = ref(false)

const videoRef = ref<HTMLVideoElement | null>(null)
const selectionOption = ref("")

const handleInput = (e: any) => {
    emit("search", e.target.value)
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

const onPause = () => {
    if (videoRef.value && video.value) {
        Requests.updateVideo(props.ipAddress, video.value)
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
        <h1>
            {{ video?.title || "Click the RV button or click a video card" }}
        </h1>
        <div class="controls">
            <select v-model="selectionOption" name="" id="">
                <option value="lte=10">< 10 Minutes</option>
                <option value="lte=20">< 20 Minutes</option>
                <option value="lte=30">< 30 Minutes</option>
                <option value="lte=40">< 40 Minutes</option>
                <option value="lte=50">< 50 Minutes</option>
                <option value="lte=60">< 60 Minutes</option>
                <option value="gte=10">> 10 Minutes</option>
                <option value="gte=20">> 20 Minutes</option>
                <option value="gte=30">> 30 Minutes</option>
                <option value="gte=40">> 40 Minutes</option>
                <option value="gte=50">> 50 Minutes</option>
                <option value="gte=60">> 60 Minutes</option>
                <option value="gte=100">> 100 Minutes</option>
            </select>
            <button
                @click="
                    Requests.getRandomVideo(
                        ipAddress,
                        emit,
                        '?' + selectionOption || '',
                    )
                ">
                RV
            </button>
            <button
                @click="
                    Requests.getRandomVideo(
                        ipAddress,
                        emit,
                        '?played=false' + '&' + selectionOption || '',
                    )
                ">
                RNV
            </button>
            <input @input="handleInput" type="text" />
            <button @click="showModal = true">UL</button>
            <button @click="Requests.deleteVideoStatus(ipAddress)">DVS</button>
        </div>
    </div>
    <div v-if="showModal" class="modal">
        <h1>Upload Video:</h1>
        <input type="file" name="" id="" />
        <input type="submit" value="Upload" />
        <input @click="showModal = false" type="button" value="Close" />
    </div>
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
.controls {
    border: 2px solid #ffdb60;
    border-radius: 5px;
    width: 100%;
    margin-left: 30px;
    padding: 20px 0;
    display: flex;
    justify-content: center;
    align-items: center;
}
select {
    border: 2px solid #ffdb60;
    border-radius: 5px;
    font-size: 20px;
    color: #ffdb60;
    padding: 10px;
    background-color: transparent;
}
.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #201449d9;
    border: 2px solid yellow;
    border-radius: 5px;
    width: 680px;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.modal input {
    width: 80%;
    cursor: pointer;
}
</style>
