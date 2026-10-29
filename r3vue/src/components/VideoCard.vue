<script setup lang="ts">
import { convertToPlayTime } from "../utils"

defineProps<{ ipAddress: string }>()
const video = defineModel("video")
</script>
<template>
    <li>
        <h2>{{ video?.title }}</h2>
        <div class="details">
            <h4>{{ "video length - " + convertToPlayTime(video.duration) }}</h4>
            <!--            <h4>-->
            <!--                <span>uploaded date - </span>-->
            <!--                {{ formatDate(video.uploaded_date) }}-->
            <!--            </h4>-->
            <h4>
                <span>number of times picked - </span>
                {{ video.video_status.selection_count }}
            </h4>
            <h4>
                <span>current play time - </span>
                {{ convertToPlayTime(video.video_status.current_play_time) }}
            </h4>
        </div>
    </li>
</template>
<style scoped>
li:hover {
    //box-shadow: 0 0 20px #c92a6f;
}

li:hover h2 {
    color: #d04c82;
    background-image: linear-gradient(#201449 2%, #432995 40%);
}

li:hover .details {
    background-color: #201449;
}

h2 {
    font-size: 40px;
    background-image: linear-gradient(#2c725f 2%, #00be88 40%);
    //background-color: #c92a6f;
    width: 100%;
    color: #201449;
    font-weight: bold;
    height: 5vh;
    text-align: center;
    padding-top: 10px;
}

h4:first-of-type {
    margin-top: 20px;
}

span {
    font-weight: bold;
    font-size: 20px;
    //color: #ffdb60;
}

.details {
    width: 100%;
    text-align: center;
    background-image: linear-gradient(
        150deg,
        #180f36 50%,
        rgba(155, 47, 90, 0.76)
    );
}

@supports (hanging-punctuation: first) and (font: -apple-system-body) and
    (-webkit-appearance: none) {
    li {
        padding-right: 20px;
    }

    h2 {
        font-size: 25px;
    }
}
</style>
