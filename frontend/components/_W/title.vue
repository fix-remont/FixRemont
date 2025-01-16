<script setup lang="ts">
const props = defineProps<{ class?: string; style?: string }>()
import { twMerge } from 'tailwind-merge'
</script>

<template>
  <div
    :style="props.style"
    :class="twMerge('mb-3 text-3xl font-bold sm:text-4xl xl:text-6xl', props.class)"
  >
    <slot />
  </div>
</template>
