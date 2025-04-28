<script setup lang="ts">
const items = [
  'Более 16 лет работаю в строительной нише. Строительное образование. Начинал мастером СМР',
  'В 2016 создал платформу для покупки и продажи стройматериалов и услуг MySupl.ru',
  'Более 5 лет занимался комплексным снабжением объектов стройматериалами',
  'Провел в 2019 году 3 крупных бизнес-форумов на 200-1500 человек',
  'Был основным подрядчиком «ТАИФ». Построил 50+объектов крупного значения',
  'Президент локальной международной палаты JCI Russia в Казани в 2019-2020 гг.',
  'Был резидентом IT-парка  и «Сколково»',
  'В 2019 создал ассоциацию строителей «Перестройка»'
]
</script>

<template>
  <div class="margin-glob-new grid grid-cols-1 gap-[2vw] md:grid-cols-2">
    <div>
      <h1 class="text-glob-xl mb-[2vw]">
        Лично
        <span class="text-primary">
          несу <br />
          ответственность <br />
        </span>
        за качество <br />
        предоставляемых услуг
      </h1>
      <div class="mb-[4vw] grid grid-cols-1 gap-[4vw] md:mb-0 md:grid-cols-2 md:gap-[1vw]">
        <div
          class="flex flex-col gap-[1vw] rounded-[4vw] bg-white p-[6vw] md:flex-row md:rounded-[1vw] md:p-[1.4vw]"
          v-for="item in items"
        >
          <img
            class="mt-[.3vw] h-[4vw] w-[4vw] self-end md:h-[1vw] md:w-[1vw] md:self-start"
            src="/icons/checkbox__checked__orange.svg"
            alt="icon"
          />
          <span class="me-[10vw] text-[4vw] md:me-0 md:text-[.9vw]"> {{ item }}</span>
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
