<script setup lang="ts">
const props = defineProps<{
	footerWithoutMargin?: true
}>()
</script>

<template>
	<SharedHeaderSigned />
	<!-- <SharedHeader /> -->
	<slot />
	<SharedFooter :footerWithoutMargin="props.footerWithoutMargin" />
</template>

<style scoped></style>
