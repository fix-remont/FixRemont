<script setup lang="ts">
import { labelPhone } from '~/assets/variables'
</script>
<template>
	<div class="block margin-glob radius-glob">
		<div class="box">
			<!-- <img src="/images/thanks/block_1.png" alt="img" />
			<div class="content">
				<div class="title title-glob">
					Благодарим <br />
					за обращение!
				</div>
				<p class="text">Ожидайте звонок с номера {{ labelPhone }}</p>
				<SharedButton fillBlack>Вернуться на сайт</SharedButton>
			</div> -->
		</div>
	</div>
</template>
<style scoped>
.block {
	display: flex;
	padding: auto;
	.box {
		flex-grow: 1;
		align-self: stretch;
		background-color: #f9af15;
	}
	/* position: relative; */
	/* display: flex;
	overflow: hidden;
	align-items: center;
	justify-content: center;

	.content {
		z-index: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 30px;
		color: white;
		padding: 50px;

		.title {
			text-align: center;
		}
	}

	img {
		position: absolute;
	} */
}
</style>
