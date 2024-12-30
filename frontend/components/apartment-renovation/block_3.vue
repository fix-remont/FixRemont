<script setup lang="ts">

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
    label: 'приходится отвлекаться от дел, бросать всё и ехать на объект без понимания, что проверять'
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
    label: 'несмотря на все старания и страдания, сроки и стоимость ремонта увеличиваются в 2-3 раза '
  },
]
</script>

<template>
  <div class="margin-glob upper">
    <div class="left">
      <div class="wrapper">
        <h2 class="title">
          <span class="orange">Избавим вас от <br/> типичных проблем </span> <br/>
          ремонта квартиры:
        </h2>
        <NuxtLink>
          <SharedButton>
            Рассчитать стоимость без посещения офиса
          </SharedButton>
        </NuxtLink>
      </div>
    </div>
    <div class="right">
      <div
          class="element"
          v-for="(item, index) in elementContent"
          :key="index"
      >
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
}

.left {
  min-height: 100%;
  align-self: stretch;
  display: flex;
}

.title {
  font-size: 3rem;
  line-height: 1.25;
  font-weight: 600;
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
}

@media (max-width: 800px) {
  .upper {
    flex-direction: column;
  }

  .title {
    font-size: 40px;
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

  .right {
    width: 100%;

    .element {
      text-align: center;

      h4 {
        width: 100%;
        font-size: 24px;
      }

      p {
        font-size: 16px;
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
    width: 50%;
    font-size: 36px;
    line-height: 40px;
    font-weight: 600;
  }

  p {
    margin-top: 1rem;
    font-size: 18px;
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