<script setup lang="ts">
const blocksWhite = [
  'Дополнительный доход <br/> от 50 000 руб за сделку',
  'Увеличите общее количество сделок',
  'Кратно повысите уровень своего сервиса',
  'Повысите лояльность, благодаря специальным предложениям',
  'Повысите свой уровень конкуренто<wbr/>способности',
  'И всё это без рисков для репутации, так как мы берём всё на себя!'
]

const blocksBlack = [
  'Избавятся от долгого подбора материала и подсчётов бюджета',
  'Не нужно искать проверенную бригаду',
  'Не нужно заниматься организацией работ',
  'Не нужно постоянно контролировать процессы',
  'Не нужно регулярно закупать и доставлять материалы',
  'И больше никаких ссор в семье на нервной почве!'
]
</script>

<template>
  <div class="margin-glob block">
    <div class="left">
      <div class="wrapper">
        <h2 class="title">
          Выгода работы
          <wbr />с нами очевидна
        </h2>
        <NuxtLink>
          <SharedButton>Стать партнером</SharedButton>
        </NuxtLink>
      </div>
    </div>

    <div class="right">
      <div class="upper">
        <h2 class="title">Для вас:</h2>
        <div class="items">
          <div class="item white" v-for="(item, index) in blocksWhite" :key="index">
            <span class="text" v-html="item"></span>
            <span class="index orange">0{{ index + 1 }}</span>
          </div>
        </div>
      </div>
      <div class="down">
        <h2 class="title">Для ваших клиентов:</h2>
        <div class="items">
          <div class="item black" v-for="(item, index) in blocksBlack" :key="index">
            <span class="text" v-html="item"></span>
            <span class="index orange">0{{ index + 1 }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  height: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 3rem;

  @media (max-width: 800px) {
    flex-direction: column;
    gap: 2rem;
  }
}

.title {
  font-size: 3rem;
  line-height: 1.25;
  font-weight: 600;

  @media (max-width: 800px) {
    font-size: 40px;
    text-align: center;
  }
}

.left {
  min-width: 40%;
  min-height: 100%;
  align-self: stretch;
  display: flex;

  .wrapper {
    width: 80%;
    display: flex;
    flex-direction: column;
    gap: 1em;
    position: sticky;
    top: 10px;
    align-self: flex-start;
  }

  @media (max-width: 800px) {
    width: 100%;
    top: 0;
    justify-content: center;
  }
}

.upper,
.down {
  .title {
    margin-bottom: 3rem;
  }

  @media (max-width: 800px) {
    display: flex;
    flex-direction: column;
    align-items: center;

    .title {
      width: 100%;
      text-align: center;
      margin-bottom: 1rem;
    }
  }
}

.items {
  display: grid;
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr 1fr;
  row-gap: 50px;
  column-gap: 50px;
  margin-bottom: 2rem;

  @media (max-width: 800px) {
    gap: 10px;
  }

  .item {
    position: relative;
    display: flex;
    align-items: flex-start;
    align-self: end;
    justify-content: space-between;
    font-size: 18px;
    font-weight: 500;
    height: 180px;
    width: 400px;
    border-radius: 24px;
    padding: 40px;

    @media (max-width: 800px) {
      width: auto;
      font-size: 16px;
      align-items: center;
      justify-content: center;
      padding: 15px;
    }

    .text {
      position: absolute;
      bottom: 30px;
      width: 75%;

      @media (max-width: 800px) {
        position: static;
        text-align: center;
      }
    }

    .index {
      position: absolute;
      top: 18px;
      right: 30px;

      @media (max-width: 800px) {
        display: none;
      }
    }
  }

  .black {
    background-color: var(--c-black);
    .text {
      color: #fff;
    }
  }

  .white {
    background-color: #fff;
  }
}
</style>
