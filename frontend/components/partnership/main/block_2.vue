<script setup lang="ts">
const items = [
  {
    title: 'Риелторам',
    list: [
      'Дополнительный заработок (от 50 т.р) за сделку',
      'Кратно повысите свой уровень сервиса',
      'Увеличите количество сделок за счёт дополнительных услуг по ремонту и строительству',
      'Повысите лояльность благодаря спец. предложениям'
    ],
    selected: false
  },
  {
    title: 'Физ. Лицам',
    list: [
      'Получите скидку на ремонт квартиры',
      'Получите скидку на строительство дома',
      'Получите скидку на ремонт офиса',
      'Получите скидку на ремонт квартиры'
    ],
    selected: false
  },
  {
    title: 'Застройщик',
    list: [
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку'
    ],
    selected: false
  }
]

const names = ['РИЕЛТОР', 'ФИЗ. ЛИЦО', 'ЗАСТРОЙЩИК']

const activeIndex = ref(0)

const setActiveIndex = (index: number) => {
  activeIndex.value = index
}
</script>

<template>
  <div class="margin-glob block">
    <div class="left">
      <h2 class="text-glob-xl">
        <span class="orange">Кому подойдёт </span>
        партнерская программа FIX-ремонт?
      </h2>
      <div class="manipulate">
        <p class="subtitle">Кто вы:</p>
        <UCarousel
          class="choices"
          :items="names"
          :ui="{
            container: 'md:gap-12 gap-2'
          }"
        >
          <template #default="{ item, index }">
            <div
              class="button-box"
              :class="{ active: activeIndex === index }"
              @click="setActiveIndex(index)"
            >
              {{ item }}
            </div>
          </template>
        </UCarousel>
      </div>
    </div>
    <div class="right">
      <UCarousel
        :items="[items[activeIndex]]"
        :ui="{
          item: 'w-full flex flex-col p-10 gap-12 md:items-start items-center'
        }"
      >
        <template #default="{ item }">
          <h4 class="text-4xl font-bold md:text-5xl">{{ item.title }}</h4>
          <ul class="w-full pl-4 text-center md:mb-4 md:list-disc md:text-start">
            <li
              class="mb-4 w-11/12 text-lg font-medium leading-6"
              v-for="(elem, index) in item.list"
              :key="index"
            >
              {{ elem }}
            </li>
          </ul>
        </template>
      </UCarousel>

      <div class="link-buttons">
        <UButton size="custom" color="orange" block> Присоединиться к программе </UButton>
        <UButton size="custom" color="white" variant="outline" block> Подробнее </UButton>
      </div>
    </div>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: row;
  align-items: center;
  align-self: stretch;
}

.left {
  width: 50%;
  align-self: stretch;

  min-height: 50vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .manipulate {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2.08vw;

    .subtitle {
      font-size: 2.6vw;
      font-weight: bold;
      text-decoration: underline;
    }

    .choices {
      max-width: 80%;
    }
  }
}

.right {
  width: 50%;
  align-self: stretch;
  min-height: 50vh;
  height: 100%;
  border-radius: 2.5vw;
  background-color: #efefef;
  padding: 4.17vw;

  .link-buttons {
    width: 50%;
    display: flex;
    flex-direction: row;
    gap: 2.08vw;
    justify-content: space-around;

    @media (max-width: 768px) {
      width: 100%;
      line-height: 1.67vw;
      font-size: 1.67vw;
      flex-direction: column;
      gap: 1vw;
      button {
        font-size: 2.5vw;
      }
    }
  }
}

.button-box {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 0.5vw 0.7vw;
  cursor: pointer;
  color: var(--c-black);
  background: #fff;
  border-radius: 2.5vw;
  border-color: var(--c-black);
  border-style: solid;
  border-width: 0.21vw;
  font-size: 1vw;
  font-weight: 450;
  aspect-ratio: 1 / 1;
  width: 7.5vw;

  &.active {
    background-color: var(--c-black);
    color: #fff;
  }
}

@media (max-width: 768px) {
  .block {
    flex-direction: column;
  }

  .left {
    width: 100%;
    gap: 5vw;
    margin-bottom: 2.08vw;
    h2 {
      text-align: center;
    }
    .manipulate {
      align-items: center;
    }
  }

  .right {
    width: 100%;
    padding: 2vw;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .button-box {
    padding: 4vw 4vw;
    font-size: 2.5vw;
    width: 20vw;
  }
}
</style>
