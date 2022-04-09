import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import StartPage from '@/views/StartPage';
import Test from '@/views/Test';
import Result from '@/views/Result';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Start',
      component: StartPage,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
    },
  ],
});
