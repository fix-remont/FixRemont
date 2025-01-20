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
        src="/images/building-houses/block_1.png"
        alt="background"
      />
      <h1 class="title-boxing">
        Строительство домов
        <br />
        под ключ по готовым
        <br />
        проектам и с
        <br />
        фиксированной ценой
      </h1>
    </div>

    <div
      class="black-box-wrap bottom-0 right-0 block w-full pl-0 pt-0 lg:absolute lg:w-[initial] lg:pl-8 lg:pt-8"
    >
      <div class="black-box w-full">
        <h3 class="bb-title">Заселитесь в квартиру мечты с мебелью в течение 3-х месяцев</h3>
        <UButton class="mt-auto" :to="hrefCalculater" size="custom" block
          >Отлайн калькулятор</UButton
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

.black-box {
  background-color: #161616;
  padding: 50px;
  border-radius: $radius;
  color: var(--c-white);
  width: 35em;
  @media (max-width: 1025px) {
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

    @media (max-width: 1100px) {
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
