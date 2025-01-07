<script setup>
const balance = 123345
const inWork = 13345
</script>

<template>
  <section class="wallet radius-glob margin-b-glob">
    <h2>Кошелёк</h2>
    <div class="wrap-info">
      <div class="balance">
        <div class="label">Баланс:</div>
        <div class="value">{{ balance }} руб</div>
      </div>

      <div class="in-work">
        <div class="label">В работе:</div>
        <div class="value">{{ inWork }} руб</div>
      </div>
    </div>
    <div class="wrap-buttons">
      <SharedButton class="button-wallet" fillOrange>Вывести средства</SharedButton>
      <SharedButton class="button-wallet">Перейти в кошелёк</SharedButton>
    </div>
  </section>
</template>

<style scoped>
.wallet {
  font-size: 32px;
  font-weight: 600;
  background-color: white;
  display: flex;
  padding: 40px;
  gap: 40px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;

  @media (max-width: 640px) {
    font-size: 16px;
    padding: 10px;
  }

  .wrap-info {
    display: flex;
    gap: 20px;
  }
  .in-work,
  .balance {
    .label {
      color: #686868;
      font-weight: 500;
      font-size: 16px;
      @media (max-width: 640px) {
        font-size: 12px;
      }
    }
  }
  .wrap-buttons {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    flex-grow: 1;

    .button-wallet {
      width: initial;
      min-width: 300px;
      flex-grow: 1;
      @media (max-width: 640px) {
        min-width: initial;
        width: 100%;
      }
    }
  }
}
</style>
