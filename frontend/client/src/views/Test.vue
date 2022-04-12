<template>
  <div>
    <div class="quiz-wrapper">
      <Question></Question>
      <hr class="quiz-line">
      <Quiz @passQuiz="passQuiz"></Quiz>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Question from '@/components/Question';
import Quiz from '@/components/Quiz';

export default {
  name: 'Test',
  components: {
    Question,
    Quiz,
  },
  methods: {
    passQuiz() {
      console.log('the end!');
      this.$router.push({ name: 'Result' });
    },
  },
};
</script>

<style>
.quiz-wrapper{
  margin: 0 auto;
  width: 70%;
  margin-top: 50px;
}
.quiz-line{
  height: 3px;
  background-color: #4cacf69b;
  border: none;
  margin-top: 30px;
  margin-bottom: 50px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
