<script setup lang="ts">
import { hrefLogo, hrefTg, hrefWatsapp, hrefPhone, labelPhone } from '~/assets/css/contacts'
</script>

<template>
	<footer :class="['footer']">
		<NuxtLink :to="hrefLogo">
			<img src="/icons/logo-for-black.svg" :class="['hover', 'logo']" alt="logo" />
		</NuxtLink>

		<p class="low-lvl-info">Первый онлайн-сервис по ремонту и строительству <span style="font-weight: 800">с фикс стоимостью</span></p>

		<p style="text-align: center">Copyright 2024. Все права защищены</p>

		<p :class="['politic', 'hover']">Политика конфиденциальности</p>

		<address class="social">
			<p class="text">
				Напишите нам,<br />
				мы сейчас онлайн
			</p>
			<a :href="hrefWatsapp">
				<img src="/icons/watsapp.svg" :class="['hover', 'icon']" alt="watsapp" />
			</a>
			<a :href="hrefTg">
				<img src="/icons/telegram.svg" :class="['hover', 'icon']" alt="watsapp" />
			</a>
		</address>

		<div class="working-mode">
			<img src="/icons/clock.svg" :class="['icon']" alt="phone" />
			<p>Звоните Пн-Вс: 8:30 - 19:00</p>
		</div>

		<div class="phone">
			<img src="/icons/phone.svg" :class="['icon']" alt="phone" />
			<a :class="['hover']" :href="hrefPhone">{{ labelPhone }}</a>
		</div>
	</footer>
</template>

<style scoped>
.footer {
	margin-top: auto;
	color: white;
	background-color: var(--c-black);
	display: grid;
	grid-template-columns: repeat(7, auto);
	justify-content: space-between;
	align-items: center;
	padding: 50px;
	border-radius: 25px 25px 0 0;

	@media (max-width: 1740px) {
		display: flex;
		flex-wrap: wrap;
		row-gap: 30px;
		column-gap: 80px;
		justify-content: center;
		/* grid-template-columns: repeat(4, auto);
		grid-template-rows: repeat(2, auto); */
	}
}

.low-lvl-info {
	font-weight: 500;
	width: 215px;
	line-height: 18px;
}

.politic {
	color: #f9af15;
	text-decoration: underline;
}
.social {
	display: flex;
	align-items: center;
	/* justify-content: space-between; */
	gap: 10px;
	padding-left: 20px;
	font-weight: 500;
	font-size: 14px;

	.text {
		text-decoration: none;
		font-style: normal;
		position: relative;

		&::before {
			content: '';
			width: 5px;
			height: 5px;
			border-radius: 50%;
			background-color: #43c460;
			position: absolute;
			left: -13px;
			top: 20px;
		}
	}

	.icon {
		width: 40px;
		height: 40px;
	}
}

.working-mode {
	display: flex;
	gap: 8px;
	font-weight: 500;
	font-size: 15px;
	align-items: center;
}

.icon {
	width: 17px;
	height: 17px;
}

.phone {
	font-size: 17px;
	display: flex;
	align-items: center;
	gap: 8px;
	font-weight: 500;
}
</style>
