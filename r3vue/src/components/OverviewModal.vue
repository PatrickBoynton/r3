<script setup lang="ts">
import { onMounted, ref } from "vue"
import { VideoContext } from "../types"
import Requests from "../requests"

const props = defineProps<{ ipAddress: string }>()
const showOverview = defineModel("showOverview")
const videoContext = ref<VideoContext | null>(null)

onMounted(async () => {
    const context = await Requests.getVideoContext(props.ipAddress)

    videoContext.value = context
})
</script>
<template>
    <div class="overview-modal">
        <h1>Overal Statistics</h1>
        <h2>Current OS: {{ videoContext?.current_os }}</h2>
        <h2>{{ videoContext?.total_videos }} Videos</h2>
        <h2>Current Video: {{ videoContext?.current_video.title }}</h2>
        <h2>Current number of plays: {{ videoContext?.video_plays }}</h2>
        <button @click="showOverview = false">Close</button>
    </div>
</template>
<style lang="css" scoped></style>
