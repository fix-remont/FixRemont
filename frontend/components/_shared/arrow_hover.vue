<script setup lang="ts">
const props = defineProps<{
  hovered: boolean
}>()
</script>

<template>
  <svg
    class="h-[6.3vw] w-[6.3vw] md:h-[2.7vw] md:w-[2.7vw]"
    width="51"
    height="50"
    viewBox="0 0 51 50"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect
      :class="['circle', { 'circle-hover': hovered }, props.hovered ? 'fill-white' : 'fill-black']"
      x="0.430664"
      y="50"
      width="50"
      height="49.9439"
      rx="24.9719"
      transform="rotate(-90 0.430664 50)"
    />
    <path
      :class="['arrow', { 'arrow-hover': hovered }, props.hovered ? 'fill-black' : 'fill-white']"
      d="M18.1777 19.2411L31.4587 32.5222L32.9023 31.0786L19.6213 17.7975L18.1777 19.2411Z"
    />
    <path
      :class="['arrow', { 'arrow-hover': hovered }, props.hovered ? 'fill-black' : 'fill-white']"
      d="M25.007 17.4779L25.007 19.5195L19.9439 19.5195L19.9439 24.5826L17.9023 24.5826L17.9023 17.4779L25.007 17.4779Z"
    />
  </svg>
</template>

<style scoped>
.circle {
  transition: fill 0.5s linear;
}

.arrow {
  transition: all 0.5s linear;
  transform-origin: center;

  &-hover {
    transform: rotate(180deg);
  }
}
</style>
