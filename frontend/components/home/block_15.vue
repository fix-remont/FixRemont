<script setup lang="ts">
const items = ref([
  {
    question: '1 Какой срок службы?',
    answer:
      '1 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '2 Какой срок службы?',
    answer:
      '2 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '3 Какой срок службы?',
    answer:
      '3 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '4 Какой срок службы?',
    answer:
      '4 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '5 Какой срок службы?',
    answer:
      '5 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '6 Какой срок службы?',
    answer:
      '6 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  },
  {
    question: '7 Какой срок службы?',
    answer:
      '7 Минимальный срок службы напыляемой жидкой битумно-латексной гидроизоляции для кровли от WPGUM составляет 20 лет. Также наша компания предоставляет 100% гарантию качества сроком от 5 лет на всю продуктовую линейку.',
    isOpen: false
  }
])

const toggleShow = (index: number) => {
  items.value[index].isOpen = !items.value[index].isOpen
}
</script>

<template>
  <div class="margin-glob block">
    <div class="box1">
      <h1 class="text-glob-xl">
        Отвечаем на <span class="orange"> самые частые вопросы </span> наших клиентов
      </h1>
      <div class="img-container">
        <img class="img" src="/images/home/block_15.png" alt="img" />
        <div class="info">
          <div class="name">Фанис Хасанов</div>
          <div class="text">
            Основатель и руководитель FIX-ремонт <br />
            Не нашли свой вопрос? Свяжитесь с нами!
          </div>
          <div class="contacts">
            <div class="phone">8 (800) 000-00-00</div>
            <img class="icon hover" src="/icons/watsapp.svg" alt="icon" />
            <img class="icon hover" src="/icons/telegram.svg" alt="icon" />
          </div>
        </div>
      </div>
    </div>
    <div class="box2">
      <div class="item" v-for="({ question, answer, isOpen }, index) in items" :key="index">
        <div class="texts">
          <span class="question">{{ question }}</span>
          <Transition>
            <div class="answer" v-show="isOpen">{{ answer }}</div>
          </Transition>
        </div>
        <img
          :class="['arrow hover', { 'arrow-opened': isOpen }]"
          @click="toggleShow(index)"
          src="/arrow-diagonal.svg"
          alt="icon"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.box2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  align-items: center;
  gap: 30px;
  @media (max-width: 1240px) {
    grid-template-columns: auto;
  }
  .item {
    display: flex;
    justify-content: space-between;
    background-color: white;
    border-radius: 25px;
    padding: 25px 47px;
    @media (max-width: 640px) {
      font-size: 14px;
      padding: 13px;
    }
    .texts {
      .question {
        font-size: 24px;
        font-weight: 700;
        @media (max-width: 640px) {
          font-size: 14px;
        }
      }
      .answer {
        font-size: 17px;
        margin-top: 10px;
        @media (max-width: 640px) {
          font-size: 12px;
        }
      }
    }
    .arrow {
      align-self: flex-start;
      margin-left: 25px;
      transition: transform 0.5s;
      @media (max-width: 640px) {
        width: 25px;
        height: 25px;
      }
      &-opened {
        transform: rotate(-180deg);
      }
    }
  }
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.5s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }
}

.box1 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  @media (max-width: 1240px) {
    grid-template-columns: auto;
  }
  .img-container {
    position: relative;
    background-color: var(--c-black);
    border-radius: 35px;
    display: flex;
    @media (max-width: 640px) {
      border-radius: 20px;
    }
    .img {
      position: absolute;
      left: 5%;
      height: 100%;
      object-fit: cover;
      object-position: left;
    }
    .info {
      margin-left: auto;
      color: white;
      gap: 15px;
      display: flex;
      flex-direction: column;
      padding: 33px;
      z-index: 1;
      @media (max-width: 640px) {
        padding: 12px;
      }
      .name {
        font-size: 32px;
        font-weight: 600;
        @media (max-width: 640px) {
          font-size: 16px;
        }
      }
      .text {
        font-size: 16px;
        @media (max-width: 640px) {
          font-size: 12px;
          width: 180px;
        }
      }
      .contacts {
        display: flex;
        gap: 10px;
        .phone {
          font-size: 32px;
          font-weight: 600;
          @media (max-width: 640px) {
            font-size: 12px;
          }
        }
        .icon {
          width: 40px;
          height: 40px;
          @media (max-width: 640px) {
            width: 20px;
            height: 20px;
          }
        }
      }
    }
  }
}
</style>
