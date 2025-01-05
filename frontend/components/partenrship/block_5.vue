<script setup lang="ts">
const items = [
  'Удобный онлайн <span class="orange">личный кабинет</span> партнера',
  '<span class="orange">Персональный</span> менеджер',
  'Следите за ходом работ прямо <span class="orange">с телефона</span',
  '<span class="orange">Оформляйте сделку</span> в личном кабинете',
]
</script>

<template>
<div class="margin-glob">
  <h1 class="title-glob md:w-4/5 mb-4">
    Весь процесс сотрудничества с нами
    на <span class="orange">100% прозрачный</span> и контролируемый
  </h1>

  <div class="wrapper">
    <div class="left">
      <div class="items">
        <div class="item" v-for="item in items" :key="item">
          <span v-html="item" class="text"></span>
          <img class="icon" src="/images/home/checkbox_checked.svg" alt="icon">
        </div>
      </div>

      <NuxtLink>
        <SharedButton>
          Зарегистрироваться на платформе
        </SharedButton>
      </NuxtLink>
    </div>
    <div class="imgWrapper">
      <img class="" alt="picture" src="/images/partnership/block_5.png" draggable="false"/>
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
        justify-content: space-between;
        width: 100%;
      }

      .icon {
        position: relative;
        top: 4px;
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