<template>
  <div class="mt-5 bg-light">
    <p class="title text-center">{{ user }}'s Gallery</p>
    <div class="container">
      <div class="row gall">
        <div @click="showModal(image)" v-for="(image, n) in images" :key=n class="photo col-sm-4 col-6 px-3 pb-4 m-auto">
          <frame :imgPath="image.img_path"></frame>
          <!-- <img @click="showModal(imageUrl)"  class="mb-2 photo" :src="imageUrl" alt="">
          <p class="text-right container">2020-04-20</p> -->
        </div>
      </div>
    </div>



    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{disabled:minIdx==0}">
          <p @click="previous" class="page-link" href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </p>
        </li>
        <span v-for="n in total" :key=n>
          <li @click="onChange(n)" v-if="n <= maxIdx && minIdx < n" :class="{active: n==currentPage}" class="page-item"><p class="page-link">{{n}}</p></li>
        </span>
        <li class="page-item" :class="{disabled:maxIdx > total}">
          <p @click="next" class="page-link" href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </p>
        </li>
      </ul>
    </nav>

    <b-modal id="modal-center" centered ref="my-modal" hide-footer hide-header>
      <div class="d-block text-center">
        <img class="share-image" :src="image.img_path" alt="">
        <b-button class="col-4" squared @click="deleteArticle()" variant="outline-danger">삭제</b-button>
        <b-button class="col-4" squared onclick="shareKakaotalk()" variant="outline-primary">공유</b-button>
        <b-button class="col-4" squared @click="hideModal" variant="outline-secondary">닫기</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>  
  import Frame from '@/components/Frame2.vue'
  import djangoURL from '@/js/django-url.js'


  export default {
    mounted() {
      this.user = this.$store.getters.user
      const user_id = this.$store.getters.userId
      djangoURL('api/v1/article/' + user_id + '/1/', this.$store.getters.requestHeader)
      .then(res => {
        this.images = res.data.data
        this.total = res.data.total
      })
    },
    components: {
      Frame
    },
    data: () => {
      return { 
        currentPage: 1,
        total: 1,
        minIdx: 0,
        maxIdx: 5,
        image: {
        },
        images: [],
        user: 'User'
      }
    },
    methods: {
      onChange(n) {
        this.currentPage = n
        const user_id = this.$store.getters.userId
        djangoURL('api/v1/article/' + user_id + '/' + n + '/', this.$store.getters.requestHeader)
        .then(res => {
          this.images = res.data.data
        })
      },
      next() {
        this.minIdx += 5
        this.maxIdx += 5
        this.currentPage = this.minIdx + 1
      },
      previous() {
        this.minIdx -= 5
        this.maxIdx -= 5
        this.currentPage = this.minIdx + 1
      },
      showModal(image) {
        this.$refs['my-modal'].show()
        this.image = image
      },
      hideModal() {
        this.$refs['my-modal'].hide()
      },
      deleteArticle() {
        djangoURL.delete('api/v1/article/'+this.image.id+'/delete/', this.$store.getters.requestHeader)
        .then(()=>{
          this.images = this.images.filter(e => {return e != this.image})
          this.hideModal()
        })
      }
    }
  }
</script>

<style scope>

.modal-body > div > img{
  width: 100%;
}
.page-item{
  cursor: pointer;
}

.ca{
  height: 100px;
  background-color: red;
}

.disabled{
  cursor: default;
}

.photo {
  cursor: pointer;
  /* width: 100%; */
  margin-top: auto;
}

.photo > div {
  height: 100%;
}
</style>