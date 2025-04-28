<script setup lang="ts">
const items = ref(Array(9))
</script>

<template>
  <WBlock class="flex flex-col gap-4">
    <WTitle>Также может быть интересно:</WTitle>

    <UCarousel class="carousel" :items="items" arrows indicators>
      <template #default="{ item }">
        <div class="radius-glob relative h-max overflow-hidden">
          <img class="w-64 sm:w-full" src="/images/home/block_14_for-blog.png" alt="img" />
          <span class="absolute left-6 top-6 rounded-full bg-[var(--c-black)] px-4 py-3 text-white"
            >Ремонт</span
          >
          <NuxtLink
            class="absolute bottom-6 left-6 pe-6 text-sm font-semibold text-white underline sm:text-xl"
            to="/blog/test_id"
            >Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?</NuxtLink
          >
        </div>
      </template>

      <template #prev="{ onClick, disabled }">
        <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
      </template>

      <template #next="{ onClick, disabled }">
        <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
      </template>
    </UCarousel>
    <UButton class="hover py-4" size="xl" color="white" block>Читать другие статьи</UButton>
  </WBlock>
</template>
