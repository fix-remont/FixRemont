<script setup lang="ts">
import { useViewport } from '~/composables/viewport'
import { hrefCabinet } from 'assets/variables'
import Bread_crumbs from '~/components/_shared/bread_crumbs.vue'

const { width } = useViewport()
</script>

<template>
  <div class="margin-glob block">
    <div class="upper">
      <img src="/images/realtors/block_1.png" alt="background" />
      <div class="crumb-container">
        <Bread_crumbs />
      </div>
      <div class="content">
        <h1 class="title-glob header">
          Приводите клиентов на
          <br />
          ремонт с фикс ценой и
          <br />
          зарабатывайте от 1 000 руб/м²
          <br />
          с каждой сделки
        </h1>
      </div>
      <div class="box-wrapper">
        <div class="black-box">
          <h3>
            Партнерская программа от первого в России онлайн-сервиса по ремонту и строительству с
            фиксированной ценой
          </h3>

          <NuxtLink class="orange link"> Подробнее </NuxtLink>

          <NuxtLink :to="hrefCabinet">
            <SharedButton class="mt-10" fillOrange> Зарегистрироваться как партнер </SharedButton>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="postcss">
$radius: 35px;
.upper {
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

.box-wrapper {
  position: absolute;
  bottom: 0;
  right: 0;
  background-color: white;
  padding-left: 20px;
  padding-top: 20px;
  border-radius: 20px 0 0;

  &::before,
  &::after {
    content: '';
    position: absolute;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    box-shadow: 15px 15px white;
  }
  &::before {
    bottom: 0;
    left: -40px;
  }
  &::after {
    right: 0;
    top: -40px;
  }
}

.black-box {
  background-color: #161616;
  padding: 50px;
  border-radius: $radius;
  color: white;
  width: 35em;

  h3 {
    width: 85%;
    font-size: 25px;
    font-weight: 500;
    line-height: 40px;
    margin-bottom: 55px;
    @media (max-width: 1500px) {
      font-size: 30px;
    }
  }

  .link {
    text-decoration: underline;
    font-weight: bold;
  }
}

.crumb-container {
  position: absolute;
  display: inline-block;
  top: 0;
  left: 0;
  padding: 20px;
  z-index: 1;
}
</style>
