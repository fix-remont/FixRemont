<script setup lang="ts">
const itemsRaw = [
	{ title: 'Дом из кирпича 560м на Барвихе', img: '/images/home/block_7__1.png' },
	{ title: 'Квартира 300м на Баумана', img: '/images/home/block_7__2.png' },
]

const items = Array(3)
	.fill(itemsRaw)
	.flat()
	.map((item, index) => ({ ...item, id: index }))
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
			<div class="item-box">
				<img :src="item.img" :alt="item.title" draggable="false" />
				<div class="text-box">
					<p class="title">{{ item.title }}</p>
					<NuxtLink :class="['link pointer']" :to="item.id">Узнать Стоимость</NuxtLink>
				</div>
			</div>
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

<style scoped>
.item-box {
	position: relative;
	font-weight: 600;
	font-size: 10px;
	@media (max-width: 640px) {
		font-size: 6px;
	}

	.text-box {
		position: absolute;
		left: 5em;
		bottom: 5em;
		font-size: 1em;

		.title {
			font-size: 3.6em;
			color: white;
			z-index: 1;
		}
		.link {
			text-decoration: underline;
			color: var(--c-orange);
			font-size: 1.8em;
			z-index: 1;
		}
	}
}
</style>
