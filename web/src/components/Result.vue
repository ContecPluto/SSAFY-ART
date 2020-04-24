<template>
  <div class="my-5 container">
    <br>
    <p class="title text-center">Lorem</p>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Labore nesciunt expedita quod quasi exercitationem mollitia fuga. In, aliquam a eveniet veritatis placeat, ipsum quia cumque laboriosam, incidunt est accusamus maxime.</p>
    <div class="row justify-content-center">
      <div class="result">
        <img class="share-image" :src="imgPath" alt="">
        <div class="w-100">
          <img class="icon" src="@/icon/kakaolink_btn_small.png" onclick="shareKakaotalk()" alt="">
        </div>
      </div>
      
    </div>
  </div>
</template>


<script>
  export default {
    mounted() {
      this.imgPath = this.$route.params.imgPath
    },
    methods: {
      shareHover() {

      }
    },
    data: () => {
      return { 
        imgPath: '',
      }
    },
  }
</script>

<style>
.result {
  position: relative;
}
.share-nav {
  position: absolute;
  height: 1.5em;
}

.share-nav-hover {
  opacity: 0.5;
}

.icon {
  float: right;
  cursor: pointer;
}
</style>