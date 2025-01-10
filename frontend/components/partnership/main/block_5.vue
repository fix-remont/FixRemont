<script setup lang="ts">
import { hrefCabinet } from 'assets/variables'

const items = [
  'Удобный онлайн <span class="orange">личный кабинет</span> партнера',
  '<span class="orange">Персональный</span> менеджер',
  'Следите за ходом работ прямо <span class="orange">с телефона</span',
  '<span class="orange">Оформляйте сделку</span> в личном кабинете'
]
</script>

<template>
  <div class="margin-glob">
    <h1 class="title-glob mb-4 md:w-4/5">
      Весь процесс сотрудничества с нами на <span class="orange">100% прозрачный</span> и
      контролируемый
    </h1>

    <div class="wrapper">
      <div class="left">
        <div class="items">
          <div class="item" v-for="item in items" :key="item">
            <img class="icon" src="/images/home/checkbox_checked.svg" alt="icon" />
            <span class="text" v-html="item"></span>
          </div>
        </div>

        <NuxtLink :to="hrefCabinet">
          <SharedButton> Зарегистрироваться на платформе </SharedButton>
        </NuxtLink>
      </div>
      <div class="imgWrapper">
        <img class="" alt="picture" src="/images/partnership/block_5.png" draggable="false" />
      </div>
    </div>
  </div>
</template>

<style scoped>
@media (max-width: 800px) {
  h1 {
    text-align: center;
  }
}
.wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;

  @media (max-width: 800px) {
    flex-direction: column;
    gap: 2rem;
  }
}

.left {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 30px;

  @media (max-width: 800px) {
    width: 100%;
    order: 2;
  }
}

.items {
  grid-area: items;
  display: flex;
  flex-wrap: wrap;
  row-gap: 30px;
  justify-content: space-between;

  .item {
    display: flex;
    gap: 10px;
    font-size: 18px;
    font-weight: 500;
    align-items: flex-start;
    width: 350px;
    padding: 20px;
    border-radius: 24px;

    @media (max-width: 800px) {
      font-size: 16px;
      padding: 10px;
      width: 100%;
    }

    .icon {
    }

    .text {
      padding: 20px;
      font-weight: 450;
    }
  }
}

.imgWrapper {
  width: 50%;

  @media (max-width: 800px) {
    width: 100%;
    order: 1;
  }
}
</style>
