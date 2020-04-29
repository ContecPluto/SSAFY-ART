<template>
    <div class="col-sm-4 col-6">
        <div class="card card-flip" >
            <div class="card-front text-white">
                <div class="card-body">
                    <img class="card-img-top" :src="imgPath" alt="">
                    <img class="card-img-side" :src="imgPath2" alt="">
                </div>
            </div>
            <div class="card-back">
                <div class="card-body">
                    <img class="card-img-top" :src="imgPath3" alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import '@/css/card-flib.css'
  export default {
    
    props: {
      imgPath: {
        type: String,
      },
      imgPath2: {
        type: String,
      },
      imgPath3: {
        type: String,
      }
    },

    // data: () => {
    //     return { 
    //         imgPath: ''
    //     }
    // }

  }
</script>

<style>
.card-body > img {
  max-height: 15em !important;
}
</style>