<script setup lang="ts">
const src = '/images/cabinet/platform-news-item.png'
const text = 'Как рассчитать стоимость через онлайн- калькулятор FIX-ремонт?'
const items = Array(3).fill({ src, text })
</script>

<template>
  <section class="section margin-b-glob">
    <h2 class="title-glob">Новости платформы</h2>
    <UCarousel
      :items="items"
      :ui="{
        // item: 'w-[400px] h-[400px]',
        container: 'gap-4'
      }"
    >
      <template #default="{ item }">
        <div class="wrap radius-glob">
          <img class="img" :src="item.src" alt="img" />
          <p class="text">{{ item.text }}</p>
        </div>
      </template>
    </UCarousel>
  </section>
</template>

<style scoped>
.section {
  .wrap {
    position: relative;
    overflow: hidden;

    .img {
      object-fit: cover;
      width: 400px;
      height: 400px;
      @media (max-width: 640px) {
        width: 250px;
        height: 250px;
      }
    }

    .text {
      position: absolute;
      z-index: 1;
      bottom: 30px;
      left: 30px;
      color: white;
      font-size: 24px;
      font-weight: 600;
      width: 80%;
      text-decoration: underline;
      @media (max-width: 640px) {
        font-size: 16px;
      }
    }
  }
}
</style>
