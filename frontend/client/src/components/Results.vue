<template>
  <div class="results-wrapper">
    <div class="results__name">
        {{ resultMethod }}
    </div>
    <div class="results__description">
      <p>{{ resultDescription }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { agile, waterfall } from '.././assets/description';

export default {
  name: 'Results',

  computed: {
    ...mapGetters(['NUM_QUESTION', 'CNT_QUESTIONS', 'QUESTIONS', 'ANSWERS', 'LIST_SCORE']),
    resultMethod() {
      return (this.LIST_SCORE.A >= this.LIST_SCORE.W) ? 'Agile' : 'Waterfall';
    },
    resultDescription() {
      return (this.LIST_SCORE.A >= this.LIST_SCORE.W) ? agile : waterfall;
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
}
</style>
