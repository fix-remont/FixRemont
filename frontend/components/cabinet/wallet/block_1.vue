<script setup lang="ts">
const items = [
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Исполнена' },
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Обработка' },
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Отмена' },
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Исполнена' },
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Исполнена' },
  { operationType: 'Вывод', amount: '300 000', date: '25.02.2024', status: 'Исполнена' }
]

const statusMap = (status: string) => {
  let result: string = ''

  if (status == 'Исполнена') {
    result = 'finished'
  } else if (status == 'Обработка') {
    result = 'handling'
  } else if (status == 'Отмена') {
    result = 'canceled'
  }

  return result
}
</script>

<template>
  <article class="margin-b-glob block">
    <h2 class="title">История операций</h2>

    <div class="radius-glob table-wrap" v-if="items.length > 0">
      <div class="table">
        <div
          v-for="(item, index) in items"
          :class="['row', { 'is-not-last': index !== items.length - 1 }]"
        >
          <div class="operation-type">
            <div class="operation-type-label">Операция:</div>
            <div class="operation-type-value">{{ item.operationType }}</div>
          </div>

          <div class="amount">
            <div class="amount-label">Сумма:</div>
            <div class="amount-value">{{ item.amount }} руб</div>
          </div>

          <div class="date">
            <div class="date-label">Дата:</div>
            <div class="date-value">{{ item.date }}</div>
          </div>

          <div :class="['status', `status-${statusMap(item.status)}`]">
            <div class="status-label">Статус:</div>
            <div class="status-value">{{ item.status }}</div>
          </div>

          <SharedButton class="button">Скачать чек</SharedButton>
        </div>
      </div>
    </div>
    <div class="table-empty radius-glob" v-else>
      <p>У вас не было операций</p>
    </div>
  </article>
</template>

<style scoped>
.block {
  .title {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 20px;
  }

  .table-wrap {
    background-color: white;
    width: 100%;
    padding: 30px 20px;
    max-height: 600px;
    overflow: scroll;
    @media (max-width: 1600px) {
      max-height: 500px;
    }

    .table {
      .is-not-last {
        border-bottom: 1px solid #e3e3e3;
      }

      width: 100%;
      .row {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 2fr 2fr;
        grid-template-areas: 'operation-type amount date status button';
        column-gap: 10px;
        justify-content: space-between;
        padding: 20px 0;
        align-items: center;
        gap: 20px;

        @media (max-width: 1600px) {
          grid-template-columns: 1fr 1fr 1fr;
          grid-template-rows: auto auto;
          grid-template-areas: 'operation-type amount date' 'status status button';
        }

        @media (max-width: 900px) {
          grid-template-columns: 1fr 1fr;
          grid-template-rows: auto auto auto auto;
          grid-template-areas: 'operation-type amount' 'date date' 'status status' 'button button';
        }

        .status {
          grid-area: status;
        }
        .date {
          grid-area: date;
        }
        .amount {
          grid-area: amount;
        }
        .operation-type {
          grid-area: operation-type;
        }

        .button {
          grid-area: button;
        }

        .operation-type,
        .amount,
        .date,
        .status {
          display: flex;
          flex-direction: column;
          padding: 10px;
        }

        .operation-type-label,
        .amount-label,
        .date-label,
        .status-label {
          font-size: 16px;
          font-weight: 500;
          color: #686868;
          @media (max-width: 640px) {
            font-size: 12px;
          }
        }

        .operation-type-value,
        .amount-value,
        .date-value,
        .status-value {
          font-size: 24px;
          font-weight: 600;
          color: var(--c-black);
          @media (max-width: 640px) {
            font-size: 16px;
          }
        }

        .status {
          border-radius: 20px;
          &-finished {
            background-color: green;
            div {
              color: white !important;
            }
          }
          &-canceled {
            background-color: red;
            div {
              color: white !important;
            }
          }
          &-handling {
            background-color: var(--c-gray);
          }
        }

        .button {
          align-self: center;
        }
      }
    }
  }
  .table-empty {
    background-color: white;
    min-height: 210px;
    display: flex;

    p {
      margin: auto;
      color: #686868;
      font-size: 16px;
      font-weight: 500;
    }
  }
}
</style>
