<script setup lang="ts">
const cards = [
	{ text: 'Без визитов на объект', iconSrc: '/icons/home_1.svg' },
	{ text: '100% гарантия фиксированной сметы', iconSrc: '/icons/home_2.svg' },
	{ text: 'Все финансовые риски берём на себя', iconSrc: '/icons/home_3.svg' },
	{ text: '36 готовых дизайн-проектов', iconSrc: '/icons/home_4.svg' },
	{ text: 'Все берем на себя и работаем под ключ', iconSrc: '/icons/home_5.svg' },
]
</script>

<template>
	<UCarousel v-slot="{ item }" :items="cards" :class="['margin-glob', 'box']" :ui="{ container: 'gap-3' }">
		<div class="item">
			<p>{{ item.text }}</p>
			<img :src="item.iconSrc" alt="icon" />
		</div>
	</UCarousel>
</template>

<style scoped>
.item {
	width: 347px;
	height: 185px;
	background-color: white;
	border-radius: 35px;
	font-size: 18px;
	font-weight: 500;
	padding: 30px 24px;
	display: flex;
	justify-content: space-between;
	@media (max-width: 640px) {
		width: 155px;
		height: 80px;
		border-radius: 15px;
		padding: 15px;
	}

	p {
		align-self: flex-end;
		@media (max-width: 640px) {
			font-size: 10px;
		}
	}

	img {
		justify-self: flex-start;
		width: 30px;
		height: 30px;
		@media (max-width: 640px) {
			width: 14px;
			height: 14px;
		}
	}
}
</style>
