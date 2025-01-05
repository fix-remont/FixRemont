<script setup lang="ts">
const items = [
  'Рабочие и мастера постоянно звонили и просили что-то довезти',
  'Супруге с маленьким ребенком приходилось практически ежедневно ездить в магазины и что-то докупать',
  'Ежедневно она тратила 2-3 часа на пробки, езду и покупки',
  'Мастера постоянно косячили, а смета непрерывно росла'
]
</script>

<template>
  <div class="margin-glob block">
    <div class="img-container">
      <img class="img radius-glob" src="/images/home/block_11.png" alt="img" draggable="false" />
      <div class="texts">
        <h1 class="title">
          Фанис <br />
          Хасанов
        </h1>
        <p class="text">
          Генеральный директор <br />
          FIX-ремонт
        </p>
      </div>
    </div>
    <div class="info">
      <h1 class="title-glob">
        Здравствуйте! <span class="orange">Меня зовут Фанис Хасанов</span> и я приветствую вас на
        нашем сайте!
      </h1>
      <p class="text text-1">
        Мы с супругой прочувствовали все сложности самостоятельного ремонта, когда продали квартиру
        и купили дом. Тогда я работал в Москве и принимать активное участие в ремонте не мог.
      </p>
      <ul class="ul list-disc">
        <li v-for="item in items">{{ item }}</li>
      </ul>
      <p class="text text-2">
        Конечно, я принял решение сменить подрядчиков. Стал искать компании, предлагающие ремонт по
        фиксированное цене и забирающие всю ответственность на себя. Таких компании на рынке не
        было. Поэтому и родилась идея создать FIX-ремонт.
      </p>
      <p class="text text-3">
        С нами заказчик получает ремонт, строительство, покупку, продажу, благоустройство,
        мебелировку и многое другое по фиксированной стоимости, потратив всего 1.5 часа личного
        времени
      </p>
    </div>
  </div>
</template>
<style scoped lang="postcss">
.block {
  display: flex;
  gap: 30px;

  @media (max-width: 1000px) {
    flex-direction: column;
  }
  .img-container {
    position: relative;
    .img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .texts {
      position: absolute;
      color: white;
      bottom: 0;
      left: 0;
      transform: translate(20px, -20px);
      font-size: 10px;
      @media (max-width: 640px) {
        font-size: 6px;
      }

      .title {
        font-size: 3.2em;
        font-weight: 600;
        line-height: 1.2em;
        margin-bottom: 20px;
      }
      .text {
        font-size: 1.5em;
        font-weight: 500;
      }
    }
  }
  .info {
    width: 890px;
    font-size: 18px;
    font-weight: 500;
    display: flex;
    flex-direction: column;
    gap: 20px;
    @media (max-width: 1000px) {
      width: 100%;
      font-size: 14px;
    }
    .text {
      &-2 {
        font-size: 24px;
        @media (max-width: 640px) {
          font-size: 18px;
        }
      }
    }
    .ul {
      margin-left: 20px;
    }
  }
}
</style>
