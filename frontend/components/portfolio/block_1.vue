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
  { title: 'Дом из кирпича 560 м2 на Барвихе 9', imgSrc: '/images/home/block_7__1.png' },
  { title: 'Дом из кирпича 560 м2 на Барвихе 10', imgSrc: '/images/home/block_7__1.png' },
])

const viewItems = computed(() => items.value.slice(0, viewItemsAmount.value))
const showMore = items.value.length > viewItems.value.length

</script>

<template>
  <WBlock>
    <p>Работаем одинаково хорошо, как на крупных объектах, так и в небольших квартирах</p>
    <WTitle> Посмотрите на наши <span class=" orange"> выполненные проекты</span> </WTitle>
    <SharedTabs @selected-tab="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />

    <div class="columns-2  gap-3">
      <div v-for="item in viewItems" class="relative radius-glob w-full">
        <img class="absolute " :src="item.imgSrc" alt="img">
        <div>
          <h2>{{ item.title }}</h2>
          <NuxtLink to="/portfolio_posts/test_id">Узнать цену</NuxtLink>
        </div>
      </div>
    </div>

    <UButton v-if="showMore" @click="viewItemsAmount = viewItemsAmount + 2" color="white" variant="outline" block
      class="py-4 hover:text-gray-700">Показать больше</UButton>
  </WBlock>
</template>
