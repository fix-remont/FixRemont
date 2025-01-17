<script setup lang="ts">
const { width } = useViewport()
import { hrefBecomePartner, hrefCalculater } from '~/assets/variables'

const items = ref([
  {
    id: 1,
    title: 'Ремонт',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: '/apartment-renovation',
    hovered: false
  },
  {
    id: 2,
    title: 'Строительство',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: '/building-houses',
    hovered: false
  },
  {
    id: 3,
    title: 'Партнёрская программа',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: hrefBecomePartner,
    hovered: false
  }
])
</script>

<template>
  <div :class="['box', 'margin-glob']">
    <div class="first radius-glob">
      <img src="/images/home/tools.png" alt="tools" draggable="false" />
      <p>Первый в России онлайн-сервис по ремонту и строительству с фиксированной стоимостью</p>
    </div>
    <div class="second">
      <div class="box-buttons radius-glob">
        <p>Воплотим вашу мечту в реальность без визитов на объект</p>
        <div :class="['buttons']">
          <NuxtLink :to="hrefCalculater">
            <SharedButton fillOrange> Онлайн-калькулятор </SharedButton>
          </NuxtLink>
          <NuxtLink :to="hrefBecomePartner">
            <SharedButton>Стать партнёром</SharedButton>
          </NuxtLink>
        </div>
      </div>
      <UCarousel class="third" v-if="items" :items="items" :ui="{ container: 'gap-6' }">
        <template #default="{ item }">
          <NuxtLink
            :to="item.href"
            @mouseover="item.hovered = true"
            @mouseout="item.hovered = false"
            :class="['item', { 'item-hovered': item.hovered }, 'cursor-pointer']"
            @click="item.hovered = true"
          >
            <span :class="['title']">{{ item.title }}</span>
            <span :class="['text']">{{ item.text }}</span>
            <img :src="item.imgSrc" alt="img" />
            <div :class="['wrap-arrow']">
              <SharedArrowHover :hovered="item.hovered" />
            </div>
          </NuxtLink>
        </template>
      </UCarousel>
    </div>
  </div>
</template>

<style scoped>
.box {
  display: flex;
  gap: 20px;
  @media (max-width: 1100px) {
    flex-direction: column;
    gap: 15px;
  }
}
.first {
  width: 50%;
  position: relative;
  height: 785px;
  display: flex;
  overflow: hidden;
  @media (max-width: 1100px) {
    width: 100%;
    background-color: #f9af15;
    height: 290px;
  }
  /* @media (max-width: 1500px) {
	}
	@media (max-width: 640px) {
		height: 245px;
		overflow: visible;
	} */
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: right center;
    @media (max-width: 1500px) {
      width: auto;
      margin-left: auto;
    }
    @media (max-width: 640px) {
      height: 245px;
    }
  }
  p {
    position: absolute;
    bottom: 75px;
    left: 75px;

    line-height: 60px;
    font-size: 45px;
    font-weight: 500;
    color: white;
    width: 400px;

    @media (max-width: 1840px) {
      font-size: 40px;
      width: 350px;
    }
    @media (max-width: 1500px) {
      font-size: 30px;
      width: 60%;
      bottom: 35px;
    }
    @media (max-width: 1000px) {
      font-size: 24px;
      width: 41vw;
      line-height: 19px;
      bottom: 26px;
      left: 26px;
    }
    @media (max-width: 1000px) {
      font-size: 16px;
    }
  }
}
.second {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  @media (max-width: 1100px) {
    width: 100%;
  }
  .box-buttons {
    background-color: var(--c-black);
    padding: 45px;
    color: white;
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-grow: 1;

    @media (max-width: 1100px) {
      padding: 25px;
    }

    .buttons {
      display: flex;
      gap: 20px;

      @media (max-width: 1460px) {
        flex-direction: column;
      }
      a {
        flex: 1;
      }
    }
    p {
      width: 300px;

      @media (max-width: 1500px) {
        width: 100%;
        font-size: 20px;
        margin-bottom: 30px;
      }

      @media (max-width: 800px) {
        line-height: 16px;
        font-size: 16px;
      }
    }
  }

  .third {
    .static-slides {
      width: 890px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      height: 100%;
      flex-grow: 1;

      @media (max-width: 1500px) {
        width: 100%;
        gap: 0;
        display: flex;
        justify-content: space-between;
      }
    }

    .item {
      position: relative;
      display: flex;
      flex-direction: column;
      color: white;
      border-radius: 35px;
      overflow: hidden;
      transition: all 1s linear;
      background-color: white;
      /* background-color: var(--c-black); */

      width: 280px;
      @media (max-width: 1500px) {
      }

      /* @media (max-width: 1000px) {
				width: initial;
				} */

      .title {
        font-weight: 500;
        font-size: 24px;
        margin: 25px 0 10px 25px;
        line-height: 32px;
        transition: all 1s linear;
        color: var(--c-black);
      }

      .text {
        width: 180px;
        font-size: 16px;
        font-weight: 400;
        margin-left: 25px;
        color: white;
      }

      img {
        position: absolute;
        z-index: -1;
        width: 100%;
        height: 100%;
      }

      .wrap-arrow {
        position: absolute;
        right: 25px;
        bottom: 25px;
      }
    }

    .item-hovered {
      background: none;
      /* background: #efefef; */

      .title {
        color: white;
        /* color: var(--c-black); */
      }

      .text {
        color: #efefef;
      }
    }
  }
}
</style>
