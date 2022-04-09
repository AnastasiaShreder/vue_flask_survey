<template>
  <div>
    <!-- <ArrowBack></ArrowBack> -->
    <router-link to="/"><Button></Button></router-link>
    <Results></Results>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import ArrowBack from '@/components/ArrowBack';
import Button from '@/components/Button';
import Results from '@/components/Results';

export default {
  name: 'Test',
  components: {
    ArrowBack,
    Button,
    Results,
  },
};
</script>

<style>
a { text-decoration: none; }
</style>
