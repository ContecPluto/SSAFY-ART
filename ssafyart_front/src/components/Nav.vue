<template>
  <div>
    <b-navbar toggleable="lg" class="text-black">
      <b-navbar-brand @click="home" class="nav-logo">SSAFY ART</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item class="text-white" @click="create">Create</b-nav-item>
          <b-nav-item class="text-white" @click="about">About</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="!isLogin" @click="showModal">Login</b-nav-item>
          <b-nav-item-dropdown v-else :text="user" left>
            <b-dropdown-item @click="edit">Edit</b-dropdown-item>
            <b-dropdown-item @click="gallery">Gallery</b-dropdown-item>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-modal body-class="p-0 w-100" centered ref="my-modal" hide-footer hide-header>
      <login-form @login="hideModal()"></login-form>
    </b-modal>

    <b-modal body-class="p-0 w-100" centered ref="edit-modal" hide-footer hide-header>
      <div class="mx-3 mb-3 edit-div">
        <p class="text-center edit-title">Edit User</p>
        <div class="edit-content">
          <p class="text-center m-0">Current password</p>
          <div class="row justify-content-center mb-3">
            <input class="mb-2 mx-auto edit-input" type="password" v-model="currentPassword" >
          </div>
          <p class="text-center m-0">New password</p>
          <div class="row justify-content-center mb-3">
            <input class="mb-2 edit-input" type="password" v-model="newPassword">
          </div>
          <p class="text-center m-0">New Password Confrim</p>
          <div class="row justify-content-center mb-3">
            <input class="edit-input" type="password" v-model="newPasswordConfrim">
          </div>
        </div>
        <hr>
        <div class="row mx-1">
          <b-button class="col-4" @click="signOut" variant="outline-danger">회원 탈퇴</b-button>
          <b-button class="col-4" @click="closeEdit" variant="outline-secondary">닫기</b-button>
          <b-button class="col-4" @click="chanege" variant="outline-primary">변경</b-button>
        </div>
      </div>
    </b-modal>
    
  </div>
</template>

<script>
  import loginForm from "@/components/Login.vue"
  import djangoURL from '@/js/django-url.js'
  import cookie from "@/js/cookie.js"
  export default {
    data: () => {
      return { 
        currentPassword: '',
        newPassword: '',
        newPasswordConfrim: '',
        errors: '',
      }
    },
    components:{
      loginForm
    },
    computed: {
      isLogin: function() {
        return this.$store.getters.isLoggedIn
      },
      user: function() {
        return this.$store.getters.user
      },
    },
    methods:{
      edit() {
        this.$refs["edit-modal"].show()
        this.currentPassword = ''
        this.newPassword = ''
        this.newPasswordConfrim = ''
      },
      closeEdit() {
        this.$refs["edit-modal"].hide()
      },
      home() {
        this.$router.push({name:"Main"})
      },
      create() {
        this.$router.push({name:"Create"})
      },
      gallery() {
        this.$router.push({name:"Gallery"})
      },
      about() {
        this.$router.push({name:"About"})
      },
      showModal() {
        this.$refs["my-modal"].show()
      },
      hideModal() {
        this.$refs["my-modal"].hide()
      },
      logout() {
        this.$store.dispatch('logout')
        cookie.logout()
        this.$router.push({name:'Main'})
      },
      signOut() {
        const user_id = this.$store.getters.userId
        djangoURL.delete('api/v1/user/' + user_id + '/', this.$store.getters.requestHeader)
        .then(()=>{
          alert('회원탈퇴가 성공적으로 진행됬어요.')
          this.$store.dispatch('logout')
          cookie.logout()
          this.closeEdit()
          this.$router.push({name:'Main'})
        })
        .catch(() =>{
          alert('문제가 생겼습니다. 잠시후 다시 시도해주세요.')
        })
      },
      checkForm() {
        this.errors = []
        if (!this.currentPassword) {
          this.errors.push("현재 비밀번호를 입력해주세요")
        }
        if (this.newPassword < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        if (this.newPasswordConfrim != this.newPassword) {
          this.errors.push("비밀번호를 확인해주세요")
        }
        if (this.errors.length === 0) {
          return true
        }
      },
      chanege() {
        if (this.checkForm()) {
          var form = new FormData()
          form.append('origin_password', this.currentPassword)
          form.append('password', this.newPassword)
          djangoURL.put('/api/v1/user/' + this.$store.getters.userId +'/', form, this.$router.requestHeader)
          .then(res => {
            alert(res.data.message)
            this.closeEdit()
          })
          .catch(err => {
            console.log(err.response)
            alert(err.response)
          })
        } else {
          var word = ""
          this.errors.forEach(element => {
            word += element + '\n'
          })
          alert(word)
        }
      }
    }
  }
</script>

<style>
.edit-title{
  position: relative;
  top: -10px;
  font-family: 'East Sea Dokdo', cursive;
  font-size: 5em;
}

.edit-content{
  position: relative;
  top: -30px;
}

.edit-content > p {
  font-size: 12px;
  color: #cfcfcf;
  text-transform: uppercase;
}

.edit-input{
  border: 0;
  border-bottom: 1px solid;
  width: 50%;
  margin-top: 5px;
  padding-bottom: 5px;
  font-size: 16px;
  border-bottom: 1px solid rgba(0,0,0,0.4);
  text-align: center;
  display: block;
  outline: none;
}

.edit-div{
  position: relative;
}

.navbar-brand{
  cursor: pointer;
}

.modal-dialog{
  height: 10px !important;
}

.nav-logo{
  font-family: 'East Sea Dokdo', cursive;
  font-size: 1.8em;
}
</style>