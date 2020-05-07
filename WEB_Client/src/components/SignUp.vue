<template>
  <div class="signin">
    <h2>VHcontest</h2>
    <form v-on:submit="sendData">
      <input class="submit-text" v-model="name" type="text" placeholder="Имя">
      <input class="submit-text" v-model="last_name" type="text" placeholder="Фамилия">
      <input class="submit-text" v-model="patronymic" type="text" placeholder="Отчество">
      <input class="submit-text" v-model="email" type="email" placeholder="Почта">
      <input class="submit-text" v-model="password" type="password" placeholder="Пароль">
      <input class="submit-text" v-model="check_password" type="password" placeholder="Повторите пароль">
      <label class="submit-checkbox">
        Соглашаюсь поставить Владу отл. 10
        <input v-model="otl" type="checkbox" required>
      </label>
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
      last_name: '',
      patronymic: '',
      email: '',
      password: '',
      check_password: '',
      error: ''
    }
  },
  methods: {
    sendData: function () {
      axios
        .post(this.$baseLink + '/sign/up', {
          name: this.name,
          last_name: this.last_name,
          patronymic: this.patronymic,
          email: this.email,
          password: this.password,
          check_password: this.check_password
        })
        .then(response => {
          switch (parseInt(response.data.status)) {
            case 0:
              this.error = ''
              break
            case 1:
              this.error = 'Пароли не совпадают'
              break
            case 2:
              this.error = 'Почта занята'
              break
            case 3:
              this.error = 'Короткий пароль'
              break
            case 4:
              this.error = 'В пароле должны быть и большие и маленькие символы'
              break
            case 5:
              this.error = 'Пароль должен содержать минимум 5 уникальных символов'
              break
            case 6:
              this.error = 'В пароле должны быть цифры'
              break
          }
        }).then(() => {
          if (this.error === '') {
            axios
              .post(this.$baseLink + '/sign/in', {
                email: this.email,
                password: this.password
              })
              .then(response => {
                localStorage.token = response.data.token
                localStorage.refreshToken = response.data.refreshToken
                this.$router.push('/')
              })
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

   .submit-checkbox {
     display: flex;
     flex-direction: row;
     justify-content: center;
     align-items: center;
     width: 100%;
     margin-bottom: 32px;
     font-family: 'Open Sans', sans-serif;
     cursor: pointer;
   }

   .submit-checkbox input[type=checkbox] {
     width: auto;
     height: auto;
     margin: 0;
     padding: 0;
     margin-left: 16px;
     cursor: pointer;
   }

   .signin form .submit-input:hover {
     background: white;
     color: #a61111;
   }

   a {
     font-family: 'Open Sans', sans-serif;
   }

   .error {
     color:  #a61111;
     font-family: 'Open Sans', sans-serif;
   }
</style>
