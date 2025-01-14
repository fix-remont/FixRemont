<script setup lang="ts">
type Tab = { label: string; value: string; selected?: boolean }

const props = defineProps<{
  tabs: Tab[]
}>()

const emit = defineEmits(['selectedTabIndex'])

const selectedIndex = ref(0)

const tabs = computed(() => {
  return props.tabs.map((tab, index) => {
    tab.selected = selectedIndex.value === index ? true : false
    return tab
  })
})

watch(selectedIndex, (index) => emit('selectedTabIndex', index))
</script>

<template>
  <article>
    <div class="tabs-container sm:gap10 mb-10 flex gap-5 sm:mb-16">
      <div
        v-for="(tab, index) in tabs"
        :class="['tab', 'radius-glob', { hover: !tab.selected }, { 'tab-selected': tab.selected }]"
        @click="selectedIndex = index"
      >
        {{ tab.label }}
      </div>
    </div>
  </article>
</template>

<style scoped>
.tabs-container {
  .tab {
    padding: 12px 28px;
    color: var(--c-black);
    background-color: white;

    @media (max-width: 640px) {
      padding: 6px 8px;
      font-size: 10px;
    }
    &-selected {
      color: white;
      background-color: var(--c-black);
    }
  }
}
</style>
