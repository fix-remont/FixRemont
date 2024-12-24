<script setup>
import { hrefInstagram, hrefPhone, hrefTg, hrefVkontakte, hrefWatsapp, hrefYoutube, labelPhone } from '~/assets/variables'

const icons1 = [
	{ src: 'watsapp.svg', href: hrefWatsapp },
	{ src: 'telegram.svg', href: hrefTg },
]

const icons2 = [
	{ src: 'youtube.svg', href: hrefYoutube },
	{ src: 'vkontakte.svg', href: hrefVkontakte },
	{ src: 'instagram.svg', href: hrefInstagram },
]
</script>
<template>
	<div class="margin-glob">
		<h1 class="title title-glob">Контакты FIX-ремонт</h1>
		<iframe
			src="https://yandex.ru/map-widget/v1/?um=constructor%3A72d03be55b62e186e1ab7ca478e690eb280706cfaf9597d3ac28019589c3df47&amp;source=constructor"
			class="yandex border-glob"
			title="Map"></iframe>
		<div class="footer">
			<div class="box1">
				<p class="working-mode">Звоните Пн-Вс: 8:30 - 19:00</p>
				<a class="phone hover" :href="hrefPhone">{{ labelPhone }}</a>
			</div>
			<div class="box2">
				<span class="text">Напишите нам, мы онлайн:</span>
				<div class="icons">
					<a v-for="icon in icons1" :href="icon.href">
						<img :src="`/icons/${icon.src}`" :class="['hover', 'icon']" :alt="icon.src" />
					</a>
				</div>
			</div>
			<div class="box3">
				<span class="text">Мы в соц. сетях:</span>
				<div class="icons">
					<a v-for="icon in icons2" :href="icon.href">
						<img :src="`/icons/${icon.src}`" :class="['hover', 'icon']" :alt="icon.src" />
					</a>
				</div>
			</div>
			<SharedButton class="button">Реквизиты для юр. лиц</SharedButton>
		</div>
	</div>
</template>
<style scoped>
.yandex {
	width: 100%;
	height: 500px;
	margin-bottom: 30px;
}

.title {
	margin-bottom: 30px;
}
.footer {
	display: grid;
	justify-content: space-between;
	align-items: center;
	/* flex-wrap: wrap; */
	grid-template-columns: repeat(4, auto);
	gap: 20px;
	grid-template-areas: 'box1 box2 box3 button';
	@media (max-width: 1150px) {
		grid-template-columns: repeat(2, 1fr);
		grid-template-areas: 'box1 box2' 'box3 button';
	}
	@media (max-width: 640px) {
		grid-template-columns: repeat(1, 100%);
		grid-template-areas: 'box1' 'box2' 'box3' 'button';
	}

	.box1 {
		grid-area: box1;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 10px;
		.working-mode {
			font-size: 16px;
			font-weight: 500;
		}
		.phone {
			font-size: 32px;
			font-weight: 700;
			@media (max-width: 750px) {
				font-size: 18px;
			}
		}
	}
	.box2 {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 10px;
		grid-area: box2;

		.text {
			font-size: 16px;
			font-weight: 500;
		}
		.icons {
			display: flex;
			gap: 10px;
			justify-content: center;
		}
	}
	.box3 {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 10px;
		grid-area: box3;

		.text {
			font-size: 16px;
			font-weight: 500;
		}
		.icons {
			display: flex;
			gap: 10px;
			justify-content: center;
		}
	}
	.icon {
		width: 40px;
	}
	.button {
		grid-area: button;

		/* width: 500px; */
		/* min-width: max-content;
		max-width: auto; */
		/* @media (max-width: 1400px) {
			width: 100%;
		} */
	}
}
</style>
