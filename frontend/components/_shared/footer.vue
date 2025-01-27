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
    class="flex flex-col items-center justify-between gap-[5vw] rounded-t-[8vw] bg-[--c-black] px-[2.2vw] py-[12vw] text-[4vw] font-medium text-white md:flex-row md:gap-0 md:rounded-t-[1.5vw] md:py-[2.2vw] md:text-[.7vw]"
    :style="{ marginTop }"
  >
    <NuxtLink :to="hrefLogo">
      <img src="/icons/logo-for-black.svg" :class="['hover', 'w-[34vw] md:w-[6vw]']" alt="logo" />
    </NuxtLink>

    <p class="line-clamp-[1vw] text-center text-[4vw] md:block md:text-[.8vw]">
      Первый онлайн-сервис по <br class="hidden md:block" />
      ремонту и строительству <br class="hidden md:block" />
      <b>с фикс стоимостью</b>
    </p>

    <p>Copyright 2024. Все права защищены</p>

    <a :class="['text-primary underline', 'hover']" :href="hrefSelfPolitic"
      >Политика конфиденциальности</a
    >

    <address class="flex items-center gap-[2vw] rounded-[1vw] pe-[1vw] ps-[2vw] md:gap-[.5vw]">
      <p class="with_point text">
        Напишите нам,<br />
        мы сейчас онлайн
      </p>
      <a :href="hrefWatsapp">
        <img
          src="/icons/watsapp.svg"
          :class="['hover', 'h-[12vw] w-[12vw] md:h-[3vw] md:w-[3vw]']"
          alt="watsapp"
        />
      </a>
      <a :href="hrefTg">
        <img
          src="/icons/telegram.svg"
          :class="['hover', 'h-[12vw] w-[12vw] md:h-[3vw] md:w-[3vw]']"
          alt="watsapp"
        />
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
    @media (max-width: 768px) {
      width: 2vw;
      height: 2vw;
      left: -6vw;
      top: 5.5vw;
    }
  }
}
</style>
