<script setup lang="ts">
// import { portfolioItemsShort as items } from '~/shared/utils/data'
import { useCustomFetch } from '~/composables/custom-fetch'

import { z } from 'zod'

const PortfolioPostSchema = z.object({
  id: z.number(),
  title: z.string(),
  deadline: z.string(),
  cost: z.number(),
  square: z.number(),
  video_link: z.string().nullable(),
  video_duration: z.string().nullable(),
  project_type: z.object({ name: z.string() }),
  images: z.array(z.string().nullable()),
  articles: z
    .array(
      z.object({
        title: z.string(),
        body: z.string()
      })
    )
    .nullable()
})

export type PortfolioPost = z.infer<typeof PortfolioPostSchema>
const { zodError, responseError, zodData } = await useCustomFetch({
  path: '/portfolio_posts',
  src: '/home/block_7',
  schema: z.array(PortfolioPostSchema)
})

const dataSuccess = !zodError && !responseError

let items: PortfolioPost[] = []
if (dataSuccess) {
  items = zodData as PortfolioPost[]
  // if (items[0]) {
  //   items[0].images[0] =
  //     'https://w7.pngwing.com/pngs/928/235/png-transparent-internet-world-wide-web-world-wide-web-consortium-world-wide-web-web-design-search-engine-optimization-globe-thumbnail.png'

  //   items[1] = items[0]
  // }
}
</script>

<template>
  <ClientOnly>
    <UCarousel
      class="margin-glob"
      v-if="dataSuccess"
      :items="items"
      :ui="{
        container: 'w-full gap-5',
        item: 'w-full lg:w-[49%]',
        indicators: {
          wrapper: 'justify-end',
          base: 'h-[5px] w-[5px] sm:h-2 sm:w-2',
          active: 'bg-[var(--c-black)]',
          inactive: 'bg-[var(--c-gray)]'
        },
        arrows: {
          wrapper: 'flex gap-2 justify-start mt-2'
        }
      }"
      arrows
      indicators
    >
      <template #default="{ item }: { item: PortfolioPost }">
        <div class="item-box" :key="item.id">
          <img v-if="item.images[0]" :src="item.images[0]" :alt="item.title" draggable="false" />
          <div class="text-box">
            <p class="title">{{ item.title }}</p>
            <NuxtLink :class="['link pointer']" to="#">Узнать Стоимость</NuxtLink>
          </div>
        </div>
      </template>
      <template #prev="{ onClick, disabled }">
        <img
          :class="[
            'arrow cursor-pointer',
            'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
            { 'opacity-60': disabled }
          ]"
          src="/images/arrow-prev.svg"
          @click="onClick"
          draggable="false"
        />
      </template>

      <template #next="{ onClick, disabled }">
        <img
          :class="[
            'arrow cursor-pointer',
            'h-[35px] w-[35px] sm:h-[60px] sm:w-[60px]',
            { 'opacity-60': disabled }
          ]"
          src="/images/arrow-next.svg"
          @click="onClick"
          draggable="false"
        />
      </template>
    </UCarousel>
  </ClientOnly>
</template>

<style scoped>
.item-box {
  position: relative;
  font-weight: 600;
  font-size: 10px;
  @media (max-width: 640px) {
    font-size: 6px;
  }

  .text-box {
    position: absolute;
    left: 5em;
    bottom: 5em;
    font-size: 1em;

    .title {
      font-size: 3.6em;
      color: white;
      z-index: 1;
    }
    .link {
      text-decoration: underline;
      color: var(--c-orange);
      font-size: 1.8em;
      z-index: 1;
    }
  }
}
</style>
