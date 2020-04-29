<template>
  <div class="mt-5">
    <div class="container start">
      <p class="title">Create</p>
      <div class="row">
        <div class="col-sm-6 col-12 mb-3">
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
        <div class="col-sm-6 col-12 mb-3">
          <div class="tabs">
              <a v-on:click="tabChange(1)" v-bind:class="[ activeTab2 === 1 ? 'active' : '' ]">Style</a>
          </div>
          <div class="content">
            <div v-if="activeTab2 === 1" class="tabcontent">
                <div class="row container px-3 py-3 mx-0 style-div">
                  <div v-for="(style, n) in styles" :key="n" class="col-sm-4 col-6 px-2">
                    <img @click="styleClick(style.type)" :class="style.type" class="mb-2 style" :src="style.url" alt="">
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
        <button v-if="!loading" class="col-4 cbtn btn btn-primary justify-content-md-center mb-3" @click="goResult">Create</button>
        <b-button v-else class="col-4 cbtn btn btn-primary justify-content-md-center mb-3"  variant="primary" disabled>
          <b-spinner small></b-spinner>
          Loading...
        </b-button>
      </div>

      
    </div>
  </div>
</template>

<script>
  import PictureInput from 'vue-picture-input'
  import '@/css/tab.css'
  import flaskURL from '@/js/flask-url.js'
  import djangoURL from '@/js/django-url.js'
  export default {
    // beforeCreate() {
    //   if (!this.$store.getters.userId) {
    //     alert('로그인이 필요합니다.')
    //     this.$router.push({name:'Main'})
    //   }
    // },
    components: {
      PictureInput
    },
    methods: {
      tabChange(n) {
        this.activeTab2 = n
        this.style = ''
        this.activeStyle = ''
      },
      onChange(image) {
        if (image) {
          return image
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
      createArticle(imgPath) {
        const user_id = this.$store.getters.userId
        var form = new FormData()
        form.append('img_path', imgPath)
        form.append('user', user_id)
        djangoURL.post('api/v1/article/', form, this.$store.getters.requestHeader)
        .then(() => {
          this.$router.push({name:'Result', params:{
            imgPath: imgPath
          }})
        })
        .catch(() =>{
          alert('오류가 발생했습니다. 잠시후 다시 시도해주세요.')
        })
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
      async goResult() {
        this.loading = true
        const content = document.querySelector('.picture-input').childNodes[1].files[0]
        if (this.activeStyle == '' || content == undefined ) {
          this.loading = false
          return         
        }
        const files = new FormData();
        files.append('type', this.activeStyle+'_models')
        files.append('photo', content)
        flaskURL.post('faststyletransfer', files)
        .then(res=>{
          this.loading = false
          this.createArticle(res.data.path)
        })
        .catch(() => {
          alert('오류가 발생했습니다. 잠시후 다시 시도해주세요.')
          this.loading = false
        })
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
        imgPath: '',
        loading: false,
        styles: [
          {
            'type' : 'the_starry_night',
            'url' : require('@/assets/styles/the_starry_night.jpg'),
          },
          {
            'type' : 'creation_of_adam',
            'url' : require('@/assets/styles/creation_of_adam.jpg'),
          },
          {
            'type' : 'wave',
            'url' : require('@/assets/styles/wave.jpg'),
          },
          {
            'type' : 'buddhism',
            'url' : require('@/assets/styles/buddhism.jpg'),
          },
          {
            'type' : 'Kandinsky',
            'url' : require('@/assets/styles/Kandinsky.jpg'),
          },
          {
            'type' : 'composition_VII',
            'url' : require('@/assets/styles/composition_VII.jpg'),
          },
          {
            'type' : 'la_muse',
            'url' : require('@/assets/styles/la_muse.jpg'),
          },
          {
            'type' : 'rain_princess',
            'url' : require('@/assets/styles/rain_princess.jpg'),
          },
          {
            'type' : 'Mondrian',
            'url' : require('@/assets/styles/Mondrian.jpg'),
          },
          {
            'type' : 'pop',
            'url' : require('@/assets/styles/pop.jpg'),
          },
          {
            'type' : 'color',
            'url' : require('@/assets/styles/color.jpg'),
          },
          {
            'type' : 'mone',
            'url' : require('@/assets/styles/mone.jpg'),
          },
          {
            'type' : 'udnie',
            'url' : require('@/assets/styles/udnie.jpg'),
          },
          {
            'type' : 'the_scream',
            'url' : require('@/assets/styles/the_scream.jpg'),
          },
          {
            'type' : 'puple',
            'url' : require('@/assets/styles/puple.jpg'),
          },
          {
            'type' : 'sand_art',
            'url' : require('@/assets/styles/sand_art.jpg'),
          },
          {
            'type' : 'white_cow',
            'url' : require('@/assets/styles/white_cow.jpg'),
          },
          {
            'type' : 'ShinYunbok',
            'url' : require('@/assets/styles/ShinYunbok.jpg'),
          },
        ]
      }
    },
  }
</script>

<style>
.style-div{
  height: 30em;
  overflow: scroll;
}

.style-div > div{
  /* height: 5em; */
  margin-bottom: 10px;
}
.style{
  height: 100%;
  width: 100%;
  max-height: 9em;
}


.preview-container[data-v-431cb064]{
  margin-top: 15px
}

.title{
  font-size: 8rem;
  font-family: 'East Sea Dokdo', cursive;
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

.picture-preview{
  z-index: 300 !important;
}

.picture-inner{
  z-index: 300 !important;
}

</style>