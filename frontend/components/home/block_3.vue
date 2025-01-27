<script setup>
import { ref } from 'vue'
import { hrefCalculater } from '~/assets/variables'
const config = useRuntimeConfig()

// import useTariffsStore from '~/stores/tariffs.ts'
// import { storeToRefs } from 'pinia'
// const { items } = storeToRefs(useTariffsStore())
// const itemsLocal = ref(items)
// console.log(items)

// import { tariffs } from '~/shared/utils/test-data'

const tariffs = [
  {
    cost: 'Фикс',
    name: 'Базовый',
    image: '/images/home/package-comfort.png',
    description: 'описание 1'
  },
  {
    cost: 'Фикс',
    name: 'Стандарт',
    image: '/images/home/package-comfort.png',
    description: 'описание 2'
  },
  {
    cost: 'Фикс',
    name: 'Комфорт',
    image: '/images/home/package-comfort.png',
    description: 'описание 3'
  },
  {
    cost: 'Фикс',
    name: 'Бизнес',
    image: '/images/home/package-comfort.png',
    description: 'описание 4'
  }
]

const itemsLocal = ref(tariffs)

const carouselRef1 = ref(null)
const carouselRef2 = ref(null)
const currentActiveIndex = ref(0)

const itemsWithSelected = computed(() => {
  return itemsLocal.value.map((item, index) => {
    const updatedItem = { ...item } // Создаем новый объект
    updatedItem.selected = index === currentActiveIndex.value

    // const indexImage = updatedItem.image.indexOf('//')
    // updatedItem.image =
    //   indexImage === -1
    //     ? updatedItem.image
    //     : `${config.public.mediaPath}${updatedItem.image.slice(indexImage + 2)}`

    return updatedItem
  })
})

// const handleUpdateCarouselByButton = (onClick, actionType, disabled) => {
//   if (disabled) return
//   onClick()
// }

onMounted(() => {
  setInterval(() => {
    if (!carouselRef1.value) return
    if (carouselRef1.value.page === carouselRef1.value.pages) {
      return carouselRef1.value.select(0)
    }
    carouselRef1.value.next()
  }, 3000)
})

const handleClickTab = (tabIndex) => {
  carouselRef1.value.select(tabIndex + 1)
  carouselRef2.value.select(tabIndex + 1)
}

watch(
  () => carouselRef1.value?.page,
  (newPage) => (currentActiveIndex.value = newPage - 1)
)
</script>

<template>
  <div
    class="margin-glob-new grid grid-cols-1 gap-[4vw] md:grid-cols-2 md:gap-[2vw]"
    v-if="itemsWithSelected.length > 0"
  >
    <div class="flex flex-col gap-[2vw] md:gap-0">
      <p class="text-glob-xl">
        Занимайтесь <br />
        <span class="text-primary">любимыми</span> делами, <br />
        а ремонт мы <br />
        возьмём на себя.
      </p>

      <div class="mt-auto">
        <p class="mb-[4vw] text-[4vw] font-medium md:mb-[1vw] md:text-[1.2vw]">
          4 пакетных решения.
          <br class="md:hidden" />
          <b><u>Выбирайте</u></b> для себя лучшее:
        </p>
        <UCarousel
          ref="carouselRef2"
          :items="itemsWithSelected"
          :ui="{
            container: 'gap-[3vw] md:gap-[1vw]'
          }"
        >
          <template #default="{ item, index }">
            <div
              class="relative flex h-[24vw] w-[24vw] items-center justify-center overflow-hidden rounded-[4vw] md:h-[6.5vw] md:w-[6.5vw] md:rounded-[1vw]"
              @click="handleClickTab(index)"
            >
              <p class="relative z-10 text-[3vw] font-semibold text-white md:text-[1vw]">
                {{ item.name.toUpperCase() }}
              </p>
              <img
                class="absolute top-0 h-full w-full object-cover"
                :src="item.image"
                alt="img"
                draggable="false"
              />
              <div
                :class="[
                  'absolute top-0 h-full w-full',
                  item.selected ? 'bg-yellow-400/50' : 'bg-black/30'
                ]"
              ></div>
            </div>
          </template>
        </UCarousel>
      </div>
    </div>
    <div class="flex flex-col gap-[4vw] md:gap-[1vw]">
      <UCarousel
        ref="carouselRef1"
        :items="itemsWithSelected"
        :ui="{
          // item: 'w-full h-full rounded-glob-new',
          container: 'gap-[1vw] relative h-full'
        }"
        arrows
      >
        <template #default="{ item }">
          <img class="rounded-glob-new w-[46vw] object-cover" :src="item.image" draggable="false" />
        </template>

        <template #prev="{ onClick, disabled }">
          <SharedArrowPrevCarousel :onClick="onClick" :disabled="disabled" />
        </template>

        <template #next="{ onClick, disabled }">
          <SharedArrowNextCarousel :onClick="onClick" :disabled="disabled" />
        </template>
      </UCarousel>

      <div
        class="rounded-glob-new grid grid-cols-1 gap-[4vw] bg-[#EFEFEF] px-[6vw] py-[6vw] md:grid-cols-2 md:gap-[1vw] md:px-[4vw] md:py-[2vw]"
      >
        <div class="flex flex-col justify-between">
          <p class="text-[7.5vw] font-bold md:text-[2.4vw]">
            {{ itemsWithSelected[currentActiveIndex]?.name }}
          </p>
          <p class="text-[3vw] text-[#818181] md:text-[1vw]">
            {{ itemsWithSelected[currentActiveIndex]?.description }}
          </p>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center gap-[4vw] md:block">
            <p class="text-[3vw] md:text-[1vw]">Стоимость:</p>
            <p class="text-[7.5vw] font-bold md:text-[2.4vw]">
              {{ itemsWithSelected[currentActiveIndex]?.cost }}
            </p>
          </div>

          <UButton class="mt-auto" :to="hrefCalculater" size="custom" block
            >Отлайн калькулятор</UButton
          >
        </div>
      </div>
    </div>
  </div>
</template>
