<script setup lang="ts">
import Requests from "../requests"
import VideoCard from "./VideoCard.vue"

const emits = defineEmits(["getVideo"])
defineProps<{ ipAddress: string }>()
const videos = defineModel('videos')
</script>
<template>
    <div class="two">
        <ul>
            <VideoCard
                :ipAddress="ipAddress"
                @click="Requests.getVideo(ipAddress, video, emits)"
                v-for="video in videos"
                :video="video"
                :key="video.id" />
        </ul>
    </div>
</template>
<style scoped>
.two {
    overflow: hidden;
    height: 90vh;
    display: flex;
    justify-content: center;
}

ul {
    overflow: scroll;
}
</style>
