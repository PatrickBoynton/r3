<script setup lang="ts">
import Requests from "../requests"
import { type Video } from "../types"
import OverviewModal from "./OverviewModal.vue"
import SelectVideoFilter from "./SelectVideoFilter.vue"
import { ref } from "vue"

const props = defineProps<{
    ipAddress: string
    handleInput: (e: any) => void
}>()
const selectionOption = defineModel("selectionOption")
const showModal = defineModel("showModal")
const video = defineModel("video")
const videos = defineModel("videos")
const showOverview = ref(false)

const onResetMetaData = async () => {
    await Requests.deleteVideoStatus(props.ipAddress)
    video.value = null
    videos.value = await Requests.getVideos(props.ipAddress)
}

const onRandomVideoSelect = async () => {
    const randomVideo: Video = await Requests.getRandomVideo(
        props.ipAddress,
        "?" + selectionOption.value || "",
    )
    video.value = randomVideo
    videos.value = await Requests.getVideos(props.ipAddress)
}

const onRandomNewVideoSelect = async () => {
    const newRandomVideo: Video = await Requests.getRandomVideo(
        props.ipAddress,
        "?" + selectionOption.value + "&played=false" || "?played=false",
    )
    video.value = newRandomVideo
    videos.value = await Requests.getVideos(props.ipAddress)
}
</script>
<template>
    <div class="controls">
        <SelectVideoFilter v-model:selection-option="selectionOption" />
        <button @click="onRandomVideoSelect">RV</button>
        <button @click="onRandomNewVideoSelect">RNV</button>
        <input @input="handleInput" type="text" />
        <button @click="showOverview = true">OV</button>
        <button @click="showModal = true">UL</button>
        <button @click="onResetMetaData">DVS</button>
    </div>
    <OverviewModal
        v-if="showOverview"
        :ipAddress="ipAddress"
        v-model:show-overview="showOverview" />
</template>
<style lang="css" scoped>
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
    border: 2px solid #ffdb60;
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
.overview-modal {
    position: absolute;
    border: 5px solid #ffdb60;
    border-radius: 5px;
    background-color: #5838c2;
    height: 40%;
    width: 40%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
}
.overview-modal button {
    width: 90%;
}
</style>
