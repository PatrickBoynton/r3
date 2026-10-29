<script setup lang="ts">
import Requests from "../requests"
import VideoCard from "./VideoCard.vue"

const props = defineProps<{ ipAddress: string }>()
const videos = defineModel("videos")
const video = defineModel("video")

const handlePickedVideo = async (vid: any) => {
    video.value = await Requests.getVideo(props.ipAddress, vid)
    videos.value = await Requests.getVideos(props.ipAddress)
}
</script>
<template>
    <div class="two">
        <div class="section">
            <button>Videos</button>
            <button>Tutorials</button>
            <button>Movies</button>
            <button>Tags</button>
        </div>
        <ul>
            <VideoCard
                :ipAddress="ipAddress"
                @click="handlePickedVideo(video)"
                v-for="video in videos"
                :video="video"
                :key="video.id" />
        </ul>
    </div>
</template>
<style scoped>
.two {
    //margin-left: 33%;
    width: 85%;
}

.section {
    //background-color: #00be88;
    background-image: linear-gradient(#2c725f 5%, #00be88 6%, #2c725f 100%);
    width: 92%;
    display: flex;
    justify-content: space-around;
    margin-bottom: 1vh;
    margin-left: 1vw;
}

.section button {
    background-color: #201449;
}

ul {
    height: 92vh;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
}

li:first-child {
    margin-top: 0;
}

@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    ul {
    }

    .two {
        //width: 79%;
    }
}
</style>
