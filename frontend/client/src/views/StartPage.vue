<template>
  <div class='app-wrapper'>
    <!-- <ArrowBack></ArrowBack> -->
    <router-link to="/test"><StartButton></StartButton></router-link>
  </div>
</template>

<script>

// eslint-disable-next-line no-unused-vars
import ArrowBack from '@/components/ArrowBack';
import StartButton from '@/components/StartButton';

export default {
  name: 'StartPage',
  components: {
    ArrowBack,
    StartButton,
  },
};
</script>

<style>
.app-wrapper{
  position: relative;
}
</style>
