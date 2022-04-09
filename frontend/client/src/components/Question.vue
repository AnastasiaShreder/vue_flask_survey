<template>
  <div class="quiz-wrapper__question">
        <div class="question__num">Вопрос 14/25</div>
        <div class="question__text">Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Nihil iste molestias animi doloremque
          sed quod quisquam maiores adipisci enim voluptatem deleniti excepturi assumenda sit,
          nobis at incidunt repudiandae, minima debitis!
        </div>
      </div>
</template>

<script>
export default {
  name: 'Question',
};

</script>

<style>
.quiz-wrapper__question{
  margin: auto;
  font-style: normal;
  font-weight: 200;
  font-size: 25px;
  line-height: 40px;
  text-align: center;
  width: 80%;
}
.question__num{
  font-size: 20px;
  font-weight: 500;
}
.question__text{
  margin-top: 15px;
}

</style>
