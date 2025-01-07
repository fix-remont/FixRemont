<script setup lang="ts"></script>

<template>
  <section class="margin-b-glob block">
    <h1 class="title-glob">Главная</h1>
    <div class="boxes">
      <div class="box1 radius-glob">
        <p class="title">Приглашайте новых клиентов и зарабатывайте с нами</p>
        <div class="wrap">
          <div class="texts">
            <p class="text">Ваша ссылка:</p>
            <p class="link hover">ref.fix-remont.ru/8GTS7LX82390</p>
            <hr />
          </div>
          <SharedButton fillBlack style="align-self: end">Скопировать ссылку</SharedButton>
        </div>
      </div>
      <div class="box2 radius-glob">
        <div class="wrapper">
          <img class="qr-code" src="/images/header-signed/qr-code.png" alt="qr-code" />
          <p>Мой QR-код для приглашения</p>
        </div>
        <SharedButton fillOrange>Открыть</SharedButton>
      </div>
    </div>
  </section>
</template>

<style scoped>
.block {
  margin-top: 20px;
  .boxes {
    display: flex;
    gap: 20px;

    @media (max-width: 1400px) {
      flex-direction: column;
    }

    .box2 {
      padding: 50px 40px;
      background-color: var(--c-black);
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      @media (max-width: 640px) {
        padding: 15px 10px;
      }

      .wrapper {
        color: white;
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
        .qr-code {
          padding: 5px;
          background-color: white;
          border-radius: 10px;
          width: 120px;
          height: 120px;
        }
        p {
          font-size: 32px;
          font-weight: 600;
          @media (max-width: 640px) {
            font-size: 18px;
          }
        }
      }
    }

    .box1 {
      background-color: var(--c-orange);
      color: white;
      padding: 50px 40px;
      font-weight: 600;
      @media (max-width: 640px) {
        padding: 15px 10px;
      }
      .title {
        font-size: 32px;
        width: 70%;
        margin-bottom: 20px;
        @media (max-width: 1400px) {
          width: initial;
        }
        @media (max-width: 640px) {
          font-size: 22px;
        }
      }
      .wrap {
        display: flex;
        gap: 30px;
        @media (max-width: 1400px) {
          flex-direction: column;
        }

        .texts {
          display: flex;
          flex-direction: column;
          gap: 20px;
          .text {
            font-size: 18px;
            font-weight: 500;
            @media (max-width: 640px) {
              font-size: 12px;
            }
          }
          .link {
            font-size: 20px;

            @media (max-width: 640px) {
              font-size: 14px;
            }
          }
        }
      }
    }
  }
}
</style>
