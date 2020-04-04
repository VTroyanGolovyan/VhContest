<template>
  <div>
    <Header></Header>
    <div>
      <div v-for="task in tasks" v-bind:key="task.id">
        <div>
          {{ task.id }}
        </div>
        <div>
          {{ task.name }}
        </div>
        <div>
          {{ task.condition }}
        </div>
        <div>
          TL {{ task.timeLimit }}
        </div>
        <div>
          ML {{ task.memoryLimit }}
        </div>
      </div>
    </div>
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
