<script setup lang="ts">
const items = [
  'На рынке с 2013 года',
  'Построили более 1 500 домов по всей РФ', 'Средний стаж строителя - 15 лет']
</script>

<template>
  <div class="margin-glob block">
    <div class="title-glob">Над вашим объектом будет работать команда <span class="orange">настоящих фанатов</span>
      своего
      дела </div>
    <div class="img-container">
      <img class="img" src="/images/home/block_10.png" alt="img">
      <div class="checkboxes-container">
        <div class="item" v-for="item in items" :key="item">
          <img class="icon" src="/images/home/checkbox_checked.svg" alt="">
          <span class="text">{{ item }}</span>
        </div>
      </div>
    </div>
    <SharedButton>Оставить заявку на консультацию от специалиста</SharedButton>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 30px;

  @media (max-width:1240px) {
    gap: 10px;
  }

  .img-container {
    position: relative;

    .checkboxes-container {
      display: flex;
      width: 100%;
      justify-content: space-evenly;
      position: absolute;
      bottom: 85px;
      flex-wrap: wrap;

      @media (max-width:640px) {
        bottom: 10px;
        left: 10px;
        justify-content: flex-start;
        flex-direction: column;
        gap: 15px;
      }

      .item {
        display: flex;
        gap: 10px;

        @media (max-width:640px) {
          gap: 5px;

        }

        .icon {
          width: 25px;
          height: 25px;

          @media (max-width:640px) {
            width: 15px;
            height: 15px;
          }
        }

        .text {
          font-size: 24px;
          font-weight: 500;
          color: white;

          @media (max-width:640px) {
            font-size: 12px;
          }

        }
      }
    }

  }
}
</style>
