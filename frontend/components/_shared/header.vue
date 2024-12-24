<script setup lang="ts">
import { hrefLogo, hrefTg, hrefWatsapp, hrefPhone, labelPhone } from '~/assets/variables'
</script>

<template>
	<header :class="['box', 'margin-glob']">
		<div class="left-part">
			<NuxtLink :to="hrefLogo">
				<img src="/icons/logo-for-white.svg" :class="['hover', 'logo']" alt="logo" />
			</NuxtLink>

			<div :class="['divider', 'divider_1']"></div>

			<p class="low-lvl-info">Первый онлайн-сервис по ремонту и строительству <span style="font-weight: 800">с фикс стоимостью</span></p>

			<div :class="['divider', 'divider_2']"></div>

			<div class="working-mode">
				<img src="/icons/clock.svg" :class="['icon']" alt="phone" />
				<p>Звоните Пн-Вс: 8:30 - 19:00</p>
			</div>

			<div :class="['divider', 'divider_3']"></div>

			<div class="phone">
				<img src="/icons/phone.svg" :class="['icon']" alt="phone" />
				<a :href="hrefPhone">{{ labelPhone }}</a>
			</div>
		</div>

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

		<div :class="['profile', 'hover']">
			<p class="red">Личный кабинет</p>
			<img src="/icons/profile.svg" alt="profile" />
		</div>

		<SharedHeaderLinks />
	</header>
</template>

<style scoped>
@define-mixin border-radius {
	border-radius: 20px;

	@media (max-width: 640px) {
		border-radius: 15px;
	}
}

.box {
	height: 80px;
	display: flex;
	gap: 20px;
	justify-content: space-between;
	margin-top: 30px;
	margin-bottom: 30px;
	@media (max-width: 640px) {
		height: 52px;
		gap: 10px;
	}
}

.left-part {
	display: flex;
	justify-content: space-evenly;
	flex-grow: 1;
	align-items: center;
	background-color: white;
	@mixin border-radius;

	@media (max-width: 1240px) {
		flex-grow: unset;
		padding: 0 30px;
	}

	@media (max-width: 480px) {
		padding: 0 10px;
	}

	.divider {
		height: 60%;
		border-left: dashed 2px #e3e3e3;
	}

	.divider_1 {
		@media (max-width: 1700px) {
			display: none;
		}
	}

	.divider_2 {
		@media (max-width: 1500px) {
			display: none;
		}
	}

	.divider_3 {
		@media (max-width: 1240px) {
			display: none;
		}
	}

	.low-lvl-info {
		font-weight: 500;
		width: 215px;
		line-height: 18px;

		@media (max-width: 1700px) {
			display: none;
		}
	}

	.logo {
		width: 110px;
		height: 45px;

		@media (max-width: 640px) {
			min-width: 73px;
		}
	}

	.working-mode {
		display: flex;
		gap: 8px;
		font-weight: 500;
		font-size: 15px;
		align-items: center;

		@media (max-width: 1500px) {
			display: none;
		}
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

		@media (max-width: 1240px) {
			display: none;
		}
	}
}

.social {
	@mixin border-radius;
	width: 300px;
	display: flex;
	align-items: center;
	justify-content: space-between;
	background-color: white;
	padding-left: 40px;
	padding-right: 30px;
	font-weight: 500;
	font-size: 14px;
	width: 300px;

	@media (max-width: 1240px) {
		flex-grow: 1;
		justify-content: space-evenly;
	}

	@media (max-width: 950px) {
		display: none;
	}

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

.profile {
	@mixin border-radius;
	width: 260px;
	padding: 0 28px;
	font-weight: 600;
	color: white;
	background-color: var(--c-black);
	font-size: 16px;
	display: flex;
	align-items: center;
	justify-content: space-between;

	@media (max-width: 1240px) {
		flex-grow: 1;
	}

	@media (max-width: 480px) {
		padding: 0;
	}

	img {
		@media (max-width: 640px) {
			width: 18px;
		}

		@media (max-width: 480px) {
			display: none;
		}
	}

	p {
		@media (max-width: 480px) {
			margin-left: auto;
			margin-right: auto;
			font-size: 10px;
		}
	}
}
</style>
