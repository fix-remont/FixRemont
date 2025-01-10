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
    <h1 class="title-glob mb-4">
      <span class="orange">Возьмём на себя</span>
      организацию и выполнение работ под ключ
    </h1>
    <div class="wrapper">
      <UCarousel
        class="carousel"
        :items="gallery1"
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
      overflow: hidden;
      display: inline-block;
      max-width: fit-content;

      img {
        width: auto;
        max-width: 100%;
        height: auto;
        display: block;
        border-radius: 24px;
      }

      .text {
        max-width: calc(100% - 34px);
        position: absolute;
        bottom: 40px;
        left: 40px;
        right: 0;
        padding: 1rem;
        color: #fff;

        h4 {
          margin-bottom: 12px;
          font-size: 1.875rem;
          font-weight: bold;
        }

        p {
          font-weight: 600;
          font-size: 18px;
        }
      }
    }
  }
}

@media (max-width: 800px) {
  /*TODO: сделать нормальный адаптив */
  .wrapper {
    flex-direction: column;

    .carousel {
      width: auto;
      max-width: 100%;
      margin: 0 auto;

      .item {
        img {
          width: 42%;
        }

        .text {
          bottom: 17px;
          left: 17px;
          width: 40%;
          padding: 0;

          h4 {
            margin-bottom: 8px;
            font-size: 18px;
          }

          p {
            font-size: 15px;
          }
        }
      }
    }
  }

  h1 {
    text-align: center;
  }
}
</style>
