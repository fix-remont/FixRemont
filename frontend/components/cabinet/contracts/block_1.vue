<script setup lang="ts">
const tabs = [
  { label: 'Текущие', value: 'inWork' },
  { label: 'Завершённые', value: 'finished' },
  { label: 'Мои договоры', value: 'mine' }
]

const selectedTabIndex = ref(0)
</script>

<template>
  <article>
    <div class="flex justify-between">
      <div>
        <h1 class="title-glob">Договоры</h1>
        <p>В этом разделе вы можете посмотреть подробнее о заказах ваших клиентов</p>
      </div>
      <UButton class="h-min rounded-full px-10 py-6" color="orange"
        >Пригласить нового клиента</UButton
      >
      <!-- <SharedButton class="h-min" fillOrange>Пригласить нового клиента</SharedButton> -->
    </div>
    <SharedTabs @selected-tab="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />
  </article>
</template>

<style scoped></style>
