import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import Router from 'vue-router' 
import Meta from 'vue-meta'
import VueButtonSpinner from 'vue-button-spinner'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

import App from './App.vue'
import About from './components/About.vue'
import Classify from './components/Classify.vue'
import Top10 from './components/Top10.vue'

Vue.use(Router)
Vue.use(Meta)
Vue.use(BootstrapVue)

Vue.component('button-spinner', VueButtonSpinner)

const router = new Router({
  routes: [
    {
      path: '/',
      name:'classify',
      component: Classify,
    },
    {
      path: '/about',
      name:'about',
      component: About,
    },
    
    {
      path: '/top10',
      name:'top10',
      component: Top10,
    },
  ],
 })

new Vue({
  el: '#app',
  render: h => h(App),
  router
})
