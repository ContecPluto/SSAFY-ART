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
export default {
  name: 'App',
  components: {
    'navBar': Nav,
    'appFooter': Footer
  },
  methods: {

  }
}
</script>

<style>
.nav {
  border-bottom: 1px solid;
  top: 0px;
  position: fixed;
  width: 100%;
  z-index: 1000000;
}

</style>
