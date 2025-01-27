<script setup lang="ts">
const items = [
  { label: 'Вконтакте', src: '/icons/vkontakte.svg', subsribed_amount: 1500 },
  { label: 'Instagram', src: '/icons/instagram.svg', subsribed_amount: 1550 },
  { label: 'Telegram', src: '/icons/telegram.svg', subsribed_amount: 500 }
]

const youtubeSubscribtions = 2500
</script>

<template>
  <div class="margin-glob-new">
    <h1 class="text-glob-xl mb-[2vw]">
      Мы максимально <span class="text-primary">открыты</span> и подтверждаем экспертность в
      социальных сетях
    </h1>
    <div class="grid grid-cols-2 gap-[2vw]">
      <div class="rounded-glob-new relative bg-[--c-black] p-[2vw]">
        <div class="flex gap-[1vw]">
          <img class="hover z-10 h-[4vw] w-[4vw]" src="/icons/youtube.svg" alt="icon-youtube" />
          <div class="text-white">
            <p class="text-[2vw] font-bold">YouTube</p>
            <p class="text-[1vw]">{{ youtubeSubscribtions }} подписчиков</p>
          </div>
        </div>
        <img class="absolute bottom-0 right-[.5vw]" src="/images/home/block_12.png" alt="img" />
      </div>
      <div class="flex flex-col gap-[1vw]">
        <div
          class="flex items-center gap-[1vw] rounded-[2vw] bg-white p-[2vw]"
          v-for="item in items"
          :key="item.src"
        >
          <img class="hover h-[4vw] w-[4vw]" :src="item.src" alt="icon" />
          <span class="text-[2vw] font-bold">{{ item.label }}</span>
          <span class="ms-auto text-[1vw]">{{ item.subsribed_amount }} подписчиков</span>
        </div>
      </div>
    </div>
  </div>
</template>
