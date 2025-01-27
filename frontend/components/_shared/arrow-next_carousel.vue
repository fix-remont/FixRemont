<script setup lang="ts">
defineProps<{
  onClick: any
  disabled: any
}>()
</script>

<template>
  <img
    :class="['cursor-pointer', 'h-[9vw] w-[9vw] md:h-[3vw] md:w-[3vw]', { 'opacity-60': disabled }]"
    src="/images/arrow-next.svg"
    @click="onClick"
    draggable="false"
  />
</template>
