<script setup lang="ts">
import {useViewport} from "~/composables/viewport";

const imagePath = '/images/apartment-renovation/block_1.png'
const { width } = useViewport()

defineProps<{
  header1: string,
  header2: string,
  imagePath: string,
  link_href: string,
}>()

</script>

<template>
<div class="margin-glob block">
  <img :src="imagePath" alt="background"/>
  <div class="content">
    <h1 class="title-glob header">
      Ремотн квартир
      <br/>
      под ключ по готовым
      <br/>
      проектам и с
      <br/>
      фиксированной ценой
    </h1>
  </div>

  <div class="black-box">
    <h2>
      Заселитесь в
      <br/>
      квартиру мечты с
      <br/>
      мебелью в течение
      <br/>
      3-х месяцев
    </h2>
    <button :class="['hover']">
      Онлайн-калькулятор
    </button>
  </div>
</div>
</template>

<style scoped lang="postcss">
$radius: 35px;

.block {
  position: relative;
}

.content {
  position: absolute;
  bottom: 0;
  margin-bottom: 5%;
  left: 100px;
}

.header {
  font-size: 50px;
  font-weight: 600;
  color: white;
  line-height: 70px;
  letter-spacing: 0.1px;
  @media (max-width: 1500px) {
    font-size: 40px;
  }
}

.black-box {
  position: absolute;
  bottom: 0;
  right: 0;
  background-color: #161616;
  padding: 50px;
  border-radius: $radius;
  color: white;
  width: 35em;
  h2 {
    font-size: 25px;
    font-weight: 500;
    line-height: 40px;
    margin-bottom: 100px;
    @media (max-width: 1500px) {
      font-size: 30px;
    }
  }
  button {
    background-color: var(--c-orange);
    color: white;
    font-size: 20px;
    font-weight: 600;
    text-align: center;
    margin-top: auto;
    width: 100%;
    padding: 25px;
    border-radius: 20em;
    transition: 0.3s;
  }
}

</style>