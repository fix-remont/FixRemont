<script setup lang="ts">
import type { Contract } from '~/shared/types/responses'
import { contract } from '~/shared/utils/test-data'

const tabs = ref([
  { label: 'Текущие', value: 'inWork' },
  { label: 'Завершённые', value: 'finished' },
  { label: 'Мои договоры', value: 'mine' }
])

const selectedTabIndex = ref(0)
const selectedTab = computed(() => {
  return tabs.value[selectedTabIndex.value].label
})

const contracts: Contract[] = Array(8).fill(contract)
</script>

<template>
  <article>
    <div class="mb-6 flex flex-col justify-between sm:flex-row">
      <h1 class="title-glob mb-6">Договоры</h1>
      <UButton class="h-min">Пригласить нового клиента</UButton>
    </div>
    <p class="mb-6">В этом разделе вы можете посмотреть подробнее о заказах ваших клиентов</p>
    <SharedTabs
      @selectedTabIndex="(tabIndex: number) => (selectedTabIndex = tabIndex)"
      :tabs="tabs"
    />

    <h1 class="mb-6 text-3xl font-semibold">{{ selectedTab }}</h1>

    <div class="mb-6 flex min-h-40 w-full items-center justify-center">
      <div
        class="grid w-full grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3"
        v-if="contracts.length > 0"
      >
        <div
          class="radius-glob flex flex-col gap-5 bg-white p-2 text-base font-semibold sm:p-5 sm:text-lg"
          v-for="item in contracts"
        >
          <span class="text-orange">№{{ item.id }}</span>
          <span class="underline">{{ item.object_location }}</span>

          <div class="flex justify-between">
            <div class="flex flex-col">
              <p class="text-sm text-gray-500">Объект:</p>
              <p>{{ item.object_type }}</p>
            </div>

            <div class="flex flex-col">
              <p class="text-sm text-gray-500">Тип заказа:</p>
              <p>{{ item.order_type }}</p>
            </div>
          </div>

          <div class="flex justify-between">
            <div>
              <p class="text-sm text-gray-500">Тариф:</p>
              <p>{{ item.tariff }}</p>
            </div>

            <div>
              <p class="text-sm text-gray-500">Площадь:</p>
              <p>{{ item.amount_of_area }}</p>
            </div>
          </div>

          <div class="bg-status-red rounded-lg p-3 text-white" v-if="item.notifications[0]">
            Требуется подписать акт
          </div>

          <div class="rounded-lg bg-[#fafafa] p-5" v-if="item.progress_of_work[0]">
            <p class="text-sm text-gray-500">Текущий этап:</p>
            <p>{{ item.progress_of_work[0].step }}</p>
          </div>

          <div class="flex justify-between">
            <p class="text-sm text-gray-500">Вознаграждение:</p>
            <p>{{ item.costs.your_reward }} руб</p>
          </div>

          <UButton to="/cabinet/contracts/test_id" variant="outline" color="black" block
            >Подробнее о заказе</UButton
          >
        </div>
      </div>
      <div class="radius-glob bg-white text-lg text-gray-500" v-else>У вас нет текущих заказов</div>
    </div>
  </article>
</template>

<style scoped></style>
