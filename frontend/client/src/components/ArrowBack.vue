<template>
  <div class='back'>
    <div class='back-arrow'>
      <img src="..\assets\Arrow.svg" alt="arrow">
    </div>
    <div class='back-txt'>
      На Главную
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArrowBack',
};
</script>

<style>
  .back{
    cursor: pointer;
    position: sticky;
    float: left;
    display: flex;
    margin-left: 37px;
    margin-top: 35px;
    gap: 24px;
    align-items: center;
  }
  .back-arrow{
    display: flex;
    align-items: center;
  }
  .back-txt{
    font-size: 20px;
    vertical-align: middle;
  }
</style>
