import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/components/SignIn'
import SignUp from '@/components/SignUp'
import TaskList from '@/components/TaskList'

import Header from '@/components/Header'
import Footer from '@/components/Footer'

Vue.component('Header', Header)
Vue.component('Footer', Footer)

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/SignUp',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/TaskList',
      name: 'TaskList',
      component: TaskList
    }
  ]
})
