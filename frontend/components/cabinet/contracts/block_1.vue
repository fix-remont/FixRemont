<script setup lang="ts">
import type { Contract } from '~/shared/types/types';
import { contract } from '~/shared/utils/data';

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
    <div class="flex justify-between mb-6 flex-col sm:flex-row">
      <h1 class="title-glob mb-6">Договоры</h1>
      <UButton class="h-min">Пригласить нового клиента</UButton>
    </div>
    <p class="mb-6">В этом разделе вы можете посмотреть подробнее о заказах ваших клиентов</p>
    <SharedTabs @selectedTabIndex="(tabIndex: number) => (selectedTabIndex = tabIndex)" :tabs="tabs" />

    <h1 class="text-3xl font-semibold mb-6">{{ selectedTab }}</h1>

    <div class=" flex justify-center items-center w-full min-h-40 mb-6">
      <div v-if="contracts.length > 0" class="grid grid-cols-1 md:grid-cols-2  xl:grid-cols-3 w-full gap-8">

        <div v-for="item in contracts"
          class=" text-base sm:text-lg font-semibold p-2 sm:p-5  radius-glob bg-white flex flex-col gap-5">
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

          <div v-if="item.notifications[0]" class="bg-status-red rounded-lg p-3 text-white">
            Требуется подписать акт
          </div>

          <div v-if="item.progress_of_work[0]" class="bg-[#fafafa] rounded-lg p-5">
            <p class="text-sm text-gray-500">Текущий этап:</p>
            <p>{{ item.progress_of_work[0].step }}</p>
          </div>

          <div class="flex justify-between">
            <p class="text-sm text-gray-500">Вознаграждение:</p>
            <p>{{ item.costs.your_reward }} руб</p>

          </div>

          <UButton to="/cabinet/contracts/test_id" variant="outline" color="black" block>Подробнее о заказе</UButton>

        </div>


      </div>
      <div v-else class="text-lg text-gray-500 bg-white radius-glob">У вас нет текущих заказов</div>
    </div>
  </article>
</template>

<style scoped></style>
