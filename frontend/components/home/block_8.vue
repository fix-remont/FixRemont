<script setup lang="ts">
const commentsRaw = [{ img: '/images/home/block_8__comments.png' }]

const videosRaw = [{ src: '/images/home/block_8__video.png' }]

const comments = Array(5).fill(commentsRaw[0])
const videos = Array(4).fill(videosRaw[0])
</script>

<template>
  <div class="margin-glob wrapper">
    <UCarousel
      :items="comments"
      :ui="{
        container: 'gap-5',
        item: 'w-full',
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
      arrows
      indicators
    >
      <template #default="{ item }">
        <div class="comment-box">
          <img :src="item.img" alt="img" draggable="false" />
        </div>
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

    <UCarousel
      :items="videos"
      :ui="{
        container: 'gap-5',
        item: 'w-full ',
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
      arrows
      indicators
    >
      <template #default="{ item }">
        <div class="video-box">
          <img :src="item.src" alt="video" draggable="false" />
        </div>
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
  </div>
  <div class="margin-glob">
    <SharedButton>Смотреть все отзывы</SharedButton>
  </div>
</template>

<style scoped>
.wrapper {
  display: flex;
  gap: 30px;
  @media (max-width: 640px) {
    flex-direction: column;
  }
}

.comment-box {
  img {
    object-fit: cover;
  }
}

.video-box {
  img {
    object-fit: cover;
  }
}
</style>
