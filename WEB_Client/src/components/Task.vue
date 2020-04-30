<template>
  <div>
    <Header></Header>
    <section class="task-list">
      Задача {{ $route.params.id }}
    </section>
    <form v-on:submit='submitSolution'>
      <textarea v-model="solution"></textarea>
      <input type="submit">
    </form>
    <Footer></Footer>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Task',
  data () {
    return {
      solution: ''
    }
  },
  methods: {
    fetchTasks: function () {
      axios
        .get(this.$baseLink + '/' + 'task/' + this.$route.params.id)
        .then(response => {
          this.tasks = response.data.data
        })
    },
    submitSolution: function () {
      axios
        .post(this.$baseLink + '/check', {
          id: this.$route.params.id,
          solution: this.solution
        })
        .then(response => {
          switch (parseInt(response.data.status)) {
            case 0:
              this.$router.push('/TaskList')
              break
            case 1:
              this.$router.push('/TaskList')
              break
            default:
          }
        })
    }
  },
  mounted () {
    this.fetchTasks()
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
