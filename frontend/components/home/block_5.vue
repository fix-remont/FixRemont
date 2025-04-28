<script setup lang="ts">
import { hrefCalculater } from '~/assets/variables'

const infoCheckboxes = [
  'Цены уже рассчитаны, а материалы подобраны и закуплены',
  'Даём юридическую гарантию сроков и качества',
  'Независимый Технадзор и тройной контроль',
  'Все бригады работают по единому регламенту',
  'Следите за ходом работ в режиме онлайн',
  'От вас не потребуется никаких визитов'
]
</script>

<template>
  <div class="margin-glob-new grid grid-cols-1 gap-[1vw] md:grid-cols-2">
    <div class="flex flex-col gap-[5vw] md:gap-[1vw]">
      <div class="bg-primary rounded-glob-new relative p-[8vw] text-white md:p-[4vw]">
        <p class="text-glob-xl mb-[4vw] md:mb-[2vw]">
          Берём все <br />
          финансовые <br />
          риски на себя
        </p>
        <p
          class="mb-[50vw] text-[4vw] font-medium leading-[6vw] md:mb-0 md:text-[1vw] md:leading-[1.4vw]"
        >
          В случае брака, дефектов или <br />
          оплошностей мастеров.<br />
          <br />
          Устраним все проблемы и решим <br />
          вопросы как с соседями, так и с <br />
          управляющей компанией.
        </p>
        <img
          class="absolute inset-0 my-auto mb-[-12vw] ml-auto w-[80vw] md:mb-0 md:w-[20vw]"
          src="/images/home/credit-card.png"
          alt="credit-card"
        />
      </div>

      <div
        class="rounded-glob-new grid grid-cols-1 gap-[4vw] bg-white px-[6vw] py-[8vw] md:grid-cols-3 md:gap-[1vw] md:px-[1.5vw] md:py-[2vw]"
      >
        <div class="flex items-center gap-[3vw] md:gap-[1vw]" v-for="text in infoCheckboxes">
          <img
            class="h-[4.5vw] w-[4.5vw] md:h-[1.4vw] md:w-[1.4vw]"
            src="/images/home/checkbox_checked.svg"
            alt="checkbox"
          />
          <span class="text-[3.5vw] text-[#808080] md:text-[.8vw]">{{ text }}</span>
        </div>
      </div>
    </div>

    <div
      class="rounded-glob-new relative flex flex-col gap-[3vw] p-[6vw] ring-[1vw] ring-black md:p-[4vw] md:ring-[.15vw]"
    >
      <h1 class="text-glob-xl mb-[1.5vw]">
        Стоимость для <br class="hidden md:block" />
        вас <span class="text-primary">не изменится,</span> <br class="hidden md:block" />
        даже при взлёте <br class="hidden md:block" />
        цен на материалы
      </h1>
      <p class="text-[3.5vw] text-[#808080] md:text-[1vw]">
        Мы всё предусмотрели: материалы закуплены заранее, <br />
        а бригады готовы выехать на объект в любой момент.
      </p>
      <UButton class="mt-auto w-full md:w-[20vw]" :to="hrefCalculater" size="custom"
        >Расчитать стоимость</UButton
      >
      <img
        class="absolute bottom-[-16vw] right-[1vw] hidden w-[15vw] md:block"
        src="/images/home/tassel.png"
        alt="tassel"
      />
    </div>
  </div>
</template>
