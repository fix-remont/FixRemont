<script setup>
const img = '/images/home/block_9.png'

const items = [
	{ label: 'Выбор опции', time: '1 мин', img, selected: false, text: '1 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!' },
	{ label: 'Выбор подходящего тарифа', time: '30 мин', img, selected: false, text: '2 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!' },
	{ label: 'Удобный выбор планировки и материала', time: '60 мин', img, selected: false, text: '3 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!' },
	{ label: 'Проведение работ сервисом FIX-ремонт', time: '', img, selected: false, text: '4 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!' },
	{ label: 'Получите — распишитесь!:)', time: '', img, selected: false, text: '5 Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!' },
]

const currentActiveIndex = ref(0)

const itemsWithSelected = computed(() => {
	return items.map((item, index) => {
		item.selected = index === currentActiveIndex.value
		return item
	})
})
</script>

<template>
	<div class="wrapper margin-glob">
		<div class="block_1">
			<div class="texts">
				<div class="title">Всего <span class="orange">4 шага и 1.5 часа</span> личного времени</div>
				<div class="text">отделяют вас от дома своей мечты</div>
			</div>
			<div class="tabs">
				<div v-for="(item, index) in itemsWithSelected"
					:class="['tab-container', { 'tab-container__selected': index == currentActiveIndex }]"
					@click="currentActiveIndex = index">
					<div class="card">
						<div class="label">{{ item.label }}</div>
						<div class="time">{{ item.time }}</div>
					</div>
					<div :class="currentActiveIndex == index ? 'sm_block_2__selected' : 'sm_block_2__not_selected'">
						<img class="img" :src="items[currentActiveIndex].img" alt="img" />
						<div class="text">{{ items[currentActiveIndex].text }}</div>
					</div>

				</div>
			</div>
		</div>
		<div class="block_2">
			<img :src="items[currentActiveIndex].img" alt="img" />
			<div class="text">{{ items[currentActiveIndex].text }}</div>
		</div>
	</div>
</template>

<style scoped>
.wrapper {
	padding: 80px;
	background-color: var(--c-black);
	/* width: 100%; */
	border-radius: 35px;
	display: flex;
	font-size: 10px;
	gap: 30px;
	color: white;

	@media (max-width: 1400px) {
		flex-direction: column;
	}

	@media (max-width: 640px) {
		font-size: 5px;
		padding: 14px;
		border-radius: 10px;

	}
}

.block_1 {
	font-size: 1em;
	width: 50%;

	@media (max-width: 1400px) {
		width: 100%;
	}

	.texts {
		font-size: 1em;

		.title {
			font-size: 6.5em;
			line-height: 1.2em;
			font-weight: 600;
			margin-bottom: 30px;
		}

		.text {
			font-size: 2em;
			font-weight: 500;
			margin-bottom: 30px;

			@media (max-width: 640px) {
				font-size: 14px;
			}
		}
	}

	.tabs {
		display: flex;
		flex-direction: column;
		gap: 15px;

		.tab-container {
			.card {
				color: #6b6b6b;
				border: #6b6b6b solid 1px;
				border-radius: 20px;
				padding: 35px;
				display: flex;
				justify-content: space-between;
				font-size: 20px;

				@media (max-width: 640px) {
					font-size: 8px;
					padding: 14px;
					border-radius: 10px;

				}

				.label {
					font-weight: 700;
				}

				.time {
					color: #6b6b6b;

				}
			}

			&__selected {
				.card {
					background-color: #ffffff;
					color: var(--c-black);
				}
			}
		}
	}
}

.block_2 {
	font-size: 1em;
	width: 50%;
	display: flex;
	flex-direction: column;
	gap: 30px;


	@media (max-width: 1400px) {
		width: 100%;
	}

	@media (max-width:640px) {
		display: none;
	}

	img {
		width: 100%;
	}

	.text {
		font-size: 3.2em;
		font-weight: 500;
	}
}

.sm_block_2__not_selected {
	display: none;
}

.sm_block_2__selected {
	display: none;

	@media (max-width:640px) {
		display: block;
		font-weight: 500;
		font-size: 12px;
		display: flex;
		flex-direction: column;
		gap: 10px;
		margin-top: 10px;
		margin-bottom: 10px;
	}
}
</style>
