<template>
  <div class="signin">
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
        .post(this.$baseLink + '/sign/in', {
          email: this.email,
          password: this.password
        })
        .then(response => {
          switch (parseInt(response.data.status)) {
            case 0:
              this.$token = response.data.token
              this.$refreshToken = response.data.refreshToken
              this.$router.push('/TaskList')
              break
            case 1:
              this.error = 'Wrong email'
              break
            case 2:
              this.error = 'Wrong password'
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
   .signin {
     display: flex;
     flex-direction: column;
     justify-content: center;
     align-items: center;
     width: 100%;
     height: 100vh;
   }
</style>
