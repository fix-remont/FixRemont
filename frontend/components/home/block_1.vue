<script setup lang="ts">
const { width } = useViewport()
import { hrefBecomePartner, hrefCalculater } from '~/assets/variables'

const items = ref([
  {
    id: 1,
    title: 'Ремонт',
    text: 'Без визитов на объект. Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: '/apartment-renovation',
    hovered: false
  },
  {
    id: 2,
    title: 'Строительство',
    text: 'Без визитов на объект. Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: '/building-houses',
    hovered: false
  },
  {
    id: 3,
    title: 'Партнёрская программа',
    text: 'Без визитов на объект. Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: hrefBecomePartner,
    hovered: false
  }
])

const carouselRef = ref()

onMounted(() => {
  setInterval(() => {
    if (!carouselRef.value) return

    if (carouselRef.value.page === carouselRef.value.pages) {
      return carouselRef.value.select(0)
    }

    carouselRef.value.next()
  }, 3000)
})
</script>

<template>
  <WBlockNew class="grid grid-cols-1 gap-[1.5vw] md:grid-cols-2">
    <div class="rounded-glob-new relative">
      <img
        class="h-full w-full object-cover"
        src="/images/home/tools.png"
        alt="tools"
        draggable="false"
      />
      <p
        class="text-glob-md absolute bottom-[6vw] left-[6vw] text-white md:bottom-[4vw] md:left-[4vw]"
      >
        Первый в России
        <br />
        онлайн-сервис <br />
        по ремонту и <br />
        строительству <br />
        с фиксированной <br />
        стоимостью
      </p>
    </div>
    <div class="flex flex-col gap-[1.5vw]">
      <div
        class="rounded-glob-new flex flex-grow flex-col bg-[--c-black] p-[5vw] text-white md:p-[2vw]"
      >
        <p
          class="mb-[5vw] text-[4vw] font-medium leading-[5vw] md:mb-0 md:text-[1.6vw] md:leading-[2.1vw]"
        >
          Воплотим вашу
          <br class="hidden md:block" />
          мечту в реальность
          <br class="hidden md:block" />
          без визитов на
          <br class="hidden md:block" />
          объект
        </p>
        <div class="mt-auto grid grid-cols-2 gap-[1vw]">
          <UButton :to="hrefCalculater">Отлайн калькулятор</UButton>
          <UButton :to="hrefBecomePartner" variant="outline" color="white">Стать партнёром</UButton>
        </div>
      </div>
      <div class="hidden grid-cols-3 gap-[1vw] md:grid">
        <NuxtLink
          class="rounded-glob-new group relative bg-[#EFEFEF] text-white hover:bg-none"
          v-for="item in items"
          to="#"
          @mouseover="item.hovered = true"
          @mouseout="item.hovered = false"
          :class="['item', { 'item-hovered': item.hovered }, 'cursor-pointer']"
          @click="item.hovered = true"
        >
          <div class="relative z-10 p-[2vw] pe-[2vw]">
            <p
              class="mb-[.4vw] text-[1.2vw] font-semibold leading-[1.4vw] text-black transition delay-500 ease-linear group-hover:text-white"
            >
              {{ item.title }}
            </p>
            <p
              class="text-[1vw] leading-[1.2vw] text-[#EFEFEF] transition delay-500 ease-linear group-hover:text-gray-300"
            >
              {{ item.text }}
            </p>
          </div>
          <img
            class="absolute top-0 z-0 h-full w-full object-cover opacity-0 transition delay-500 ease-linear group-hover:opacity-100"
            :src="item.imgSrc"
            alt="img"
          />
          <SharedArrowHover class="absolute bottom-[1vw] right-[1vw]" :hovered="item.hovered" />
        </NuxtLink>
      </div>
      <UCarousel
        class="block md:hidden"
        v-if="items"
        ref="carouselRef"
        :items="items"
        :ui="{ container: 'gap-[2vw]' }"
      >
        <template #default="{ item }">
          <NuxtLink
            class="relative w-[40vw] overflow-hidden rounded-[4vw] text-white"
            to="#"
            @mouseover="item.hovered = true"
            @mouseout="item.hovered = false"
            :class="['item', { 'item-hovered': item.hovered }, 'cursor-pointer']"
            @click="item.hovered = true"
          >
            <div class="relative z-10 p-[4vw]">
              <p
                class="mb-[.4vw] pb-[3vw] text-[4vw] font-semibold leading-[3.5vw] text-white md:text-[1.2vw]"
              >
                {{ item.title }}
              </p>
              <p class="text-[3vw] leading-[3.5vw] text-white md:leading-[1.2vw]">
                {{ item.text }}
              </p>
            </div>
            <img
              class="absolute bottom-0 top-0 z-0 h-full w-full object-cover"
              :src="item.imgSrc"
              alt="img"
            />
            <SharedArrowHover class="absolute bottom-[4vw] right-[4vw]" :hovered="true" />
          </NuxtLink>
        </template>
      </UCarousel>
    </div>
  </WBlockNew>
</template>
