<script setup lang="ts">
import { hrefLogo, hrefTg, hrefWatsapp, hrefPhone, labelPhone } from '~/assets/variables'
</script>

<template>
  <header
    :class="[
      'flex h-[16vw] justify-between text-[3vw] font-medium leading-none md:h-[4vw] md:text-[.8vw]',
      'margin-glob-new mt-[4vw] md:mt-[2vw]'
    ]"
  >
    <div
      class="flex items-center gap-[2vw] rounded-[4.5vw] bg-white px-[4vw] md:rounded-[1vw] md:px-[1.4vw]"
    >
      <NuxtLink :to="hrefLogo">
        <img src="/icons/logo-for-white.svg" :class="['hover', 'w-[22vw] md:w-[6vw]']" alt="logo" />
      </NuxtLink>

      <p class="line-clamp-[1vw] hidden text-[.8vw] md:block">
        Первый онлайн-сервис по <br />
        ремонту и строительству <br />
        <b>с фикс стоимостью</b>
      </p>

      <div class="hidden items-center gap-[.3vw] md:flex">
        <img class="w-[1vw]" src="/icons/clock.svg" alt="phone" />
        <p class="text-[.9vw]">Звоните Пн-Вс: 8:30 - 19:00</p>
      </div>

      <div class="hidden items-center gap-[.3vw] md:flex">
        <img class="w-[1vw]" src="/icons/phone.svg" alt="phone" />
        <a class="text-[.9vw]" :href="hrefPhone">{{ labelPhone }}</a>
      </div>
    </div>

    <address
      class="hidden items-center gap-[.5vw] rounded-[1vw] bg-white pe-[1vw] ps-[2vw] md:flex"
    >
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

    <NuxtLink
      to="/cabinet"
      :class="[
        'flex w-[36vw] items-center justify-center rounded-[4.5vw] bg-[--c-black] px-[1vw] text-white md:w-[20vw] md:justify-between md:rounded-[1vw]',
        'hover'
      ]"
    >
      <p class="w-max">Личный кабинет</p>
      <img class="hidden h-[1.7vw] w-[1.7vw] md:block" src="/icons/profile.svg" alt="profile" />
    </NuxtLink>

    <SharedHeaderLinks />
  </header>
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
    top: 0.7vw;
  }
}
</style>
