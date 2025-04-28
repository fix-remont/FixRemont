<script setup lang="ts">
const img = '/images/home/block_9.png'

const items = ref([
  {
    label: 'Выбор опции',
    time: '1 мин',
    img,
    selected: false,
    text: '1 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!'
  },
  {
    label: 'Выбор подходящего тарифа',
    time: '30 мин',
    img,
    selected: false,
    text: '2 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!'
  },
  {
    label: 'Удобный выбор планировки и материала',
    time: '60 мин',
    img,
    selected: false,
    text: '3 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!'
  },
  {
    label: 'Проведение работ сервисом FIX-ремонт',
    time: '',
    img,
    selected: false,
    text: '4 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!'
  },
  {
    label: 'Получите — распишитесь!:)',
    time: '',
    img,
    selected: false,
    text: '5 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!'
  }
])

const currentActiveIndex = ref(0)

const itemsWithSelected = computed(() => {
  return items.value.map((item, index) => {
    item.selected = index === currentActiveIndex.value
    return item
  })
})

onMounted(() => {
  const maxIndex = items.value.length - 1
  setInterval(() => {
    currentActiveIndex.value =
      currentActiveIndex.value == maxIndex ? 0 : currentActiveIndex.value + 1
  }, 3000)
})
</script>

<template>
  <div
    class="margin-glob-new rounded-glob-new grid grid-cols-1 gap-[3vw] bg-[--c-black] p-[4vw] text-white md:grid-cols-2"
  >
    <div class="">
      <p class="text-glob-xl">
        Всего <span class="text-primary">4 шага и 1.5 часа</span> <br />
        личного времени
      </p>
      <p class="my-[2vw] text-[3vw] font-semibold md:my-[1.5vw] md:text-[1vw]">
        отделяют вас от дома своей мечты
      </p>
      <div class="flex flex-col gap-[3vw] md:gap-[1vw]">
        <div v-for="(item, index) in itemsWithSelected" @click="currentActiveIndex = index">
          <div
            :class="[
              { 'bg-white': index == currentActiveIndex },
              'flex h-[14vw] items-center justify-between rounded-[4vw] px-[6vw] font-medium text-[#6B6B6B] ring-[.1vw] ring-[#6B6B6B] md:h-[6vw] md:rounded-[1vw] md:px-[2vw]'
            ]"
          >
            <div
              :class="[
                { 'font-semibold text-[--c-black]': index == currentActiveIndex },
                'text-[2.5vw] md:text-[1vw]'
              ]"
            >
              {{ item.label }}
            </div>
            <div class="text-[2.5vw] md:text-[1vw]">{{ item.time }}</div>
          </div>

          <div class="my-[2vw] block md:hidden" v-if="index == currentActiveIndex">
            <img class="mb-[2vw] w-full" :src="items[currentActiveIndex].img" alt="img" />
            <div class="text-[4vw]">{{ items[currentActiveIndex].text }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="hidden md:block">
      <img class="mb-[2vw] w-full" :src="items[currentActiveIndex].img" alt="img" />
      <div class="text-[2vw]">{{ items[currentActiveIndex].text }}</div>
    </div>
  </div>
</template>

<style scoped></style>
