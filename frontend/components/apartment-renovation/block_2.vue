<script setup lang="ts">
const commentsRaw = [{ img: '/images/apartment-renovation/block_2__comments.png' }]

const comments = Array(7).fill(commentsRaw[0])
</script>

<template>
  <div class="margin-glob block">
    <div class="titles">
      <h1 class="title-glob">
        О чём
        <span class="orange">с грустью рассказывают</span>
        те, <br />
        кто делал ремонт самостоятельно?
      </h1>
      <p class="subtitle-glob">
        сотни подобных историй от наших клиентов со всей страны мы слышим регулярно
      </p>
    </div>

    <div class="wrapper">
      <UCarousel
        :items="comments"
        :ui="{
          container: 'gap-5',
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
        <template #default="{ item }">
          <div class="comment-box">
            <img :src="item.img" alt="img" draggable="false" />
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
    </div>
  </div>
</template>

<style scoped lang="postcss">
@media (max-width: 800px) {
  .titles {
    text-align: center;
  }

  .wrapper {
    width: 100%;
    margin-top: 1rem;
  }

  .comment-box {
    max-width: 94vw;
    display: flex;
    justify-content: center;
    align-items: center;
    img {
      width: 100%;
    }
  }
}
</style>
