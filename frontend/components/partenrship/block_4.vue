<script setup lang="ts">
const carousel1 = [
  {
    imgSrc: '/images/partnership/block_4_1.png',
    title: 'С нас: подбор проверенных специалистов',
    label: 'в нашей базе более 1 000 надежных бригад'
  }
]

const carousel2 = [
  {
    imgSrc: '/images/partnership/block_4_2.png',
    title: 'С вас: простая регистрация',
    label: 'на нашей платформе'
  }
]
const gallery1 = Array(5).fill(carousel1[0])
const gallery2 = Array(5).fill(carousel2[0])

</script>

<template>
<div class="margin-glob">
  <h1 class="title-glob mb-4 ">
    <span class="orange">Возьмём на себя</span>
    организацию и выполнение работ под ключ
  </h1>
  <div class="wrapper">
    <UCarousel
      :items="gallery1"
      arrows
      indicators
      :ui="{
        container: 'gap-3 rounded-3xl',
        indicators: { wrapper: 'justify-end', base: 'h-[5px] w-[5px] sm:h-2 sm:w-2', active: 'bg-[var(--c-black)]', inactive: 'bg-[var(--c-gray)]' },
        arrows: {
          wrapper: 'flex gap-2 justify-start mt-2',
        },
      }"
      class="w-1/2 h-1/2"
    >
      <template #default="{ item }">
        <div class="relative rounded-3xl">
          <img :src="item.imgSrc" alt="img" draggable="false"/>
          <div class="absolute bottom-10 left-10 right-0 p-4 text-white">
            <h4 class="text-3xl font-bold mb-3">{{ item.title }}</h4>
            <p class="text-lg font-bolder">{{ item.label }}</p>
          </div>
        </div>
      </template>

      <template #prev="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
					src="/images/arrow-prev.svg"
					@click="onClick"
					draggable="false" />
			</template>

			<template #next="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
					src="/images/arrow-next.svg"
					@click="onClick"
					draggable="false" />
      </template>
    </UCarousel>

    <UCarousel
      :items="gallery2"
      arrows
      indicators
      :ui="{
        container: 'gap-3 rounded-3xl',
        indicators: { wrapper: 'justify-end', base: 'h-[5px] w-[5px] sm:h-2 sm:w-2', active: 'bg-[var(--c-black)]', inactive: 'bg-[var(--c-gray)]' },
        arrows: {
          wrapper: 'flex gap-2 justify-start mt-2',
        },
      }"
      class="w-1/2 h-1/2"
    >
      <template #default="{ item }">
        <div class="relative rounded-3xl">
          <img :src="item.imgSrc" alt="img" draggable="false"/>
          <div class="absolute bottom-10 left-10 right-0 p-4 text-white">
            <h4 class="text-3xl font-bold mb-3">{{ item.title }}</h4>
            <p class="text-lg font-bolder">{{ item.label }}</p>
          </div>
        </div>
      </template>

      <template #prev="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
					src="/images/arrow-prev.svg"
					@click="onClick"
					draggable="false" />
			</template>

			<template #next="{ onClick, disabled }">
				<img
					:class="['arrow cursor-pointer', 'w-[35px] h-[35px] sm:w-[60px] sm:h-[60px]', { 'opacity-60': disabled }]"
					src="/images/arrow-next.svg"
					@click="onClick"
					draggable="false" />
      </template>
    </UCarousel>
  </div>
</div>
</template>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;
}

@media (max-width: 800px) {
  /*TODO: сделать нормальный адаптив */
  .wrapper {
    flex-direction: column;
  }

  h1 {
    text-align: center;
  }
}

</style>