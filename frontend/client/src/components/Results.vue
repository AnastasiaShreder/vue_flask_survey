<template>
  <div class="results-wrapper">
    <div class="results__name">
      <span class='method'>{{ resultMethod[0] }}</span>
      <br>подходит Вашему проекту на {{ resultMethod[2] }}%
    </div>
    <div class="results__description">
      <p>{{ resultMethod[1] }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { scrum, fdd, dsdm } from '.././assets/description';

export default {
  name: 'Results',
  computed: {
    ...mapGetters(['NUM_QUESTION', 'CNT_QUESTIONS', 'QUESTIONS', 'ANSWERS', 'LIST_SCORE']),
    resultMethod() {
      const res = {};
      if ((this.LIST_SCORE.F >= this.LIST_SCORE.S) && (this.LIST_SCORE.F >= this.LIST_SCORE.D)) {
        res[0] = 'Feature Driven Development';
        res[1] = fdd;
        res[2] = (this.LIST_SCORE.F / this.CNT_QUESTIONS) * 100;
      }
      if ((this.LIST_SCORE.D >= this.LIST_SCORE.F) && (this.LIST_SCORE.D >= this.LIST_SCORE.S)) {
        res[0] = 'Dynamic Systems Development Method';
        res[1] = dsdm;
        res[2] = (this.LIST_SCORE.D / this.CNT_QUESTIONS) * 100;
      }
      if ((this.LIST_SCORE.S >= this.LIST_SCORE.F) && (this.LIST_SCORE.S >= this.LIST_SCORE.D)) {
        res[0] = 'Scrum';
        res[1] = scrum;
        res[2] = (this.LIST_SCORE.S / this.CNT_QUESTIONS) * 100;
      }
      return res;
    },
  },
};
</script>

<style>
.results-wrapper{
  margin: auto;
  width: 80%;
  /* position: absolute; */
  margin-top: 130px;
  height: 300px;
}
.results__name{
  background: linear-gradient(135deg, #12BCB0 20%, #b587de 70%) !important;
  color: #fff;
  font-size: 18px !important;
}
.method{
  text-transform: uppercase;
  font-size: 36px;
}
.results__name, .results__description{
  background: #fff;
  border-radius: 40px;
  text-align: start;
  padding: 20px;
  padding-left: 30px;
  font-size: 26px;
}
.results__description{
  margin-top: 20px;
  background:
    linear-gradient(white, white) padding-box,
    linear-gradient(to right, #12BCB0 20%, #b587de 70%) border-box;
  border-radius: 40px;
  border: 10px solid transparent;
  /* border: 20px solid transparent;
  border-radius: 20px;
  border-image: linear-gradient(135deg, #12BCB0 20%, #b587de 70%);
  border-image-slice: 1; */
}
.results__text {
  background: linear-gradient(135deg, #12BCB0 20%, #FABE0E 70%)
}
</style>
