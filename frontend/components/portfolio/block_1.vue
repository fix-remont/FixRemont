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
  <div class="margin-glob block">
    <p>Работаем одинаково хорошо, как на крупных объектах, так и в небольших квартирах</p>
    <h1 class="title title-glob">
      Посмотрите на наши <span class="orange"> выполненные проекты</span>
    </h1>
    <SharedTabs @selected-tab="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />
  </div>
</template>

<style scoped>
.block {
  .title {
    margin-bottom: 30px;
    @media (max-width: 640px) {
      margin-bottom: 10px;
    }
  }
  .tabs-container {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;

    @media (max-width: 640px) {
      gap: 5px;
      margin-bottom: 10px;
    }
    .tab {
      padding: 12px 28px;
      color: var(--c-black);
      background-color: white;

      @media (max-width: 640px) {
        padding: 6px 8px;
        font-size: 10px;
      }
      &-selected {
        color: white;
        background-color: var(--c-black);
      }
    }
  }
}
</style>
