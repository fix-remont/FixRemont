<script setup lang="ts">
const items = [
  '25 бригад и более, чем 30 сотрудников в штате',
  'Сдаём каждый год  более 150 объектов',
  'Работаем без посредников',
  'Был основным подрядчиком компании ТАИФ'
]
</script>

<template>
  <div class="margin-glob-new grid grid-cols-1 gap-[2vw] md:grid-cols-2">
    <div class="md:flex md:flex-col md:justify-between">
      <section>
        <h1 class="text-glob-xl mb-[2vw]">
          Лично
          <span class="text-primary">
            несу <br />
            ответственность <br />
          </span>
          за качество <br />
          предоставляемых услуг
        </h1>
        <p class="subtitle-glob mb-[2em] md:w-4/5">
          За 10 лет мы выполнили более 1 000 объектов и не получили ни одной жалобы на качество
          работы и обслуживания
        </p>
      </section>
      <div class="mb-[4vw] grid grid-cols-1 gap-[4vw] md:mb-0 md:grid-cols-2 md:gap-[1vw]">
        <div
          class="flex flex-col gap-[1vw] rounded-[4vw] bg-white p-[6vw] md:h-[10vw] md:flex-row md:justify-between md:rounded-[1vw] md:p-[2.2vw]"
          v-for="(item, index) in items"
        >
          <span
            class="orange order-2 mt-[.3vw] h-[4vw] w-[4vw] self-end font-bold md:h-[1vw] md:w-[1vw] md:self-start"
          >
            0{{ index + 1 }}
          </span>
          <span class="order-1 me-[10vw] text-[4vw] md:me-0 md:flex md:items-end md:text-[.9vw]">
            {{ item }}</span
          >
        </div>
      </div>
    </div>
    <div class="rounded-glob-new relative">
      <img class="h-full w-full object-cover" src="/images/home/block_11.png" alt="img" />
      <div class="absolute bottom-[6vw] left-[6vw] text-white md:bottom-[3vw] md:left-[3vw]">
        <p
          class="mb-[4vw] text-[6vw] font-semibold leading-[8vw] md:mb-[2vw] md:text-[2vw] md:leading-[2.5vw]"
        >
          Фанис <br />
          Хасанов
        </p>
        <p class="text-[3vw] md:text-[.8vw]">
          Генеральный директор <br />
          FIX РЕМОНТ
        </p>
      </div>
    </div>
  </div>
</template>
