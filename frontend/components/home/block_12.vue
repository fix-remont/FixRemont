<script setup lang="ts">
const items = [
	{ label: 'Вконтакте', src: '/icons/vkontakte.svg', subsribed_amount: 1500 },
	{ label: 'Instagram', src: '/icons/instagram.svg', subsribed_amount: 1550 },
	{ label: 'Telegram', src: '/icons/telegram.svg', subsribed_amount: 500 },
]

const youtubeSubscribtions = 2500
</script>

<template>
	<div class="block margin-glob">
		<h1 class="title title-glob">Мы максимально <span class="orange">открыты</span> и подтверждаем экспертность в социальных сетях</h1>
		<div class="box-2">
			<div class="video-box">
				<div class="youtube">
					<img class="icon" src="/icons/youtube.svg" alt="icon-youtube" />
					<div class="texts">
						<p class="label">YouTube</p>
						<p class="subscribtions">{{ youtubeSubscribtions }} подписчиков</p>
					</div>
				</div>
				<img class="main-img" src="/images/home/block_12.png" alt="img" />
			</div>
			<div class="social-box">
				<div class="item-box" v-for="item in items" :key="item.src">
					<img class="item-icon" :src="item.src" alt="icon" />
					<span class="item-label">{{ item.label }}</span>
					<span class="subscribed-amount">{{ item.subsribed_amount }} подписчиков</span>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.block {
	font-size: 10px;
	@media (max-width: 640px) {
		font-size: 4px;
	}
	.title {
	}

	.box-2 {
		display: flex;
		gap: 30px;
		@media (max-width: 1240px) {
			flex-direction: column;
			gap: 10px;
		}

		.video-box {
			width: 49%;
			border-radius: 3.5em;
			position: relative;
			color: white;
			background-color: var(--c-black);
			display: flex;
			@media (max-width: 1240px) {
				width: 100%;
			}

			.youtube {
				display: flex;
				gap: 30px;
				position: absolute;
				left: 55px;
				top: 50px;
				align-items: center;
				@media (max-width: 640px) {
					gap: 10px;
					left: 20px;
					top: 20px;
				}
				.icon {
					@media (max-width: 640px) {
						width: 25px;
						height: 25px;
					}
				}

				.texts {
					.label {
						font-size: 4em;
						font-weight: 700;
					}

					.subscribtions {
						font-size: 1.8em;
						font-weight: 500;
					}
				}
			}

			.main-img {
				margin-top: auto;
			}
		}

		.social-box {
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			gap: 10px;
			width: 49%;
			@media (max-width: 1240px) {
				width: 100%;
			}
			.item-box {
				display: flex;
				align-items: center;
				padding: 3.5em 4.7em;
				color: var(--c-black);
				background-color: white;
				border-radius: 3.5em;
				gap: 3em;

				.item-icon {
					width: 7em;
					height: 7em;
					/* @media (max-width: 640px) {
						width: 21px;
						height: 21px;
					} */
				}
				.item-label {
					font-size: 4em;
					font-weight: 700;
				}
				.subscribed-amount {
					margin-left: auto;
					font-size: 1.8em;
					font-weight: 500;
				}
			}
		}
	}
}
</style>
