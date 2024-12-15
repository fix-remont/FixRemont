<script setup lang="ts">
const { width } = useViewport()
import ArrowHover from '~/components/shared/arrow_hover.vue'
import ToolsImgBlock from '~/components/home/tools_img_block.vue'
import { hrefBecomePartner, hrefCalculater } from '~/assets/css/variables'

let slides = [
	{
		title: 'Ремонт',
		text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
		imgSrc: '/images/home/block1-img1.png',
		hovered: ref(false),
	},
	{
		title: 'Строительство',
		text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
		imgSrc: '/images/home/block1-img1.png',
		hovered: ref(false),
	},
	{
		title: 'Партнёрская программа',
		text: 'Без визитов на объект.Заезжайте в готовую квартире уже через 6-8 месяцев',
		imgSrc: '/images/home/block1-img1.png',
		hovered: ref(false),
	},
]

onMounted(() => {
	slides = slides.map((item) => {
		item.hovered.value = width.value < 640 ? true : false
		return item
	})
})
</script>

<template>
	<div :class="['box', 'margin-glob']">
		<ToolsImgBlock area="first" />
		<div :class="['second']">
			<div :class="['box-buttons']">
				<p>Воплотим вашу мечту в реальность без визитов на объект</p>
				<div :class="['buttons']">
					<NuxtLink :to="hrefCalculater" :class="['hover', 'btn', 'btn-calculator']"> Онлайн-калькулятор </NuxtLink>
					<NuxtLink :to="hrefBecomePartner" :class="['hover', 'btn', 'btn-to-partner']"> Стать партнёром </NuxtLink>
				</div>
			</div>
		</div>
		<div :class="['third']">
			<UCarousel :ui="{ item: 'w-[280px]', container: 'gap-2' }" v-if="width < 1000" v-slot="{ item }" :items="slides">
				<div
					:class="['item', { item__hovered: !item.hovered.value }]"
					@click="() => (item.hovered.value = true)"
					@mouseover="() => (item.hovered.value = true)"
					@mouseout="() => (item.hovered.value = width < 640 ? true : false)">
					<span :class="['title']">{{ item.title }}</span>
					<span :class="['text']">{{ item.text }}</span>
					<img :src="item.imgSrc" alt="img" />
					<div :class="['wrap-arrow']">
						<ArrowHover :hovered="item.hovered.value" />
					</div>
				</div>
			</UCarousel>
			<div v-else :class="['static-slides']">
				<div
					v-for="item of slides"
					:key="item.title"
					:class="['item', { item__hovered: !item.hovered.value }]"
					@click="() => (item.hovered.value = true)"
					@mouseover="() => (item.hovered.value = true)"
					@mouseout="() => (item.hovered.value = false)">
					<span :class="['title']">{{ item.title }}</span>
					<span :class="['text']">{{ item.text }}</span>
					<img :src="item.imgSrc" alt="img" />
					<div :class="['wrap-arrow']">
						<ArrowHover :hovered="item.hovered.value" />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="postcss">
$radius: 35px;

.box {
	display: grid;
	gap: 20px;
	grid-template-columns: auto 890px;
	grid-template-rows: 550px auto;
	grid-template-areas: 'first second' 'first third';

	@media (max-width: 1500px) {
		display: flex;
		flex-direction: column;
		gap: 15px;
	}
}

.second {
	grid-area: second;

	.box-buttons {
		width: 890px;
		border-radius: $radius;
		background-color: var(--c-black);
		height: 100%;
		padding: 45px;
		color: white;
		font-size: 32px;
		font-weight: 500;
		line-height: 42px;
		display: flex;
		flex-direction: column;
		justify-content: space-between;

		@media (max-width: 1500px) {
			width: 100%;
			padding: 25px;
		}

		p {
			width: 300px;

			@media (max-width: 1500px) {
				width: 100%;
				font-size: 20px;
				margin-bottom: 30px;
			}

			@media (max-width: 800px) {
				line-height: 16px;
				font-size: 16px;
			}
		}

		.buttons {
			display: grid;
			grid-template-columns: repeat(2, 1fr);
			gap: 20px;

			@media (max-width: 600px) {
				grid-template-columns: auto;
				grid-template-rows: auto auto;
				font-size: 16px;
			}

			.btn {
				border-radius: 60px;
				padding: 20px;
				flex-grow: 1;
				border: 2px solid var(--c-orange);
				font-size: 20px;
				text-align: center;

				@media (max-width: 1500px) {
					padding: 10px;
					font-size: 16px;
				}
			}

			.btn-calculator {
				background-color: var(--c-orange);
			}

			.btn-to-partner {
				border-color: white;
			}
		}
	}
}

.third {
	grid-area: third;

	.static-slides {
		width: 890px;
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 20px;
		height: 100%;
		flex-grow: 1;

		@media (max-width: 1500px) {
			width: 100%;
			gap: 0;
			display: flex;
			justify-content: space-between;
		}
	}

	.item {
		position: relative;
		display: flex;
		flex-direction: column;
		color: white;
		border-radius: 35px;
		overflow: hidden;
		background: none;
		transition: all 1s linear;

		@media (max-width: 1500px) {
			width: 280px;
		}

		/* @media (max-width: 1000px) {
			width: initial;
		} */

		.title {
			font-weight: 500;
			font-size: 24px;
			margin: 25px 0 10px 25px;
			line-height: 32px;
			transition: all 1s linear;
		}

		.text {
			width: 180px;
			font-size: 16px;
			font-weight: 400;
			margin-left: 25px;
			color: white;
		}

		img {
			position: absolute;
			z-index: -1;
			width: 100%;
			height: 100%;
		}

		.wrap-arrow {
			position: absolute;
			right: 25px;
			bottom: 25px;
		}
	}

	.item__hovered {
		background-color: #efefef;

		.title {
			color: var(--c-black);
		}

		.text {
			color: #efefef;
		}
	}
}
</style>
