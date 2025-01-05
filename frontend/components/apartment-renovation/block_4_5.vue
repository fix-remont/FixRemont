<script setup lang="ts">
const items = [
  '25 бригад и более, чем 30 сотрудников в штате',
  'Сдаём каждый год  более 150 объектов',
  'Работаем без посредников',
  'Был основным подрядчиком компании ТАИФ'
]
</script>

<template>
  <div class="block2 margin-glob">
    <h1 class="title title-glob">
      Лично <span class="orange"> несу ответственность </span> за качество предоставляемых услуг
    </h1>
    <div class="img-container">
      <img class="img" src="/images/home/block_11.png" alt="img" />
      <div class="text-container">
        <p class="text1">Фанис Хасанов</p>
        <p class="text2">
          Генеральный директор <br />
          FIX РЕМОНТ
        </p>
      </div>
    </div>
    <div class="items">
      <div class="item" v-for="item in items" :key="item">
        <img class="icon" src="/icons/checkbox__checked__orange.svg" alt="icon" />
        <span class="text"> {{ item }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.block2 {
  display: grid;
  grid-template-areas: 'title img' 'items img';
  grid-template-columns: 700px auto;
  gap: 30px;

  @media (max-width: 1240px) {
    grid-template-areas: 'title' 'img' 'items';
    grid-template-columns: auto;
    gap: 10px;
  }

  .title {
    grid-area: title;
  }

  .img-container {
    grid-area: img;
    display: flex;
    position: relative;
    color: white;

    .img {
      width: 100%;
      height: auto;
      object-fit: cover;
      border-radius: 35px;

      /* object-position: ; */
      @media (max-width: 800px) {
        border-radius: 20px;
      }
    }

    .text-container {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      bottom: 20px;
      left: 20px;
      position: absolute;

      .text1 {
        font-size: 32px;
        font-weight: 600;

        @media (max-width: 800px) {
          font-size: 20px;
        }
      }

      .text2 {
        font-size: 15px;
        font-weight: 500;

        @media (max-width: 800px) {
          font-size: 12px;
        }
      }
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

      @media (max-width: 800px) {
        width: auto;
        font-size: 16px;
      }

      .icon {
        position: relative;
        top: 4px;
      }

      .text {
      }
    }
  }
}
</style>
