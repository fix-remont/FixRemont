<script setup lang="ts">
const items = [
  'На рынке с 2013 года',
  'Построили более 1 500 домов по всей РФ',
  'Средний стаж строителя - 15 лет'
]
</script>

<template>
  <div class="margin-glob-new">
    <div class="text-glob-xl mb-[5vw] md:mb-[1vw]">
      Над вашим объектом будет работать команда
      <span class="text-primary">настоящих фанатов</span> своего дела
    </div>
    <div class="relative mb-[4vw] md:mb-[2vw]">
      <img
        class="rounded-glob-new h-[70vw] w-full object-cover md:h-auto"
        src="/images/home/block_10.png"
        alt="img"
      />
      <div
        class="absolute bottom-[6vw] left-[6vw] flex w-full flex-col justify-around gap-[4vw] text-white md:bottom-[2vw] md:left-0 md:flex-row md:gap-0"
      >
        <div class="flex items-center gap-[1vw]" v-for="item in items" :key="item">
          <img
            class="h-[4vw] w-[4vw] md:h-[1.5vw] md:w-[1.5vw]"
            src="/images/home/checkbox_checked.svg"
            alt=""
          />
          <span class="text-[3vw] font-medium md:text-[1vw]">{{ item }}</span>
        </div>
      </div>
    </div>
    <UButton block :to="'#'" color="white" variant="outline" size="custom"
      >Оставить заявку на консультацию от специалиста</UButton
    >
  </div>
</template>
