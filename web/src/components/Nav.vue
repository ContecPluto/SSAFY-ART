<template>
  <div>
    <b-navbar toggleable="lg" class="text-black">
      <b-navbar-brand @click="home">SSAFY ART</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item class="text-white" href="#">Link</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    methods:{
      home() {
        this.$router.push({name:"Main"})
      }
    }
  }
</script>

<style>
.navbar-brand{
  cursor: pointer;
}
</style>