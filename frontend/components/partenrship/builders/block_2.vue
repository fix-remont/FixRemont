<script setup lang="ts"></script>

<template>
  <article class="margin-glob block">
    <h1 class="title-glob">
      <span class="orange"> Как будет выглядеть </span>
      наше сотрудничество?
    </h1>
    <!--  TODO: нарисовать схему в хтмл вместо фотки-->
    <div class="img-wrapper">
      <img src="/images/builders/block_2.png" alt="block_2" draggable="false" />
    </div>
  </article>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
</style>
