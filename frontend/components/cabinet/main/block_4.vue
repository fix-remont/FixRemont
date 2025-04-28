<script setup lang="ts">
defineProps<{
  title?: string
}>()

let items = [
  {
    object: 'Квартира',
    tarif: 'Бизнес',
    location: 'Казань, ул. Волкова',
    reward: 32000,
    currentStep: 'Установка полов',
    isFinished: false
  },
  {
    object: 'Квартира',
    tarif: 'Бизнес',
    location: 'Казань, ул. Волкова',
    reward: 32000,
    currentStep: 'Установка полов',
    isFinished: false
  },
  {
    object: 'Квартира',
    tarif: 'Бизнес',
    location: 'Казань, ул. Волкова',
    reward: 32000,
    currentStep: 'Установка полов',
    isFinished: false
  },
  {
    object: 'Квартира',
    tarif: 'Бизнес',
    location: 'Казань, ул. Волкова',
    reward: 32000,
    currentStep: 'Объект сдан',
    isFinished: true
  }
]
// items = []
</script>

<template>
  <section class="margin-b-glob block">
    <h2 class="title">{{ title ?? 'Мои клиенты' }}</h2>
    <div class="radius-glob table" v-if="items.length > 0">
      <div
        v-for="(item, index) in items"
        :class="['row', { 'is-not-last': index !== items.length - 1 }]"
      >
        <div class="object">
          <div class="object-label">Объект:</div>
          <div class="object-value">{{ item.object }}</div>
        </div>

        <div class="tarif">
          <div class="tarif-label">Тариф:</div>
          <div class="tarif-value">{{ item.tarif }}</div>
        </div>

        <div class="location">
          <div class="location-label">Локация:</div>
          <div class="location-value">{{ item.location }}</div>
        </div>

        <div class="reward">
          <div class="reward-label">Вознаграждение:</div>
          <div class="reward-value">{{ item.reward }}</div>
        </div>

        <div :class="['current-step', { finished: item.isFinished }]">
          <div class="wrap">
            <div class="current-step-label">Текущий этап:</div>
            <div class="current-step-value">{{ item.currentStep }}</div>
          </div>
          <img class="icon hover" src="/images/cabinet/door-out.svg" alt="door-out" />
        </div>
      </div>
    </div>
    <div class="table-empty radius-glob" v-else>
      <p>У вас нет текущих {{ !title ? 'заказов' : 'договоров' }}</p>
    </div>
  </section>
</template>

<style scoped>
.block {
  .title {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 10px;
    @media (max-width: 640px) {
      font-size: 16px;
    }
  }

  .table {
    background-color: white;
    width: 100%;
    padding: 30px 20px;

    .is-not-last {
      border-bottom: 1px solid #e3e3e3;
    }

    .row {
      display: grid;
      grid-template-columns: 1fr 1fr 1.5fr 1fr 2fr;
      grid-template-areas: '. . . . current-step current-step';
      column-gap: 10px;
      justify-content: space-between;
      padding: 20px 0;
      align-items: center;

      @media (max-width: 1750px) {
        grid-template-columns: 1fr 1fr 1.5fr;
        grid-template-rows: auto auto;
        grid-template-areas: '. . .' '. current-step current-step';
      }

      @media (max-width: 1200px) {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto auto;
        grid-template-areas: '. .' '. .' 'current-step current-step';
      }

      .object,
      .tarif,
      .location,
      .reward {
        display: flex;
        flex-direction: column;
        padding: 10px;
      }

      .current-step {
        display: flex;
        align-items: center;
        gap: 10px;
        grid-area: current-step;
        border-radius: 15px;

        @media (max-width: 640px) {
          background-color: #fafafa;
        }

        .wrap {
          padding: 10px;
          border-radius: 15px;
          background-color: #fafafa;
          flex-grow: 1;
        }
        .icon {
          width: 50px;
          height: 50px;
          @media (max-width: 640px) {
            width: 30px;
            height: 30px;
            margin: 10px;
          }
        }
      }

      .object-label,
      .tarif-label,
      .location-label,
      .reward-label,
      .current-step-label {
        font-size: 16px;
        font-weight: 500;
        color: #686868;
        @media (max-width: 640px) {
          font-size: 12px;
        }
      }

      .object-value,
      .tarif-value,
      .location-value,
      .reward-value,
      .current-step-value {
        font-size: 24px;
        font-weight: 600;
        color: var(--c-black);
        @media (max-width: 640px) {
          font-size: 16px;
        }
      }

      .finished {
        border-radius: 15px;

        .wrap {
          background-color: var(--c-black);
          .current-step-value {
            color: white;
          }
        }

        @media (max-width: 640px) {
          background-color: var(--c-black);
        }
      }
    }
  }

  .table-empty {
    font-size: 16px;
    font-weight: 500;
    height: 210px;
    background-color: white;
    display: flex;
    color: #686868;
    p {
      margin: auto;
    }
  }
}
</style>
