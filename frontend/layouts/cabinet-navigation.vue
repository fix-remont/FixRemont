<script setup lang="ts"></script>

<template>
  <div class="margin-glob wrapper">
    <CabinetNavigation />
    <div class="content">
      <slot />
    </div>
  </div>
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
