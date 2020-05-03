<template>
  <div class="signin">
    <h2>VHcontest</h2>
    <form v-on:submit="sendData">
      <input class="submit-text" v-model="name" type="text" placeholder="Имя">
      <input class="submit-text" v-model="lastName" type="text" placeholder="Фамилия">
      <input class="submit-text" v-model="name" type="text" placeholder="Отчество">
      <input class="submit-text" v-model="name" type="text" placeholder="Имя">
      <input class="submit-text" v-model="email" type="email" placeholder="Почта">
      <input class="submit-text" v-model="password" type="password" placeholder="Пароль">
      <input class="submit-text" v-model="checkPassword" type="password" placeholder="Повторите пароль">
      <input class="submit-input" type="submit" value="Зарегистрироваться">
      <div class="error" v-if="error != ''">
        {{error}}
      </div>
      <router-link to="/">У меня есть аккаунт, войти</router-link>
    </form>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'SignIn',
  data () {
    return {
      name: '',
      lastName: '',
      patronymic: '',
      email: '',
      password: '',
      checkPassword: '',
      error: ''
    }
  },
  methods: {
    sendData: function () {
      axios
        .post(this.$baseLink + '/sign/up', {
          email: this.email,
          password: this.password
        })
        .then(response => {
          switch (parseInt(response.data.status)) {
            case 0:
              /* Make it global for all components */
              this.$token = response.data.token
              this.$refreshToken = response.data.refreshToken
              /* Save to localStorage */
              localStorage.token = response.data.token
              localStorage.refreshToken = response.data.refreshToken
              /* Refresh to the tasks list */
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
    /* checks if we were signed in */
    if (localStorage.token && localStorage.refreshToken) {
      this.$token = localStorage.token
      this.$refreshToken = localStorage.refreshToken
      this.$router.push('/TaskList')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
   h2 {
     color: #a61111;
     font-size: 2.5rem;
     margin: 0;
     padding: 0;
     margin-bottom: 32px;
     font-family: 'Open Sans', sans-serif;
   }

   .signin {
     display: flex;
     flex-direction: column;
     justify-content: center;
     align-items: center;
     width: 100%;
     height: 100vh;
   }

   .signin form {
     display: flex;
     flex-direction: column;
     justify-content: flex-start;
     align-items: center;
     width: 30%;
     padding: 32px;
     box-shadow: 0 0 5px 1px #b5b5b5;
     border-radius: 3px;
   }

   .signin form input {
     width: calc(100% - 16px);
     padding: 8px;
     margin-bottom: 32px;
     font-size: 1rem;
     border: none;
     outline: none;
     text-align: center;
   }

   .signin form .submit-input {
     display: flex;
     border: solid 2px #a61111;
     box-sizing: content-box;
     background: #a61111;
     color: white;
     padding: 8px;
     margin-bottom: 16px;
     cursor: pointer;
     transition: all ease 0.6s;
   }

   .signin form .submit-text {
     border-bottom: solid 2px #a61111;
   }

   .signin form .submit-input:hover {
     background: white;
     color: #a61111;
   }
</style>
