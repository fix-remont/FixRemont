<script setup lang="ts">
import { ConsultationFormFromBlogSchema, type ConsultationFormFromBlog } from '~/shared/types/forms'
import type { FormSubmitEvent } from '#ui/types'
import { hrefSelfPolitic } from '~/assets/variables'
import { twMerge } from 'tailwind-merge'

const selectorOptions = [
  { value: 'telegram', label: 'Написать в Telegram' },
  { value: 'watsapp', label: 'Написать в Watsapp' }
]

const state = ref({
  phone: undefined,
  messenger: selectorOptions[0].value,
  isAgree: true
})
const onSubmit = (event: FormSubmitEvent<ConsultationFormFromBlog>) => {
  console.log(event.data)
}

const props = defineProps<{
  class?: string
}>()
</script>

<template>
  <div
    :class="
      twMerge(
        'radius-glob top-2 block h-max w-full bg-[var(--c-black)] p-4 text-white md:p-12 lg:sticky lg:w-[570px] lg:min-w-[570px]',
        props.class
      )
    "
  >
    <p class="mb-5 text-sm font-semibold">Получите бесплатный файл</p>
    <h2 class="mb-5 text-lg font-bold md:text-4xl">
      <span class="orange">ТОП-7 рекомендаций </span> от наших специалистов по выбору материалов для
      внутренней отделки вашего жилья
    </h2>
    <p class="mb-5 text-sm font-semibold">Куда выслать файл</p>
    <UForm
      class="flex flex-col gap-4"
      @submit="onSubmit"
      :state="state"
      :schema="ConsultationFormFromBlogSchema"
    >
      <UFormGroup name="messanger">
        <USelect v-model="state.messenger" :options="selectorOptions" variant="darkGray" />
      </UFormGroup>

      <UFormGroup name="phone">
        <UInput v-model="state.phone" placeholder="Введите номер телефона" variant="darkGray" />
      </UFormGroup>

      <SharedButton type="submit" fillOrange>Записаться на консультацию</SharedButton>

      <UFormGroup name="isAgree">
        <UCheckbox
          v-model="state.isAgree"
          :ui="{
            base: ' w-[20px] h-[20px]  checked:bg-[var(--c-orange)] hover:checked:bg-[var(--c-orange)] focus:checked:bg-[var(--c-orange)]'
          }"
        >
          <template #label>
            <span class="text-white">
              Согласен с условиями
              <a class="hover underline" :href="hrefSelfPolitic">Политики конфиденциальности</a>
            </span>
          </template>
        </UCheckbox>
      </UFormGroup>
    </UForm>
  </div>
</template>
