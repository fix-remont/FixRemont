<script setup lang="ts">
const items = [
  { label: 'Карта МИР', codeNumber: 2980 },
  { label: 'Карта МИР', codeNumber: 2980 },
  { label: 'Карта МИР', codeNumber: 2980 }
]
</script>

<template>
  <article class="withdrowal-types margin-b-glob">
    <h1 class="title">Способы вывода</h1>
    <div class="content">
      <div class="wrap-items" v-if="items.length > 0">
        <div class="item" v-for="item in items">
          <div class="wrap-part wrap-part-1">
            <img class="card-icon" src="/images/cabinet/mir.svg" alt="" />
            <span class="label">{{ item.label }}</span>
          </div>

          <div class="wrap-part wrap-part-2">
            <div class="wrap-points">
              <span class="point"></span>
              <span class="point"></span>
              <span class="point"></span>
              <span class="point"></span>
            </div>
            <span class="code-number">{{ item.codeNumber }}</span>
            <img class="close-button hover" src="/images/cabinet/close-button.svg" alt="add-item" />
          </div>
        </div>
      </div>
      <div class="item-empty" v-else>У вас нет способов вывода</div>
      <div class="add-item">
        <p class="text">Добавить новый способ вывода</p>
        <img class="add-button hover" src="/images/cabinet/plus-button.svg" alt="add-item" />
      </div>
    </div>
  </article>
</template>

<style scoped lang="postcss">
.withdrowal-types {
  .title {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 20px;
  }

  .content {
    background-color: white;
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 20px;

    .wrap-items {
      display: flex;
      flex-direction: column;
      gap: 10px;

      .item {
        display: flex;
        align-items: center;
        font-size: 20px;
        font-weight: 600;
        gap: 20px;
        border-bottom: solid 1px var(--c-gray);
        padding: 5px;
        width: 100%;

        @media (max-width: 640px) {
          flex-direction: column;
          align-items: stretch;
        }

        .wrap-part {
          display: flex;
          gap: 20px;
          align-items: center;
          /* &-1 { */
          /* } */
          &-2 {
            flex-grow: 1;
          }
        }

        .label {
          margin-right: 20px;
        }
        .wrap-points {
          .point {
            display: inline-block;
            width: 10px; /* Размер точки */
            height: 10px;
            background-color: black; /* Цвет точки */
            border-radius: 50%; /* Круглая форма */
            margin-right: 4px; /* Расстояние между точками */
          }
        }
        /* .code-number {
        } */
        .close-button {
          width: 50px;
          height: 50px;
          margin-left: auto;
        }
      }
    }
    .add-item {
      display: flex;
      align-items: center;
      font-size: 16px;
      font-weight: 600;
      .text {
      }
      .add-button {
        margin-left: auto;
        width: 50px;
        height: 50px;
      }
    }

    .item-empty {
      text-align: center;
      color: #686868;
      font-size: 16px;
      font-weight: 500;
    }
  }
}
</style>
