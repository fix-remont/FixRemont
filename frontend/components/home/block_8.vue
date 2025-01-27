<script setup lang="ts">
const commentsRaw = [{ img: '/images/home/block_8__comments.png' }]
const videosRaw = [{ src: '/images/home/block_8__video.png' }]

const comments = Array(5).fill(commentsRaw[0])
const videos = Array(4).fill(videosRaw[0])
</script>

<template>
  <div
    class="grid-rows-auto margin-glob-new grid grid-cols-1 gap-[2vw] md:grid-cols-[30vw_62vw] md:grid-rows-[35vw]"
  >
    <UCarousel
      :items="comments"
      :ui="{
        container: 'gap-[1vw]',
        arrows: {
          wrapper: 'static md:absolute'
        }
      }"
      arrows
      indicators
    >
      <template #default="{ item }">
        <img
          class="runded-glob-new h-full w-[80vw] object-cover md:w-[30vw]"
          :src="item.img"
          alt="img"
          draggable="false"
        />
      </template>

      <template #prev="{ onClick, disabled }">
        <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
      </template>

      <template #next="{ onClick, disabled }">
        <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
      </template>
    </UCarousel>

    <UCarousel
      :items="videos"
      :ui="{
        container: 'gap-[1vw]',
        arrows: {
          wrapper: 'static md:absolute'
        }
      }"
      arrows
      indicators
    >
      <template #default="{ item }">
        <img
          class="runded-glob-new h-full w-[80vw] object-cover md:w-[62vw]"
          :src="item.src"
          alt="video"
          draggable="false"
        />
      </template>

      <template #prev="{ onClick, disabled }">
        <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
      </template>

      <template #next="{ onClick, disabled }">
        <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
      </template>
    </UCarousel>
  </div>
  <div class="margin-glob">
    <UButton class="hover py-6 text-lg" to="#" color="white" block>Смотреть все отзывы</UButton>
  </div>
</template>
