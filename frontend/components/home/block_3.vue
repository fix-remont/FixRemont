<script setup>
import { ref } from 'vue'
import { hrefCalculater } from '~/assets/variables'

const items = [
	{ label: 'Базовый', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Стандарт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Комфорт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Бизнес', img: '/images/home/package-comfort.png', selected: false },
]

const carouselRef1 = ref(null)
const carouselRef2 = ref(null)
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
	carouselRef1.value.select(tabIndex + 1)
	carouselRef2.value.select(tabIndex + 1)
}

watch(
	() => carouselRef1.value?.page,
	(newPage) => (currentActiveIndex.value = newPage - 1)
)
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
			ref="carouselRef1"
			:items="items"
			class="carousel-area"
			:ui="{ item: 'w-full h-full rounded-xl sm:rounded-3xl overflow-hidden', container: 'gap-2 relative h-full', arrows: { wrapper: 'absolute bottom-0' } }"
			arrows>
			<template #default="{ item }">
				<img class="slide" :src="item.img" draggable="false" />
			</template>

			<template #prev="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', { arrow_disabled: disabled }]"
					src="/images/arrow-prev.svg"
					@click="handleUpdateCarouselByButton(onClick, 'prev', disabled)" />
			</template>

			<template #next="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', { arrow_disabled: disabled }]"
					src="/images/arrow-next.svg"
					:disabled="disabled"
					@click="handleUpdateCarouselByButton(onClick, 'next', disabled)" />
			</template>
		</UCarousel>

		<div class="tabs-area">
			<p :class="['text']">
				4 пакетных решения. <b><u>Выбирайте</u></b> для себя лучшее:
			</p>
			<UCarousel
				ref="carouselRef2"
				:items="itemsWithSelected"
				class="tabs-container"
				:ui="{
					container: 'gap-2',
					item: ['w-16 sm:w-32', 'h-16 sm:h-32', 'rounded-lg sm:rounded-3xl', ' overflow-hidden relative cursor-pointer hover:opacity-90'],
				}">
				<template #default="{ item, index }">
					<div @click="handleClickTab(index)" class="h-full">
						<p :class="['label']">{{ item.label.toUpperCase() }}</p>
						<img :class="['img']" :src="item.img" alt="img" />
						<div :class="['blanket', { blanket_selected: item.selected }]"></div>
					</div>
				</template>
			</UCarousel>
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

<style scoped>
.box {
	display: grid;
	grid-template-columns: 50% 50%;
	grid-template-rows: 500px 290px;
	grid-template-areas: 'text carousel' 'tabs info';
	gap: 30px;

	@media (max-width: 1200px) {
		grid-template-columns: 100%;
		grid-template-rows: auto auto auto auto;
		grid-template-areas: 'text' 'tabs' 'carousel' 'info';
	}
}

.text-area {
	grid-area: text;
	font-size: 65px;
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

	.blanket {
		position: absolute;
		top: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.3);

		&_selected {
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

		@media (max-width: 640px) {
			font-size: 10px;
		}
	}

	.img {
		height: 100%;
		object-fit: cover;
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

		@media (max-width: 640px) {
			flex-direction: column;
			padding: 0.4em 0.8em;
		}

		.info {
			width: 7em;
			display: flex;
			flex-direction: column;
			justify-content: space-between;

			.title {
				font-weight: 600;

				@media (max-width: 640px) {
					font-size: 24px;
				}
			}

			.text {
				font-size: 0.4em;
				color: #818181;
				font-weight: 600;

				@media (max-width: 640px) {
					font-size: 14px;
				}
			}
		}

		.to-calculator {
			display: flex;
			flex-direction: column;
			margin-left: auto;

			@media (max-width: 640px) {
				margin-left: initial;
			}

			.text {
				font-size: 0.4em;

				@media (max-width: 640px) {
					font-size: 14px;
				}
			}

			.title {
				font-weight: 600;

				@media (max-width: 640px) {
					font-size: 24px;
				}
			}

			.btn {
				border-radius: 2em;
				padding: 20px;
				font-size: 0.4em;
				color: white;
				text-align: center;
				background-color: var(--c-orange);
				margin-top: auto;

				@media (max-width: 640px) {
					font-size: 12px;
				}
			}
		}
	}
}
</style>
