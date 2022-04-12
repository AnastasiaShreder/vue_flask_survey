import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    numQuestion: 1,
    countQuestions: 0,
    listQuestions: [],
    listAnswers: {},
    listScore: { A: 0, W: 0, O: 0 },
  },
  getters: {
    NUM_QUESTION: state => state.numQuestion,
    CNT_QUESTIONS: state => state.countQuestions,
    QUESTIONS: state => state.listQuestions,
    ANSWERS: state => state.listAnswers,
    LIST_SCORE: state => state.listScore,
  },
  mutations: {
    CHANGE_COUNT_QUESTION(state, cnt) {
      state.countQuestions = cnt;
    },
    CHANGE_NUM_QUESTION(state) {
      state.numQuestion += 1;
    },
    RESET_NUM_QUESTION(state) {
      state.numQuestion = 1;
    },
    CHANGE_LIST(state, newList) {
      state.listQuestions = newList;
    },
    CHANGE_ANSWERS(state, newList) {
      state.listAnswers = newList;
    },
    CHANGE_SCORE(state, method) {
      state.listScore[method] += 1;
    },
  },
  actions: {
    changeCnt({ commit }, cnt) {
      const newCnt = cnt;
      commit('CHANGE_COUNT_QUESTION', newCnt);
    },
    changeNum({ commit }) {
      commit('CHANGE_NUM_QUESTION');
    },
    changeList({ commit }, list) {
      const newList = list;
      commit('CHANGE_LIST', newList);
    },
    changeAnswers({ commit }, list) {
      const newList = list;
      commit('CHANGE_ANSWERS', newList);
    },
    changeScore({ commit }, method) {
      commit('CHANGE_SCORE', method);
    },
    resetNum({ commit }) {
      commit('RESET_NUM_QUESTION');
    },
  },
  modules: {},
});
