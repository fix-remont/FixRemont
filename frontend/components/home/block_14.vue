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
          :arrows="width <= 640"
          :indicators="width <= 640"
          :ui="{
            container: 'gap-5'
          }"
        >
          <template #default="{ item }">
            <div class="item-box">
              <img class="img" :src="item.img" alt="img" />
              <div class="content">
                <div class="remont hover">Ремонт</div>
                <NuxtLink class="text" to="/blog/test_id">{{ item.text }}</NuxtLink>
              </div>
            </div>
          </template>

          <template #prev="{ onClick, disabled }">
            <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
          </template>

          <template #next="{ onClick, disabled }">
            <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
          </template>
        </UCarousel>
        <UButton block to="/blog" color="white" variant="outline" size="custom"
          >Перейти в блог</UButton
        >
      </div>
      <div class="youtube-wrapper">
        <div class="video-wrapper">
          <img class="img" src="/images/home/block_14_for-video.png" alt="" />
          <img class="icon hover" src="/icons/play-button.svg" alt="icon" />
        </div>
        <UButton block to="#" color="red" variant="outline" size="custom"
          >Перейти в YouTube</UButton
        >
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
