<script setup lang="ts">
const selectionOption = defineModel('selectionOption')
</script>

<template>
 <select v-model="selectionOption" name="" id="">
            <option value="" selected>No Filter.</option>
            <option value="lte=10">< 10 Minutes</option>
            <option value="lte=20">< 20 Minutes</option>
            <option value="lte=30">< 30 Minutes</option>
            <option value="lte=40">< 40 Minutes</option>
            <option value="lte=50">< 50 Minutes</option>
            <option value="lte=60">< 60 Minutes</option>
            <option value="gte=10">> 10 Minutes</option>
            <option value="gte=20">> 20 Minutes</option>
            <option value="gte=30">> 30 Minutes</option>
            <option value="gte=40">> 40 Minutes</option>
            <option value="gte=50">> 50 Minutes</option>
            <option value="gte=60">> 60 Minutes</option>
            <option value="gte=100">> 100 Minutes</option>
        </select>
</template>

<style scoped>

</style>