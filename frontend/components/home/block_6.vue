<script setup lang="ts">
import { hrefOtzovik, hrefYandex } from '~/assets/variables'

const items = [
  { label: 'Яндекс', name: 'yandex', href: hrefYandex, imgSrc: '/images/home/yandex.svg' },
  { label: 'Отзовик', name: 'otzovik', href: hrefOtzovik, imgSrc: '/images/home/otzovik.svg' }
]
</script>

<template>
  <div :class="['margin-glob', 'font-size-wrapper']">
    <div class="text">Но лучше всего о нас расскажут</div>

    <div class="box">
      <div class="title-block">
        <div class="title">Выполненные работы и отзывы клиентов</div>
      </div>

      <UCarousel
        class="items"
        :items="items"
        :ui="{ item: 'sm:w-[430px] w-[130px]', container: 'gap-4' }"
      >
        <template #default="{ item }">
          <div class="item">
            <div class="first-line">
              <img class="stars-img" src="/images/home/feedback-stars.png" alt="" />
              <span class="stars-amount"><b>4.7</b></span>
            </div>
            <br />
            <div class="second-line">
              <img :class="[`${item.name}-img`]" :src="item.imgSrc" alt="img" />
              <a class="link" :href="item.href">Смотреть отзывы на {{ item.label }}</a>
            </div>
          </div>
        </template>
      </UCarousel>
    </div>
  </div>
</template>

<style scoped>
.font-size-wrapper {
  font-size: 10px;
  @media (max-width: 640px) {
    font-size: 6px;
  }
}
.text {
  font-size: 2em;
  font-weight: 500;
  margin-bottom: 2em;
}
.box {
  display: flex;
  gap: 3em;
  @media (max-width: 1200px) {
    flex-direction: column;
  }
  .title-block {
    width: 50%;
    @media (max-width: 1200px) {
      width: 100%;
    }
    .title {
      font-size: 6.5em;
      line-height: 1.1em;
      font-weight: 600;
    }
  }
  .items {
    min-width: 49%;
    .item {
      flex: 1;
      padding: 3.5em 4.3em;
      background-color: white;
      border-radius: 3em;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      @media (max-width: 640px) {
        align-items: center;
        font-size: 12px !important;
        padding: 2em 2em;
      }
      .first-line {
        display: flex;
        .stars-img {
        }
        .stars-amount {
        }
      }
      .second-line {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 1.4em;
        gap: 1em;
        @media (max-width: 640px) {
          flex-direction: column;
        }
        .yandex-img {
        }
        .otzovik-img {
        }
        .link {
          text-decoration: underline;
          text-align: center;
          @media (max-width: 640px) {
            font-size: 12px;
          }
        }
      }
    }
  }
}
</style>
