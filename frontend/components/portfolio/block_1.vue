<script setup lang="ts">
import { portfolioItemsShort as items } from '~/shared/utils/data'

const selectedIndex = ref(0)

const tabsRow = [
	{ label: 'Все', value: 'all', selected: false },
	{ label: 'Ремонт квартир', value: 'appartament_renovation', selected: false },
	{ label: 'Строительство домов', value: 'house_construction', selected: false },
]
const tabs = computed(() => {
	return tabsRow.map((tab, index) => {
		tab.selected = selectedIndex.value === index ? true : false
		return tab
	})
})
</script>

<template>
	<div class="block margin-glob">
		<p>Работаем одинаково хорошо, как на крупных объектах, так и в небольших квартирах</p>
		<h1 class="title title-glob">Посмотрите на наши <span class="orange"> выполненные проекты</span></h1>
		<div class="tabs-container">
			<div :class="['tab', 'radius-glob', 'hover', { 'tab-selected': tab.selected }]" v-for="(tab, index) in tabs" @click="selectedIndex = index">
				{{ tab.label }}
			</div>
		</div>
	</div>
</template>

<style scoped>
.block {
	.title {
		margin-bottom: 30px;
		@media (max-width: 640px) {
			margin-bottom: 10px;
		}
	}
	.tabs-container {
		display: flex;
		gap: 15px;
		margin-bottom: 30px;

		@media (max-width: 640px) {
			gap: 5px;
			margin-bottom: 10px;
		}
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
}
</style>
