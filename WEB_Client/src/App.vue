<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');
    #app {
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
    }

    body {
      padding: 0;
      margin: 0;
    }

    select {
      background: #d2d2d2;
      padding: 0 16px;
      width: 100%;
      border: none;
      outline: none;
      position: relative;
      appearance: none;
      height: 40px;
    }

    .select-wrapper {
      position: relative;
      border-radius: 4px;
      overflow: hidden;
      box-sizing: border-box;
      padding-right: 20px;
    }

    .select-wrapper::after {
      content: "<>";
      display: flex;
      width: 40px;
      height: 20px;
      position: absolute;
      top: 10px;
      font-size: 12px;
      right: -10px;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      transform: rotate(90deg);
      color: white;
      background-color: #a61111;
      cursor: no-drop;
    }

</style>
