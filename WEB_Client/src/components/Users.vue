<template>
  <div>
    <Header></Header>
    <section class="list">
      <div class="list-header">
        <div>
          ID
        </div>
        <div>
          Фамилия
        </div>
        <div>
          Имя
        </div>
        <div>
          Отчество
        </div>
        <div>
          Почта
        </div>
      </div>
      <div class="item" v-for="user in users" v-bind:key="user.id">
        <div>
          {{ user.id }}
        </div>
        <div>
          {{ user.name }}
        </div>
        <div>
          {{ user.last_name }}
        </div>
        <div>
          {{ user.patronymic }}
        </div>
        <div>
          {{ user.email }}
        </div>
      </div>
    </section>
    <Footer></Footer>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Users',
  data () {
    return {
      users: []
    }
  },
  methods: {
    fetchUsers: function () {
      axios
        .get(
          this.$baseLink + '/' +
          localStorage.getItem('token') +
          '/' + 'users_list'
        )
        .then(response => {
          if (response.data.status === '0') {
            this.users = response.data.data
          } else {
            this.$router.push('/')
          }
        })
    }
  },
  mounted () {
    this.fetchUsers()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .list {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 60%;
    padding: 32px 20%;
    font-family: 'Open Sans', sans-serif;
  }

  .item, .list-header {
    width: calc(100% - 32px);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    padding: 16px 16px;
  }

  .item div, .list-header div {
      width: 20%;
      overflow: hidden;
      text-overflow: ellipsis;
  }

  .list-header {
    box-shadow: 0 0 5px 1px #b5b5b5;
    border-radius: 4px;
  }

  .item {
    cursor: pointer;
    border-bottom: solid 1px #b5b5b5;
  }
</style>
