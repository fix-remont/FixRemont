<script setup lang="ts">
const carousel1 = [
  {
    imgSrc: '/images/partnership/block_4_1.png',
    title: 'С нас: подбор проверенных специалистов',
    label: 'в нашей базе более 1 000 надежных бригад'
  }
]

const carousel2 = [
  {
    imgSrc: '/images/partnership/block_4_2.png',
    title: 'С вас: простая регистрация',
    label: 'на нашей платформе'
  }
]
const gallery1 = Array(5).fill(carousel1[0])
const gallery2 = Array(5).fill(carousel2[0])
</script>

<template>
  <div class="margin-glob">
    <h1 class="text-glob-xl mb-4">
      <span class="orange">Возьмём на себя</span>
      организацию <br />
      и выполнение работ под ключ
    </h1>
    <div class="wrapper">
      <UCarousel
        class="carousel"
        :items="gallery1"
        arrows
        indicators
        :ui="{
          container: 'rounded-3xl gap-4',
          indicators: {
            wrapper: 'justify-end',
            base: 'h-[5px] w-[5px] sm:h-2 sm:w-2',
            active: 'bg-[var(--c-black)]',
            inactive: 'bg-[var(--c-gray)]'
          },
          arrows: {
            wrapper: 'flex gap-2 justify-start'
          }
        }"
      >
        <template #default="{ item }">
          <div class="item">
            <img :src="item.imgSrc" alt="img" draggable="false" />
            <div class="text">
              <h4>{{ item.title }}</h4>
              <p>{{ item.label }}</p>
            </div>
          </div>
        </template>

        <template #prev="{ onClick, disabled }">
          <img
            alt="arrow"
            :class="[
              'arrow cursor-pointer',
              'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
              { 'opacity-60': disabled }
            ]"
            src="/images/arrow-prev.svg"
            @click="onClick"
            draggable="false"
          />
        </template>

        <template #next="{ onClick, disabled }">
          <img
            alt="arrow"
            :class="[
              'arrow cursor-pointer',
              'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
              { 'opacity-60': disabled }
            ]"
            src="/images/arrow-next.svg"
            @click="onClick"
            draggable="false"
          />
        </template>
      </UCarousel>

      <UCarousel
        class="carousel"
        :items="gallery2"
        arrows
        indicators
        :ui="{
          container: 'gap-3 rounded-3xl',
          indicators: {
            wrapper: 'justify-end',
            base: 'h-[5px] w-[5px] sm:h-2 sm:w-2',
            active: 'bg-[var(--c-black)]',
            inactive: 'bg-[var(--c-gray)]'
          },
          arrows: {
            wrapper: 'flex gap-2 justify-start mt-2'
          }
        }"
      >
        <template #default="{ item }">
          <div class="item">
            <img :src="item.imgSrc" alt="img" draggable="false" />
            <div class="text">
              <h4>{{ item.title }}</h4>
              <p>{{ item.label }}</p>
            </div>
          </div>
        </template>

        <template #prev="{ onClick, disabled }">
          <img
            alt="arrow"
            :class="[
              'arrow cursor-pointer',
              'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
              { 'opacity-60': disabled }
            ]"
            src="/images/arrow-prev.svg"
            @click="onClick"
            draggable="false"
          />
        </template>

        <template #next="{ onClick, disabled }">
          <img
            alt="arrow"
            :class="[
              'arrow cursor-pointer',
              'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
              { 'opacity-60': disabled }
            ]"
            src="/images/arrow-next.svg"
            @click="onClick"
            draggable="false"
          />
        </template>
      </UCarousel>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;

  .carousel {
    width: 50%;
    height: 50%;

    .item {
      position: relative;
      border-radius: 24px;

      @media (max-width: 1700px) {
        max-width: 45vw;
      }

      img {
        border-radius: 24px;
      }

      .text {
        max-width: 26vw;
        position: absolute;
        bottom: 2vw;
        left: 2vw;
        right: 0;
        padding: 1vw;
        color: #fff;

        h4 {
          margin-bottom: 1vw;
          font-size: 1.6vw;
          font-weight: bold;
        }

        p {
          font-weight: 600;
          font-size: 1vw;
        }
      }
    }
  }
}

@media (max-width: 768px) {
  h1 {
    text-align: center;
  }

  .wrapper {
    flex-direction: column;

    .carousel {
      width: auto;
      max-width: 100%;
      margin: 0 auto;

      .item {
        max-width: 92vw;

        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        .text {
          max-width: 85%;
          bottom: 2.5vw;
          left: 2.5vw;
          padding: 1.5vw;

          h4 {
            margin-bottom: 8px;
            font-size: 3vw;
          }

          p {
            font-size: 2vw;
          }
        }
      }
    }
  }
}
</style>
