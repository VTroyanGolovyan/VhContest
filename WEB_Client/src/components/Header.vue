<template>
  <div>
    <header>
      <div class="logo">
        VHcontest
      </div>
      <nav>
        <router-link to="/TaskList">Aрхив</router-link>
        <div v-on:click="signOut">Выйти</div>
      </nav>
    </header>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Header',
  data () {
    return {
    }
  },
  methods: {
    signOut: function () {
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
      axios
        .get(this.$baseLink + '/sign/out')
        .then(response => {

        })
      this.$router.push('/')
    }
  },
  mounted () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    header {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      padding: 0px 20%;
      height: 72px;
      width: 60%;
      box-shadow: 0 0 5px 1px #b5b5b5;
    }

    .logo {
      color: #a61111;
      font-size: 1.75rem;
    }

    nav {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      height:72px;
    }

    nav a, nav div {
      text-decoration: none;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: black;
      height:72px;
      cursor: pointer;
      padding: 0 16px;
      font-size: 1rem;
      position: relative;
    }

    nav a::after, nav div::after {
      display: flex;
      content: " ";
      height: 2px;
      width: 0%;
      position: absolute;
      bottom: 0px;
      background: #a61111;
      transition: all ease 0.6s;
    }

    nav a:hover::after, nav div:hover::after {
      width: 100%;
    }
</style>
