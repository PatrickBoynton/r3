<script setup lang="ts">
import Requests from '../requests'
import { type Video } from '../types'

const props = defineProps<{ipAddress: string, emit: any, handleInput: (e: any) => void, video: any}>()

const selectionOption = defineModel('selectionOption')
const showModal = defineModel('showModal')


const onResetMetaData = async () => {
    await Requests.deleteVideoStatus(props.ipAddress)
    props.video.value = null
    await Requests.getVideos(props.ipAddress)
}

const onRandomVideoSelect = async () => {
    const randomVideo: Video = await Requests.getRandomVideo(
                        props.ipAddress,
                        props.emit,
                        '?' + selectionOption.value || '',
                    )
    props.video.value = randomVideo
    await Requests.getVideos(props.ipAddress)
}
</script>
<template>
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
                @click="onRandomVideoSelect">
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
            <button @click="onResetMetaData">DVS</button>
        </div>

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