<script setup lang="ts">
const items = [
  { src: '/icons/vkontakte.svg', subsribed_amount: 1500 },
  { src: '/icons/instagram.svg', subsribed_amount: 1550 },
  { src: '/icons/telegram.svg', subsribed_amount: 500 },
]

const youtubeSubscribtions = 2500
</script>

<template>
  <div class="block margin-glob">
    <h1 class="title title-glob">Мы максимально <span class="orange">открыты</span> и подтверждаем экспертность в
      социальных
      сетях </h1>
    <div class="video-box">
      <div class="youtube">
        <img class="icon" src="/icons/youtube.svg" alt="icon-youtube">
        <div class="texts">
          <p class="label">YouTube</p>
          <p class="subscribtions">{{ youtubeSubscribtions }} подписчиков</p>
        </div>
      </div>
      <img class="main-img" src="/images/home/block_12.png" alt="img">
    </div>
    <div class="social-box">
      <div class="item-box" v-for="item in items" :key="item.src">
        <img class="item-img" :src="item.src" alt="icon">
        <span class="subscribed-amount">{{ item.subsribed_amount }} подписчиков</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.block {
  .title {}

  .video-box {
    .youtube {
      .icon {}

      .texts {
        .label {}

        .subscribtions {}
      }

    }

    .main-img {}
  }

  .social-box {
    .item-box {
      .item-img {}

      .subscribed-amount {}
    }
  }
}
</style>
