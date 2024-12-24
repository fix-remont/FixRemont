<script setup lang="ts">
import { hrefCalculater } from '~/assets/variables'

const infoCheckboxes = [
	'Цены уже рассчитаны, а материалы подобраны и закуплены',
	'Даём юридическую гарантию сроков и качества',
	'Независимый Технадзор и тройной контроль',
	'Все бригады работают по единому регламенту',
	'Следите за ходом работ в режиме онлайн',
	'От вас не потребуется никаких визитов',
]
</script>

<template>
	<div :class="['box', 'margin-glob']">
		<div class="info">
			<div class="credit-card-block">
				<p class="title">Берём все финансовые риски на себя</p>
				<span class="text"
					>В случае брака, дефектов или оплошностей мастеров.<br /><br />Устраним все проблемы и решим вопросы как с соседями, так и с
					управляющейкомпанией.</span
				>
				<img class="credit-card-img" src="/images/home/credit-card.png" alt="credit-card" />
			</div>

			<div class="checkboxes-block">
				<div class="item" v-for="text in infoCheckboxes">
					<img class="checkbox" src="/images/home/checkbox_checked.svg" alt="checkbox" />
					<span class="text">{{ text }}</span>
				</div>
			</div>
		</div>

		<div class="to-calculator-block">
			<h1 class="title">Стоимость для вас <span class="orange">не изменится,</span> даже при взлёте цен на материалы</h1>
			<p class="text">Мы всё предусмотрели: материалы закуплены заранее, а бригады готовы выехать на объект в любой момент.</p>
			<NuxtLink :to="hrefCalculater" :class="['hover', 'button']">Расчитать стоимость</NuxtLink>
			<img class="tassel-img" src="/images/home/tassel.png" alt="tassel" />
		</div>
	</div>
</template>

<style scoped>
.box {
	display: flex;
	gap: 20px;
	font-size: 10px;
	@media (max-width: 1200px) {
		flex-direction: column;
	}
	@media (max-width: 800px) {
		font-size: 8px;
	}
	@media (max-width: 640px) {
		font-size: 6px;
	}
}

.info {
	width: 50%;
	@media (max-width: 1200px) {
		width: auto;
	}
	font-size: 1em;
	display: flex;
	flex-direction: column;
	gap: 3em;

	.credit-card-block {
		color: white;
		border-radius: 3.5em;
		padding: 8em 20% 8em 5em;
		background-color: var(--c-orange);
		position: relative;
		display: flex;
		flex-direction: column;
		gap: 2em;
		@media (max-width: 640px) {
			padding: 8em 5em 40em 5em;
		}
		.title {
			font-size: 6.5em;
			line-height: 1.1em;
			font-weight: 600;
			z-index: 1;
		}
		.text {
			font-weight: 500;
			font-size: 2em;
			z-index: 1;
		}
		.credit-card-img {
			position: absolute;
			right: 0;
			z-index: 0;
			@media (max-width: 640px) {
				width: 276px;
				bottom: -4em;
			}
		}
	}

	.checkboxes-block {
		padding: 3.3em 5em;
		display: flex;
		flex-wrap: wrap;
		font-size: 10px;
		background-color: white;
		border-radius: 3em;
		justify-content: space-between;
		gap: 2em;
		.item {
			width: 25em;
			@media (max-width: 640px) {
				width: auto;
			}
			display: flex;
			align-items: center;
			gap: 2em;
			.checkbox {
				width: 25px;
			}
			.text {
				font-size: 1.6em;
				color: #808080;
			}
		}
	}
}

.to-calculator-block {
	width: 50%;
	@media (max-width: 1200px) {
		width: auto;
	}
	display: flex;
	flex-direction: column;
	gap: 2em;
	border-radius: 3em;
	border: 0.2em solid var(--c-black);
	padding: 8em 5em;
	position: relative;
	overflow: hidden;
	font-size: 1em;
	@media (max-width: 640px) {
		padding: 3em;
	}
	.title {
		font-size: 6.5em;
		font-weight: 600;
		line-height: 1.1em;
		z-index: 1;
		@media (max-width: 640px) {
			font-size: 5em;
		}
	}
	.text {
		font-size: 2em;
		color: #808080;
		z-index: 1;
		width: 70%;
		@media (max-width: 640px) {
			width: initial;
		}
	}
	.button {
		border-radius: 20em;
		padding: 20px;
		font-size: 2em;
		color: white;
		text-align: center;
		font-weight: 600;
		background-color: var(--c-orange);
		margin-top: auto;
		width: 50%;
		min-width: 270px;
		@media (max-width: 640px) {
			width: auto;
			min-width: 0;
		}

		@media (max-width: 640px) {
			font-size: 12px;
		}
	}
	.tassel-img {
		position: absolute;
		bottom: -234px;
		right: 38px;
		z-index: 0;
		@media (max-width: 640px) {
			display: none;
		}
	}
}
</style>
