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
        src="/images/home/package-comfort.png"
        alt="background"
      />
      <h1 class="text:2xl absolute bottom-10 left-10 font-bold text-white xl:text-4xl">
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
        <h3 class="text:2xl mb-4 font-bold text-white xl:text-3xl">
          Заселитесь в
          <br />
          квартиру мечты с
          <br />
          мебелью в течение
          <br />
          3-х месяцев
        </h3>
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
  @media (max-width: 1024px) {
    width: initial;
  }
}
</style>
