<script setup lang="ts">
import { hrefCabinet } from 'assets/variables'

const items = [
  'Удобный онлайн <span class="orange">личный кабинет</span> партнера',
  '<span class="orange">Персональный</span> менеджер',
  'Следите за ходом работ прямо <span class="orange">с телефона</span',
  '<span class="orange">Оформляйте сделку</span> в личном кабинете'
]
</script>

<template>
  <div class="margin-glob">
    <h1 class="text-glob-xl mb-4 md:w-4/5">
      Весь процесс сотрудничества с нами на <span class="orange">100% прозрачный</span> и
      контролируемый
    </h1>

    <div class="flex flex-col items-center justify-between gap-[1.5vw] md:flex-row md:gap-[2vw]">
      <div class="order-2 flex w-full flex-col gap-[1.5vw] md:order-1 md:w-[65vw]">
        <div class="items">
          <div
            class="flex w-full items-start gap-[1vw] rounded-[24px] bg-white p-[2vw] md:w-[25vw] md:p-[1.5vw]"
            v-for="item in items"
            :key="item"
          >
            <img class="icon" src="/images/home/checkbox_checked.svg" alt="icon" />
            <span class="p-[1vw] text-lg font-semibold md:text-base" v-html="item"></span>
          </div>
        </div>
        <UButton :to="hrefCabinet" color="white" variant="outline">
          Зарегистрироваться на платформе
        </UButton>
      </div>
      <div class="order-1 h-full w-full md:order-2 md:w-1/2">
        <img
          class="h-full w-full"
          alt="picture"
          src="/images/partnership/block_5.png"
          draggable="false"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.items {
  grid-area: items;
  display: flex;
  flex-wrap: wrap;
  row-gap: 1vw;
  column-gap: 1vw;
}
</style>
