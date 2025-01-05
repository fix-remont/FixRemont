<script setup lang="ts">
import {
  hrefCabinet,
  hrefCabinetContracts,
  hrefCabinetNews,
  hrefCabinetPartnerProgram,
  hrefCabinetProfile,
  hrefCabinetSupport,
  hrefLogo,
  hrefMakeOrder,
  hrefMessages,
  hrefPhone,
  hrefTg,
  hrefWatsapp,
  labelPhone
} from '~/assets/variables'

const openNavigation = ref(true)
const openDetails = ref(false)

const handleClickNavigation = () => {
  if (openNavigation.value) {
    openNavigation.value = false
    openDetails.value = false
  } else {
    openNavigation.value = true
    openDetails.value = false
  }
}

const handleClickDetails = () => {
  if (openDetails.value) {
    openNavigation.value = false
    openDetails.value = false
  } else {
    openNavigation.value = false
    openDetails.value = true
  }
}

const navigationLinks = [
  { href: hrefCabinet, label: 'Главная' },
  { href: hrefCabinetContracts, label: 'Договоры' },
  { href: hrefCabinetPartnerProgram, label: 'Партнёрская программа' },
  { href: hrefCabinetProfile, label: 'Профиль' },
  { href: hrefCabinetNews, label: 'Новости платформы' },
  { href: hrefCabinetSupport, label: 'Служба поддержки' }
]
</script>

<template>
  <header :class="['box-large', 'margin-glob']">
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

      <NuxtLink class="phone-container" :to="hrefCabinetSupport">
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
  <header
    :class="[
      'box-small',
      'margin-glob',
      { 'opened-navigation': openNavigation },
      { 'opened-details': openDetails }
    ]"
  >
    <div class="first-line">
      <NuxtLink class="logo-container" :to="hrefLogo">
        <img class="logo hover" src="/icons/logo-without-text.svg" alt="logo" />
      </NuxtLink>

      <div class="drop-down-menu">
        <img src="/images/header-signed/avatar.png" alt="avatar" />
        <p class="text">
          <b>
            Ильсур
            <br />
            Халитов
          </b>
        </p>
        <img
          class="arrow hover"
          @click="handleClickDetails"
          :src="openDetails ? '/icons/arrow-black-up.svg' : '/icons/arrow-white-down.svg'"
          alt="arrow"
        />
      </div>
      <img
        class="toggle-navigation hover"
        :src="openNavigation ? '/icons/close-button.svg' : '/icons/burger.svg'"
        alt="close-button"
        draggable="false"
        loading="eager"
        @click="handleClickNavigation"
      />
    </div>

    <NuxtLink class="make-order hover" :to="hrefMakeOrder"> Оформить заказ </NuxtLink>

    <div class="opened-navigation-block" v-if="openNavigation">
      <div class="navigation-links">
        <NuxtLink class="link hover" v-for="link in navigationLinks" :to="link.href">
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
    </div>

    <div class="opened-details-block" v-if="openDetails">
      <div class="links">
        <div class="bell-box hover grid-item">
          <img src="/images/header-signed/bell.svg" alt="bell" />
          <span>Сообщения</span>
        </div>
        <div class="support-box hover grid-item">
          <img src="/images/header-signed/phone.svg" alt="" />
          <span>Поддержка</span>
        </div>
        <div class="profile-box hover grid-item">
          <span>Мой профиль</span>
          <img src="/images/header-signed/profile.svg" alt="bell" />
        </div>
      </div>
      <SharedButton fillBlack>Выйти из профиля</SharedButton>
    </div>
  </header>
</template>

<style scoped>
.box-small {
  display: none;
  @media (max-width: 1800px) {
    display: flex;
    flex-direction: column;
  }

  .first-line {
    display: flex;
    justify-content: space-between;
    height: 52px;
    margin-top: 30px;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 15px;

    .logo-container {
      border-radius: 15px;
      width: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: white;
    }

    .drop-down-menu {
      display: flex;
      align-items: center;
      border-radius: 15px;
      background-color: var(--c-black);
      color: white;
      flex-grow: 1;
      /* gap: 10px; */
      /* padding: 0 10px; */
      justify-content: space-evenly;

      img {
        width: 30px;
        height: 30px;
      }
      .arrow {
        width: 15px;
      }
      .text {
        font-weight: 600;
        font-size: 12px;
      }
    }
    .toggle-navigation {
      width: 52px;
      height: 100%;
    }
  }
  .make-order {
    display: block;
    color: white;
    background-color: var(--c-orange);
    width: 100%;
    border-radius: 50px;
    text-align: center;
    font-weight: 600;
    font-size: 10px;
    padding: 10px 0;
  }
}

.opened-navigation {
  position: fixed;
  margin: 0;
  top: 0;
  background-color: #fafafa;
  width: 100%;
  padding: 30px 55px;
  height: 100vh;
  z-index: 10;

  @media (max-width: 1240px) {
    padding: 20px 36px;
  }

  @media (max-width: 640px) {
    padding: 12px 22px;
  }

  &-block {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    align-items: center;
    gap: 20px;

    .navigation-links {
      text-decoration: underline;
      font-weight: 600;
      font-size: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }

    .phone {
      font-weight: 600;
      font-size: 22px;
    }
    .social {
      background-color: white;
      width: 100%;
      border-radius: 20px;
      height: 73px;
      justify-content: center;
      display: flex;
    }

    .qr-code-block {
      display: flex;
      justify-content: space-between;
      background-color: white;
      width: 100%;
      border-radius: 20px;
      padding: 10px;
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
  }
}
.opened-details {
  position: fixed;
  margin: 0;
  top: 0;
  width: 100%;
  padding: 30px 55px;
  height: 100vh;
  z-index: 10;
  background-color: var(--c-black);
  flex: 1;

  @media (max-width: 1240px) {
    padding: 20px 36px;
  }

  @media (max-width: 640px) {
    padding: 12px 22px;
  }

  .drop-down-menu {
    background-color: white !important;
    color: var(--c-black) !important;
  }
  .opened-details-block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 20px 0;
    flex-grow: 1;
    .links {
      display: grid;
      color: white;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      grid-template-areas: 'bell-box support-box' 'profile-box profile-box';

      .grid-item {
        background-color: white;
        border-radius: 15px;
        display: flex;
        color: var(--c-black);
        font-size: 12px;
        font-weight: 600;
        align-items: center;
        justify-content: space-between;
        padding: 20px;
      }

      .bell-box {
        grid-area: bell-box;
      }
      .support-box {
        grid-area: support-box;
      }
      .profile-box {
        grid-area: profile-box;
      }
    }
  }
}
.box-large {
  display: flex;
  height: 80px;
  margin-top: 30px;

  @media (max-width: 1800px) {
    display: none;
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
}
</style>
