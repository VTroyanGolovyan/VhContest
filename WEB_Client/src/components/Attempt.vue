<template>
  <div>
    <Header></Header>
    <section class="task-list">
      <div class="task-list-header">
        <div>
          ID теста
        </div>
        <div>
          Время
        </div>
        <div>
          Память
        </div>
        <div>
          Результат
        </div>
      </div>
      <div class="task-item" v-for="test in tests" v-bind:key="test.id">
        <div>
          {{ test.test_id }}
        </div>
        <div>
          {{ test.time }}ms
        </div>
        <div>
          {{ test.memory }}mb
        </div>
        <div>
          {{ test.result }}
        </div>
      </div>
    </section>
    <Footer></Footer>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Attempt',
  data () {
    return {
      tests: []
    }
  },
  methods: {
    fetchTests: function () {
      axios
        .get(
          this.$baseLink + '/' +
          localStorage.getItem('token') +
          '/' + 'attempt' + '/' +
          this.$route.params.id
        )
        .then(response => {
          if (response.data.status === '0') {
            this.tests = response.data.data
          } else {
            this.$router.push('/')
          }
        })
    }
  },
  mounted () {
    this.fetchTests()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .task-list {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 60%;
    padding: 32px 20%;
    font-family: 'Open Sans', sans-serif;
  }

  .task-item, .task-list-header {
    width: calc(100% - 32px);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    padding: 16px 16px;
  }

  .task-item div, .task-list-header div {
      width: 25%;
  }

  .task-list-header {
    box-shadow: 0 0 5px 1px #b5b5b5;
    border-radius: 4px;
  }

  .task-item {
    cursor: pointer;
    border-bottom: solid 1px #b5b5b5;
  }
</style>
