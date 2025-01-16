<script setup lang="ts">
const tabs = [
  { label: 'Все', value: 'all' },
  { label: 'Ремонт квартир', value: 'appartament_renovation' },
  { label: 'Строительство домов', value: 'house_construction' }
]
const selectedTabIndex = ref(0)
const viewItemsAmount = ref(4)

const items = ref([
  { title: 'Дом из кирпича 560 м2 на Барвихе 1', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 2', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 3', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 4', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 5', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 6', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 7', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 8', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 9', imgSrc: '/images/home/block_7__1.png' }
])

const viewItems = computed(() => items.value.slice(0, viewItemsAmount.value))
const showMore = computed(() => items.value.length > viewItems.value.length)
</script>

<template>
  <WBlock>
    <p>Работаем одинаково хорошо, как на крупных объектах, так и в небольших квартирах</p>
    <WTitle> Посмотрите на наши <span class="orange"> выполненные проекты</span> </WTitle>
    <SharedTabs @selected-tab="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />

    <div class="mb-4 grid grid-cols-1 gap-4 xl:grid-cols-2">
      <div class="relative" v-for="item in viewItems">
        <img class="w-full" :src="item.imgSrc" alt="img" />
        <div class="absolute bottom-2 left-2 sm:bottom-8 sm:left-8">
          <h2 class="mb-1 w-[80%] text-base font-bold text-white sm:mb-5 sm:text-2xl">
            {{ item.title }}
          </h2>
          <NuxtLink class="text-orange underline" to="/portfolio/test_id">Узнать цену</NuxtLink>
        </div>
      </div>
    </div>

    <UButton
      class="py-4 hover:text-gray-700"
      v-if="showMore"
      @click="viewItemsAmount = viewItemsAmount + 2"
      color="white"
      variant="outline"
      block
      >Показать больше</UButton
    >
  </WBlock>
</template>
