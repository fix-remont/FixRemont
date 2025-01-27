<script setup lang="ts">
import { hrefOtzovik, hrefYandex } from '~/assets/variables'

const items = [
  { label: 'Яндекс', name: 'yandex', href: hrefYandex, imgSrc: '/images/home/yandex.svg' },
  { label: 'Отзовик', name: 'otzovik', href: hrefOtzovik, imgSrc: '/images/home/otzovik.svg' }
]
</script>

<template>
  <div class="margin-glob-new">
    <p class="mb-[2vw] text-[3vw] font-medium md:mb-[1vw] md:text-[1vw]">
      Но лучше всего о нас расскажут
    </p>

    <div class="flex flex-col gap-[2vw] md:flex-row">
      <div class="text-glob-xl">
        Выполненные работы <br />
        и отзывы клиентов
      </div>

      <div class="ml-0 grid grid-cols-2 gap-[3vw] md:ml-auto md:flex md:gap-[1vw]">
        <div
          class="ms:flex-raw flex flex-col gap-[2vw] rounded-[1vw] bg-white p-[4vw] md:flex-row md:p-[2vw]"
          v-for="item in items"
        >
          <div class="flex flex-col items-center justify-between gap-[3vw] md:items-start">
            <img class="w-[16vw] md:w-[5vw]" src="/images/home/feedback-stars.png" alt="" />
            <img class="w-[25vw] md:w-[6vw]" :src="item.imgSrc" alt="img" />
          </div>
          <a
            class="mt-auto text-center text-[3vw] font-semibold underline md:text-[.7vw]"
            :href="item.href"
            >Смотреть отзывы на {{ item.label }}</a
          >
        </div>
      </div>
    </div>
  </div>
</template>
