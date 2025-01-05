<script setup lang="ts">
const state = ref({
  clientsRepair: undefined,
  clientsBuild: undefined,
  total: 0,
})

const placeholders = {
  clientsRepair: 'Например, 10',
  clientsBuild: 'Например, 8',
}

const labels = {
  clientsRepair: 'Количество клиентов на ремонт',
  clientsBuild: 'Количество клиентов на строительство',
}

const validationMessage = ref('')

function validateNaturalNumber(event: InputEvent) {
  const target = event.target as HTMLInputElement
  target.value = target.value.replace(/[^1-9]/g, '')
}

function onSubmit() {
  if (!state.value.clientsRepair || !state.value.clientsBuild) {
    validationMessage.value = 'Пожалуйста, паполните все поля'
    return
  }
  validationMessage.value = ''
  state.value.total = Math.floor(Math.random() * 1000000) + 1
  console.log('Form submitted:', state.value)
}
</script>

<template>
<div class="margin-glob block">
  <div class="left">
    <h1 class="title-glob">
      <span class="orange"> Спрогнозируйте свой <br/> доход </span>
      прямо сейчас
    </h1>
    <p class="subtitle-glob">
      В расчёт возьмём средние данные по пакетам
    </p>
  </div>
  <div class="right">
    <h1 class="title-glob">
      Итого:
      <u>{{ state.total }}</u>
      руб
    </h1>
    <p>*расчёт ориентировочный и не несёт в себе никаких гарантий</p>
  </div>
  <UForm class="down" :state="state" @submit.preven="onSubmit">
    <UFormGroup name="clientsRepair" :label="labels.clientsRepair">
      <UInput
          v-model="state.clientsRepair"
          :placeholder="placeholders.clientsRepair"
          variant="none"
          class="mt-4"
          @input="validateNaturalNumber"
      />
    </UFormGroup>

    <UFormGroup name="clientsBuild" :label="labels.clientsBuild">
      <UInput
          v-model="state.clientsBuild"
          :placeholder="placeholders.clientsBuild"
          variant="none"
          class="mt-4"
          @input="validateNaturalNumber"
      />
    </UFormGroup>

    <div class="container">
      <p v-if="validationMessage" class="text-red-600 text-sm font-medium mb-4 block">{{ validationMessage }}</p>
      <SharedButton fillBlack type="submit">
        Рассчитать доход
      </SharedButton>
    </div>
  </UForm>
</div>
</template>

<style scoped>

.block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;

  @media (max-width: 800px) {
    grid-template-rows: auto auto auto;
    grid-template-columns: 1fr;
    align-items: center;
  }
}

.left {
  text-align: center;
  @media (max-width: 800px) {
    order: 1;
  }
}

.right {
  padding: 40px 80px;
  border-radius: 35px;
  border-color: var(--c-black);
  border-style: solid;
  border-width: 3px;

  p {
    margin-top: 1rem;
    font-size: 16px;
    color: #808080;
  }

  @media (max-width: 800px) {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px 40px;
    text-align: center;
    order: 3;
    h1 {
      width: 65%;
    }
  }
}

.down {
  grid-column: span 2;
  width: 100%;
  margin-top: 3rem;
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: end;

    @media (max-width: 800px) {
    order: 2;
    margin-bottom: 2rem;
    margin-top: 2rem;
  }
}

.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
</style>