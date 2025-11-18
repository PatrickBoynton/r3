<script setup lang="ts">
import Requests from "../requests"
import VideoCard from "./VideoCard.vue"
import type { Video } from "../types.ts"

const emits = defineEmits(["getVideo"])
defineProps<{ ipAddress: string; videos: Video[] }>()
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
