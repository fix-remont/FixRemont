<script setup lang="ts"></script>

<template>
  <NuxtLayout>
    <div class="margin-glob wrapper">
      <CabinetNavigation />
      <div class="content">
        <CabinetMainBlock1 />
        <CabinetMainBlock2 />
        <CabinetMainBlock5 />
        <CabinetMainBlock6 />
        <CabinetMainBlock7 />
      </div>
    </div>
  </NuxtLayout>
</template>

<style scoped>
.wrapper {
  display: flex;
  gap: 30px;

  .content {
    flex-grow: 1;
  }
}
</style>
