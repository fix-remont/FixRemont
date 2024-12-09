<script setup>
import { ref } from 'vue'

const items = [
	{ label: 'Базовый', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Стандарт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Комфорт', img: '/images/home/package-comfort.png', selected: false },
	{ label: 'Бизнес', img: '/images/home/package-comfort.png', selected: false },
]

const carousel = ref(null)
const currentActiveIndex = ref(0)

const itemsWithSelected = computed(() => {
	return items.map((item, index) => {
		item.selected = index === currentActiveIndex.value
		return item
	}

	)
})
const handleUpdateCarousel = (onClick, actionType, disabled) => {
	if (disabled) return
	onClick()
	const pagePrev = carousel.value.page

	if (actionType == 'next')
		currentActiveIndex.value = pagePrev
	else if (actionType == 'prev')
		currentActiveIndex.value = pagePrev - 2

}

const handleClickTab = (tabIndex) => {
	currentActiveIndex.value = tabIndex
	carousel.value.select(tabIndex + 1)
}
// function goToSlide(slideNumber) {
// 	carousel.value.select(slideNumber)
// }
</script>

<template>
	<div :class="['margin-glob', 'box']">
		<div class="text-area">
			<p>
				Занимайтесь
				<span class="orange">любимыми</span> делами,
				а ремонт мы
				возьмём на себя.
			</p>
		</div>

		<UCarousel ref="carousel" :items="items" class="carousel-area"
			:ui="{ item: 'w-full h-full rounded-3xl overflow-hidden', container: 'gap-2 relative h-full', arrows: { wrapper: 'absolute bottom-0' } }"
			arrows>
			<template #default="{ item }">
				<img class="slide" :src="item.img" draggable="false" />
			</template>

			<template #prev="{ onClick, disabled }">
				<img :class="['arrow', { arrow_disabled: disabled }]" src="/images/arrow-prev.svg"
					@click="handleUpdateCarousel(onClick, 'prev', disabled)" />
			</template>

			<template #next="{ onClick, disabled }">
				<img :class="['arrow', { arrow_disabled: disabled }]" src="/images/arrow-next.svg" :disabled="disabled"
					@click="handleUpdateCarousel(onClick, 'next', disabled)" />
			</template>
		</UCarousel>

		<div class="tabs-area">
			<p :class="['text']">4 пакетных решения. <b><u>Выбирайте</u></b> для себя лучшее:</p>
			<div :class="['tabs-container']">

				<div v-for="(item, index) in itemsWithSelected" @click="handleClickTab(index)"
					:class="['tab', { tab_selected: item.selected }]" :key="index">
					<p :class="['label']">{{ item.label.toUpperCase() }}</p>
					<img :class="['img']" :src="item.img" alt="img">
					<div :class="['blanket']"></div>
				</div>
			</div>
		</div>

		<div class="info-area"></div>
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

.text-area {
	grid-area: text;
	font-size: 65px;
	font-weight: 600;
	line-height: 80px;
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

	.text {
		font-size: 24px;
		font-weight: 500;
		margin-bottom: 30px;
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
				font-size: 16px;
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
	background-color: #EFEFEF;
	border-radius: 35px;
	width: 100%;
	height: 100%;
}
</style>
