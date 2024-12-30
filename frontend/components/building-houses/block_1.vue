<script setup lang="ts">
import { useViewport } from '~/composables/viewport'
import Bread_crumbs from '~/components/_shared/bread_crumbs.vue'
import { hrefCalculater } from '~/assets/variables'

const { width } = useViewport()

</script>

<template>
	<div class="margin-glob block">
		<div class="upper">
			<img src="/images/building-houses/block_1.png" alt="background" />
			<div class="crumb-container">
				<Bread_crumbs />
			</div>
			<div class="content">
				<h1 class="title-glob header">
					Строительство домов
					<br />
					под ключ по готовым
					<br />
					проектам и с
					<br />
					фиксированной ценой
				</h1>
			</div>
			<div class="box-wrapper">
				<div class="black-box">
					<h2>
						6 месяцев до
						<br />
						готового дома мечты
						<br />
						с благоустройством
						<br />
						и ремонтом
					</h2>
					<NuxtLink :to="hrefCalculater">
						<SharedButton fillOrange> Онлайн-калькулятор </SharedButton>
					</NuxtLink>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="postcss">
$radius: 35px;
.upper {
	position: relative;
}

.content {
	position: absolute;
	bottom: 0;
	margin-bottom: 5%;
	left: 100px;
}

.header {
	font-size: 50px;
	font-weight: 600;
	color: white;
	line-height: 70px;
	letter-spacing: 0.1px;
	@media (max-width: 1500px) {
		font-size: 40px;
	}
}

.box-wrapper {
	position: absolute;
	bottom: 0;
	right: 0;
	background-color: white;
	padding-left: 20px;
	padding-top: 20px;
	border-radius: 20px 0 0;

	&::before,
	&::after {
		content: '';
		position: absolute;
		width: 40px;
		height: 40px;
		border-radius: 50%;
		box-shadow: 15px 15px white;
	}
	&::before {
		bottom: 0;
		left: -40px;
	}
	&::after {
		right: 0;
		top: -40px;
	}
}

.black-box {
	background-color: #161616;
	padding: 50px;
	border-radius: $radius;
	color: white;
	width: 35em;
	h2 {
		font-size: 25px;
		font-weight: 500;
		line-height: 40px;
		margin-bottom: 100px;
		@media (max-width: 1500px) {
			font-size: 30px;
		}
	}
}

.crumb-container {
	position: absolute;
	display: inline-block;
	top: 0;
	left: 0;
	padding: 20px;
	z-index: 1;
}
</style>
