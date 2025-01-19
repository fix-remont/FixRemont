<script setup lang="ts">
import { contract } from '~/shared/utils/test-data'

const totalCosts = Object.values(contract.costs).reduce((acc, value) => {
  acc += value
  return acc
}, 0)
</script>

<template>
  <article class="mb-5 flex flex-col gap-8">
    <div class="mb-6 flex flex-col justify-between sm:flex-row">
      <h1 class="title-glob mb-6">Заказ №{{ contract.id }}</h1>
      <UButton class="h-min">Пригласить нового клиента</UButton>
    </div>

    <div class="radius-glob bg-white p-2 font-semibold sm:p-6">
      <p class="mb-5 text-2xl">Информация об объекте</p>
      <div class="flex flex-wrap items-center justify-between gap-5">
        <div>
          <p class="text-sm text-gray-500">Объект:</p>
          <p>{{ contract.object_type }}</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Тип заказа:</p>
          <p>{{ contract.order_type }}</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Тариф:</p>
          <p>{{ contract.tariff }}</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Площадь:</p>
          <p>{{ contract.amount_of_area }}</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Локация:</p>
          <p>{{ contract.object_location }}</p>
        </div>
      </div>
    </div>

    <div class="radius-glob bg-white p-2 font-semibold sm:p-6">
      <p class="mb-5 text-2xl">Расчёт сметы</p>
      <div class="flex flex-wrap items-center justify-between gap-5">
        <div>
          <p class="text-sm text-gray-500">Общая стоимость:</p>
          <p>{{ totalCosts }} руб</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Материалы:</p>
          <p>{{ contract.costs.materials }} руб</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Работы:</p>
          <p>{{ contract.costs.work_process }} руб</p>
        </div>

        <div>
          <p class="text-sm text-gray-500">Ваше вознаграждение:</p>
          <p>{{ contract.costs.your_reward }} руб</p>
        </div>

        <UButton class="w-full sm:w-[initial]">Скачать полную смету</UButton>
      </div>
    </div>

    <div class="grid grid-cols-1 gap-8 xl:grid-cols-2">
      <div class="radius-glob bg-white p-2 font-semibold sm:p-6">
        <p class="mb-5 text-2xl">Информация о клиенте:</p>
        <div class="flex flex-col gap-5">
          <div>
            <p class="text-sm text-gray-500">Клиент:</p>
            <p>{{ contract.client_info.name }}</p>
          </div>
          <UDivider />

          <div>
            <p class="text-sm text-gray-500">Номер телефона:</p>
            <p>{{ contract.client_info.phone }}</p>
          </div>

          <UDivider />

          <div>
            <p class="text-sm text-gray-500">Email:</p>
            <p>{{ contract.client_info.email }}</p>
          </div>
          <UDivider />

          <div>
            <p class="text-sm text-gray-500">Дата заказа:</p>
            <p>{{ contract.client_info.order_date }}</p>
          </div>
        </div>
      </div>

      <div
        class="radius-glob bg-white p-2 font-semibold sm:p-6"
        v-if="contract.notifications.length > 0"
      >
        <p class="mb-5 text-2xl">Уведомления по заказу:</p>
        <div class="flex flex-col gap-5">
          <div
            class="flex flex-col items-start md:flex-row md:items-center"
            v-for="item in contract.notifications"
          >
            <div class="flex flex-col">
              <div class="flex items-center gap-3">
                <span :class="[`bg-${item.status}-500`, 'h-2 w-2 rounded-full']"></span>
                <span>{{ item.type }}</span>
              </div>
              <p class="text-sm text-gray-500" v-if="item.text">{{ item.text }}</p>
            </div>
            <UButton class="ms-auto w-full justify-center md:w-72" color="white" variant="outline"
              >Открыть</UButton
            >
          </div>
        </div>
      </div>

      <div
        class="radius-glob bg-white p-2 font-semibold sm:p-6"
        v-if="contract.payments.length > 0"
      >
        <p class="mb-5 text-2xl">Оплата:</p>
        <div class="flex flex-col gap-5">
          <div
            class="flex flex-col items-start md:flex-row md:items-center"
            v-for="item in contract.payments"
          >
            <div class="flex flex-col">
              <div class="flex items-center gap-3">
                <span :class="[`bg-${item.status}-500`, 'h-2 w-2 rounded-full']"></span>
                <span>{{ item.amount }} руб</span>
              </div>
              <p class="text-sm text-gray-500" v-if="item.text">{{ item.text }}</p>
            </div>
            <UButton
              class="ms-auto w-full justify-center md:w-72"
              :color="item.status"
              variant="outline"
              >Открыть
            </UButton>
          </div>
        </div>
      </div>

      <div
        class="radius-glob bg-white p-2 font-semibold sm:p-6"
        v-if="contract.documents.length > 0"
      >
        <p class="mb-5 text-2xl">Документы:</p>
        <div class="flex flex-col gap-5">
          <div
            class="flex flex-col items-start md:flex-row md:items-center"
            v-for="item in contract.documents"
          >
            <div class="flex flex-col">
              <div class="flex items-center gap-3">
                <span :class="[`bg-${item.status}-500`, 'h-2 w-2 rounded-full']"></span>
                <span>{{ item.type }} руб</span>
              </div>
              <p class="text-sm text-gray-500" v-if="item.text">{{ item.text }}</p>
            </div>
            <UButton class="ms-auto w-full justify-center md:w-72" color="white" variant="outline"
              >Скачать</UButton
            >
          </div>
        </div>
      </div>
    </div>
  </article>
</template>
