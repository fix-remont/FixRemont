<script setup lang="ts"></script>
<template>
  <NuxtLayout>
    <div class="margin-glob radius-glob block">
      <h1 class="title title-glob">Такой страницы не существует!</h1>
      <p class="text">Возможно, страница устарела или была удалена</p>
      <SharedButton class="button" fillOrange>
        <NuxtLink to="/"> Перейти на главную </NuxtLink>
      </SharedButton>
      <img class="img" src="/images/404.png" alt="404" />
    </div>
  </NuxtLayout>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  background-color: var(--c-black);
  flex-grow: 1;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 20px 20px 0 20px;

  .title {
    color: white;
    margin-top: 120px;
    text-align: center;
    @media (max-width: 1500px) {
      margin-top: 20px;
    }
    @media (max-width: 840px) {
      font-size: 30px;
    }
  }
  .text {
    text-align: center;
    font-size: 20px;
    color: white;
  }
  .button {
    width: 345px;
    @media (max-width: 840px) {
      width: 90%;
    }
  }
  .img {
    width: 740px;
    @media (max-width: 840px) {
      width: 400px;
    }
  }
}
</style>
