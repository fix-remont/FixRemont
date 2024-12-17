<script setup lang="ts">
const props = defineProps<{
	youtube?: true
}>()
</script>

<template>
	<button :class="['hover', { youtube }]">
		<slot />
	</button>
</template>

<style scoped>
button {
	width: 100%;
	padding: 32px;
	border-radius: 500px;
	font-size: 20px;
	font-weight: 600;
	border: 2px solid;

	@media (max-width: 640px) {
		font-size: 12px;
		padding: 16px;
	}
}
.youtube {
	color: #ff2600;
	border-color: #ff2600;
}
</style>
