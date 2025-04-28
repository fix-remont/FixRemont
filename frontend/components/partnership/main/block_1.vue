<script setup lang="ts">
import { hrefBecomePartner, hrefCabinet, hrefCalculater } from 'assets/variables'

const items = ref([
  {
    id: 1,
    title: 'Риэлторам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/realtors`,
    hovered: false
  },
  {
    id: 2,
    title: 'Застройщикам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/builders`,
    hovered: false
  },
  {
    id: 3,
    title: 'Физическим лицам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/individuals`,
    hovered: false
  }
])
</script>

<template>
  <WBlock class="bg-image radius-glob relative">
    <SharedBreadCrumbs class="top-10 z-10 hidden lg:absolute lg:block" />
    <img
      class="radius-glob md:hidden lg:z-0 lg:block"
      src="/images/partnership/block_1.png"
      alt="background"
    />
    <div class="radius-glob bg-orange block h-[40vw] lg:hidden">
      <img
        class="z-0 object-contain object-center"
        src="/images/partnership/block_1_mob.png"
        alt="background"
      />
      <h1 class="text-glob-md z-10 w-[26vw] text-white">
        Зарабатывайте 10% комиссию с каждой сделки FIX-ремонт
      </h1>
    </div>
    <h1
      class="text-glob-md left-12 top-[32rem] z-10 w-[26vw] text-white md:hidden lg:absolute lg:block"
    >
      Зарабатывайте 10% комиссию с каждой сделки FIX-ремонт
    </h1>
    <div class="black-box right-0 top-0 w-full lg:absolute lg:z-10">
      <h3 class="bb-title">
        Партнерская программа от первого в России онлайн-сервиса по ремонту и строительству с
        фиксированной ценой
      </h3>
      <UButton class="mt-auto" :to="hrefCalculater" size="custom" block>
        Зарегистрироваться, как партнёр
      </UButton>
    </div>
    <div class="bottom-0 right-0 hidden w-[47vw] grid-cols-3 gap-[1vw] md:grid lg:absolute lg:z-10">
      <NuxtLink
        class="rounded-glob-new group relative bg-[#EFEFEF] text-white hover:bg-none"
        v-for="item in items"
        to="#"
        @mouseover="item.hovered = true"
        @mouseout="item.hovered = false"
        :class="['item', { 'item-hovered': item.hovered }, 'cursor-pointer']"
        @click="item.hovered = true"
      >
        <div class="relative p-[2vw] pe-[2vw] lg:z-10">
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
  </WBlock>
</template>

<style scoped lang="postcss">
$radius: 35px;

.black-box {
  background-color: #161616;
  padding: 50px;
  border-radius: $radius;
  color: var(--c-white);
  width: 35em;

  @media (max-width: 1024px) {
    width: initial;
  }

  @media (max-width: 600px) {
    padding: 35px;
  }

  @media (max-width: 450px) {
    padding: 30px;
  }

  .bb-title {
    font-size: 1.5vw;
    margin-bottom: 5rem;
    @apply font-normal;
    color: white;
    width: 75%;

    @media (max-width: 1030px) {
      width: 100%;
      margin-bottom: 2rem;
    }

    @media (max-width: 768px) {
      font-size: 3vw;
    }
  }
}

.item {
}
</style>
