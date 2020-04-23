<template>
    <div class="col-sm-4">
        <div class="card card-flip" >
            <div class="card-front text-white">
                <div class="card-body">
                    <img class="card-img-top" :src="imgPath" alt="">
                </div>
            </div>
            <div class="card-back bg-white">
                <div class="card-body">
                    <img class="card-img-top" :src="imgPath2" alt="">
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

</style>