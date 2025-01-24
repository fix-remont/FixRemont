<script setup lang="ts">
import {
  hrefLogo,
  hrefTg,
  hrefWatsapp,
  hrefPhone,
  labelPhone,
  hrefSelfPolitic
} from '~/assets/variables'

const props = defineProps<{
  footerWithoutMargin?: boolean
}>()

const marginTop = ref('auto')
if (props.footerWithoutMargin) marginTop.value = '0'
</script>

<template>
  <footer
    class="flex items-center justify-between rounded-t-[1.5vw] bg-[--c-black] px-[2.2vw] py-[2.2vw] text-[.7vw] font-medium text-white"
    :style="{ marginTop }"
  >
    <NuxtLink :to="hrefLogo">
      <img src="/icons/logo-for-black.svg" :class="['hover', 'w-[6vw]']" alt="logo" />
    </NuxtLink>

    <p class="line-clamp-[1vw] hidden text-[.8vw] md:block">
      Первый онлайн-сервис по <br />
      ремонту и строительству <br />
      <b>с фикс стоимостью</b>
    </p>

    <p>Copyright 2024. Все права защищены</p>

    <a :class="['text-primary underline', 'hover']" :href="hrefSelfPolitic"
      >Политика конфиденциальности</a
    >

    <address class="hidden items-center gap-[.5vw] rounded-[1vw] pe-[1vw] ps-[2vw] md:flex">
      <p class="with_point text">
        Напишите нам,<br />
        мы сейчас онлайн
      </p>
      <a :href="hrefWatsapp">
        <img src="/icons/watsapp.svg" :class="['hover', 'h-[3vw] w-[3vw]']" alt="watsapp" />
      </a>
      <a :href="hrefTg">
        <img src="/icons/telegram.svg" :class="['hover', 'h-[3vw] w-[3vw]']" alt="watsapp" />
      </a>
    </address>

    <div class="flex items-center gap-[.3vw]">
      <img class="" src="/icons/clock.svg" alt="phone" />
      <p>Звоните Пн-Вс: 8:30 - 19:00</p>
    </div>

    <div class="flex items-center gap-[.3vw]">
      <img class="" src="/icons/phone.svg" alt="phone" />
      <a :class="['hover']" :href="hrefPhone">{{ labelPhone }}</a>
    </div>
  </footer>
</template>

<style scoped>
.with_point {
  position: relative;
  &::before {
    content: '';
    width: 0.3vw;
    height: 0.3vw;
    border-radius: 50%;
    background-color: #43c460;
    position: absolute;
    left: -1vw;
    top: 1vw;
  }
}
</style>
