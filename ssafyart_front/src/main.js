import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import routes from './routes'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import store from './store'
import cookie from './js/cookie'
// import cookie from '@/js/cookie.js'

Vue.config.productionTip = false
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
});


router.afterEach((to, from) => {
  var isLogin = false
  from
  if (cookie.token()) {
    isLogin = true
  } 
  if (isLogin) {
    cookie.updateCookie()
  }
  if (to.meta.loginRequire) {
    if (!isLogin) {
      alert('로그인이 필요합니다.')
      router.push({name:'Main'})
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
