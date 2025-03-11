<script setup lang="ts">
const state = ref({
  clientsRepair: undefined,
  clientsBuild: undefined,
  total: 0
})

const placeholders = {
  clientsRepair: 'Например, 10',
  clientsBuild: 'Например, 8'
}

const labels = {
  clientsRepair: 'Количество клиентов на ремонт',
  clientsBuild: 'Количество клиентов на строительство'
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
      <h1 class="text-glob-xl">
        <span class="orange">
          Спрогнозируйте свой <br />
          доход
        </span>
        прямо сейчас
      </h1>
      <p class="subtitle-glob">В расчёт возьмём средние данные по пакетам</p>
    </div>
    <div class="right">
      <h1 class="text-glob-xl">
        Итого:
        <u>{{ state.total }}</u>
        руб
      </h1>
      <p class="subtitle-glob text-[#808080]">
        *расчёт ориентировочный и не несёт в себе никаких гарантий
      </p>
    </div>
    <UForm class="down" :state="state" @submit.preven="onSubmit">
      <UFormGroup name="clientsRepair">
        <template #label>
          <span class="text-sm font-semibold text-black">{{ labels.clientsRepair }}</span>
        </template>
        <UInput
          class="mt-4"
          v-model="state.clientsRepair"
          :placeholder="placeholders.clientsRepair"
          variant="none"
          @input="validateNaturalNumber"
        />
      </UFormGroup>

      <UFormGroup name="clientsBuild">
        <template #label>
          <span class="text-sm font-semibold text-black">{{ labels.clientsBuild }}</span>
        </template>
        <UInput
          class="mt-4"
          v-model="state.clientsBuild"
          :placeholder="placeholders.clientsBuild"
          variant="none"
          @input="validateNaturalNumber"
        />
      </UFormGroup>

      <div class="container">
        <p class="mb-4 block text-sm font-medium text-red-600" v-if="validationMessage">
          {{ validationMessage }}
        </p>
        <SharedButton fillBlack type="submit"> Рассчитать доход</SharedButton>
      </div>
    </UForm>
  </div>
</template>

<style scoped>
.block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;

  @media (max-width: 768px) {
    grid-template-rows: auto auto auto;
    grid-template-columns: 1fr;
    align-items: center;
  }
}

.left {
  @media (max-width: 768px) {
    text-align: center;
    order: 1;
  }
}

.right {
  padding: 2.5vw 7vw;
  border-radius: 24px;
  border: 3px solid var(--c-black);

  @media (max-width: 768px) {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 3.13vw 4.17vw;
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
  margin-top: 3vw;
  display: grid;
  gap: 2vw;
  align-items: end;
  grid-template-columns: 1fr 1fr 1fr;

  @media (max-width: 768px) {
    order: 2;
    margin-bottom: 2vw;
    margin-top: 2vw;
  }
}

.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  button {
    @media (max-width: 768px) {
      padding: 15px;
    }
  }
}
</style>
