<script setup lang="ts">
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
  <WBlock>
    <div class="third grid grid-cols-1 gap-5 xl:grid-cols-3">
      <NuxtLink
        v-for="item in items"
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
    </div>
  </WBlock>
</template>

<style scoped>
.third {
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

    /* width: 280px; */
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
      margin-bottom: 20px;
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
</style>
