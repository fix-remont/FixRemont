<script setup lang="ts">
import { useViewport } from '~/composables/viewport'
import { hrefCalculater } from '~/assets/variables'

const { width } = useViewport()
</script>

<template>
  <WBlock class="relative">
    <div class="radius-glob relative mb-10 overflow-hidden lg:mb-0">
      <SharedBreadCrumbs class="top-10 z-10 hidden lg:absolute lg:block" />
      <img
        class="radius-glob max-h-[700px] w-full object-cover"
        src="/images/builders/block_1.png"
        alt="background"
      />
      <h1 class="title-boxing">
        Продавайте квартиры с готовым ремонтом по фиксированной цене от FIX-ремонт
      </h1>
    </div>

    <div
      class="black-box-wrap bottom-0 right-0 block w-full pl-0 pt-0 lg:absolute lg:w-[initial] lg:pl-8 lg:pt-8"
    >
      <div class="black-box w-full">
        <h3 class="bb-title">
          Повысьте качество ваших объектов и дополнительно зарабатывайте на “ремонте в ипотеку”
        </h3>
        <NuxtLink class="orange cursor-pointer underline"> Подробнее </NuxtLink>
        <UButton class="mt-4" :to="hrefCalculater" size="custom" block
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
</style>
