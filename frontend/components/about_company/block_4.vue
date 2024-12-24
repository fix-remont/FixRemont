<script setup lang="ts"></script>

<template>
	<div class="block margin-glob">
		<div class="box-1 radius-glob">
			<img src="/images/about_company/block_4-puzle.png" alt="img" />

			<div class="title title-glob">Приглашаем к сотрудничеству Партнеров для совместной реализации проектов</div>

			<div class="list">
				<div class="sub-title">У вас есть база потенциальных клиентов на ремонт или строительство?</div>
				<ul class="list-disc">
					<li>С вас — клиенты. С нас — надежная и бесперебойная организация всех работ.</li>
					<li>Работаем как с физ.лицами, так и с юр.лицами.</li>
				</ul>
			</div>
		</div>
		<div class="box-2 radius-glob">
			<div class="title title-glob">До <span class="orange">-10% от суммы</span> чека - это ваша комиссия за приведенного клиента</div>
			<div class="buttons">
				<SharedButton fillBlack>Зарегистрироваться в личном кабинете партнёра</SharedButton>
				<SharedButton> Узнать подробнее </SharedButton>
			</div>
			<img src="/images/about_company/block_4-percent.png" alt="img" />
		</div>
	</div>
</template>

<style scoped>
.block {
	display: flex;
	gap: 30px;
	@media (max-width: 1500px) {
		flex-direction: column;
	}

	.box-2 {
		width: 50%;
		border: 3px solid var(--c-black);
		position: relative;
		padding: 50px;
		overflow: hidden;

		@media (max-width: 1500px) {
			width: 100%;
		}

		@media (max-width: 640px) {
			padding: 15px;
		}
		img {
			position: absolute;
			right: 0;
			top: 0;
			@media (max-width: 1000px) {
				display: none;
			}
		}
		.title {
			width: 70%;
			margin-bottom: 20px;
			@media (max-width: 1000px) {
				width: 100%;
			}
		}
		.buttons {
			display: flex;
			flex-direction: column;
			gap: 20px;
			@media (max-width: 1500px) {
				width: 70%;
			}
			@media (max-width: 1000px) {
				width: 100%;
			}
		}
	}
	.box-1 {
		position: relative;
		background-color: #f9af15;
		width: 50%;
		color: white;
		padding: 50px;
		overflow: hidden;
		display: flex;
		flex-direction: column;
		justify-content: space-between;

		@media (max-width: 1500px) {
			width: 100%;
		}
		@media (max-width: 640px) {
			padding: 15px;
		}
		img {
			position: absolute;
			height: 100%;
			right: 0;
		}
		.title {
			position: relative;
			z-index: 1;
			margin-bottom: 20px;
			/* @media (max-width: 640px) {
				font-size: 22px;
			} */
		}
		.list {
			position: relative;
			z-index: 1;
			.sub-title {
				margin-bottom: 20px;
			}
			ul {
				margin-left: 20px;
			}
		}
	}
}
</style>
