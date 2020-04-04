import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/components/SignIn'
import TaskList from '@/components/TaskList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/TaskList',
      name: 'TaskList',
      component: TaskList
    }
  ]
})
