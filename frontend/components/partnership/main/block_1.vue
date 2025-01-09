<script setup lang="ts">
import Bread_crumbs from '~/components/_shared/bread_crumbs.vue'
import {hrefBecomePartner} from 'assets/variables'

const items = ref([
  {
    id: 1,
    title: 'Риэлторам',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    hovered: false,
    href: `${hrefBecomePartner}/realtors`
  },
  {
    id: 2,
    title: 'Застройщикам',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    hovered: false,
    href: `${hrefBecomePartner}/builders`
  },
  {
    id: 3,
    title: 'Физическим <br/> лицам',
    text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    hovered: false,
    href: `${hrefBecomePartner}/individuals`
  }
])
</script>

<template>
  <div class="margin-glob block">
    <div class="crumb-container">
      <Bread_crumbs />
    </div>
    <div class="content">
      <h1>
        Зарабатывайте 10%
        <br />
        комиссию с каждой
        <br />
        сделки FIX-ремонт
      </h1>
    </div>
    <div class="black-box">
      <h3>
        Партнерская программа от первого в России онлайн-сервиса по ремонту и строительству с
        фиксированной ценой
      </h3>
      <NuxtLink>
        <SharedButton fillOrange> Зарегистрироваться, как партнёр </SharedButton>
      </NuxtLink>
    </div>
    <UCarousel class="third" v-if="items" :items="items" :ui="{ container: 'gap-2' }">
      <template #default="{ item }">
        <NuxtLink
          :to="item.href"
          @mouseover="item.hovered = true"
          @mouseout="item.hovered = false"
          :class="['item', { 'item-hovered': item.hovered }, 'cursor-pointer']"
          @click="item.hovered = true"
        >
          <span v-html="item.title" :class="['title']"></span>
          <span :class="['text']">{{ item.text }}</span>
          <img :src="item.imgSrc" alt="img" />
          <div :class="['wrap-arrow']">
            <SharedArrowHover :hovered="item.hovered" />
          </div>
        </NuxtLink>
      </template>
    </UCarousel>
  </div>
</template>

<style scoped lang="postcss">
$radius: 35px;

.block {
  min-height: 50rem;
  background-image: url('/images/partnership/block_1.png');
  background-repeat: no-repeat;
  position: relative;
  overflow: hidden;
  align-self: stretch;
}

.crumb-container {
  position: absolute;
  display: inline-block;
  top: 0;
  left: 0;
  padding: 20px;
  z-index: 1;
}

.content {
  display: inline-block;
  position: absolute;
  bottom: 5rem;
  left: 100px;
  color: #fff;

  h1 {
    font-size: 55px;
    font-weight: 600;
    line-height: 70px;
    letter-spacing: -1px;
  }
}

.black-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 7rem;
  position: absolute;
  right: 0;
  top: 1rem;
  z-index: 1;
  padding: 45px;
  width: 31rem;
  border-radius: $radius;
  color: #fff;
  background-color: var(--c-black);

  h3 {
    display: inline-block;
    font-size: 30px;
    font-weight: 500;
    line-height: 40px;
  }

  button {
    padding: 30px;
    font-size: 19px;
  }
}

.third {
  position: absolute;
  bottom: 1rem;
  right: 0;

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

    width: 260px;
    height: 230px;
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
      width: 160px;
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
</style>
