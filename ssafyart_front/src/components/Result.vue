<template>
  <div class="my-5 container">
    <p class="title text-center m-0">Result</p>
    <div class="row justify-content-center mb-3">
      <div class="result">
        <!-- <img src="" alt=""> -->
        <frame :imgPath="imgPath"></frame>
      </div>
    </div>


    <p class="text-center">당신의 사진으로 작품이 완성되었습니다. 갤러리를 통해 저장되며 공유, 삭제를 할 수 있습니다.</p>
    <div class="row justify-content-center mb-2">
      <b-button class="mr-3" variant="primary" @click="create">Create</b-button>
      <b-button @click="gallery">Gallery</b-button>
    </div>
  </div>
</template>


<script>
  import Frame from './Frame.vue'
  export default {
    components:{
      Frame
    },
    mounted() {
      if (this.$route.params.imgPath == undefined) {
        alert('잘못된 접근입니다.')
        this.$router.push({name:'Main'})
      }
      this.imgPath = this.$route.params.imgPath
    },
    methods: {
      create() {
        this.$router.push({name : 'Create'})
      },
      gallery() {
        this.$router.push({name:"Gallery", params:{User_seq:1}})
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
  background-size: cover;
}
.result-text{
  font-size: 4em;
}
</style>