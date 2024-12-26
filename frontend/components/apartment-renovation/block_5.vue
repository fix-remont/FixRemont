<script setup lang="ts">
const imagePath = '/images/apartments-renovation/block_5__gallery.png'
let items = [
  {
    title: 'Кухня: внеплановые затраты удвоили стоимость ремонта ',
    points: [
        'Мастера сняли потолок, переделали электрику, наклеили обои и уложили керамогранит на стену',
        'При монтаже натяжного потолка рабочие попали в силовой кабель',
        'Пришлось снимать керамогранит, отклеивать обои и делать электрику заново',
        'Бегом по магазинам за новыми материалами',
        'Снова приходится клеить обои, укладывать керамогранит и натягивать потолок',
    ],
    final: 'затраты умножились на 2 ',
    image: imagePath,
  }
]

const gallery = Array(5).fill(items[0])

</script>

<template>
  <div class="block margin-glob">
    <div class="titles">
      <h1 class="title-glob">При самостоятельном ремонте вы
        <br/>
        <span class="orange">рискуете потратить в два раза больше</span>
      </h1>
      <p class="subtitle-glob">3 примера непредвиденного роста затрат:</p>
    </div>

    <div class="gallery">


    </div>
  </div>
</template>

<style scoped>
.titles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 3rem;
}
</style>