import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    numQuestion: 1,
    countQuestions: 0,
    listQuestions: [],
  },
  getters: {
    NUM_QUESTION: state => state.numQuestion,
    CNT_QUESTIONS: state => state.countQuestions,
    QUESTIONS: state => state.listQuestions,
  },
  mutations: {
    CHANGE_COUNT_QUESTION(state, cnt) {
      state.countQuestions = cnt;
    },
    CHANGE_LIST(state, newList) {
      state.listQuestions = newList;
    },
  },
  actions: {
    changeNum({ commit }, num) {
      const newNum = num;
      commit('CHANGE_COUNT_QUESTION', newNum);
    },
    changeList({ commit }, list) {
      const newList = list;
      commit('CHANGE_LIST', newList);
    },
  },
  modules: {},
});
