<script setup>
import { ref } from 'vue'

const items = [
	{ label: 'Базовый', img: '/images/home/package-comfort.png' },
	{ label: 'Стандарт', img: '/images/home/package-comfort.png' },
	{ label: 'Комфорт', img: '/images/home/package-comfort.png' },
	{ label: 'Бизнес', img: '/images/home/package-comfort.png' },
]

const carousel = ref(null)

const update = (onClick, page) => {
	console.log(page)
	onClick()
}
// function goToSlide(slideNumber) {
// 	carousel.value.select(slideNumber)
// }
</script>

<template>
	<div :class="['margin-glob', 'box']">
		<div class="text"></div>

		<UCarousel
			ref="carousel"
			:items="items"
			class="carousel"
			:ui="{ item: 'w-full h-full rounded-3xl overflow-hidden', container: 'gap-2 relative h-full', arrows: { wrapper: 'absolute bottom-0' } }"
			arrows>
			<template #default="{ item }">
				<img class="slide" :src="item.img" draggable="false" />
			</template>

			<template #prev="{ onClick, disabled, ...page }">
				<img :class="['arrow', { arrow_disabled: disabled }]" src="/images/arrow-prev.svg" @click="update(onClick, page)" />
			</template>

			<template #next="{ onClick, disabled }">
				<img :class="['arrow', { arrow_disabled: disabled }]" src="/images/arrow-next.svg" :disabled="disabled" @click="update(onClick)" />
			</template>
		</UCarousel>

		<div class="tabs"></div>

		<div class="info"></div>
		<!-- <button @click="goToSlide(2)">Перейти на второй слайд</button> -->
	</div>
</template>

<style scoped>
.box {
	display: grid;
	grid-template-columns: 50% 50%;
	grid-template-rows: 500px 290px;
	grid-template-areas: 'text carousel' 'tabs info';
	gap: 30px;
}

.text {
	grid-area: text;
}
.carousel {
	grid-area: carousel;
	.slide {
		object-fit: cover;
	}
	.arrow {
		width: 50px;
		height: 50px;
		padding-left: 10px;
		padding-bottom: 10px;

		&_disabled {
			opacity: 0.5;
		}
	}
}
.tabs {
	grid-area: tabs;
}
.info {
	grid-area: info;
}
</style>
