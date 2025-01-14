<script setup lang="ts">
import { portfolioItemsShort as items } from '~/shared/utils/data'

const tabs = [
  { label: 'Все', value: 'all' },
  { label: 'Ремонт квартир', value: 'appartament_renovation' },
  { label: 'Строительство домов', value: 'house_construction' }
]
const selectedTabIndex = ref(0)
</script>

<template>
  <UiBlock>
    <p>Работаем одинаково хорошо, как на крупных объектах, так и в небольших квартирах</p>
    <UiTitle> Посмотрите на наши <span class="orange"> выполненные проекты</span> </UiTitle>

    <SharedTabs @selected-tab="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />
  </UiBlock>
</template>
