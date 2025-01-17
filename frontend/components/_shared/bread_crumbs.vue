<script setup lang="ts">
type BreadcrumbItem = {
  label: string
  to: string | undefined
}

const route = useRoute()

//////////////////////////////////////////
type paths = ['portfolio', 'contacts']
const labels = {
  portfolio: 'Портфолио',
  contacts: 'Контакты',
  about_company: 'О компании',
  blog: 'Блог',
  'feedback-from-clients': 'Отзывы',
  services: 'Услуги'
}
/////////////////////////////////////////

const chanks = route.path.split('/').slice(1) as unknown as paths
const lastChankIndex = chanks.length - 1
const initAcc: BreadcrumbItem[] = [{ label: 'Главная', to: '/' }]

const items: BreadcrumbItem[] = chanks.reduce((acc, chank, index) => {
  const lastPath = acc[acc.length - 1].to || ''
  const currentPath = `${lastPath}/${chank}`
  const isLast = lastChankIndex === index

  const item: BreadcrumbItem = {
    label: labels[chank],
    to: isLast ? undefined : currentPath
  }

  return [...acc, item]
}, initAcc)
</script>

<template>
  <div class="margin-glob">
    <UBreadcrumb
      :links="items"
      :ui="{
        wrapper: 'mb-[20px] sm:mb-[50px]',
        li: 'text-[10px] sm:text-[15px]',
        active: 'text-[--c-black]',
        inactive: 'text-[var(--c-inactive-crumb)]'
      }"
    />
  </div>
</template>
