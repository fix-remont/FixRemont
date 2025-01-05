<script setup lang="ts">
import { hrefSelfPolitic, hrefTg, hrefWatsapp } from '~/assets/variables'
import { FeedBackFormschema, type FeedBackForm } from '~/shared/types/forms'
import type { FormSubmitEvent } from '#ui/types'
import { _padding } from '#tailwind-config/theme'

const icons1 = [
  { src: 'watsapp.svg', href: hrefWatsapp },
  { src: 'telegram.svg', href: hrefTg }
]

const state = ref({
  message: undefined,
  phone: undefined,
  email: undefined,
  isAgree: true
})

const placeholders = {
  message: 'Сообщение',
  phone: 'Ваш номер телефона',
  email: 'Ваш e-mail'
}

async function onSubmit(event: FormSubmitEvent<FeedBackForm>) {
  console.log(event.data)
}
</script>

<template>
  <div class="margin-glob">
    <div class="info radius-glob">
      <h1 class="title title-glob">Форма обратной связи</h1>
      <div class="texts">
        <p>Оставьте нам сообщение, отзыв или предложение.</p>
        <p>Ответ пришлём на указанный e-mail.</p>
        <div class="with-icons">
          <p>Или напишите нам в мессенджер</p>
          <a v-for="icon in icons1" :href="icon.href">
            <img :src="`/icons/${icon.src}`" :class="['hover', 'icon']" :alt="icon.src" />
          </a>
        </div>
      </div>
    </div>
    <div class="box">
      <UForm class="form" :state="state" :schema="FeedBackFormschema" @submit="onSubmit">
        <UFormGroup name="message">
          <UTextarea v-model="state.message" :placeholder="placeholders.message" variant="none" />
        </UFormGroup>

        <UFormGroup name="phone">
          <UInput v-model="state.phone" :placeholder="placeholders.phone" variant="none" />
        </UFormGroup>

        <UFormGroup name="email">
          <UInput v-model="state.email" :placeholder="placeholders.email" variant="none" />
        </UFormGroup>

        <SharedButton type="submit" fillBlack>Отправить сообщение</SharedButton>

        <UFormGroup class="checkbox-box" name="isAgree">
          <UCheckbox
            v-model="state.isAgree"
            :ui="{
              base: 'w-[20px] h-[20px]  checked:bg-[var(--c-orange)] hover:checked:bg-[var(--c-orange)] focus:checked:bg-[var(--c-orange)]'
            }"
          >
            <template #label>
              <span class="text">
                Согласен с условиями
                <a :class="['politic', 'hover']" :href="hrefSelfPolitic"
                  >Политики конфиденциальности</a
                >
              </span>
            </template>
          </UCheckbox>
        </UFormGroup>
      </UForm>
      <div class="img-container">
        <img class="img radius-glob" src="/images/contacts/block_2.png" alt="img" />
        <div class="texts">
          <p class="text1">
            Александр <br />
            Иванов
          </p>
          <p class="text2">
            Менеджер по продажам <br />
            FIX-ремонт
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.box {
  display: flex;
  gap: 30px;
  @media (max-width: 1000px) {
    flex-direction: column;
  }
  .form {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    gap: 30px;
    .checkbox-box {
      display: flex;

      font-size: 14px;
      font-weight: 500;
      .text {
        a {
          text-decoration: underline;
        }
      }
    }
  }
  .img-container {
    position: relative;
    width: 50%;
    @media (max-width: 1000px) {
      width: 100%;
    }
    img {
      object-fit: cover;
      object-position: left;
      height: 100%;
      width: 100%;
    }

    .texts {
      position: absolute;
      color: white;
      top: 30px;
      right: 30px;
      font-size: 10px;
      @media (max-width: 1100px) {
        font-size: 7px;
      }
      @media (max-width: 860px) {
        top: 10px;
        right: 10px;
      }
      .text1 {
        font-size: 3.2em;
        line-height: 1.3em;
        font-weight: 600;
        margin-bottom: 20px;
      }
      .text2 {
        font-size: 1.5em;
        font-weight: 500;
      }
    }
  }
}
.info {
  color: white;
  background-color: var(--c-black);
  padding: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 20px;
  @media (max-width: 640px) {
    padding: 20px;
    flex-direction: column;
  }

  .title {
    @media (max-width: 640px) {
      font-size: 24px;
    }
  }
  .texts {
    font-size: 20px;
    font-weight: 500;
    display: flex;
    flex-direction: column;
    gap: 10px;

    @media (max-width: 800px) {
      font-size: 12px;
    }
    .with-icons {
      display: flex;
      align-items: center;
      gap: 10px;
    }
  }
}
</style>
