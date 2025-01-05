<script setup lang="ts">
const { width } = useViewport()
const items = [
  {
    text: '1 Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?',
    img: '/images/home/block_14_for-blog.png'
  },
  {
    text: '2 Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?',
    img: '/images/home/block_14_for-blog.png'
  },
  {
    text: '3 Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?',
    img: '/images/home/block_14_for-blog.png'
  },
  {
    text: '4 Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?',
    img: '/images/home/block_14_for-blog.png'
  },
  {
    text: '5 Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?',
    img: '/images/home/block_14_for-blog.png'
  }
]
</script>

<template>
  <div class="margin-glob block">
    <h1 class="title-glob">
      Ведём блог, делимся <span class="orange"> многолетним опытом </span> и практической
      информацией
    </h1>
    <div class="box">
      <div class="carousel-wrapper">
        <UCarousel
          class="carousel"
          :items="items"
          :ui="{
            container: 'gap-[9px] sm:gap-[50px] w-full sm:w-[initial]',
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
          :arrows="width <= 640"
          :indicators="width <= 640"
        >
          <template #default="{ item }">
            <div class="item-box">
              <img class="img" :src="item.img" alt="img" />
              <div class="content">
                <div class="remont hover">Ремонт</div>
                <div class="text">{{ item.text }}</div>
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
        <SharedButton>Перейти в блог</SharedButton>
      </div>
      <div class="youtube-wrapper">
        <div class="video-wrapper">
          <img class="img" src="/images/home/block_14_for-video.png" alt="" />
          <img class="icon hover" src="/icons/play-button.svg" alt="icon" />
        </div>
        <SharedButton youtube>Перейти в YouTube</SharedButton>
      </div>
    </div>
  </div>
</template>

<style scoped>
.box {
  display: grid;
  grid-template-columns: auto 570px;
  gap: 50px;
  margin-top: 40px;
  @media (max-width: 1400px) {
    grid-template-columns: auto;
  }
  .carousel-wrapper {
    .carousel {
      margin-bottom: 60px;
      @media (max-width: 640px) {
        margin-bottom: 15px;
      }
    }
    .item-box {
      position: relative;
      overflow: hidden;

      .img {
        @media (max-width: 640px) {
          width: 270px;
        }
      }
      .content {
        position: absolute;
        color: white;
        top: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        left: 15px;
        font-size: 12px;

        .remont {
          margin-top: 20px;
          padding: 10px 15px;
          background-color: var(--c-black);
          width: max-content;
          border-radius: 20px;
          @media (max-width: 640px) {
            font-size: 6px;
            padding: 5px 6px;
          }
        }
        .text {
          font-size: 27px;
          font-weight: 600;
          margin-bottom: 20px;
          @media (max-width: 640px) {
            font-size: 14px;
          }
        }
      }
    }
  }
  .youtube-wrapper {
    display: flex;
    flex-direction: column;
    gap: 60px;
    @media (max-width: 640px) {
      gap: 15px;
    }
    .video-wrapper {
      position: relative;
      .img {
        @media (max-width: 1400px) {
          width: 100%;
        }
      }
      .icon {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        @media (max-width: 640px) {
          width: 35px;
          height: 35px;
        }
      }
    }
  }
}
</style>
