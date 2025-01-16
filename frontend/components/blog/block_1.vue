<script setup lang="ts">
const tabs = [
  { label: 'Все', value: 'all' },
  { label: 'Ремонт квартир', value: 'all' },
  { label: 'Строительстрво домов', value: 'all' },
  { label: 'Полезное', value: 'all' }
]

const items = ref(Array(9))
const viewItemsAmount = ref(4)

const viewItems = computed(() => {
  return items.value.slice(0, viewItemsAmount.value)
})

function handleShowMoreItems() {
  viewItemsAmount.value = viewItemsAmount.value + 2
}
const hasShowMore = computed(() => items.value.length > viewItemsAmount.value)
</script>

<template>
  <WBlock>
    <p class="mb-5">Делимся полезными идеями и раскрываем секреты ремонта и строительства</p>
    <WTitle class="mb-5"> Полезные статьи </WTitle>
    <SharedTabs :tabs="tabs"></SharedTabs>
    <div class="relative flex flex-col gap-5 lg:flex-row">
      <div>
        <div class="grid grid-cols-1 grid-rows-[max-content] gap-5 xl:grid-cols-2">
          <div class="radius-glob relative h-max overflow-hidden" v-for="item in viewItems">
            <img class="w-full" src="/images/home/block_14_for-blog.png" alt="img" />
            <span
              class="absolute left-6 top-6 rounded-full bg-[var(--c-black)] px-4 py-3 text-white"
              >Ремонт</span
            >
            <NuxtLink
              class="absolute bottom-6 left-6 pe-6 font-semibold text-white underline"
              to="/blog/test_id"
              >Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?</NuxtLink
            >
          </div>
        </div>
        <UButton
          class="hover my-8"
          v-if="hasShowMore"
          @click="handleShowMoreItems"
          color="white"
          block
          size="xl"
          >Показать больше</UButton
        >
      </div>
      <SharedFormConsultationForBlog />
    </div>
  </WBlock>
</template>
