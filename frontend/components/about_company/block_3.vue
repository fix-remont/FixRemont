<script setup lang="ts"></script>
<template>
	<div class="block margin-glob">
		<div class="box">
			<h1 class="title">Работаем с клиентами по всей территории Российской Федерации</h1>

			<p class="text">Несколько бригад в каждом регионе страны</p>
		</div>
		<img class="img" src="/images/about_company/block_3-map.svg" alt="map" />
	</div>
</template>

<style scoped>
.block {
	position: relative;
	.box {
		position: absolute;
		top: 0;
		width: 70%;
		font-size: 10px;
		@media (max-width: 1680px) {
			font-size: 8px;
		}
		@media (max-width: 1680px) {
			font-size: 6px;
		}
		@media (max-width: 1050px) {
			font-size: 4px;
		}
		@media (max-width: 700px) {
			position: static;
			width: 100%;
		}
		.title {
			font-size: 6em;
			font-weight: 600;
			line-height: 1.2em;
		}
		.text {
			font-size: 2em;
			font-weight: 500;
		}
	}
}
</style>
