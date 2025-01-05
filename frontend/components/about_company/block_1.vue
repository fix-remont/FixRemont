<script setup lang="ts">
const items1 = [
  { label: 'Реализовано проектов', amount: '15 000+' },
  { label: 'Довольных клиентов', amount: '99,8%' },
  { label: 'Лет на рынке РФ', amount: '10+' }
]
const items2 = [
  {
    title: 'Сфера деятельности',
    text: 'Ремонт, строительство и обслуживание квартир, жилых домов под ключ'
  },
  {
    title: 'Миссия',
    text: 'Повысить культуру и сервис сферы строительства, чтобы каждый заказчик мог получить качество без переделок и контроля исполнителей'
  },
  {
    title: 'Цели',
    text: [
      'Создание управляющей компании-регулятора',
      'Повышение качества услуг за счёт разработки единых стандартов',
      'Перемены в сфере, чтобы для людей ремонт перестал быть больной темой '
    ]
  }
]
</script>

<template>
  <div class="margin-glob block">
    <h1 class="title-glob">О компании Fix-ремонт</h1>
    <UCarousel class="carousel1" :items="items1" :ui="{ container: 'gap-5' }">
      <template #default="{ item }">
        <div class="item radius-glob">
          <div class="amount orange">{{ item.amount }}</div>
          <div class="label">{{ item.label }}</div>
        </div>
      </template>
    </UCarousel>
    <UCarousel class="carousel2" :items="items2" :ui="{ container: 'gap-5' }">
      <template #default="{ item }">
        <div class="item radius-glob">
          <div class="title">{{ item.title }}</div>
          <ul class="ul list-disc" v-if="Array.isArray(item.text)">
            <li class="li" v-for="li in item.text">{{ li }}</li>
          </ul>
          <div class="text" v-else>{{ item.text }}</div>
        </div>
      </template>
    </UCarousel>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 30px;
  @media (max-width: 640px) {
    gap: 10px;
  }
  .carousel1 {
    .item {
      width: 570px;
      height: 250px;
      background-color: white;
      padding: 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      @media (max-width: 640px) {
        width: 280px;
        height: 120px;
        padding: 10px;
      }

      .label {
        font-size: 20px;
        font-weight: 500;
        @media (max-width: 640px) {
          font-size: 10px;
        }
      }
      .amount {
        align-self: flex-end;
        font-weight: 600;
        font-size: 70px;
        @media (max-width: 640px) {
          font-size: 24px;
        }
      }
    }
  }
  .carousel2 {
    .item {
      width: 570px;
      height: 250px;
      color: white;
      padding: 36px;
      background-color: var(--c-black);
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      @media (max-width: 640px) {
        width: 280px;
        height: 120px;
        padding: 10px;
      }

      .title {
        font-size: 40px;
        font-weight: 600;
        @media (max-width: 640px) {
          font-size: 20px;
        }
      }
      .text {
        font-size: 18px;
        font-weight: 500;
        line-height: 20px;
        @media (max-width: 640px) {
          font-size: 9px;
          line-height: 11px;
        }
      }
      .ul {
        padding-left: 15px;
        font-size: 18px;
        font-weight: 500;
        line-height: 20px;
        @media (max-width: 640px) {
          font-size: 9px;
          line-height: 11px;
        }
      }
    }
  }
}
</style>
