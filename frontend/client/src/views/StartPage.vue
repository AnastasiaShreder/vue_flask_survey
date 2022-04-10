<template>
  <div class='app-wrapper'>
    <!-- <ArrowBack></ArrowBack> -->
    <router-link to="/test" ><StartButton @click='onClickStartTest'></StartButton></router-link>
  </div>
</template>

<script>

// eslint-disable-next-line no-unused-vars
import axios from 'axios';
import ArrowBack from '@/components/ArrowBack';
import StartButton from '@/components/StartButton';

export default {
  name: 'StartPage',
  components: {
    ArrowBack,
    StartButton,
  },
  methods: {
    onClickStartTest() {
      axios.get('http://localhost:5000/quiz')
        .then((response) => {
        // eslint-disable-next-line no-console
          console.log(response);
        })
      // Если запрос с ошибкой
        .catch((error) => {
        // eslint-disable-next-line no-console
          console.log(error);
        });
      // получение всех вопросов и ответов
    },
  },
  created() {
    axios.get('http://localhost:5000/ping')
      // Если запрос успешен
      .then((response) => {
        // eslint-disable-next-line no-console
        console.log('Сервер готов к работе ', response);
      })
      // Если запрос с ошибкой
      .catch((error) => {
        // eslint-disable-next-line no-console
        console.log(error);
      });
  },
};
</script>

<style>
.app-wrapper{
  position: relative;
}
</style>
