<script setup lang="ts">
const src = '/images/home/block_4_2.png'
</script>

<template>
  <div :class="['box', 'margin-glob']">
    <p class="text_1">
      Подберём для вас <span class="orange"> выгодное </span>кредитное предложение
    </p>
    <p class="text_2">
      <span class="orange">от 5% до 10%</span><br />
      у банков-партнёров
    </p>
    <img :src="src" alt="img" />
  </div>
</template>

<style scoped>
.box {
  border-radius: 35px;
  background-color: var(--c-black);
  padding: 45px 50px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  overflow: hidden;
  @media (max-width: 640px) {
    flex-direction: column;
    gap: 20px;
    align-items: flex-start;
    padding: 15px;
  }
}

.text_1 {
  font-size: 50px;
  font-weight: 600;
  line-height: 60px;
  z-index: 1;
  width: 40%;

  @media (max-width: 1240px) {
    font-size: 24px;
    line-height: 30px;
  }
  @media (max-width: 640px) {
    width: auto;
  }
}

.text_2 {
  font-size: 38px;
  font-weight: 500;
  line-height: 50px;
  z-index: 1;
  width: max-content;
  @media (max-width: 1240px) {
    font-size: 22px;
    line-height: 30px;
  }
  @media (max-width: 640px) {
    margin-bottom: 220px;
    width: auto;
  }
}

img {
  position: absolute;
  z-index: 0;
  width: 500px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  @media (max-width: 640px) {
    font-size: 24px;
    line-height: 30px;
    top: 80%;
  }
}
</style>
