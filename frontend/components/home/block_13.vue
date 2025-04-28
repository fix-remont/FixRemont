<script setup lang="ts"></script>

<template>
  <div class="margin-glob block">
    <img class="bg-img" src="/images/home/block_13.png" alt="bg-img" />
    <div class="content">
      <img class="play-button hover" src="/icons/play-button.svg" alt="play-button" />
      <p class="text">
        Посмотрите <br />
        2-х минутный ролик <br />
        о нашем подходе <br />
        к работе
      </p>
    </div>
  </div>
</template>

<style scoped>
.block {
  position: relative;
  /* min-height: 225px; */
  .bg-img {
    @media (max-width: 640px) {
      border-radius: 20px;
      min-height: 225px;
      object-fit: cover;
    }
  }
  .content {
    position: absolute;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    top: 0;
    left: 40px;
    @media (max-width: 640px) {
      left: 17px;
    }

    .play-button {
      width: 125px;
      height: 125px;
      margin-top: 40px;
      @media (max-width: 1240px) {
        width: 35px;
        height: 35px;
      }
      @media (max-width: 640px) {
        margin-top: 17px;
      }
    }
    .text {
      color: white;
      font-size: 65px;
      font-weight: 600;
      margin-bottom: 40px;
      @media (max-width: 1500px) {
        font-size: 40px;
      }
      @media (max-width: 1000px) {
        font-size: 22px;
      }
      @media (max-width: 640px) {
        font-size: 16px;
        margin-bottom: 17px;
      }
    }
  }
}
</style>
