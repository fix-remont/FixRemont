<script setup lang="ts">
import { hrefBecomePartner, hrefCabinet, hrefCalculater } from 'assets/variables'

const items = ref([
  {
    id: 1,
    title: 'Риэлторам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/realtors`,
    hovered: false
  },
  {
    id: 2,
    title: 'Застройщикам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/builders`,
    hovered: false
  },
  {
    id: 3,
    title: 'Физическим лицам',
    text: 'Без визитов на объект. Заезжайте в готовую квартиру уже через 6-8 месяцев',
    imgSrc: '/images/home/block1-img1.png',
    href: `${hrefBecomePartner}/individuals`,
    hovered: false
  }
])
</script>

<template>
  <WBlock class="bg-orange radius-glob relative">
    <div class="radius-glob block-image relative">
      <SharedBreadCrumbs class="breadcrumbs" />
      <img class="background-image" src="/images/partnership/block_1.png" alt="background" />
      <h1 class="title-boxing">Зарабатывайте 10% комиссию с каждой сделки FIX-ремонт</h1>
    </div>

    <div class="black-box-wrap">
      <div class="black-box">
        <h3 class="bb-title">
          Обеспечим ваших клиентов сервисом и услугой высшего уровня без рисков для репутации
        </h3>
        <NuxtLink class="orange-link"> Подробнее </NuxtLink>
        <UButton class="register-button" :to="hrefCalculater" size="custom" block>
          Зарегистрироваться как партнер
        </UButton>
      </div>
    </div>

    <div class="cards-wrapper">
      <UCarousel class="cards" v-if="items" :items="items" :ui="{ container: 'gap-6' }">
        <template #default="{ item }">
          <NuxtLink
            class="item"
            :to="item.href"
            @mouseover="item.hovered = true"
            @mouseout="item.hovered = false"
            :class="{ 'item-hovered': item.hovered }"
            @click="item.hovered = true"
          >
            <span class="title">{{ item.title }}</span>
            <span class="text">{{ item.text }}</span>
            <img :src="item.imgSrc" alt="img" />
            <div class="wrap-arrow">
              <SharedArrowHover :hovered="item.hovered" />
            </div>
          </NuxtLink>
        </template>
      </UCarousel>
    </div>
  </WBlock>
</template>

<style scoped lang="postcss">
$radius: 35px;

.black-box-wrap {
  background-color: var(--c-white);
  top: 0;
  right: 0;
  position: absolute;
  padding: 2rem 2rem 5rem;

  @media (max-width: 1245px) {
    border-bottom-left-radius: $radius;
  }

  @media (max-width: 1024px) {
    position: static;
    padding: 1rem;
    border-radius: 0;
  }
}

.block-image {
  margin-bottom: 2.5rem;
  overflow: hidden;
  position: relative;

  @media (max-width: 1024px) {
    margin-bottom: 0;
  }
}

.breadcrumbs {
  position: absolute;
  top: 10px;
  z-index: 10;

  @media (max-width: 1024px) {
    display: none;
  }
}

.background-image {
  max-height: 700px;
  width: 100%;
  object-fit: cover;
  border-radius: $radius;
}

.title-boxing {
  font-size: 45px;
  font-weight: bold;
  line-height: 60px;
  color: white;
  position: absolute;
  bottom: 5rem;
  left: 5rem;
  width: 35%;

  @media (max-width: 1500px) {
    font-size: 40px;
    line-height: 50px;
    bottom: 4rem;
    left: 4rem;
  }

  @media (max-width: 1400px) {
    font-size: 35px;
    line-height: 45px;
    bottom: 3rem;
    left: 3rem;
  }

  @media (max-width: 1200px) {
    font-size: 30px;
    line-height: 40px;
    bottom: 2rem;
    left: 2rem;
  }

  @media (max-width: 1024px) {
    font-size: 40px;
    line-height: 60px;
    bottom: 3rem;
    left: 3rem;
    width: 60%;
  }

  @media (max-width: 600px) {
    font-size: 20px;
    line-height: 30px;
  }

  @media (max-width: 450px) {
    font-size: 16px;
    line-height: 25px;
    bottom: 1rem;
    left: 1rem;
  }
}

.black-box {
  background-color: #161616;
  padding: 50px;
  border-radius: $radius;
  color: var(--c-white);
  width: 35em;

  @media (max-width: 1024px) {
    width: initial;
  }

  @media (max-width: 600px) {
    padding: 35px;
  }

  @media (max-width: 450px) {
    padding: 30px;
  }

  .bb-title {
    font-size: 30px;
    margin-bottom: 1rem;
    font-weight: bold;
    color: white;
    width: 75%;

    @media (max-width: 1200px) {
      font-size: 24px;
      margin-bottom: 1.5rem;
      width: 80%;
    }

    @media (max-width: 1030px) {
      width: 100%;
    }

    @media (max-width: 600px) {
      font-size: 16px;
    }
  }
}

.orange-link {
  color: var(--c-orange);
  text-decoration: underline;
  cursor: pointer;
}

.register-button {
  margin-top: 1rem;
}

.cards-wrapper {
  max-width: 50.2vw;
  background-color: var(--c-white);
  border-top-left-radius: $radius;
  bottom: 0;
  right: 0;
  position: absolute;
  padding: 2rem 2rem 0;

  @media (max-width: 1200px) {
    padding-top: 4rem;
    border-radius: 0;
  }

  @media (max-width: 1030px) {
    padding-top: 6rem;
  }

  @media (max-width: 1024px) {
    position: relative;
    padding-top: 2rem;
    padding-left: 0;
    padding-right: 0;
    max-width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

.cards {
  @media (max-width: 1024px) {
    max-width: 90vw;
  }
  .item {
    position: relative;
    display: flex;
    flex-direction: column;
    color: white;
    border-radius: $radius;
    overflow: hidden;
    transition: all 0.3s linear;
    background-color: white;
    width: 280px;
    min-height: 180px;

    @media (max-width: 1400px) {
      min-height: 200px;
    }

    @media (max-width: 1200px) {
      min-height: 220px;
    }

    @media (max-width: 800px) {
      min-height: 130px;
    }

    .title {
      font-weight: 500;
      font-size: 24px;
      margin: 25px 0 10px 25px;
      line-height: 32px;
      transition: all 0.3s linear;
      color: var(--c-black);

      @media (max-width: 800px) {
        font-size: 20px;
      }
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

    .title {
      color: white;
    }

    .text {
      color: #efefef;
    }
  }
}
</style>
