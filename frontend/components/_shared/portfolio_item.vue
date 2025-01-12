<script setup lang="ts">
import type { PortfolioPost } from '../home/block_7.vue'

const props = defineProps<{
  item: PortfolioPost
}>()

const src = props.item.images[0] ?? undefined
</script>

<template>
  <div class="item-box">
    <img v-if="src" :src="src" :alt="item.title" draggable="false" />
    <div class="text-box">
      <p class="title">{{ item.title }}</p>
      <NuxtLink :class="['link pointer']" to="#">Узнать Стоимость</NuxtLink>
    </div>
  </div>
</template>

<style scoped>
.item-box {
  position: relative;
  font-weight: 600;
  font-size: 10px;
  @media (max-width: 640px) {
    font-size: 6px;
  }

  .text-box {
    position: absolute;
    left: 5em;
    bottom: 5em;
    font-size: 1em;

    .title {
      font-size: 3.6em;
      color: white;
      z-index: 1;
    }
    .link {
      text-decoration: underline;
      color: var(--c-orange);
      font-size: 1.8em;
      z-index: 1;
    }
  }
}
</style>
