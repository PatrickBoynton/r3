<script setup lang="ts">
import Requests from "../requests"
import { type Video } from "../types"
import OverviewModal from "./OverviewModal.vue"
import SelectVideoFilter from "./SelectVideoFilter.vue"
import { ref } from "vue"
import Modal from "./Modal.vue";

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
const onVideoUploadPressed = () => {
  showModal.value = true
}
</script>
<template>
    <div class="controls">
        <SelectVideoFilter v-model:selection-option="selectionOption" />
        <button @click="onRandomVideoSelect">RV</button>
        <button @click="onRandomNewVideoSelect">RNV</button>
        <input @input="handleInput" type="text" id="search" name="search"/>
        <button @click="showOverview = true">OV</button>
        <button @click="onVideoUploadPressed">UL</button>
        <button @click="onResetMetaData">DVS</button>
    </div>
      <h2>
            {{ video?.title || "Click the RV button or click a video card." }}
      </h2>
    <OverviewModal
        v-if="showOverview"
        :ipAddress="ipAddress"
        v-model:show-overview="showOverview" />
    <Modal :ipAddress="ipAddress"/>
</template>
<style lang="css" scoped>
.controls {
     background-image: linear-gradient(#2c725f 5%, #00be88 6%, #2c725f 100%);
    border-radius: 5px;
    width: 100%;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    //margin-bottom: 15%;
}

select {
    border: 2px solid #ffdb60;
    border-radius: 5px;
    font-size: 20px;
    color: #ffdb60;
    background-color: #180f36;
    padding: 10px;
}
.controls button {
  background-color: #180f36;
}
.controls button:hover {
  background-color: #d04c82;
  border: 2px solid #180f36;
}
.controls input {
  border: none;
  background-color: #201449;
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
    background-color: #201449;
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
h2 {
  font-size: 50px;
  background: linear-gradient(#432995, #c92a6f 60%);
  background-clip:  text;
 -webkit-text-fill-color: transparent;
}
@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    .controls {
      width: 101%;
      height: 20%;
    }
    input {
      width: 200px;
    }
    h2 {
      font-size: 25px;
    }
}
</style>
