<script setup lang="ts">
import { hrefLogo, hrefMessages } from '~/assets/variables'
</script>

<template>
  <header :class="['box', 'margin-glob']">
    <div class="left-part">
      <NuxtLink :to="hrefLogo">
        <img src="/icons/logo-for-white.svg" :class="['hover', 'logo']" alt="logo" />
      </NuxtLink>

      <div class="divider"></div>

      <p class="low-lvl-info">
        Первый онлайн-сервис по ремонту и строительству
        <span style="font-weight: 800">с фикс стоимостью</span>
      </p>
    </div>

    <div class="right-part">
      <NuxtLink class="bell-container" :to="hrefMessages">
        <img class="hover" src="/images/header-signed/bell.svg" alt="icon" />
      </NuxtLink>

      <NuxtLink class="phone-container" :to="hrefMessages">
        <img class="hover" src="/images/header-signed/phone.svg" alt="icon" />
      </NuxtLink>

      <SharedButton class="make-order" fillOrange>Оформить заказ </SharedButton>

      <div :class="['profile', 'hover']">
        <p class="red">Мой профиль</p>
        <img src="/icons/profile.svg" alt="profile" />
      </div>

      <div class="avatar-container">
        <img src="/images/header-signed/avatar.png" alt="avatar" />

        <p class="text">
          <b>
            Ильсур
            <br />
            Халитов
          </b>
        </p>
      </div>
    </div>
  </header>
</template>

<style scoped>
.box {
  display: flex;
  height: 80px;
  margin-top: 30px;
}

.right-part {
  margin-left: auto;
  align-items: center;
  display: flex;
  gap: 10px;
  font-size: 16px;
  font-weight: 600;

  .avatar-container {
    display: flex;
    align-items: center;
    background-color: white;
    height: 100%;
    padding: 0 10px;
    gap: 10px;
    border-radius: 20px;

    .text {
    }
  }

  .bell-container {
    width: 80px;
    height: 100%;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
  }

  .phone-container {
    width: 80px;
    height: 100%;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
  }

  .make-order {
    font-size: 16px;
    border-radius: 20px;
    padding: 0px 30px;
    height: 100%;
    width: initial;
  }

  .profile {
    color: white;
    background-color: var(--c-black);
    border-radius: 20px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    gap: 40px;

    img {
      width: 18px;
    }
  }
}

.left-part {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  background-color: white;
  border-radius: 20px;
  font-size: 12px;
  padding-left: 25px;
  padding-right: 25px;
  gap: 25px;

  .divider {
    height: 60%;
    border-left: dashed 2px #e3e3e3;
  }
}
</style>
