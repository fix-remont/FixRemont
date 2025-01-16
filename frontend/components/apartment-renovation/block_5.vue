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
/* === Общие базовые стили === */
.container {
  padding: 2rem;
}

.titles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 3rem;
}

.title {
  font-size: 2.5rem;
  text-align: center;
}

.subtitle {
  font-size: 1.2rem;
  text-align: center;
}

.highlight {
  color: var(--c-orange);
}

/* === Галерея === */
.gallery-box {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.text-part {
  width: 35%;
  padding: 20px;
}

.text-part h4 {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.text-part ul {
  list-style-type: disc;
  padding-left: 20px;
}

.text-part li {
  font-size: 1rem;
  color: #818181;
  margin-bottom: 0.5rem;
}

.img-part {
  width: calc(35% + 5%);
  height: auto;
}

.img-part img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 24px;
}

/* === Медиа-запросы === */

/* Мобильные устройства */
@media (max-width: 800px) {
  .gallery-box {
    flex-direction: column;
  }

  .text-part,
  .img-part {
    width: 100%;
  }
}

/* Планшеты */
@media (max-width: 1200px) {
  .gallery-box {
    width: 90vw;
    flex-direction: column;
    gap: 1rem;
  }

  .text-part {
    width: 80%;
  }

  .img-part {
    width: calc(80% + 5%);
  }
}

/* Десктопы */
@media (min-width: 1201px) {
  .gallery-box {
    max-width: 93vw;
    justify-content: space-around;
  }

  .text-part {
    width: 35%;
  }

  .img-part {
    width: calc(40% + 5%);
  }
}
</style>
