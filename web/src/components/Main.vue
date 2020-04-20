<template>
  <div>
    <div id="logo" class="mb-5">
      <p id="logo-word">
        <span id="logo-word-main">SSAFY ART</span><br>
        <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita, reprehenderit.</span><br><br>
        <button class="btn btn-primary" @click="goCreate">create</button>
      </p>
    </div>
    <div class="container mb-5">
      <p class="partHeader">Turn Any Photo Into An Artwork</p>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti assumenda accusamus sint vero cupiditate, maiores molestias non molestiae unde quidem dicta in nostrum aspernatur aperiam asperiores dolorum vel id officia!</p>
      <div class="row">
        <p class="col-sm-4">1. Upload photo</p>
        <p class="col-sm-4">2. Choose style</p>
        <p class="col-sm-4">3. Submit</p>
        <img src="@/assets/step1.jpg" class="col-sm-4" alt="">
        <img src="@/assets/step2.jpg" class="col-sm-4" alt="">
        <img src="@/assets/step3.png" class="col-sm-4" alt="">
      </div>
    </div>
    <div class="bg-light">
      <div class="container">
        <p class="partHeader">Example</p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
          Est iste velit eaque molestiae quis illo debitis accusantium recusandae atque voluptates.
        </p>
        <div class="row">
          <card-flib class="mb-3" v-for="n in 9" :key="n" :imgPath="imgPath" :imgPath2="imgPath2"></card-flib>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Card from './Card.vue'
  export default {
    data: () => {
      return { 
        imgPath: require('@/assets/card1.jpg'),
        imgPath2: require('@/assets/card2.png')
      }
    },
    components: {
      cardFlib: Card
    },
    methods: {
      goCreate() {
        this.$router.push({name:'Create'})
      }
    }
  }
</script>

<style>
.partHeader {
  font-size: 2.5em;
}

#logo{
  background-image: url("../assets/main.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 100%;
  height: 300px;
  display: table
}

#logo-word {
  color: white;
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

#logo-word-main{
  font-size: 3em;
}
</style>