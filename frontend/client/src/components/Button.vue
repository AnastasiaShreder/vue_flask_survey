<template>
  <div>
    <div class="btn-wrapper">
      <button class='btn-hover' @click="onClickRestart">Повторить опрос</button>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  name: 'Button',
  methods: {
    ...mapActions(['changeNum', 'resetNum']),
    onClickRestart() {
      this.resetNum();
    },
  },
};
</script>

<style>
.btn-wrapper{
  /* float: right; */
  margin-top: 25px;
  width: 98%;
  display: flex;
  justify-content: flex-end;
}
.btn-hover {
    width: 200px;
    font-size: 16px;
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    text-decoration: none;
    /* margin: 20px; */
    height: 55px;
    text-align:center;
    border: none;
    background-size: 300% 100%;
    border-radius: 50px;
    moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
    background-image: linear-gradient(to right, #6F1ED7, #3aafdd, #30AAD0, #6F1ED7);
    box-shadow: 0 4px 15px 0 rgba(116, 79, 168, 0.75);
}
.btn-hover:hover {
    background-position: 100% 0;
    moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}
.btn-hover:focus {
  outline: none;
}
.btn-hover:active {
  background:#30AAD0;
}
</style>
