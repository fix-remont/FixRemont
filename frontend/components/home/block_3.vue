<script setup>
import { ref } from 'vue'
import { hrefCalculater } from '~/assets/css/variables'

const items = [
	{ label: 'Базовый', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Стандарт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Комфорт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Бизнес', img: '/images/home/package-comfort.png', selected: false },
]

const carouselRef = ref(null)
const currentActiveIndex = ref(0)

const itemsWithSelected = computed(() => {
	return items.map((item, index) => {
		item.selected = index === currentActiveIndex.value
		return item
	})
})
const handleUpdateCarouselByButton = (onClick, actionType, disabled) => {
	if (disabled) return
	onClick()
}

const handleClickTab = (tabIndex) => {
	carouselRef.value.select(tabIndex + 1)
}

watch(
	() => carouselRef.value?.page,
	(newPage) => (currentActiveIndex.value = newPage - 1)
)

// autoplay
// onMounted(() => {
// 	setInterval(() => {
// 		if (!carouselRef.value) return

// 		if (carouselRef.value.page === carouselRef.value.pages) {
// 			currentActiveIndex.value = 0
// 			return carouselRef.value.select(0)
// 		}

// 		currentActiveIndex.value = carouselRef.value.page
// 		carouselRef.value.next()
// 	}, 5000)
// })
</script>

<template>
	<div :class="['margin-glob', 'box']">
		<div class="text-area">
			<p>
				Занимайтесь
				<span class="orange">любимыми</span> делами, а ремонт мы возьмём на себя.
			</p>
		</div>

		<UCarousel
			ref="carouselRef"
			:items="items"
			class="carousel-area"
			:ui="{ item: 'w-full h-full rounded-3xl overflow-hidden', container: 'gap-2 relative h-full', arrows: { wrapper: 'absolute bottom-0' } }"
			arrows>
			<template #default="{ item }">
				<img class="slide" :src="item.img" draggable="false" />
			</template>

			<template #prev="{ onClick, disabled }">
				<img :class="['arrow', { arrow_disabled: disabled }]" src="/images/arrow-prev.svg" @click="handleUpdateCarouselByButton(onClick, 'prev', disabled)" />
			</template>

			<template #next="{ onClick, disabled }">
				<img
					:class="['arrow', { arrow_disabled: disabled }]"
					src="/images/arrow-next.svg"
					:disabled="disabled"
					@click="handleUpdateCarouselByButton(onClick, 'next', disabled)" />
			</template>
		</UCarousel>

		<div class="tabs-area">
			<p :class="['text']">
				4 пакетных решения. <b><u>Выбирайте</u></b> для себя лучшее:
			</p>
			<div :class="['tabs-container']">
				<div v-for="(item, index) in itemsWithSelected" @click="handleClickTab(index)" :class="['tab', { tab_selected: item.selected }]" :key="index">
					<p :class="['label']">{{ item.label.toUpperCase() }}</p>
					<img :class="['img']" :src="item.img" alt="img" />
					<div :class="['blanket']"></div>
				</div>
			</div>
		</div>

		<div class="info-area">
			<div class="block">
				<div class="info">
					<p class="title">{{ items[currentActiveIndex]?.label }}</p>
					<p class="text">Для ценителей дорогого минималистичного стиля</p>
				</div>
				<div class="to-calculator">
					<p class="text">Стоимость:</p>
					<p class="title">Фикс</p>
					<NuxtLink :to="hrefCalculater" :class="['hover', 'btn', 'btn-calculator']"> Онлайн-калькулятор </NuxtLink>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="postcss">
.box {
	--s: 890px;
	display: grid;
	grid-template-columns: 50% 50%;
	grid-template-rows: var(--s) 290px;
	grid-template-areas: 'text carousel' 'tabs info';
	gap: 30px;
	@media (max-width: 1200px) {
		grid-template-columns: 100%;
		grid-template-rows: auto auto auto auto;
		grid-template-areas: 'text' 'tabs' 'carousel' 'info';
	}
}

.text-area {
	--s: 65px;
	grid-area: text;
	font-size: var(--s);
	font-weight: 600;
	p {
		line-height: 1.2em;
		@media (max-width: 1200px) {
			font-size: 0.5em;
		}
	}
}

.carousel-area {
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

.tabs-area {
	grid-area: tabs;
	align-self: flex-end;
	font-size: 24px;

	.text {
		font-weight: 500;
		margin-bottom: 30px;

		@media (max-width: 1200px) {
			font-size: 0.5em;
		}
	}

	.tabs-container {
		display: flex;
		gap: 30px;

		.tab {
			position: relative;
			border-radius: 20px;
			overflow: hidden;
			width: 125px;
			height: 125px;

			.blanket {
				position: absolute;
				top: 0;
				width: 100%;
				height: 100%;
				background-color: rgba(0, 0, 0, 0.3);
			}

			&_selected {
				.blanket {
					background-color: rgba(249, 175, 21, 0.5);
				}
			}

			.label {
				position: absolute;
				font-size: 0.7em;
				font-weight: 600;
				color: white;
				transform: translate(-50%, -50%);
				top: 50%;
				left: 50%;
				z-index: 2;
			}

			.img {
				height: 100%;
				object-fit: cover;
			}
		}
	}
}

.info-area {
	grid-area: info;
	font-size: 50px;
	width: 100%;
	height: 100%;

	@media (max-width: 1700px) {
		font-size: 40px;
	}
	@media (max-width: 1400px) {
		font-size: 35px;
	}
	.block {
		background-color: #efefef;
		border-radius: 0.7em;
		overflow: hidden;
		width: 100%;
		height: 100%;
		display: flex;
		padding: 0.9em 1.7em;

		.info {
			width: 7em;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			.title {
				font-weight: 600;
			}
			.text {
				font-size: 0.4em;
				color: #818181;
			}
		}
		.to-calculator {
			display: flex;
			flex-direction: column;
			margin-left: auto;
			.text {
				font-size: 0.4em;
			}
			.title {
				font-weight: 600;
			}
			.btn {
				border-radius: 2em;
				padding: 20px;
				font-size: 0.4em;
				color: white;
				text-align: center;
				background-color: var(--c-orange);
				margin-top: auto;

				/* @media (max-width: 1500px) {
					padding: 10px;
					font-size: 16px;
				} */
			}
		}
	}
}
</style>
