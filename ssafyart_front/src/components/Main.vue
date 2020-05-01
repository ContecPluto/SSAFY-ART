<template>
  <div>
    <br>
    <div id="logo" class="mb-5">
      <div id="logo-word">
        <p id="logo-word-main" class="mb-3">SSAFY ART</p>
        <p id="logo-word-content">원하는 예술가의 스타일로 당신의 사진을 다시 그려보세요.</p>
        <button class="btn btn-primary mb-3 logo-button" @click="goCreate">create</button>
        <!-- <button class="button-ani logo-button" @click="goCreate">
          Create
          <span></span><span></span><span></span><span></span>
        </button> -->
        
      </div>
    </div>
    <div class="container mb-5">
      <p class="partHeader">사진 변화하기</p>
      <p class="partContent">우리는 당신을 위해 여러가지 스타일의 예술가의 그림을 준비했어요. 당신은 다음의 3단계에 맞춰 선택해주세요. 그러면 우리가 준비한 알고리즘은 당신의 사진을 선택한 스타일로 다시 그려줄거에요.</p>
      <div class="row step">
        <p class="col-4">1. 사진을 업로드하기</p>
        <p class="col-4">2. 스타일을 선택하기</p>
        <p class="col-4">3. 제출하기</p>
        <img src="@/assets/contents/cow.jpeg" class="col-4" alt="">
        <img src="@/assets/styles/white_cow.jpg" class="col-4" alt="">
        <img src="@/assets/results/result_153738.jpg" class="col-4" alt="">
      </div>
    </div>
    <div class="bg-light">
      <div class="container">
        <p class="partHeader mb-2">Example</p>
        <div class="row">
          <card-flib class="mb-2 p-2" v-for="(example, n) in examples" :key="n" :imgPath="example.imgPath" :imgPath2="example.imgPath2" :imgPath3="example.imgPath3"></card-flib>
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
        examples: [
          {
            imgPath: require('@/assets/contents/europe2.jpg'),
            imgPath2: require('@/assets/styles/creation_of_adam.jpg'),
            imgPath3: require('@/assets/results/europe2.jpg_transform.jpg'),
          },
          {
            imgPath: require('@/assets/contents/europe.jpg'),
            imgPath2: require('@/assets/styles/white_cow.jpg'),
            imgPath3: require('@/assets/results/164000.jpg'),
          },
          {
            imgPath: require('@/assets/contents/wave_picture.jpg'),
            imgPath2: require('@/assets/styles/wave.jpg'),
            imgPath3: require('@/assets/results/wave_picture_wave_transform.jpg'),
          },
          {
            imgPath: require('@/assets/contents/bulkho4.jpg'),
            imgPath2: require('@/assets/styles/buddhism.jpg'),
            imgPath3: require('@/assets/results/bulkho4.jpg_transform.jpg'),
          },
          {
            imgPath: require('@/assets/contents/creek.jpg'),
            imgPath2: require('@/assets/styles/ShinYunbok.jpg'),
            imgPath3: require('@/assets/results/result_194650.jpg'),
          },
          {
            imgPath: require('@/assets/contents/venezia.jpg'),
            imgPath2: require('@/assets/styles/Kandinsky.jpg'),
            imgPath3: require('@/assets/results/venezia.jpg_transform.jpg'),
          },
          {
            imgPath: require('@/assets/contents/city.png'),
            imgPath2: require('@/assets/styles/the_starry_night.jpg'),
            imgPath3: require('@/assets/results/164000_city.jpg'),
          },
          {
            imgPath: require('@/assets/contents/last-supper.jpg'),
            imgPath2: require('@/assets/styles/udnie.jpg'),
            imgPath3: require('@/assets/results/last-supper_transform.jpg'),
          },
          {
            imgPath: require('@/assets/contents/car.jpg'),
            imgPath2: require('@/assets/styles/composition_VII.jpg'),
            imgPath3: require('@/assets/results/164000_car.jpg'),
          },
          {
            imgPath: require('@/assets/contents/sad.jpg'),
            imgPath2: require('@/assets/styles/la_muse.jpg'),
            imgPath3: require('@/assets/results/result_19323.jpg'),
          },
          {
            imgPath: require('@/assets/contents/bird.jpg'),
            imgPath2: require('@/assets/styles/sand_art.jpg'),
            imgPath3: require('@/assets/results/result_1959.jpg'),
          },
          {
            imgPath: require('@/assets/contents/btidge.jpg'),
            imgPath2: require('@/assets/styles/the_scream.jpg'),
            imgPath3: require('@/assets/results/result_20141.jpg'),
          },
          
        ],
       
      }
    },
    components: {
      cardFlib: Card,
    },
    methods: {
      goCreate() {
        this.$router.push({name:'Create'})
      }
    }
  }
</script>

<style>


.button-ani {
    --c: rgb(0, 0, 0);
    color: var(--c);
    font-size: 16px;
    border: 0.3em solid var(--c);
    border-radius: 0.5em;
    width: 12em;
    height: 3em;
    text-transform: uppercase;
    font-weight: bold;
    font-family: sans-serif;
    letter-spacing: 0.1em;
    text-align: center;
    line-height: 3em;
    position: relative;
    overflow: hidden;
    z-index: 1;
    transition: 0.5s;
    margin: 1em;
}

.button-ani span {
    position: absolute;
    width: 25%;
    height: 100%;
    background-color: var(--c);
    transform: translateY(150%);
    border-radius: 50%;
    left: calc((var(--n) - 1) * 25%);
    transition: 0.5s;
    transition-delay: calc((var(--n) - 1) * 0.1s);
    z-index: -1;
}

.button-ani:hover {
    color: white;
}

.button-ani:hover span {
    transform: translateY(0) scale(2);
}

.button-ani span:nth-child(1) {
    --n: 1;
}

.button-ani span:nth-child(2) {
    --n: 2;
}

.button-ani span:nth-child(3) {
    --n: 3;
}

.button-ani span:nth-child(4) {
    --n: 4;
}

.partHeader {
  font-size: 3em;
}

.partContent{
  font-size: 1.3em;
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
  font-size: 10em;
  font-family: 'East Sea Dokdo', cursive;
  position: relative;
}

#logo-word-content{
  position: relative;
  top: -50px;
  font-size: 1.1em;
}

.logo-button{
  position: relative;
  top: -40px;
}

.step > p{
  font-weight: bold;
  text-align: center;
}
</style>