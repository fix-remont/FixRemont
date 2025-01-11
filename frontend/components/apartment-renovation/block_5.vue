<script setup lang="ts">
const imagePath = 'images/apartment-renovation/block_5__gallery.png'
let items = [
  {
    title: 'Кухня: внеплановые затраты удвоили стоимость ремонта ',
    points: [
      'Мастера сняли потолок, переделали электрику, наклеили обои и уложили керамогранит на стену',
      'При монтаже натяжного потолка рабочие попали в силовой кабель',
      'Пришлось снимать керамогранит, отклеивать обои и делать электрику заново',
      'Бегом по магазинам за новыми материалами',
      'Снова приходится клеить обои, укладывать керамогранит и натягивать потолок'
    ],
    final: 'затраты умножились на 2 ',
    image: imagePath
  }
]

const gallery = Array(5).fill(items[0])
</script>

<template>
  <div class="margin-glob block">
    <div class="titles">
      <h1 class="title-glob">
        При самостоятельном ремонте вы
        <br />
        <span class="orange">рискуете потратить в два раза больше</span>
      </h1>
      <p class="subtitle-glob">3 примера непредвиденного роста затрат:</p>
    </div>

      <UCarousel
        class="gallery"
        :items="gallery"
        arrows
        indicators
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
      >
        <template #default="{ item }">
          <div class="gallery-box">
            <div class="text-part">
              <h4>{{ item.title }}</h4>
              <ul>
                <li v-for="(point, index) in item.points" :key="index">{{ point }}</li>
              </ul>
              <h4><span class="orange">Итог: </span> {{ item.final }}</h4>
            </div>
            <div class="img-part">
              <img :src="item.image" alt="img" draggable="false" />
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
  </div>
</template>

<style scoped>
.titles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 3rem;
}

.gallery-box {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  div {
    border-radius: 24px;
  }
}

.text-part {
  width: 35%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2rem;
  padding: 20px;

  h4 {
    color: var(--c-black);
    font-size: 30px;
    font-weight: bold;
    line-height: 1.2;
  }

  ul {
    list-style-type: disc;
  }

  li {
    color: #818181;
    margin-left: 20px;
    width: 80%;
    margin-bottom: 0.5rem;
  }
}

.img-part {
  width: 40%;
  height: 100%;
}

/*TODO: исправить центровку элементов в мобилке*/
@media (max-width: 800px) {
  .gallery {
    width: 100%;
  }


  .gallery-box {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: fit-content;
  }

  .text-part {
    order: 1;
    display: flex;
    align-items: center;

    h4 {
      font-size: 24px;
    }
  }

  .img-part {
    order: 0;
    object-fit: cover;
  }

  .titles {
    text-align: center;
  }
}
</style>
