<template>
  <div id="app">
    <div class="nav bg-light">
      <b-container>
        <nav-bar></nav-bar>
      </b-container>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
      <app-footer class="footer"></app-footer>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Nav from '@/components/Nav'
import Footer from '@/components/Footer.vue'
import cookie from '@/js/cookie.js'
export default {
  name: 'App',
  beforeCreate() {
    var jwt = cookie.token()
    if (jwt === undefined || jwt == '') {
      this.$store.dispatch('login', false)
    } 
    else {
      this.$store.dispatch('login', true)
    }
  },
  components: {
    'navBar': Nav,
    'appFooter': Footer
  },
 data: () => {
    return { 
      loginEv : false
    }
  },
  
}
</script>

<style>
.nav {
  border-bottom: 1px solid;
  top: 0px;
  position: fixed;
  width: 100%;
  z-index: 1000;
}

</style>
