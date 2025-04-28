<script setup lang="ts">
const open = ref(false)

const items = [
  // [
  //   { label: 'Услуги', link: '/services' },
  //   { label: 'О компании', link: '/about_company' },
  //   { label: 'Наши объекты', link: '/portfolio' },
  //   { label: 'Отзывы', link: '/feedback-from-clients' },
  //   { label: 'Блог', link: '/blog' },
  //   { label: 'Контакты', link: '/contacts' }
  // ]
  [
    { label: 'Услуги', link: '#' },
    { label: 'О компании', link: '#' },
    { label: 'Наши объекты', link: '#' },
    { label: 'Отзывы', link: '#-from-clients' },
    { label: 'Блог', link: '#' },
    { label: 'Контакты', link: '#' }
  ]
]
</script>

<template>
  <!-- <div class="block w-[16vw] md:w-[4vw]"> -->
  <UDropdown
    v-model:open="open"
    mode="click"
    :ui="{
      wrapper: 'h-full w-[16vw] md:w-[4vw]  rounded-[20px]  rounded-[4.5vw]  md:rounded-[1vw]',
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
  <!-- </div> -->
</template>

<style scoped>
.block {
  .icon {
    height: 100%;
    width: 100%;
  }
}
</style>
