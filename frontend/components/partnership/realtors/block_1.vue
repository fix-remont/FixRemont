<script setup lang="ts">
import { hrefCalculater } from '~/assets/variables'
</script>

<template>
  <WBlock class="relative">
    <div class="radius-glob relative mb-10 overflow-hidden lg:mb-0">
      <SharedBreadCrumbs class="top-10 z-10 hidden lg:absolute lg:block" />
      <img
        class="radius-glob max-h-[700px] w-full object-cover"
        src="/images/realtors/block_1.png"
        alt="background"
      />
      <h1 class="title-boxing">
        Приводите клиентов на ремонт с фикс ценой и зарабатывайте от <br />
        1 000 руб/м² с каждой сделки
      </h1>
    </div>

    <div
      class="black-box-wrap bottom-0 right-0 block w-full pl-0 pt-0 lg:absolute lg:w-[initial] lg:pl-8 lg:pt-8"
    >
      <div class="black-box w-full">
        <h3 class="bb-title">
          Обеспечим ваших клиентов сервисом и услугой высшего уровня без рисков для репутации
        </h3>
        <NuxtLink class="orange cursor-pointer underline"> Подробнее </NuxtLink>
        <UButton class="mt-[3vw]" :to="hrefCalculater" size="custom" block
          >Зарегистрироваться как партнер</UButton
        >
      </div>
    </div>
  </WBlock>
</template>

<style scoped lang="postcss">
$radius: 35px;
.content {
  position: absolute;
  bottom: 0;
  margin-bottom: 5%;
  left: 100px;
}

.black-box-wrap {
  background-color: var(--c-white);
  border-radius: $radius 0 0;

  &::before,
  &::after {
    content: '';
    position: absolute;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    box-shadow: 35px 35px var(--c-white);

    @media (max-width: 1024px) {
      display: none;
    }
  }
  &::before {
    bottom: 0;
    left: -70px;
  }
  &::after {
    right: 0;
    top: -70px;
  }
}

.title-boxing {
  width: 43vw;
  font-size: 2.5vw;
  font-weight: bold;
  line-height: 3vw;
  color: white;
  position: absolute;
  bottom: 2.5vw;
  left: 2.5vw;

  @media (max-width: 768px) {
    color: #e9e9e9;
    font-size: 3.5vw;
    line-height: 5vw;
    bottom: 3vw;
    left: 3vw;
  }
}

.black-box {
  background-color: #161616;
  padding: 2.5vw;
  border-radius: $radius;
  color: var(--c-white);
  width: 32vw;
  @media (max-width: 1025px) {
    width: initial;
  }
  @media (max-width: 768px) {
    padding: 3.5vw;
  }

  .bb-title {
    font-size: 1.5vw;
    margin-bottom: 1.5vw;
    @apply font-semibold;
    color: white;
    width: 75%;

    @media (max-width: 1030px) {
      width: 100%;
      margin-bottom: 2rem;
    }

    @media (max-width: 768px) {
      font-size: 3vw;
    }
  }
}
</style>
