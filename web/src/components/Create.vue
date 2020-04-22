<template>
  <div>
    <div class="container mb-2 start">
      <p class="title">Lorem</p>
      <p class="content">Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur aspernatur reprehenderit minus magni pariatur ipsa, illum tempora perspiciatis neque ea, ipsum corporis quam quaerat! Laudantium architecto placeat unde maxime illum!</p>
      <p class="m-0">1. Lorem, ipsum dolor.</p>
      <p class="m-0">2. Lorem, ipsum dolor.</p>
      <p class="mb-5">3. Lorem, ipsum dolor.</p>
      <div class="row">
        <div class="col-6 mb-3">
          <div class="tabs">
              <a v-on:click="activeTab=1" v-bind:class="[ activeTab === 1 ? 'active' : '' ]">Photo</a>
          </div>
          <div class="content">
            <div v-if="activeTab === 1" class="tabcontent">
                <picture-input
                ref="pictureInput" 
                @change="photoChange" 
                @remove="photoRemove"
                width="500" 
                height="500" 
                margin="16" 
                accept="image/jpeg, image/png" 
                size="10" 
                buttonClass="btn btn-primary"
                :removable="true">
              </picture-input>
            </div>
          </div>
        </div>
        <div class="col-6">
          <div class="tabs">
              <a v-on:click="activeTab2=1" v-bind:class="[ activeTab2 === 1 ? 'active' : '' ]">Style</a>
              <a v-on:click="activeTab2=2" v-bind:class="[ activeTab2 === 2 ? 'active' : '' ]">Upload Style</a>
          </div>
          <div class="content">
            <div v-if="activeTab2 === 1" class="tabcontent">
                <div class="row px-2 py-3">
                  <div v-for="n in 9" :key="n" class="col-4">
                    <img @click="styleClick('style'+n)" :class="'style'+n" class="mb-2 style" src="@/assets/example_style.jpg" alt="">
                  </div>

                </div>
            </div>
            <div v-if="activeTab2 === 2" class="tabcontent">
                <picture-input
                ref="pictureInput" 
                @change="styleChange"
                @remove="styleRemove"
                width="500" 
                height="500" 
                margin="16" 
                accept="image/jpeg, image/png" 
                size="10" 
                buttonClass="btn btn-primary"
                :removable="true">
              </picture-input>
            </div>
          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <button class="col-4 cbtn btn btn-primary justify-content-md-center" @click="goResult">Create</button>
      </div>
    </div>
  </div>
</template>

<script>
  import PictureInput from 'vue-picture-input'
  import '@/css/tab.css'
  export default {
    components: {
      PictureInput
    },
    methods: {
      onChange(image) {
        console.log('New picture selected!')
        if (image) {
          console.log('Picture loaded.')
          return image
        } else {
          console.log('FileReader API not supported: use the <form>, Luke!')
        }
      },
      styleChange(image) {
        this.style = this.onChange(image)
      },
      photoChange(image) {
        this.photo = this.onChange(image)
      },
      photoRemove() {
        this.photo = ''
      },
      styleRemove() {
        this.style = ''
      },
      styleClick(e) {
        if (this.activeStyle !== '') {
          var rem = document.getElementsByClassName(this.activeStyle)
          rem[0].classList.remove('activeStyle')
        } 
        this.activeStyle = e
        var target = document.getElementsByClassName(e)
        target[0].classList.add('activeStyle')
      },
      goResult() {
        this.$router.push({name:'Result', params:{
          'imgPath': this.imgPath
        }})
      }
    },
    data: () => {
      return { 
        activeTab: 1,
        activeTab2: 1,
        activeStyle: '',
        style: '',
        photo: '',
        image:'',
        imgPath: require('@/assets/step3.png'),
      }
    },
  }
</script>

<style>
.title{
  font-size: 2.5em;
}
.box{
  background-color: #C9C9C9;
}
.picture-inner{
  background-color: #fff;
  font-size: 13px !important;
}

.picture-preview{
  background-color: #fff !important;
}

.start{
  margin-top: 100px;
}

.style{
  opacity: 0.7;
  cursor: pointer;
  max-width: 100%;
}

.style:hover{
  opacity: 1;
}

.activeStyle{
  box-shadow: 0px 0px 7px 3px;
  max-width: 100%;
  opacity: 1;
}
</style>