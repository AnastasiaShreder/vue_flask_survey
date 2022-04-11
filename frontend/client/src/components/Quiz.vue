<template>
  <div class="quiz-wrapper__answers" >
    <div class="answers__A answer answer-animated answer-back">
      <div class="answer__box" @click="onClickAnswer">
        <div class="letter__wrapper">
          <div class="answers__letter">
            <p><img src="../assets/A.svg" alt="A" width="15px" height="15px"></p>
          </div>
        </div>
        <div class="answers__text">
          {{ getAnswers('0') }}
        </div>
      </div>
    </div>
    <div class="answers__B answer">
      <div class="answer__box" @click="onClickAnswer">
        <div class="letter__wrapper">
          <div class="answers__letter">
            <p><img src="../assets/B.svg" alt="B" width="15px" height="15px"></p>
          </div>
        </div>
        <div class="answers__text">
          {{ getAnswers('1') }}
        </div>
      </div>
    </div>
    <div class="answers__C answer">
      <div class="answer__box" @click="onClickAnswer">
        <div class="letter__wrapper">
          <div class="answers__letter">
            <p><img src="../assets/C.svg" alt="C" width="16px" height="15px"></p>
          </div>
        </div>
        <div class="answers__text">
          {{ getAnswers('2') }}
        </div>
      </div>
    </div>
    <div class="answers__D answer">
      <div class="answer__box" @click="onClickAnswer">
        <div class="letter__wrapper">
          <div class="answers__letter">
            <p><img src="../assets/D.svg" alt="D" width="15px" height="15px"></p>
          </div>
        </div>
        <div class="answers__text">
          {{ getAnswers('3') }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Quiz',
  data: () => ({
    isOver: false,
  }),
  methods: {
    ...mapActions(['changeScore', 'changeNum']),
    onClickAnswer(event) {
      // const elem = Object.entries((this.ANSWERS)[this.NUM_QUESTION - 1]);
      // console.log(elem[0][0]);
      const answers = (this.ANSWERS)[this.NUM_QUESTION - 1];
      const el = (event.target.textContent).trim();
      console.log(el);
      const method = answers[el];
      // this.changeScore();
      console.log(method);
      if (this.NUM_QUESTION < this.CNT_QUESTIONS) {
        this.changeScore(method);
        this.changeNum();
      } else {
        this.changeScore(method);
        console.log('the end!');
        this.$emit('passQuiz');
        this.isOver = true;
      }
    },
  },
  computed: {
    ...mapGetters(['NUM_QUESTION', 'CNT_QUESTIONS', 'QUESTIONS', 'ANSWERS']),
    // getAnswers() {
    //   return n => (Object.entries(this.ANSWERS)[`${n}`][0][0]);
    // },
    getAnswers() {
      const elem = Object.entries((this.ANSWERS)[this.NUM_QUESTION - 1]);
      return n => (elem[`${n}`][0]);
    },
  },
};
</script>

<style>
.letter__wrapper {
  /* height: 100px; */
  position: relative;
  box-sizing: content-box;
  margin-right: 20px;
}
.quiz-wrapper__answers {
  margin: auto;
  width: 70%;
  height: 350px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.answer {
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 32px;
  width: 100%;
  transition: all .2s;
  /* padding: 2px; */
}
.answer:hover{
  background: #9a8cdfc4;
  cursor: pointer;
}
.answer:hover .answers__letter{
  background: radial-gradient(
    ellipse at center,
    rgb(179, 195, 252) 70%,
    /* rgba(0, 128, 172, 1) 70%, */ rgba(0, 128, 172, 0) 75%
  );
}
.answer:active{
  background:#beb4ecc4;
  transform: translateY(-10px);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.answer__box {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  padding-left: 15px;
}
.answers__letter {
  background: radial-gradient(
    ellipse at center,
    rgba(52, 195, 252, 100%) 70%,
    /* rgba(0, 128, 172, 1) 70%, */ rgba(0, 128, 172, 0) 75%
  );
  width: 28px;
}
.answers__text {
  display: flex;
  /* justify-content: center; */
  align-items: center;
  text-align:start;
}
.answers__letter {
  color: white;
  position: relative;
  margin: 0;
}
.answers__letter p {
  font-size: 21px;

  height: 100%;
  line-height: 1.25;
  padding: 0;
  text-align: center;
  /* text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.3); */
}
.answers__letter::before {
  content: "";
  float: left;
  height: 100%;
  width: 50%;
  shape-outside: polygon(
    0 0,
    98% 0,
    50% 6%,
    23.4% 17.3%,
    6% 32.6%,
    0 50%,
    6% 65.6%,
    23.4% 82.7%,
    50% 94%,
    98% 100%,
    0 100%
  );
  shape-margin: 7%;
}
.answers__letter p::before {
  content: "";
  float: right;
  height: 100%;
  width: 50%;
  shape-outside: polygon(
    2% 0%,
    100% 0%,
    100% 100%,
    2% 100%,
    50% 94%,
    76.6% 82.7%,
    94% 65.6%,
    100% 50%,
    94% 32.6%,
    76.6% 17.3%,
    50% 6%
  );
  shape-margin: 7%;
}
</style>
