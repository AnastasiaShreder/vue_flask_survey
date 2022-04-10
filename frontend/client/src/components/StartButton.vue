<template>
  <div class="start-wrapper">
    <div class="start-wrapper__border"></div>
    <div class='start-wrapper__btn'>
      <button class='start-btn' @click='onClickStartTest'>Начать тестирование</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StartButton',
  methods: {
    onClickStartTest() {
      axios.get('http://localhost:5000/quiz')
        .then((response) => {
        // eslint-disable-next-line no-console
          console.log(response.data);
        })
      // Если запрос с ошибкой
        .catch((error) => {
        // eslint-disable-next-line no-console
          console.log(error);
        });
      // получение всех вопросов и ответов
    },
  },
};
</script>

<style>
.start-wrapper{
  width: 50%;
  position: absolute;
  margin-top: 250px;
  margin-left: 25%;
  height: 300px;
}
.start-wrapper__border {
  /* position: absolute; */
  left: 0px;
  top: 0px;
  right: 0px;
  bottom: 0px;
}
.start-wrapper__btn{
  margin-top: 115px;
  margin-right: 300px;
}
.start-btn{
  position: absolute;
  background: #2C91F3;
  padding: 16px 24px;
  box-shadow: 6px 6px 1px rgba(255, 252, 252, 0.36);
  border-radius: 6px;
  border: none;
  color: white;
  font-weight: 400;
  font-size: 24px;
  line-height: 30px;
  text-align: center;
  cursor: pointer;
  z-index: 3;
}
.start-btn:hover{
  background: #8c49d3a9;
}
.start-wrapper:before,
.start-wrapper:after,
.start-wrapper__border:before,
.start-wrapper__border:after {
  position: absolute;
  width: 235px;
  height: 155px;
  content: '';
  border-color: #7BABF2;
  border-style: solid;
}

.start-wrapper:before {
  display: none;
}

.start-wrapper:after {
  right: 0px;
  top: 0px;
  border-width: 3px 3px 0 0;
}

.start-wrapper__border:before {
  display: none;
}

.start-wrapper__border:after {
  left: 0px;
  bottom: 0px;
  border-width: 0 0 3px 3px;
}
</style>
