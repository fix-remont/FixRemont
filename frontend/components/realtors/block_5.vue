<script setup lang="ts">
const comments = ['/images/realtors/block_5.png']
const items = Array(8).fill(comments[0])
</script>

<template>
  <article class="margin-glob block">
    <h1 class="title-glob">
      Посмотрите,<span class="orange"> что говорят о нас</span> наши текущие партнеры
    </h1>

    <UCarousel
      :items="items"
      arrows
      indicators
      :ui="{
        container: 'gap-5 rounded-3xl',
        indicators: {
          wrapper: 'justify-end',
          base: 'h-[5px] w-[5px] sm:h-2 sm:w-2',
          active: 'bg-[var(--c-black)]',
          inactive: 'bg-[var(--c-gray)]'
        },
        arrows: {
          wrapper: 'flex gap-2 justify-start mt-2'
        }
      }"
    >
      <template #default="{ item }">
        <img :src="item" alt="comment" draggable="false" />
      </template>

      <template #prev="{ onClick, disabled }">
        <img
          :class="[
            'arrow cursor-pointer',
            'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
            { 'opacity-60': disabled }
          ]"
          src="/images/arrow-prev.svg"
          @click="onClick"
          draggable="false"
        />
      </template>

      <template #next="{ onClick, disabled }">
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
    </UCarousel>
  </article>
</template>

<style scoped>
@media (max-width: 800px) {
  .block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  h1 {
    text-align: center;
  }
}
</style>
