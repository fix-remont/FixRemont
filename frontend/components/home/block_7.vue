<script setup lang="ts">
// import { portfolioItemsShort as items } from '~/shared/utils/test-data'

// const { items } = storeToRefs(usePortfolioPostsStore())
let id = 0
const items = [
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  },
  {
    id: id++,
    title: 'Дом из кирпича 560м на Барвихе',
    images: ['/images/home/block_7__1.png'],
    project_type: { name: 'Ремонт квартир' }
  },
  {
    id: id++,
    title: 'Квартира 300м на Баумана',
    images: ['/images/home/block_7__2.png'],
    project_type: { name: 'Строительство домов' }
  }
]

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
  <!-- <ClientOnly> -->
  <UCarousel
    class="margin-glob-new"
    ref="carouselRef"
    :items="items"
    :ui="{
      container: 'gap-[2vw]',
      indicators: {
        wrapper: 'justify-end',
        base: 'h-[2vw] w-[2vw] md:h-[.5vw] md:w-[.5vw]',
        active: 'bg-[--c-black]',
        inactive: 'bg-[--c-gray]'
      },
      arrows: {
        wrapper: 'static'
      }
    }"
    arrows
    indicators
  >
    <template #default="{ item }">
      <div class="rounded-glob-new relative flex h-[50vw] w-[80vw] p-[4vw] md:h-[30vw] md:w-[46vw]">
        <img
          class="absolute left-0 top-0 h-full w-full object-cover"
          :src="item.images[0]"
          :alt="item.title"
          draggable="false"
        />
        <div class="z-10 mt-auto">
          <p class="mb-[1vw] text-[3vw] font-semibold text-white md:text-[1.7vw]">
            {{ item.title }}
          </p>
          <NuxtLink class="pointer text-primary text-[2vw] underline md:text-[1vw]" to="#"
            >Узнать Стоимость</NuxtLink
          >
        </div>
      </div>
    </template>
    <template #prev="{ onClick, disabled }">
      <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
    </template>

    <template #next="{ onClick, disabled }">
      <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
    </template>
  </UCarousel>
  <!-- </ClientOnly> -->
</template>
