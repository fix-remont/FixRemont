<script setup lang="ts">
const items = [
  '25 бригад и более, чем 30 сотрудников в штате',
  'Сдаём каждый год  более 150 объектов',
  'Работаем без посредников',
  'Был основным подрядчиком компании ТАИФ',
]
</script>

<template>
  <div class="margin-glob block">
    <div class="block-choice">
      <div class="titles">
        <p class="subtitle-glob">Давайте сравним</p>
        <h2 class="title-glob">
          <span class="orange">Что выгоднее и надёжнее?</span>
          <br/>
          Обратиться в FIX-ремонт или нанять бригаду?
        </h2>
      </div>
      <div class="container">
        <div class="choicer left-choice">
          <h3 class="choice-title">
            Бригада строителей
          </h3>
          <div class="reasons">
            <h4>Финансовые траты</h4>
            <ul>
              <li>На докупку материалов</li>
              <li>На бензин для поездок по магазинам</li>
              <li>На переделки и неучтенные расходы</li>
            </ul>
          </div>
          <div class="reasons">
            <h4>Временные затраты</h4>
            <ul>
              <li>Договорились с бригадой</li>
              <li>Работа главным на объекте каждый день от 3-х часов</li>
            </ul>
          </div>
          <div class="reasons">
            <h4>Нервы</h4>
            <ul>
              <li>Всё не в радость, состояние критическое</li>
              <li>Выливается в семейные ссоры</li>
            </ul>
          </div>
        </div>

        <div class="choicer right-choice">
          <h3 class="choice-title">
            Сервис FIX-ремонт
          </h3>
          <div class="reasons">
            <h4>Финансовые траты</h4>
            <ul>
              <li>Единоразовая оплата сервису, который сам закупает, доставляет материалы, а также нанимает и
                контролирует всю бригаду
              </li>
            </ul>
          </div>
          <div class="reasons">
            <h4>Временные затраты</h4>
            <ul>
              <li>Заключили договор</li>
              <li>Заехали на готовый объект</li>
            </ul>
          </div>
          <div class="reasons">
            <h4>Нервы</h4>
            <ul>
              <li>Команда FIX-ремонт заботится о клиентах <br> и выполнит всю работу не дергая вас по пустякам и решая
                вопросы самостоятельно
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <HomeBlock3/>
    <HomeBlock4/>
    <HomeBlock6/>
    <HomeBlock7/>
    <HomeBlock8/>
    <HomeBlock9/>
    <HomeBlock10/>
    <div class="block2 margin-glob">
      <h1 class="title title-glob">Лично <span class="orange"> несу ответственность </span> за качество предоставляемых
        услуг
      </h1>
      <div class="img-container">
        <img class="img" src="/images/home/block_11.png" alt="img">
        <div class="text-container">

          <p class="text1">Фанис Хасанов</p>
          <p class="text2">Генеральный директор <br> FIX РЕМОНТ</p>
        </div>
      </div>
      <div class="items">
        <div class="item" v-for="item in items" :key="item">
          <img class="icon" src="/icons/checkbox__checked__orange.svg" alt="icon">
          <span class="text"> {{ item }}</span>
        </div>

      </div>
    </div>
    <HomeBlock12 />
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.block-choice {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.titles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 3rem;
}

.container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 3rem;
}

.choice-title {
  font-weight: bold;
  font-size: 48px;
}

.choicer {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  align-items: flex-start;
  border-radius: 24px;
  padding: 45px;
}

.left-choice {
  background-color: #EFEFEF;
  color: #000;

  .reasons li {
    color: #808080;
  }
}

.right-choice {
  background-color: var(--c-black);
  color: #fff;
}

.reasons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 85%;

  h4 {
    font-size: 30px;
    line-height: 32px;
    font-weight: 450;
  }

  ul {
    list-style-type: disc;
  }

  li {
    margin-left: 20px;
  }
}

@media (max-width: 768px) {
  .container {
    display: flex;
    flex-direction: column;
    gap: 3rem;
  }

  .block-choice {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .choicer {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: flex-start;
    border-radius: 24px;
  }

  .choice-title {
    font-size: 30px;
  }

  .reasons {
    h4 {
      font-size: 25px;
    }
  }
}

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
      ;

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