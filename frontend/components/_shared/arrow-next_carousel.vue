<script setup lang="ts">
defineProps<{
  onClick: any
  disabled: any
}>()
</script>

<template>
  <img
    :class="[
      'arrow cursor-pointer',
      'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
      { 'opacity-60': disabled }
    ]"
    src="/images/arrow-next.svg"
    @click="onClick"
    draggable="false"
  />
</template>
