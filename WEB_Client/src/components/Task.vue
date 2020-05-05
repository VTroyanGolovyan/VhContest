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
            Время: {{ task.time_limit }}ms
          </div>
          <div class="limit">
            Память: {{ task.memory_limit }}M
          </div>
        </div>
        <div class="condition">
          {{task.condition}}
        </div>
        <div class="examples">
          <div class="example">
            <h2>
               Входные данные
            </h2>
            <textarea v-model="task.input_description" readonly></textarea>
          </div>
          <div class="example">
            <h2>
               Выходные данные
            </h2>
            <textarea v-model="task.output_description" readonly></textarea>
          </div>
        </div>
        <div class="examples">
          <div class="example">
            <h2>
               Пример ввода
            </h2>
            <textarea v-model="task.input_example" readonly></textarea>
          </div>
          <div class="example">
            <h2>
               Пример вывода
            </h2>
            <textarea v-model="task.output_example" readonly></textarea>
          </div>
        </div>
      </div>
      <div class="task-form">
        <form v-on:submit="submitSolution">
          <div class="editor">
            <div id='editor'>
            </div>
          </div>
          <div class="form-bottom">
            <label class="select-wrapper">
              <select v-on:change="changeTheme" v-model="theme">
                <option value="1">Темная тема</option>
                <option value="2">Светлая тема</option>
              </select>
            </label>
            <label class="select-wrapper">
              <select v-on:change="changeLanguage" v-model="language">
                <option>python</option>
                <option>javascript</option>
                <option>c++</option>
                <option>php</option>
                <option>java</option>
              </select>
            </label>
            <input type="submit" value="Отправить решение">
          </div>
        </form>
      </div>
      <div class="header">
        <h2 v-if="attempts.length > 0">
           Попытки
        </h2>
        <h2 v-if="attempts.length === 0">
           Не было попыток
        </h2>
      </div>
      <div v-if="attempts.length > 0" class="attempts">
        <div class="attemts-top">
          <div>
            Id
          </div>
          <div>
            Язык
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
        <div class="attempt" v-for="attempt in attempts" v-bind:key="attempt.id">
          <div>{{attempt.id}}</div>
          <div>
            {{attempt.language}}
          </div>
          <div>
            {{attempt.time}}ms
          </div>
          <div>
            {{attempt.memory}}mb
          </div>
          <div>{{attempt.result}}</div>
        </div>
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
      attempts: [],
      solution: '',
      language: 'python',
      theme: '1'
    }
  },
  methods: {
    fetchTask: function () {
      axios
        .get(this.$baseLink + '/' + 'task/' + this.$route.params.id)
        .then(response => {
          this.task = response.data.data
        })
    },
    fetchAttempts: function () {
      axios
        .get(this.$baseLink + '/' + 'attempts/' + this.$route.params.id)
        .then(response => {
          this.attempts = response.data.data.reverse()
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
          task_id: this.$route.params.id,
          language: this.language,
          solution: this.solution
        })
        .then(response => {})
    }
  },
  mounted () {
    this.fetchTask()
    this.fetchAttempts()
    editor = ace.edit('editor')
    editor.setFontSize('16px')
    editor.setTheme('ace/theme/monokai')
    editor.getSession().setMode('ace/mode/python')
    editor.getSession().on('change', () => {
      this.solution = editor.getSession().getValue()
    })
    this.interval = setInterval(() => {
      this.fetchAttempts()
    }, 1000)
  },
  beforeDestroy () {
    clearInterval(this.interval)
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
  .task-form {
    margin-bottom: 16px;
  }
  .task-form, .task-form form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  .form-bottom {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
  }

  input {
    height: 40px;
    border-radius: 4px;
  }

  .select-wrapper {
    margin: 0 4px 0 0;
  }

  input[type=submit] {
    background: #a61111;
    outline: none;
    color: white;
    border: none;
    box-sizing: content-box;
    cursor: pointer;
    padding: 0 16px;
  }
  .task-info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    font-family: 'Open Sans', sans-serif;
    margin-bottom: 24px;
    width: 100%;
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
   .header {
     display: flex;
     flex-direction: row;
     justify-content: center;
     width: 100%;
     font-family: 'Open Sans', sans-serif;
     margin-bottom: 8px;
   }
   .attemts-top {
     cursor: pointer;
     width: calc(100% - 32px);
     display: flex;
     flex-direction: row;
     justify-content: space-around;
     padding: 16px 16px;
     background: white;
     box-shadow: 0 0 5px 1px #b5b5b5;
     border-radius: 4px;
   }
   .attempts {
     font-family: 'Open Sans', sans-serif;
     display: flex;
     flex-direction: column;
     justify-content: flex-start;
     align-items: center;
     width: 100%;
   }
   .attempt {
     border-bottom: solid 1px #b5b5b5;
     width: calc(100% - 32px);
     display: flex;
     flex-direction: row;
     justify-content: space-around;
     padding: 16px 16px;
   }
   .attempt div, .attemts-top div {
      width: 20%;
   }
   .examples {
     display: flex;
     flex-direction: row;
     justify-content: space-between;
     width: 100%;
     align-items: stretch;
   }
   .example {
     width: calc(50% - 32px);
     box-sizing: border-box;
     display: flex;
     padding-top: 16px;
     flex-direction: column;
     justify-content: center;
   }
   .example textarea {
     font-family: 'Open Sans', sans-serif;
     box-sizing: border-box;
     resize: vertical;
     width: 100%;
     min-height: 60px;
     max-width: 100%;
     min-width: 100%;
     background: #d2d2d2;
     border-radius: 4px;
     border: none;
     padding: 8px;
     cursor: default;
     flex-grow: 1;
   }
</style>
