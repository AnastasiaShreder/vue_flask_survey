<template>
  <div class="quiz-wrapper__question">
        <div class="question__num">Вопрос {{ NUM_QUESTION }}/{{ CNT_QUESTIONS }}</div>
        <div class="question__text">{{ questionText }}
        </div>
      </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Question',
  computed: {
    ...mapGetters(['NUM_QUESTION', 'CNT_QUESTIONS', 'QUESTIONS']),
    questionText() {
      return this.QUESTIONS[this.NUM_QUESTION - 1];
    },
  },
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
