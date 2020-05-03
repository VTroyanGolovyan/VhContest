<template>
  <div>
    <Header></Header>
    <section class="task-list">
      <div class="task-list-header">
        <div>
          ID
        </div>
        <div>
          Имя
        </div>
        <div>
          Лимит времени
        </div>
        <div>
          Лимит памяти
        </div>
      </div>
      <router-link tag="div" :to="{ name: 'Task', params: { id: task.id }}" class="task-item" v-for="task in tasks" :key="task.id">
        <div>
          {{ task.id }}
        </div>
        <div>
          {{ task.name }}
        </div>
        <div>
          {{ task.time_limit }}ms
        </div>
        <div>
          {{ task.memory_limit }}mb
        </div>
      </router-link>
    </section>
    <Footer></Footer>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'TaskList',
  data () {
    return {
      tasks: []
    }
  },
  methods: {
    fetchTasks: function () {
      axios
        .get(this.$baseLink + '/' + 'task_list')
        .then(response => {
          this.tasks = response.data.data
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
