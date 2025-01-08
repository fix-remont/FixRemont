<script setup lang="ts"></script>

<template>
  <article class="margin-glob block">
    <div class="picture-wrapper">
      <img alt="iphone" src="/images/realtors/block_6.png" />
    </div>
    <div class="right">
      <div class="titles">
        <h2 class="title">
          <span class="orange">
            Выплачиваем от <br />
            1 000 руб</span>
          за каждый замер, даже если договор не закроется
        </h2>
        <p class="subtitle-glob">
          и проводим регулярные розыгрыши IPhone 15 Pro Max среди партнеров
        </p>
      </div>
      <div class="video">
        <div class="img-wrapper">
          <img class="play-button hover" alt="play-button" src="/icons/play-button.svg" />
        </div>
        <div class="notation">
          <p class="text">Посмотреть видео с нашего последнего розыгрыша IPhone</p>
          <p class="time">1:25 мин</p>
        </div>
      </div>
      <NuxtLink>
        <SharedButton>Стать партнером</SharedButton>
      </NuxtLink>
    </div>
  </article>
</template>

<style scoped>
.block {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 5rem;

  @media (max-width: 800px) {
    flex-direction: column;
    gap: 2rem;
  }
}

.picture-wrapper {
  border-radius: 24px;

  @media (max-width: 800px) {
    order: 2;
  }
}

.title {
  font-size: 55px;
  font-weight: 550;
  line-height: 65px;
  width: 75%;

  @media (max-width: 1240px) {
    font-size: 45px;
  }

  @media (max-width: 640px) {
    width: auto;
    font-size: 30px;
    line-height: 40px;
  }
}

.right {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: flex-start;
  width: 50%;

  a {
    width: 100%;
  }

  @media (max-width: 800px) {
    width: 100%;
    align-items: center;
    gap: 1.5rem;
    order: 1;
  }
}

.video {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  width: 50%;

  @media (max-width: 800px) {
    width: 60%;
  }

  .img-wrapper {
    width: 30%;

    @media (max-width: 800px) {
      width: 65%;
    }
  }

  .text {
    font-size: 18px;
    font-weight: bold;
    line-height: 23px;
    margin-bottom: 8px;

    @media (max-width: 800px) {
      font-size: 15px;
      line-height: 18px;
    }
  }

  .time {
    font-size: 12px;
    font-weight: lighter;
  }
}
</style>
