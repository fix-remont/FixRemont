<script setup lang="ts">
const subTitle =
	'Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet. Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.'

const items = [
	'Amet minim mollit non deserunt ullamco est sit aliqua dolor',
	'do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet. Amet minim mollit non deserunt ullamco est sit aliqua dolor ',
	'do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.',
]

const isOpened = ref(false)
</script>

<template>
	<div class="block margin-glob">
		<h1 class="title">Текст, который важен для SEO</h1>
		<div :class="['texts', { 'texts-opened': isOpened }]">
			<div class="blanket"></div>
			<p class="sub-title">{{ subTitle }}</p>
			<ul class="list list-disc">
				<li class="item" v-for="(item, index) in items" :key="index">{{ item }}</li>
			</ul>
		</div>
		<div class="toggle" @click="isOpened = !isOpened">
			<span>Раскрыть полностью</span>
			<img :class="['arrow', { 'arrow-opened': isOpened }]" src="/arrow-down.svg" alt="arrow" />
		</div>
	</div>
</template>

<style scoped>
.block {
}

.title {
	font-size: 36px;
	font-weight: 600;
	margin-bottom: 30px;

	@media (max-width: 640px) {
		font-size: 20px;
	}
}
.texts {
	position: relative;
	max-height: 120px;
	overflow: hidden;
	@media (max-width: 640px) {
		font-size: 14px;
	}
	/* mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0)); */
	/* -webkit-mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0)); */
	margin-bottom: 20px;
	transition: all 1s;

	.blanket {
		position: absolute;
		width: 100%;
		height: 100%;
		background: linear-gradient(rgba(250, 250, 250, 0), rgba(250, 250, 250, 1));
		transition: all 1s;
	}

	.sub-title {
		margin-bottom: 20px;
	}
	.list {
		margin-left: 20px;
		.item {
		}
	}
	&-opened {
		max-height: none;
		mask-image: none;
		.blanket {
			background: none;
		}
	}
}
.toggle {
	display: flex;
	gap: 10px;

	span {
		text-decoration: underline;
		font-size: 16px;
		font-weight: 600;
	}
	.arrow {
		transform: rotate(0);
		transition: transform 1s;

		&-opened {
			transform: rotate(180deg);
		}
	}
}
</style>
