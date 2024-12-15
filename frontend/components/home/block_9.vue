<script setup>
const img = '/images/home/block_9.png'

const items = [
	{ text: 'Выбор опции', time: '1 мин', img, selected: false },
	{ text: 'Выбор подходящего тарифа', time: '30 мин', img, selected: false },
	{ text: 'Удобный выбор планировки и материала', time: '60 мин', img, selected: false },
	{ text: 'Проведение работ сервисом FIX-ремонт', time: '', img, selected: false },
	{ text: 'Получите — распишитесь!:)', time: '', img, selected: false },
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
				<div
					v-for="(item, index) in itemsWithSelected"
					:class="['tab-container', { 'tab-container__selected': index == currentActiveIndex }]"
					@click="currentActiveIndex = index">
					<div class="card">
						<div class="text">{{ item.text }}</div>
						<div class="time">{{ item.time }}</div>
					</div>
				</div>
			</div>
		</div>
		<div class="block_2">
			<img :src="items[currentActiveIndex].img" alt="img" />
			<div class="text">Выбирайте подходящий тариф под ваш бюджет. Цена фиксированная!</div>
		</div>
	</div>
</template>

<style scoped>
.wrapper {
	padding: 80px;
	background-color: var(--c-black);
	width: 100%;
	border-radius: 35px;
	display: flex;
	font-size: 10px;
	gap: 30px;
	color: white;
	@media (max-width: 1400px) {
		flex-direction: column;
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
				.text {
				}
				.time {
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

	img {
		width: 100%;
	}
	.text {
		font-size: 3.2em;
		font-weight: 500;
	}
}
</style>
