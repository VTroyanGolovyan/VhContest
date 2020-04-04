<template>
  <div class="hello">
    <div>VHcontest</div>
    <form v-on:submit="sendData">
      <input v-model="email" type="email">
      <input v-model="password" type="password">
      <input type="submit">
      <div>
        {{error}}
      </div>
    </form>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'SignIn',
  data () {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    sendData: function () {
      axios
        .get(this.$baseLink + '/signin', {
          email: this.email,
          password: this.password
        })
        .then(response => {
          switch (response.data.status) {
            case 0:
              this.$token = response.data.$token
              this.$refreshToken = response.data.refreshToken
              this.$router.push('/TaskList')
              break
            default:
          }
        })
    }
  },
  mounted () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
