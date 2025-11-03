<script setup lang="ts">
import { type Video } from "../App.vue"
import VideoCard from "./VideoCard.vue"

defineProps<{ videos: Video[]; ipAddress: string }>()
</script>
<template>
    <!-- <div class="three">
        <ul class="played">
            <VideoCard v-for="video in videos" 
                        :ipAddress="ipAddress"
                        :video="video" 
                        :key="video.id" 
                        @getVideo="handlePickedVideo(video as Video)"/>

        </ul>
    </div> -->
</template>
<style scoped>
.played {
    display: flex;
}
</style>
