<script setup lang="ts"></script>

<template>
  <NuxtLayout>
    <SharedBreadCrumbs />
    <PortfolioIdBlock1 />
    <HomeBlock7>
      <template #title>
        <WTitle class="margin-glob">Другие реализованные проекты</WTitle>
      </template>
      <template #button>
        <UButton class="margin-glob w-[initial] py-3 sm:py-6" to="/portfolio" block color="white"
          >Смотреть все портфолио</UButton
        >
      </template>
    </HomeBlock7>
    <PortfolioBlock2 />
    <HomeBlock16 />
  </NuxtLayout>
</template>

<style scoped></style>
