<script setup lang="ts">
defineProps<{
	area: string
}>()
const imagePath = '/images/home/tools.png'
</script>

<template>
	<div :class="[area]">
		<img :src="imagePath" alt="tools" />
		<p>Первый в России онлайн-сервис по ремонту и строительству с фиксированной стоимостью</p>
	</div>
</template>

<style scoped>
$radius: 35px;

.first {
	grid-area: first;
	flex-grow: 1;
	position: relative;
	height: 785px;
	display: flex;
	border-radius: $radius;
	overflow: hidden;
	@media (max-width: 1500px) {
		height: 290px;
		background-color: #f9af15;
	}
	@media (max-width: 640px) {
		height: 245px;
		overflow: visible;
	}
	img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: right center;
		@media (max-width: 1500px) {
			width: auto;
			border-radius: $radius;
			margin-left: auto;
		}
		@media (max-width: 640px) {
			height: 245px;
		}
	}
	p {
		position: absolute;
		bottom: 75px;
		left: 75px;

		line-height: 60px;
		font-size: 45px;
		font-weight: 500;
		color: white;
		width: 400px;

		@media (max-width: 1840px) {
			font-size: 40px;
			width: 350px;
		}
		@media (max-width: 1500px) {
			font-size: 30px;
			width: 60%;
			bottom: 35px;
		}
		@media (max-width: 1000px) {
			font-size: 24px;
			width: 41vw;
			line-height: 19px;
			bottom: 26px;
			left: 26px;
		}
		@media (max-width: 1000px) {
			font-size: 16px;
		}
	}
}
</style>
