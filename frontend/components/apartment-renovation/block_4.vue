<script setup lang="ts"></script>

<template>
  <div class="block-choice margin-glob">
    <div class="titles">
      <p class="subtitle-glob">Давайте сравним</p>
      <h2 class="title-glob">
        <span class="orange">Что выгоднее и надёжнее?</span>
        <br />
        Обратиться в FIX-ремонт или нанять бригаду?
      </h2>
    </div>
    <div class="container">
      <div class="choicer left-choice">
        <h3 class="choice-title">Бригада строителей</h3>
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
        <h3 class="choice-title">Сервис FIX-ремонт</h3>
        <div class="reasons">
          <h4>Финансовые траты</h4>
          <ul>
            <li>
              Единоразовая оплата сервису, который сам закупает, доставляет материалы, а также
              нанимает и контролирует всю бригаду
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
            <li>
              Команда FIX-ремонт заботится о клиентах <br />
              и выполнит всю работу не дергая вас по пустякам и решая вопросы самостоятельно
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.titles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 3rem;
}

.container {
  min-width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  gap: 3rem;
}

.choice-title {
  font-weight: bold;
  font-size: 3vw;

  @media (max-width: 768px) {
    font-size: 4vw;
  }
}

.choicer {
  width: 50%;
  min-height: 100%;
  display: flex;
  align-self: stretch;
  flex-direction: column;
  gap: 1.5rem;
  align-items: flex-start;
  border-radius: 24px;
  padding: 3vw;
}

.left-choice {
  background-color: #efefef;
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
    font-size: 2vw;
    line-height: 2.2vw;
    font-weight: 450;

    @media (max-width: 768px) {
      font-size: 3vw;
      line-height: 3.2vw;
    }
  }

  ul {
    list-style-type: disc;
  }

  li {
    margin-left: 1vw;
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
    align-items: center;
    border-radius: 24px;
  }

  .choice-title {
    width: 85%;
  }
}
</style>
