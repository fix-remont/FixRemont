<script setup lang="ts">
import {
  cabinetNavigationLinks,
  hrefPhone,
  hrefTg,
  hrefWatsapp,
  labelPhone
} from '~/assets/variables'
</script>

<template>
  <div class="radius-glob navigation">
    <div class="navigation-links">
      <NuxtLink class="link hover" v-for="link in cabinetNavigationLinks" :to="link.href">
        {{ link.label }}
      </NuxtLink>
    </div>

    <div class="working-mode">
      <img src="/icons/clock.svg" :class="['icon']" alt="phone" />
      <p>Звоните Пн-Вс: 8:30 - 19:00</p>
    </div>

    <div class="phone">
      <img src="/icons/phone.svg" :class="['icon']" alt="phone" />
      <a :href="hrefPhone">{{ labelPhone }}</a>
    </div>

    <div class="qr-code-block">
      <img class="qr-code-img" src="/images/header-signed/qr-code.png" alt="qr" />
      <div class="actions-block">
        <p>Мой QR-код</p>
        <div class="actions">
          <p class="hover">Открыть</p>
          <p class="hover">Скопировать ссылку</p>
        </div>
      </div>
    </div>

    <address class="social">
      <p class="text">
        Напишите нам,<br />
        мы сейчас онлайн
      </p>
      <a :href="hrefWatsapp">
        <img src="/icons/watsapp.svg" :class="['hover', 'icon']" alt="watsapp" />
      </a>
      <a :href="hrefTg">
        <img src="/icons/telegram.svg" :class="['hover', 'icon']" alt="watsapp" />
      </a>
    </address>

    <div class="logout-block">
      <img src="/images/header-signed/avatar.png" alt="avatar" />
      <p class="text">
        <b>
          Ильсур
          <br />
          Халитов
        </b>
      </p>

      <p class="logout hover">
        Выйти из
        <br />
        аккаунта
      </p>
    </div>
  </div>
</template>

<style scoped>
.navigation {
  background-color: white;
  display: flex;
  flex-direction: column;
  padding: 30px 20px;
  gap: 20px;
  height: max-content;

  @media (max-width: 1800px) {
    display: none;
  }

  .navigation-links {
    text-decoration: underline;
    font-weight: 600;
    font-size: 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .phone {
    font-weight: 600;
    font-size: 22px;
  }

  .working-mode,
  .phone {
    display: flex;
    gap: 10px;
    align-items: center;
  }
  .social {
    background-color: #fafafa;
    width: 100%;
    border-radius: 20px;
    height: 73px;
    justify-content: center;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .qr-code-block {
    display: flex;
    justify-content: space-between;
    background-color: white;
    width: 100%;
    border-radius: 20px;
    padding: 10px;
    gap: 10px;
    .actions-block {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      font-weight: 600;
      .actions {
        text-decoration: underline;
        color: var(--c-orange);
      }
    }
  }

  .logout-block {
    background-color: var(--c-black);
    border-radius: 20px;
    padding: 10px;
    display: flex;
    align-items: center;
    font-size: 16px;
    font-weight: 600;
    gap: 15px;
    min-width: max-content;
    img {
      width: 65px;
    }
    .text {
      color: white;
    }
    .logout {
      color: var(--c-orange);
      margin-left: 70px;
      text-decoration: underline;
    }
  }
}
</style>
