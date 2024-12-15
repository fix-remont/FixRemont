<script setup lang="ts">
defineProps<{
	hovered: boolean
}>()

const white = '#fff'
const black = '#161616'
</script>

<template>
	<svg width="51" height="50" viewBox="0 0 51 50" fill="none" xmlns="http://www.w3.org/2000/svg">
		<rect :class="['circle', { circle__hover: hovered }]" x="0.430664" y="50" width="50" height="49.9439" rx="24.9719" transform="rotate(-90 0.430664 50)" />
		<path :class="['arrow', { arrow__hover: hovered }]" d="M18.1777 19.2411L31.4587 32.5222L32.9023 31.0786L19.6213 17.7975L18.1777 19.2411Z" :fill="white" />
		<path
			:class="['arrow', { arrow__hover: hovered }]"
			d="M25.007 17.4779L25.007 19.5195L19.9439 19.5195L19.9439 24.5826L17.9023 24.5826L17.9023 17.4779L25.007 17.4779Z"
			:fill="white" />
	</svg>
</template>

<style scoped lang="postcss">
$time: 1s;
.circle {
	transition: fill $time linear;
	fill: v-bind(black);

	&__hover {
		fill: v-bind(white);
	}
}
.arrow {
	transition: all $time linear;
	fill: v-bind(white);
	transform-origin: center;
	&__hover {
		transform: rotate(180deg);
		fill: v-bind(black);
	}
}
</style>
