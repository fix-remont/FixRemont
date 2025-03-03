<script setup lang="ts">
import { hrefCalculater } from 'assets/variables'

let elementContent = [
  {
    title: 'Долгий выбор материала и подсчёты бюджета',
    label: 'ссоры и траты времени на переподбор, когда желание не сходится с бюджетом'
  },
  {
    title: 'Бесконечный поиск хороших исполнителей',
    label: 'снова траты времени на поиск, выбор и общение без понимания средних цен'
  },
  {
    title: 'Организация всех работ',
    label: 'попытки выстроить очередность процессов без должного опыта'
  },
  {
    title: 'Постоянный контроль',
    label:
      'приходится отвлекаться от дел, бросать всё и ехать на объект без понимания, что проверять'
  },
  {
    title: 'Разборки, кто прав, а кто виноват',
    label: 'нервная система одна, а виноватых  всё равно не найти'
  },
  {
    title: 'Регулярный закуп и доставка материалов',
    label: 'вместо работы после отдыха - похождения по строительным магазинам и поездки на объект'
  },
  {
    title: 'И в результате:',
    label:
      'несмотря на все старания и страдания, сроки и стоимость ремонта увеличиваются в 2-3 раза '
  }
]
</script>

<template>
  <div class="margin-glob upper">
    <div class="left">
      <div class="wrapper">
        <h2 class="text-glob-xl">
          <span class="orange"
            >Избавим вас от <br />
            типичных проблем
          </span>
          <br />
          ремонта квартиры:
        </h2>
        <NuxtLink :to="hrefCalculater">
          <SharedButton> Рассчитать стоимость без посещения офиса </SharedButton>
        </NuxtLink>
      </div>
    </div>
    <div class="right">
      <div class="element" v-for="(item, index) in elementContent" :key="index">
        <h4>{{ item.title }}</h4>
        <p>{{ item.label }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.upper {
  display: flex;
  height: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 3rem;

  @media (max-width: 1200px) {
    gap: 8rem;

    button {
      padding: 20px;
    }
  }

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 0;
  }
}

.left {
  min-height: 100%;
  align-self: stretch;
  display: flex;
}

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 1em;
  position: sticky;
  top: 10px;
  align-self: flex-start;
}

.right {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 2em;

  @media (max-width: 1400px) {
    .element h4 {
      width: 100%;
    }
  }

  @media (max-width: 768px) {
    width: 100%;

    .element {
      text-align: center;

      h4 {
        width: 100%;
        font-size: 4vw;
      }

      p {
        font-size: 2.8vw;
      }
    }
  }
}

@media (max-width: 768px) {
  .title {
    font-size: 8vw;
  }

  .left {
    width: 100%;
    top: 0;
    z-index: 1;
    justify-content: center;
    margin-bottom: 2rem;

    .wrapper {
      text-align: center;
      display: flex;
      align-items: center;
      flex-direction: column;
      gap: 1em;

      a {
        width: 100%;
      }
    }
  }
}

.element {
  display: flex;
  flex-direction: column;
  gap: 1em;
  border-radius: 24px;
  padding: 3rem;

  h4 {
    width: 80%;
    font-size: 2.2vw;
    font-weight: 600;
  }

  p {
    margin-top: 1rem;
    font-size: 1.2vw;
    line-height: 28px;
  }
}

.element:nth-child(odd) {
  background-color: var(--c-black);
  color: #fff;
}

.element:nth-child(even) {
  background-color: #fff;
  color: var(--c-black);
}

.element:last-child h4 {
  color: var(--c-orange);
}
</style>
