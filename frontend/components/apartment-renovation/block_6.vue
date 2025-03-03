<script setup lang="ts">
import { hrefCalculater } from 'assets/variables'
</script>

<template>
  <div class="margin-glob flex flex-col gap-8">
    <div
      class="flex flex-col items-center justify-around gap-8 rounded-[24px] bg-[var(--c-orange)] p-[3vw] md:flex-row md:p-[2vw]"
    >
      <div class="flex flex-col gap-2 font-semibold text-white">
        <h4 class="text-center text-[4.5vw] md:text-left md:text-[2vw]">
          Исключите риски и доверьте свой объект FIX-ремонт
        </h4>
        <h5 class="text-center text-[3vw] md:text-left md:text-[1.2vw]">
          мы не просто берём все финансовые риски на себя, но и закрепляем их юридически
        </h5>
      </div>
      <UButton class="p-[3vw] md:w-[20vw] md:p-[1.5vw]" color="white" :to="hrefCalculater"
        >Онлайн-калькулятор</UButton
      >
    </div>
  </div>
</template>

<style scoped>
@media (max-width: 768px) {
  a {
    width: 100%;
  }
}
</style>
