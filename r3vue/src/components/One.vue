<script lang="ts" setup>
import { ref } from 'vue'
import type { Video } from '../types'
import Requests from '../requests';

const props = defineProps<{ipAddress: string}>()
const emit = defineEmits(['getRandomVideo', 'search'])

const video = defineModel<Video | null>('video')
const currentPlayTime = ref(0)

const videoRef = ref<HTMLVideoElement | null>(null)

const handleInput = (e: any) => {
  emit('search', e.target.value)
}

const getTime = () => {
  if(videoRef.value) {
    currentPlayTime.value = videoRef.value.currentTime
    if(videoRef.value.paused && video.value) {
    video.value.video_status.current_play_time = currentPlayTime.value as number
    }
  }
}

const onMetadataLoaded = () => {
  if(videoRef.value) {
    videoRef.value.currentTime = video.value?.video_status.current_play_time as number
  }
}

const onPause = () => {
  if(videoRef.value && video.value) {
    Requests.updateVideo(props.ipAddress, video.value)
  }
}
</script>
<template>
    <div class="one">
        <video ref="videoRef" 
                :src="video?.url"
                controls 
                @pause="onPause" 
                @timeupdate="getTime" 
                @loadedmetadata="onMetadataLoaded"/>
        <h1>{{video?.title ||
              'Click the RV button or click a video card'}}</h1>
        <div class="controls">
          <select name="" id="">
            <option value="">< 10 Minutes</option>
            <option value="">< 20 Minutes</option>
            <option value="">< 30 Minutes</option>
            <option value="">< 40 Minutes</option>
            <option value="">< 50 Minutes</option>
            <option value="">< 60 Minutes</option>
            <option value="">> 10 Minutes</option>
            <option value="">> 20 Minutes</option>
            <option value="">> 30 Minutes</option>
            <option value="">> 40 Minutes</option>
            <option value="">> 50 Minutes</option>
            <option value="">> 60 Minutes</option>
            <option value="">> 100 Minutes</option>
          </select>
          <button @click="Requests.getRandomVideo(ipAddress, emit)">RV</button>
          <button @click="Requests.getRandomVideo(ipAddress, emit, '?played=false')">RNV</button>
          <input @input="handleInput" type="text" >
          <button @click="Requests.deleteVideoStatus(ipAddress)">DVS</button>
    </div>
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
  border: 2px solid #FFDB60;
  border-radius: 5px;
  width: 100%;
  margin-left: 30px;
  padding: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
select {
  border: 2px solid #FFDB60;
  border-radius: 5px;
  font-size: 20px;
  color: #FFDB60;
  padding: 10px;
  background-color: transparent;
}
</style>