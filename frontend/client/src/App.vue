<template>
  <div id="app">
    <transition name="fade" mode="out-in">
      <router-view>
      </router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 1340px;
  /* min-width: 700px; */
  height: 824px;
  margin: auto;
  margin-top: 60px;
  overflow:hidden;
  border: 1px rgb(255, 255, 255) solid;
  background-color: blue;
  background: url('\assets\background.png') no-repeat;
  background-size: cover;
  box-shadow: 0px 1px 10px rgba(62, 139, 159, 0.5);
}
body{
  font-family: Roboto, Helvetica, Arial, sans-serif;
  background: url('\assets\background.png') no-repeat;
  background-size: cover;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
