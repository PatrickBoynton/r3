<script setup lang="ts">
const showModal = defineModel("showModal")
</script>
<template>
    <div class="modal" v-if="showModal">
        <h1>Upload Video:</h1>
        <input type="file" name="" id="" />
        <input type="submit" value="Upload" />
        <input @click="showModal = false" type="button" value="Close" />
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
