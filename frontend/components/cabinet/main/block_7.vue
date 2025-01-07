<script setup lang="ts"></script>

<template>
  <article class="margin-b-glob article radius-glob">
    <h2 class="title">
      <span class="orange"> Есть вопросы? </span> <br />
      Обратитесь в нашу службу поддержки
    </h2>
    <div class="buttons">
      <SharedButton fillBlack>Задать вопрос</SharedButton>
      <SharedButton>Найти ответ на вопрос в FAQ</SharedButton>
    </div>
  </article>
</template>

<style scoped>
.article {
  display: flex;
  gap: 20px;
  padding: 35px;
  border: 2px solid var(--c-black);

  @media (max-width: 1700px) {
    flex-direction: column;
  }

  @media (max-width: 640px) {
    padding: 15px;
  }

  .title {
    font-size: 32px;
    font-weight: 600;
  }
  .buttons {
    display: flex;
    flex-grow: 1;
    gap: 20px;
    min-width: 800px;

    @media (max-width: 1000px) {
      min-width: initial;
      flex-direction: column;
    }

    button {
      align-self: center;
    }
  }
}
</style>
