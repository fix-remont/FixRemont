<script setup lang="ts">
const open = ref(false)

const items = [[{ label: 'Наши объекты', link: '/portfolio' }]]
</script>

<template>
	<div class="block">
		<UDropdown
			v-model:open="open"
			mode="click"
			:ui="{
				wrapper: 'h-full w-full rounded-[20px]',
				padding: 'px-[15px] py-[15px]',
				width: 'w-max',
				rounded: 'rounded-[20px]',
				item: { padding: 'px-[15px] py-[5px]', rounded: 'rounded-[20px]', size: 'text-[18px] color-[var(--c-black)]' },
			}"
			:items="items">
			<img v-if="open" class="icon hover" src="/icons/close-button.svg" alt="close-button" draggable="false" />
			<img v-else class="icon hover" src="/icons/burger.svg" draggable="false" alt="burger" />

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
	}
}
</style>
