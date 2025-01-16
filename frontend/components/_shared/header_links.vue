<script setup lang="ts">
const open = ref(false)

const items = [
  [
    { label: 'О компании', link: '/about_company' },
    { label: 'Наши объекты', link: '/portfolio' },
    { label: 'Отзывы', link: '/feedback-from-clients' },
    { label: 'Блог', link: '/blog' },
    { label: 'Контакты', link: '/contacts' }
  ]
]
</script>

<template>
  <div class="block">
    <UDropdown
      v-model:open="open"
      mode="click"
      :ui="{
        wrapper: 'h-[52px] w-[52px] sm:h-full sm:w-full rounded-[20px]',
        padding: 'px-[15px] py-[15px]',
        width: 'w-max',
        rounded: 'rounded-[20px]',
        item: {
          padding: 'px-[15px] py-[5px]',
          rounded: 'rounded-[20px]',
          size: 'text-[18px] color-[var(--c-black)]'
        }
      }"
      :items="items"
    >
      <img
        class="icon hover"
        :src="open ? '/icons/close-button.svg' : '/icons/burger.svg'"
        alt="close-button"
        draggable="false"
        loading="eager"
      />

      <template #item="{ item }">
        <NuxtLink :to="item.link">
          {{ item.label }}
        </NuxtLink>
      </template>
    </UDropdown>
  </div>
</template>

<style scoped>
.block {
  .icon {
    height: 100%;
    width: 100%;
  }
}
</style>
