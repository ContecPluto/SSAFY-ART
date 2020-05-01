<template>
    <div class="cont" :class="{'w-100':isMobile()}">
      <div class="form sign-in" :class="{'m-auto':isMobile()}">
        <h2>로그인</h2>
        <label>
          <span>ID</span>
          <input type="text" v-model="username" @keypress.enter="login">
        </label>
        <label>
          <span>Password</span>
          <input type="password" v-model="password" @keypress.enter="login">
        </label>
        <button type="button" class="submit" @click="login">Sign In</button>
        <!-- <button type="button" class="fb-btn">Connect with <span>facebook</span></button> -->
      </div>
      <div v-if="!isMobile()" class="sub-cont">
        <div class="img">
          <div class="img__text m--up">
            <h2>새로 오셨나요?</h2>
            <br>
            <p>회원가입을 진행하고 저희와 함께 깜짝 놀랄만한 작품을 만들어 보세요.</p>
          </div>
          <div class="img__text m--in">
            <h2>회원이신가요?</h2>
            <br>
            <p>이미 가입한 회원이시라면 로그인을 진행해주세요.</p>
          </div>
          <div @click="imgBtn" class="img__btn">
            <span class="m--up">Sign Up</span>
            <span class="m--in">Sign In</span>
          </div>
        </div>
        <div class="form sign-up">
          <h2>회원가입</h2>
          <label>
            <span>ID</span>
            <input v-model="signup.username" type="text" />
          </label>
          <label>
            <span>Password</span>
            <input v-model="signup.password" type="password" />
          </label>
          <label>
            <span>Password confirm</span>
            <input v-model="signup.passwordConfirm" type="password" />
          </label>
          <button @click="signUp" type="button" class="submit">Sign Up</button>
          <!-- <button type="button" class="fb-btn">Join with <span>facebook</span></button> -->
        </div>
      </div>
    </div>
</template>

<script>
  import djangoURL from '@/js/django-url.js'
  import cookie from '@/js/cookie.js'
  export default {
    data: () => {
      return {
        username : '',
        password : '',

        signup: {
          username: '',
          password: '',
          passwordConfirm : ''
        }
        
      }
    },
    methods: {
      imgBtn() {
        document.querySelector('.cont').classList.toggle('s--signup');
      },
      isMobile() {
        if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
          return true
        } else {
          return false
        }
      },
      showModal() {
        this.$refs['forgot'].show()
      },
      async login() {
        if (this.checkForm()) {
          var form = new FormData()
          form.append('username', this.username)
          form.append('password', this.password)
          djangoURL.post('api-token-auth/', form)
            .then(res => {
              cookie.cookieCreate(res.data.token, this.username)
              this.$store.dispatch('login', true)
              this.$emit('login')
            })
            .catch(err => {
              if (err.response.status) {
                alert('로그인정보가 맞지 않습니다.')
              }
              console.log(err)
            })
        } else {
          var word = ""
          this.errors.forEach(element => {
            word += element + '\n'
          })
          alert(word)
        }
      },
      signUp() {
        if (this.checkForm2()) {
          var form = new FormData()
          form.append('username', this.signup.username)
          form.append('password', this.signup.password)
          djangoURL.post('api/v1/user/', form)
            .then(res => {
              alert(res.data.message)
              this.imgBtn()
            })
            .catch(err => {
              if(err.response.data.username) {
                alert(err.response.data.username)
              } 
            })
        } else {
          var word = ""
          this.errors.forEach(element => {
            word += element + '\n'
          })
          alert(word)
        }
      },
      checkForm() {
        this.errors = []
        if (!this.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        if (this.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        if (this.errors.length === 0) {
          return true
        }
      },

      checkForm2() {
        this.errors = []
        if (!this.signup.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        if (this.signup.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        if (this.signup.passwordConfirm != this.signup.password) {
          this.errors.push("비밀번호를 확인해주세요")
        }
        if (this.errors.length === 0) {
          return true
        }
      },
    }
  }
</script>

<style lang="scss" scoped>
*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  background: #ededed;
}

input, button {
  border: none;
  outline: none;
  background: none;
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
}

$contW: 600px;
$imgW: 260px;
$formW: $contW - $imgW;
$switchAT: 1.2s;

$inputW: 260px;
$btnH: 36px;

$diffRatio: ($contW - $imgW) / $contW;

@mixin signUpActive {
  .cont.s--signup & {
    @content;
  }
}

.tip {
  font-size: 20px;
  margin: 40px auto 50px;
  text-align: center;
}

.cont {
  overflow: hidden;
  position: relative;
  width: $contW;
  height: 550px;
  background: #fff;
}

.form {
  position: relative;
  width: $formW;
  height: 100%;
  transition: transform $switchAT ease-in-out;
  padding: 50px 0px 0;
}

.sub-cont {
  overflow: hidden;
  position: absolute;
  left: $formW;
  top: 0;
  width: $contW;
  height: 100%;
  padding-left: $imgW;
  background: #fff;
  transition: transform $switchAT ease-in-out;

  @include signUpActive {
    transform: translate3d($formW * -1,0,0);
  }
}

button {
  display: block;
  margin: 0 auto;
  width: $inputW;
  height: $btnH;
  border-radius: 30px;
  color: #fff;
  font-size: 15px;
  cursor: pointer;
}

.img {
  overflow: hidden;
  z-index: 2;
  position: absolute;
  left: 0;
  top: 0;
  width: $imgW;
  height: 100%;
  padding-top: 360px;

  &:before {
    content: '';
    position: absolute;
    right: 0;
    top: 0;
    width: $contW;
    height: 100%;
    background-image: url('https://images.unsplash.com/flagged/photo-1572392640988-ba48d1a74457?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80');
    background-size: cover;
    transition: transform $switchAT ease-in-out;
  }

  &:after {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.6);
  }

  @include signUpActive {
    &:before {
      transform: translate3d($formW,0,0);
    }
  }

  &__text {
    z-index: 2;
    position: absolute;
    left: 0;
    top: 50px;
    width: 100%;
    padding: 0 20px;
    text-align: center;
    color: #fff;
    transition: transform $switchAT ease-in-out;

    h2 {
      margin-bottom: 10px;
      font-weight: normal;
    }

    p {
      font-size: 14px;
      line-height: 1.5;
    }

    &.m--up {

      @include signUpActive {
        transform: translateX($imgW*2);
      }
    }

    &.m--in {
      transform: translateX($imgW * -2);

      @include signUpActive {
        transform: translateX(0);
      }
    }
  }

  &__btn {
    overflow: hidden;
    z-index: 2;
    position: relative;
    width: 100px;
    height: $btnH;
    margin: 0 auto;
    background: transparent;
    color: #fff;
    text-transform: uppercase;
    font-size: 15px;
    cursor: pointer;
    
    &:after {
      content: '';
      z-index: 2;
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      border: 2px solid #fff;
      border-radius: 30px;
    }

    span {
      position: absolute;
      left: 0;
      top: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      transition: transform $switchAT;
      
      &.m--in {
        transform: translateY($btnH*-2);
        
        @include signUpActive {
          transform: translateY(0);
        }
      }
      
      &.m--up {
        @include signUpActive {
          transform: translateY($btnH*2);
        }
      }
    }
  }
}

h2 {
  width: 100%;
  font-size: 26px;
  text-align: center;
}

label {
  display: block;
  width: $inputW;
  margin: 25px auto 0;
  text-align: center;

  span {
    font-size: 12px;
    color: #cfcfcf;
    text-transform: uppercase;
  }
}

input {
  display: block;
  width: 100%;
  margin-top: 5px;
  padding-bottom: 5px;
  font-size: 16px;
  border-bottom: 1px solid rgba(0,0,0,0.4);
  text-align: center;
}

.forgot-pass {
  margin-top: 15px;
  text-align: center;
  font-size: 12px;
  color: #cfcfcf;
}

.submit {
  margin-top: 40px;
  margin-bottom: 20px;
  background: #d4af7a;
  text-transform: uppercase;
}

.fb-btn {
  border: 2px solid #d3dae9;
  color: darken(#d3dae9, 20%);

  span {
    font-weight: bold;
    color: darken(#768cb6, 20%);
  }
}

.sign-in {
  transition-timing-function: ease-out;

  @include signUpActive {
    transition-timing-function: ease-in-out;
    transition-duration: $switchAT;
    transform: translate3d($formW,0,0);
  }
}

.sign-up {
  transform: translate3d($contW * -1,0,0);

  @include signUpActive {
    transform: translate3d(0,0,0);
  }
}

.icon-link {
  position: absolute;
  left: 5px;
  bottom: 5px;
  width: 32px;

  img {
    width: 100%;
    vertical-align: top;
  }

  &--twitter {
    left: auto;
    right: 5px;
  }
}
</style>