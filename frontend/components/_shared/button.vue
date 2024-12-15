<script setup lang="ts">
defineProps<{}>()
</script>

<template>
	<button :class="['hover']">
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
	border: 2px var(--c-black) solid;

	@media (max-width: 640px) {
		font-size: 12px;
		padding: 16px;
	}
}
</style>
