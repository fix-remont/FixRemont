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
      'Получите скидку на ремонт квартиры',
    ],
    selected: false
  },
  {
    title: 'Застройщик',
    list: [
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку',
      'Кешбек за каждую сделку',
    ],
    selected: false
  }
]

const names = [
  'РИЕЛТОР',
  'ФИЗ. ЛИЦО',
  'ЗАСТРОЙЩИК'
]

const activeIndex = ref(0);

const setActiveIndex = (index: number) => {
  activeIndex.value = index;
};
</script>

<template>
  <div class="margin-glob block">
    <div class="left">
      <h2 class="title-glob">
        <span class="orange">Кому подойдёт </span>
        партнерская программа FIX-ремонт?
      </h2>
      <div class="manipulate">
        <p class="subtitle">
          Кто вы:
        </p>
        <UCarousel
            :items="names"
            :ui="{
              container: 'md:gap-12 gap-2',
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
            <h4 class="md:text-5xl font-bold text-4xl">{{ item.title }}</h4>
            <ul class="md:list-disc pl-4 md:mb-4 text-center md:text-start w-full">
              <li
                  v-for="(elem, index) in item.list" :key="index"
                  class="w-11/12 text-lg font-medium leading-6 mb-4"
              >
                {{ elem }}
              </li>
            </ul>
        </template>
      </UCarousel>

      <div class="link-buttons">
        <NuxtLink>
          <SharedButton fill-orange>
            Присоединиться к программе
          </SharedButton>
        </NuxtLink>

        <NuxtLink class="button2">
          <SharedButton>
            Подробнее
          </SharedButton>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.left {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 10rem;

  .manipulate {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;

    .subtitle {
      font-size: 25px;
      font-weight: bold;
      text-decoration: underline;
    }
  }
}

.right {
  width: 50%;
  height: 100%;
  border-radius: 24px;
  background-color: #EFEFEF;
  padding: 40px;
}

.button-box {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 30px 10px;
  cursor: pointer;
  color: var(--c-black);
  background: #fff;
  border-radius: 24px;
  border-color: var(--c-black);
  border-style: solid;
  border-width: 2px;
  font-size: 17px;
  font-weight: 450;
  letter-spacing: 0.001px;
  aspect-ratio: 1 / 1;
  width: 130px;

  &.active {
    background-color: var(--c-black);
    color: #fff;
  }
}

.link-buttons {
  width: 100%;
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: space-around;

  .button2 {
    width: 40%;
  }
}

@media (max-width: 640px) {
  .block {
    flex-direction: column;
  }

  .left {
    width: 100%;
    gap: 5rem;
    margin-bottom: 2rem;
    h2 {
      text-align: center;
    }
    .manipulate {
      align-items: center;
    }
  }

  .right {
    width: 100%;
    padding: 20px;
  }

  .button-box {
    padding: 20px 10px;
    font-size: 14px;
    width: 100px;
  }

  .link-buttons {
    flex-direction: column;
    gap: 10px;

    .button2 {
      width: 100%;
    }
  }

}
</style>