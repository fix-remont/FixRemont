<script setup lang="ts">
import { contract } from '~/shared/utils/data';


const totalCosts = Object.values(contract.costs).reduce((acc, value) => {
  acc += value
  return acc
}, 0)
</script>

<template>
  <article class="flex flex-col gap-8 mb-5">
    <div class="flex justify-between mb-6 flex-col sm:flex-row">
      <h1 class="title-glob mb-6">Заказ №{{ contract.id }}</h1>
      <UButton class="h-min">Пригласить нового клиента</UButton>
    </div>

    <div class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
      <p class="text-2xl mb-5">Информация об объекте</p>
      <div class="flex flex-wrap justify-between items-center gap-5">
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

    <div class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
      <p class="text-2xl mb-5">Расчёт сметы</p>
      <div class="flex flex-wrap justify-between items-center gap-5">
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


    <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">


      <div class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
        <p class="text-2xl mb-5">Информация о клиенте:</p>
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

      <div v-if="contract.notifications.length > 0" class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
        <p class="text-2xl mb-5">Уведомления по заказу:</p>
        <div class="flex flex-col gap-5">
          <div v-for="item in contract.notifications" class="flex flex-col md:flex-row  items-start md:items-center">
            <div class="flex flex-col">
              <div class="flex gap-3 items-center">
                <span :class="[`bg-${item.status}-500`, 'rounded-full w-2 h-2']"></span>
                <span>{{ item.type }}</span>

              </div>
              <p v-if="item.text" class="text-sm text-gray-500">{{ item.text }}</p>
            </div>
            <UButton class=" ms-auto w-full md:w-72 justify-center" color="white" variant="outline">Открыть</UButton>
          </div>
        </div>
      </div>

      <div v-if="contract.payments.length > 0" class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
        <p class="text-2xl mb-5">Оплата:</p>
        <div class="flex flex-col gap-5">
          <div v-for="item in contract.payments" class="flex flex-col md:flex-row  items-start md:items-center">
            <div class="flex flex-col">
              <div class="flex gap-3 items-center">
                <span :class="[`bg-${item.status}-500`, 'rounded-full w-2 h-2']"></span>
                <span>{{ item.amount }} руб</span>

              </div>
              <p v-if="item.text" class="text-sm text-gray-500">{{ item.text }}</p>
            </div>
            <UButton class=" ms-auto w-full md:w-72 justify-center" :color="item.status" variant="outline">Открыть
            </UButton>
          </div>
        </div>
      </div>

      <div v-if="contract.documents.length > 0" class="p-2 sm:p-6 bg-white radius-glob font-semibold ">
        <p class="text-2xl mb-5">Документы:</p>
        <div class="flex flex-col gap-5">
          <div v-for="item in contract.documents" class="flex flex-col md:flex-row  items-start md:items-center">
            <div class="flex flex-col">
              <div class="flex gap-3 items-center">
                <span :class="[`bg-${item.status}-500`, 'rounded-full w-2 h-2']"></span>
                <span>{{ item.type }} руб</span>

              </div>
              <p v-if="item.text" class="text-sm text-gray-500">{{ item.text }}</p>
            </div>
            <UButton class=" ms-auto w-full md:w-72 justify-center" color="white" variant="outline">Скачать</UButton>
          </div>
        </div>
      </div>

    </div>
  </article>
</template>