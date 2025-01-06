<script setup lang="ts"></script>

<template>
  <div class="margin-glob block">
    <div class="titles">
      <h1 class="title-glob">
        FIX-ремонт — это более
        <br />
        <span class="orange">
          36 готовых дизайнерских
          <br />
          решений
        </span>
        под любой бюджет
      </h1>
      <p class="subtitle-glob">
        с реализацией “под ключ” и без финансовых и репутационных рисков для партнёров
      </p>
    </div>
    <NuxtLink class="w-full">
      <SharedButton>Пройти 3D-тур по проектам</SharedButton>
    </NuxtLink>
  </div>
</template>

<style scoped lang="postcss">
.block {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 3rem;
  padding: 70px;
  border-radius: 24px;
  background-image: url('/images/realtors/block_2.png');
  background-position: center;
  color: #fff;

  .titles h1 {
    margin-top: 21rem;
  }
}
</style>
