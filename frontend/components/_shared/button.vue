<script setup lang="ts">
const props = defineProps<{
  youtube?: true
  fillOrange?: true
  fillBlack?: true
  fillBlackWithOutline?: true
  class?: string
}>()
</script>

<template>
  <button
    :class="[
      'hover',
      { youtube },
      { fillOrange },
      { fillBlack },
      { fillBlackWithOutline },
      props.class
    ]"
  >
    <slot />
  </button>
</template>

<style scoped>
button {
  width: 100%;
  padding: 32px;
  border-radius: 500px;
  font-size: 20px;
  font-weight: 600;
  border: 2px solid;

  @media (max-width: 640px) {
    font-size: 12px;
    padding: 16px;
  }
}
.youtube {
  color: #ff2600;
  border-color: #ff2600;
}
.fillOrange {
  color: white;
  background-color: var(--c-orange);
  border-color: var(--c-orange);
}

.fillBlack {
  color: white;
  background-color: var(--c-black);
  border-color: var(--c-black);
}

.fillBlackWithOutline {
  color: white;
  background-color: var(--c-black);
}
</style>
