/* eslint-disable no-undef */
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    numQuestion: 1,
    countQuestions: 0,
    listQuestions: {},
  },
  getters: {
    NUM_QUESTION: state => state.numQuestion,
    CNT_QUESTIONS: state => state.countQuestions,
    QUESTIONS: state => state.listQuestions,
  },
  mutations: {
    CHANGE_NUM_QUESTION(newNum) {
      state.numQuestion = newNum;
    },
    CHANGE_LIST(newNum) {
      state.numQuestion = newNum;
    },
  },
  actions: {
    changeNum({ commit }, num) {
      const newNum = num;
      commit('CHANGE_EFF', newNum);
    },
  },
});
