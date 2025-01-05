<script setup lang="ts">
import { ConsultationFormSchema, type ConsultationForm } from '~/shared/types/forms'
import type { FormSubmitEvent } from '#ui/types'

const selectorOptions = [
  { value: 'telegram', label: 'Написать в Telegram' },
  { value: 'watsapp', label: 'Написать в Watsapp' }
]

const state = ref({
  phone: undefined,
  messenger: selectorOptions[0].value
})

const onSubmit = (event: FormSubmitEvent<ConsultationForm>) => {
  console.log(event.data)
}
</script>

<template>
  <div class="margin-glob block">
    <div class="img-box">
      <div class="text-container">
        <p class="text1">
          Саид <br />
          Низамов
        </p>
        <p class="text2">
          Генеральный инженер <br />
          FIX РЕМОНТ
        </p>
      </div>
      <img class="radius-glob" src="/images/contacts/block_2.png" alt="img" />
    </div>

    <div class="content-box">
      <div>
        <p class="text1">Остались вопросы?</p>
        <h1 class="title-glob">
          <span class="orange">Запишитесь</span> на консультацию от инженера FIX-ремонт
        </h1>
        <ul class="list list-disc">
          <li>Поможем подобрать тариф</li>
          <li>Расскажем про сроки строительства</li>
          <li>Озвучим стоимость материалов</li>
          <li>Поделимся опытом решения подобных задач</li>
        </ul>
      </div>

      <p class="text2">Как с вами связаться?</p>
      <UForm class="form" @submit="onSubmit" :state="state" :schema="ConsultationFormSchema">
        <UFormGroup name="messanger">
          <USelect v-model="state.messenger" :options="selectorOptions" variant="none" />
        </UFormGroup>

        <UFormGroup name="phone">
          <UInput v-model="state.phone" placeholder="Введите номер телефона" variant="none" />
        </UFormGroup>

        <SharedButton type="submit" fillBlack>Записаться на консультацию</SharedButton>
      </UForm>
    </div>
  </div>
</template>

<style scoped>
.block {
  overflow: hidden;

  .content-box {
    background-color: white;
    border-radius: 35px;
    padding: 60px;

    @media (max-width: 640px) {
      padding: 10px;
    }

    .text1,
    text2 {
      margin-bottom: 20px;
      font-size: 20px;
      font-weight: 500;
    }
    .text2 {
      display: flex;
      width: 100%;
      margin-bottom: 20px;
    }
    .list {
      font-size: 20px;
      font-weight: 500;
      margin-left: 20px;
      margin-top: 20px;
      margin-bottom: 50px;
    }
    .form {
      display: flex;
      width: 100%;
      gap: 20px;

      @media (max-width: 1300px) {
        flex-direction: column;
      }

      & > div {
        flex: 1;
      }
      button {
        flex: 1;
        height: 92px;
      }
    }
  }

  .img-box {
    background-color: #fafafa;
    float: right;
    border-radius: 0 0 0 35px;
    position: relative;

    @media (max-width: 1600px) {
      float: none;
      margin-bottom: 20px;
    }

    &::before,
    &::after {
      content: '';
      position: absolute;
      width: 70px;
      height: 70px;
      border-radius: 50%;
    }
    &::before {
      left: -70px;
      top: 0;
      box-shadow: 35px -35px #fafafa;
    }
    &::after {
      right: 0;
      bottom: -70px;
      box-shadow: 35px -35px #fafafa;
    }

    @media (max-width: 1600px) {
      &::after,
      &::before {
        box-shadow: none;
      }
    }
    .text-container {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      top: 20px;
      right: 20px;
      position: absolute;
      color: white;
      .text1 {
        font-size: 32px;
        font-weight: 600;

        @media (max-width: 800px) {
          font-size: 20px;
        }
        @media (max-width: 640px) {
          font-size: 16px;
        }
      }

      .text2 {
        font-size: 15px;
        font-weight: 500;

        @media (max-width: 800px) {
          font-size: 12px;
        }
        @media (max-width: 640px) {
          font-size: 12px;
        }
      }
    }

    img {
      margin-left: 30px;
      margin-bottom: 30px;
      @media (max-width: 1600px) {
        margin-left: 0;
        margin-bottom: 0;
        width: 100%;
      }
    }
  }
}
</style>
