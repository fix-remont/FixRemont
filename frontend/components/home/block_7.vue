<script setup lang="ts">
import { portfolioItemsShort as items } from '#build/imports'
</script>

<template>
	<UCarousel
		class="margin-glob"
		:items="items"
		:ui="{
			container: 'w-full gap-5',
			item: 'w-full lg:w-[49%]',
			indicators: { wrapper: 'justify-end', base: 'h-[5px] w-[5px] sm:h-2 sm:w-2', active: 'bg-[var(--c-black)]', inactive: 'bg-[var(--c-gray)]' },
			arrows: {
				wrapper: 'flex gap-2 justify-start mt-2',
			},
		}"
		arrows
		indicators>
		<template #default="{ item }">
			<SharedPortfolioItem :item="item" />
		</template>

		<template #prev="{ onClick, disabled }">
			<img
				:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
				src="/images/arrow-prev.svg"
				@click="onClick"
				draggable="false" />
		</template>

		<template #next="{ onClick, disabled }">
			<img
				:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
				src="/images/arrow-next.svg"
				@click="onClick"
				draggable="false" />
		</template>
	</UCarousel>
</template>
