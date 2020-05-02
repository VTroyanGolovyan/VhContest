<template>
  <div>
    <Header></Header>
    <section class="task">
      <div class="task-info">
        <h2>
           {{ task.id + '. ' + task.name }}
        </h2>
        <div class="limits">
          <div class="limit">
            Время: {{task.time_limit}}ms
          </div>
          <div class="limit">
            Память: {{task.time_limit}}M
          </div>
        </div>
        <div class="condition">
          {{task.condition}}
        </div>
      </div>
      <div class="task-form">
        <form v-on:submit="submitSolution">
          <div class="editor">
            <div id='editor'>
            </div>
          </div>
          <div class="form-bottom">
            <select v-on:change="changeTheme" v-model="theme">
              <option value="1">Темная тема</option>
              <option value="2">Светлая тема</option>
            </select>
            <select v-on:change="changeLanguage" v-model="language">
              <option>python</option>
              <option>javascript</option>
              <option>c++</option>
            </select>
            <input type="submit" value="Отправить решение">
          </div>
        </form>
      </div>
    </section>
    <Footer></Footer>
  </div>
</template>
<script>
import axios from 'axios'
import * as ace from 'brace'

import 'brace/mode/javascript'
import 'brace/mode/python'
import 'brace/mode/c_cpp'

import 'brace/theme/monokai'
import 'brace/theme/chrome'

let editor

export default {
  name: 'Task',
  data () {
    return {
      task: {
        id: 0,
        name: '1',
        condition: '',
        memory_limit: '',
        time_limit: ''
      },
      solution: '',
      language: 'python',
      theme: '1'
    }
  },
  methods: {
    fetchTasks: function () {
      axios
        .get(this.$baseLink + '/' + 'task/' + this.$route.params.id)
        .then(response => {
          this.task = response.data.data
        })
    },
    changeTheme: function () {
      if (this.theme === '1') {
        editor.setTheme('ace/theme/monokai')
      } else {
        editor.setTheme('ace/theme/chrome')
      }
    },
    changeLanguage: function () {
      if (this.language === 'python') {
        editor.getSession().setMode('ace/mode/python')
      } else if (this.language === 'javascript') {
        editor.getSession().setMode('ace/mode/javascript')
      } else if (this.language === 'c++') {
        editor.getSession().setMode('ace/mode/c_cpp')
      }
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
    editor = ace.edit('editor')
    editor.setFontSize('16px')
    editor.setTheme('ace/theme/monokai')
    editor.getSession().setMode('ace/mode/javascript')
    editor.getSession().on('change', () => {
      this.solution = editor.getSession().getValue()
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .task {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 60%;
    padding: 32px 20%;
  }

  .task-form, .task-form form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  textarea {
    display: none;

  }

  .form-bottom {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
  }
  input, select {
    height: 40px;
    border-radius: 4px;
  }
  input[type=submit] {
    background: #a61111;
    outline: none;
    color: white;
    border: none;
    box-sizing: content-box;
    cursor: pointer;
  }
  .task-info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    font-family: 'Open Sans', sans-serif;
    margin-bottom: 24px;
  }
  .limits {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-bottom: 8px;
  }
  .limit {
    margin: 0 12px;
    font-size: 1.2rem;
  }
  h2 {
    color: #a61111;
    font-size: 1.5rem;
    margin: 0;
    padding: 0;
    margin-bottom: 8px;
  }
  .condition {
    font-size: 1.2rem;
  }
  #editor, #editor div{
    font-family: monospace !important;
  }
  .editor {
    display: block;
    position: relative;
    width: 100%;
    height: 400px;
    margin-bottom: 4px;
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 0 5px 1px #b5b5b5;
  }
  #editor {
       margin: 0;
       padding: 0;
       position: absolute;
       top: 0;
       bottom: 0;
       left: 0;
       right: 0;
       width: 100%;
       height: 100%;
   }
</style>
