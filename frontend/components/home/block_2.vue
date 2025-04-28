<script setup lang="ts">
const cards = [
  { text: 'Без визитов на объект', iconSrc: '/icons/home_1.svg' },
  { text: '100% гарантия фиксированной сметы', iconSrc: '/icons/home_2.svg' },
  { text: 'Все финансовые риски берём на себя', iconSrc: '/icons/home_3.svg' },
  { text: '36 готовых дизайн-проектов', iconSrc: '/icons/home_4.svg' },
  { text: 'Все берем на себя и работаем под ключ', iconSrc: '/icons/home_5.svg' }
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
  <div class="margin-glob-new">
    <div class="hidden grid-cols-5 gap-[1vw] md:grid">
      <div class="flex flex-col gap-[2vw] rounded-[1.5vw] bg-white p-[2vw]" v-for="item in cards">
        <img class="ms-auto h-[1.6vw] w-[1.6vw]" :src="item.iconSrc" alt="icon" />
        <p class="text-[.9vw] font-medium">{{ item.text }}</p>
      </div>
    </div>

    <UCarousel
      class="block md:hidden"
      v-slot="{ item }"
      ref="carouselRef"
      :items="cards"
      :ui="{ container: 'gap-[2vw]' }"
    >
      <div class="flex w-[40vw] flex-col gap-[2vw] rounded-[3vw] bg-white p-[3vw]">
        <img class="ms-auto h-[4vw] w-[4vw]" :src="item.iconSrc" alt="icon" />
        <p class="text-[2vw] font-medium">{{ item.text }}</p>
      </div>
    </UCarousel>
  </div>
</template>
