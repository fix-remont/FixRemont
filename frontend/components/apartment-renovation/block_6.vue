<script setup lang="ts">
import { hrefCalculater } from 'assets/variables'
</script>

<template>
  <div class="margin-glob block">
    <div class="no-risk-block">
      <div class="text-container">
        <h4>Исключите риски и доверьте свой объект FIX-ремонт</h4>
        <h5>мы не просто берём все финансовые риски на себя, но и закрепляем их юридически</h5>
      </div>
      <NuxtLink :to="hrefCalculater">
        <SharedButton> Онлайн-калькулятор </SharedButton>
      </NuxtLink>
    </div>
  </div>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.no-risk-block {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 35px;
  border-radius: 35px;
  justify-content: space-around;
  background-color: var(--c-orange);

  button {
    background-color: var(--c-black);
    color: #fff;
    border: transparent;
  }
}

.text-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  color: #fff;

  h4 {
    font-weight: bolder;
    font-size: 40px;
  }

  h5 {
    font-weight: 450;
    font-size: 25px;
  }
}

@media (max-width: 800px) {
  .no-risk-block {
    flex-direction: column;
    align-items: center;
    gap: 2rem;

    a {
      width: 100%;
    }
  }

  .text-container {
    align-items: center;
    text-align: center;

    h4 {
      font-size: 30px;
    }
    h5 {
      font-size: 20px;
    }
  }
}
</style>
