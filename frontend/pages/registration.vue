<script setup lang="ts">
import type { FormSubmitEvent } from '#ui/types'
import type { FeedBackForm } from '#shared/types/forms'
import { hrefSelfPolitic } from 'assets/variables'

const state = ref({
  email: undefined,
  password: undefined,
  repeat_password: undefined,
  isAgree: true
})

const placeholders = {
  email: 'E-mail',
  password: 'Введите пароль',
  repeat_password: 'Повторите пароль'
}

async function onSubmit(event: FormSubmitEvent<FeedBackForm>) {
  console.log(event.data)
}

const password_state = ref({
  password: '',
  showPassword: true
})
const rep_password_state = ref({
  password: '',
  showPassword: true
})

function togglePassword() {
  password_state.value.showPassword = !password_state.value.showPassword
}

function toggleRepPassword() {
  rep_password_state.value.showPassword = !rep_password_state.value.showPassword
}
</script>

<template>
  <NuxtLayout>
    <WBlock class="flex flex-row items-center justify-between">
      <section
        class="radius-glob flex min-h-full w-1/3 flex-col items-center justify-around self-stretch bg-white p-12"
      >
        <UForm
          class="form min-h-1/2 flex w-full flex-col items-start gap-5"
          :state="state"
          @submit="onSubmit"
        >
          <article>
            <h3 class="w-full text-left text-4xl font-semibold">Регистрация</h3>
            <p class="mt-3 text-base font-normal">Зарегистрируйтесь, используя электронную почту</p>
          </article>

          <UFormGroup class="w-full" name="email">
            <template #label>
              <label class="labels" for="email">Электронная почта:</label>
            </template>
            <UInput
              class="input-style"
              id="email"
              v-model="state.email"
              :placeholder="placeholders.email"
              variant="none"
            />
          </UFormGroup>

          <UFormGroup class="w-full" name="password">
            <template #label>
              <label class="labels" for="password">Пароль:</label>
            </template>
            <UInput
              class="input-style"
              id="password"
              v-model="state.password"
              :type="password_state.showPassword ? 'password' : 'text'"
              :placeholder="placeholders.password"
              variant="none"
            />
            <button
              class="absolute right-[70%] top-[64%] -translate-y-1/2 transform"
              type="button"
              @click="togglePassword"
            >
              <img
                :src="
                  password_state.showPassword ? '/icons/hide-passwd.svg' : '/icons/show-passwd.svg'
                "
                alt="toggle-visibility1"
              />
            </button>
          </UFormGroup>

          <UFormGroup class="w-full" name="repeat_password">
            <template #label>
              <label class="labels" for="repeat-password">Повторите пароль:</label>
            </template>
            <UInput
              class="input-style"
              id="repeat-password"
              v-model="state.repeat_password"
              :type="rep_password_state.showPassword ? 'password' : 'text'"
              :placeholder="placeholders.repeat_password"
              variant="none"
            />
            <button
              class="absolute right-[70%] top-[80%] -translate-y-1/2 transform"
              type="button"
              @click="toggleRepPassword"
            >
              <img
                :src="
                  rep_password_state.showPassword
                    ? '/icons/hide-passwd.svg'
                    : '/icons/show-passwd.svg'
                "
                alt="toggle-visibility2"
              />
            </button>
          </UFormGroup>

          <UFormGroup class="checkbox-box" name="isAgree">
            <UCheckbox
              v-model="state.isAgree"
              :ui="{
                base: 'w-[20px] h-[20px]  checked:bg-[var(--c-orange)] hover:checked:bg-[var(--c-orange)] focus:checked:bg-[var(--c-orange)]'
              }"
            >
              <template #label>
                <span class="text-black">
                  Я согласен с
                  <a class="text-orange underline" :href="hrefSelfPolitic"
                    >политикой обработки персональных данных
                  </a>
                </span>
              </template>
            </UCheckbox>
          </UFormGroup>

          <SharedButton type="submit" fill-black>Зарегистрироваться</SharedButton>
        </UForm>
        <p class="mt-8 text-lg font-semibold">
          Уже зарегистрированы?
          <NuxtLink class="orange underline" to="#">Войдите в аккаунт</NuxtLink>
        </p>
      </section>
      <section class="radius-glob w-[60%]">
        <img class="w-full" alt="registration-picture" src="/images/registration/reg_picture.png" />
      </section>
    </WBlock>
  </NuxtLayout>
</template>

<style scoped>
.labels {
  @apply text-base font-normal text-black;
}

.input-style {
  @apply relative mt-3;
}
</style>
