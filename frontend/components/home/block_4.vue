<script setup lang="ts"></script>

<template>
  <div
    class="margin-glob-new rounded-glob-new relative flex flex-col items-start justify-between gap-[6vw] bg-[--c-black] px-[6vw] py-[8vw] pb-[60vw] text-white md:flex-row md:items-center md:px-[4vw] md:py-[3vw]"
  >
    <p
      class="relative z-10 text-[7.7vw] font-semibold leading-[9vw] md:text-[2.6vw] md:leading-[3vw]"
    >
      Подберём для вас <br />
      <span class="text-primary"> выгодное </span>кредитное <br />
      предложение
    </p>
    <p class="relative z-10 text-[5vw] font-medium leading-[6vw] md:text-[2vw] md:leading-[2.5vw]">
      <span class="text-primary">от 5% до 10%</span><br />
      у банков-партнёров
    </p>
    <img
      :class="['absolute', 'md:inset-0 md:m-auto md:w-[50vw] md:pb-[2vw] md:ps-[8vw]', 'img-small']"
      src="/images/home/block_4_2.png"
      alt="img"
    />
  </div>
</template>

<style scoped>
.img-small {
  @media (max-width: 768px) {
    bottom: -12vw;
    right: -15vw;
    transform: rotate(-30deg) scale(1.3);
  }
}
</style>
