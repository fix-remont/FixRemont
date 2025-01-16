<script setup lang="ts">
type PortfolioPost = {
  id: number
  title: string
  work_completion_time: string
  price_amount: string
  object_area: string
  img_title: string
  img_result?: string
  images: (null | string)[]
  type_of_work: string
  videos: {
    overview: { duration: string; item: string }
    others: (null | { duration: string; item: string })[]
  }
  texts: {
    task: string
    steps_of_work: ({ title: string; content: string } | null)[]
  }
}

const item: PortfolioPost = {
  id: 1,
  title: 'Дом из кирпича 560 м2 на Барвихе',
  work_completion_time: '15 дней',
  price_amount: '2 500 000 руб',
  object_area: '240 м',
  img_title: '/images/home/block_7__1.png',
  images: [
    '/images/home/block_7__1.png',
    '/images/home/block_7__1.png',
    '/images/home/block_7__1.png',
    '/images/home/block_7__1.png',
    '/images/home/block_7__1.png'
  ],
  type_of_work: 'Строительство домов',
  videos: {
    overview: { duration: '0:18 сек', item: '/images/home/block_7__1.png' },
    others: []
  },
  texts: {
    task: 'Театр, специализирующийся на разнообразных представлениях, выразил желание усовершенствовать свои технические возможности для привлечения новой аудитории и создания незабываемых визуальных впечатлений. Заказчик искал комплексное решение для обновления мультимедийного оборудования на сцене и в зрительном зале.',
    steps_of_work: [
      {
        title: 'Анализ потребностей и проектирование.',
        content:
          'Начали с тщательного анализа потребностей театра и его амбиций. Определили желаемые эффекты, аудиовизуальные элементы, типы представлений и ожидаемую аудиторию.'
      },
      {
        title: 'Подбор оборудования.',
        content:
          'Определение наилучших производителей и моделей оборудования, учитывая баланс между качеством и бюджетом. Выбрали проекторы высокой разрешающей способности, звуковые системы с четким и мощным звучанием, а также подвижные световые приборы для динамичных эффектов.'
      },
      {
        title: 'Производство.',
        content:
          'Определение наилучших производителей и моделей оборудования, учитывая баланс между качеством и бюджетом. Выбрали проекторы высокой разрешающей способности, звуковые системы с четким и мощным звучанием, а также подвижные световые приборы для динамичных эффектово.'
      },
      {
        title: 'Тестирование и обучение персонала.',
        content:
          'Провели комплексное тестирование оборудования перед открытием для публики. Провели обучение персонала театра по работе с новой техникой, чтобы максимально эффективно использовать ее на представлениях.'
      }
    ]
  }
}

const infos = [
  { label: 'Сроки', value: `${item.work_completion_time}` },
  { label: 'Стоимость', value: `${item.price_amount}` },
  { label: 'Площадь объекта', value: `${item.object_area}` }
]
</script>

<template>
  <WBlock class="flex flex-col gap-4">
    <WTitle>{{ item.title }}</WTitle>
    <div class="flex flex-wrap gap-10">
      <div v-for="info in infos">
        <p class="text-xs text-[#C1C1C1] sm:text-sm">{{ info.label }}</p>
        <p class="text-sm font-bold text-[#161616] sm:text-xl">{{ info.value }}</p>
      </div>
    </div>
    <div class="radius-glob relative overflow-hidden">
      <img class="w-full" :src="item.img_title" alt="img=title" />
      <span
        class="absolute left-5 top-5 rounded-md bg-white px-5 py-2 font-semibold text-black sm:left-10 sm:top-10"
        >{{ item.type_of_work.toUpperCase() }}</span
      >
    </div>
    <div class="radius-glob relative overflow-hidden">
      <img class="w-full" :src="item.videos.overview.item" alt="video" />

      <img
        class="hover absolute bottom-5 left-5 h-10 w-10 sm:bottom-10 sm:left-10 sm:h-16 sm:w-16"
        src="/icons/play-button.svg"
      />
      <span
        class="absolute left-5 top-5 rounded-md bg-white px-5 py-2 font-semibold text-black sm:left-10 sm:top-10"
        >{{ item.videos.overview.duration }}</span
      >
    </div>
    <div class="radius-glob bg-white px-8 py-8">
      <WTitle class="mb-6">Задача</WTitle>
      <p class="mb-6">{{ item.texts.task }}</p>
      <WTitle class="mb-6">Ход работы:</WTitle>
      <div class="mb-6" v-for="step in item.texts.steps_of_work">
        <h3>
          <b> {{ step?.title }}</b>
        </h3>
        <p>{{ step?.content }}</p>
      </div>
    </div>
    <UCarousel
      v-if="item.images.length > 0"
      v-slot="{ item }"
      :items="item.images"
      :ui="{ container: 'gap-10' }"
    >
      <img :src="item" width="300" height="400" draggable="false" alt="img" />
    </UCarousel>
  </WBlock>
</template>
