<template>
  <div id='root-default'>
    <header></header>
    <section class="content">
      <slot/>
    </section>
    <footer>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Default-test',
};
</script>

<style scoped>
#root-default {
  width: 1240px;
  height: 300px;
  margin: auto;
  overflow:hidden;
  background-color: blue;
}
</style>
