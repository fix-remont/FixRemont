<script setup lang="ts"></script>

<template>
  <div class="margin-glob block">
    <div class="titles">
      <h1 class="text-glob-xl">
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
    <UButton variant="outline" block color="white"> Пройти 3D-тур по проектам </UButton>
  </div>
</template>

<style scoped lang="postcss">
.block {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2.5vw;
  padding: 5vw;
  border-radius: 24px;
  background-image: url('/images/realtors/block_2.png');
  background-position: center;
  color: #fff;

  .titles h1 {
    margin-top: 20vw;
  }
}

@media (max-width: 768px) {
  .block {
    align-items: center;
    text-align: center;

    .titles h1 {
      margin-top: 0;
    }
  }
}
</style>
