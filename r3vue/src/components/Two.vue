<script setup lang="ts">
import Requests from "../requests"
import { type Video } from "../types"
import VideoCard from "./VideoCard.vue"
const emit = defineEmits(["getVideo"])
defineProps<{ videos: Video[]; ipAddress: string }>()
</script>
<template>
    <div class="two">
        <ul>
            <VideoCard
                :ipAddress="ipAddress"
                @click="Requests.getVideo(ipAddress, video)"
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
    display: flex;
    justify-content: center;
}
ul {
    overflow: scroll;
}
</style>
