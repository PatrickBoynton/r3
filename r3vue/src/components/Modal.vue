<script setup lang="ts">
import Requests from "../requests.ts"
import { ref } from "vue"

const showModal = defineModel("showModal")
const props = defineProps<{ ipAddress: string }>()
const selectedFile = ref(null)

const sendData = async (e: any) => {
    const formData = new FormData()
    formData.append('file', selectedFile.value)
    console.log(`Form data: ${formData}`)
    try {
      await Requests.uploadVideo(formData)
    } catch (e) {
      throw new Error(`Upload failed: ${e.message}`)
    }
    showModal.value = false
    await Requests.getVideos(props.ipAddress)
}

const onFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement
  selectedFile.value = target.files?.[0] ?? null
}
</script>
<template>
    <div class="modal" v-if="showModal">
        <h1>Upload Video:</h1>
        <form
            method="POST"
            @submit.prevent="(e) => sendData(e)"
            enctype="multipart/form-data">
            <input type="file" name="file" id="file" @change="onFileChange" />
            <input type="submit" name="btn" value="Upload" id="btn" />
            <input
                @click="showModal = false"
                type="button"
                value="Close"
                id="close" />
        </form>
    </div>
</template>
<style>
.modal {
    border: 2px solid #ffdb60;
    border-radius: 5px;
    background-color: #432995;
    display: flex;
    flex-direction: column;
    width: 600px;
    height: 400px;
    position: absolute;
    top: 20%;
    left: 30%;
    justify-content: center;
    align-items: center;
}

.modal input {
    width: 90%;
}

.modal input:hover {
    background-color: #d04c82;
    color: #432995;
}
</style>
