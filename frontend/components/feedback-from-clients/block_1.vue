<script setup lang="ts">
const videos = Array(4)

const images = Array(60)
</script>

<template>
  <WBlock>
    <p>С 2013 года нам доверились уже более 10 000 клиентов</p>
    <WTitle class="mb-8"> Отзывы наших клиентов </WTitle>
    <UButton class="hover mb-7 py-4 ring-black" color="white" size="xl" block
      >Оставить отзыв</UButton
    >

    <div class="mb-6 grid grid-cols-1 grid-rows-[max-content] gap-5 lg:grid-cols-2">
      <div class="relative" v-for="item in videos">
        <img class="h-auto w-full" src="/images/home/block_14_for-video.png" alt="" />
        <div
          class="absolute left-3 top-3 rounded-full bg-white px-2 py-2 sm:left-8 sm:top-8 sm:px-6 sm:py-4"
        >
          0.18 сек
        </div>
        <div
          class="absolute bottom-3 left-3 flex items-center gap-5 text-white sm:bottom-8 sm:left-8"
        >
          <img class="hover h-8 w-8 sm:h-12 sm:w-12" src="/icons/play-button.svg" alt="video" />
          <div>
            <p class="text-lg font-semibold sm:text-2xl">Наталья Рыбакова</p>
            <p class="text-xs sm:text-base">Квартира 130 м2 на Баумана</p>
          </div>
        </div>
      </div>
    </div>

    <WTitle class="mb-8">Отзывы с независимых площадок </WTitle>
    <UCarousel :items="images" arrows indicators>
      <template #default="{ item }">
        <div class="w-80">
          <img class="h-auto w-full" src="/images/home/block_8__comments.png" alt="" />
        </div>
      </template>

      <template #prev="{ onClick, disabled }">
        <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
      </template>

      <template #next="{ onClick, disabled }">
        <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
      </template>
    </UCarousel>
  </WBlock>
</template>
