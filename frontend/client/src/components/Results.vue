<template>
  <div class="results-wrapper">
    <div class="results__name">
        Agile - Scrum
    </div>
    <div class="results__description">
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit.
        Soluta beatae blanditiis sapiente molestias laudantium esse
        nemo cumque expedita pariatur natus.
        Doloremque id ab porro modi molestias
        earum sapiente, nam, deserunt reprehenderit
        impedit expedita esse ipsam necessitatibus aliquam saepe at.
        Assumenda alias maiores soluta similique
        excepturi debitis explicabo cum repellendus error?</p>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit.
        Soluta beatae blanditiis sapiente molestias laudantium esse
        nemo cumque expedita pariatur natus.
        Doloremque id ab porro modi molestias
        earum sapiente, nam, deserunt reprehenderit
        impedit expedita esse ipsam necessitatibus aliquam saepe at.
        Assumenda alias maiores soluta similique
        excepturi debitis explicabo cum repellendus error?</p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Results',

  computed: {
    ...mapGetters(['NUM_QUESTION', 'CNT_QUESTIONS', 'QUESTIONS', 'ANSWERS']),
    resultMethod() {
      const elem = Object.entries((this.ANSWERS)[this.NUM_QUESTION - 1]);
      return 0;
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
