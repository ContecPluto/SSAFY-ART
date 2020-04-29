<template>
  <div class="my-5 container">
    <br>
    <p class="title">About us</p>
    <div class="about-word">
      <p>우리는 남녀노소 누구나 몇번의 클릭만으로 예술적인 그림을 만들고 공유할 수 있는 사이트를 만들기 위해 모였습니다.</p>
      <p>사진을 업로드하고 좋아하는 작품을 선택하세요.</p>
      <p>깜짝 놀랄만한 작품이 탄생하게 될 것입니다.</p>
      <br>
      <p>내가 가지고 있는 사진을 원하는 그림 스타일로 바꿀 수 있습니다.</p>
      <br>
      <p>자, 그럼 지금부터 좋아하는 아티스트의 스타일로 사진을 바꿔볼까요?</p>
    </div>
    <br>

    <div class="d-flex row justify-content-center">
      <div class="col-2 m-1">
        <img class="profile" src="@/assets/about/joong-bae-JEON.jpg" alt="">
        <p class="text-center m-0 font-weight-bold about-text-title">전중배</p>
        <p class="text-center m-0 about-text-content">프로젝트 관리</p>
        <p class="text-center about-text-content">데이터확보 및 전처리</p>
      </div>
      <div class="col-2 m-1">
        <img class="profile" src="@/assets/about/Kang_Taeyang.jpg" alt="">
        <p class="text-center m-0 font-weight-bold about-text-title">강태양</p>
        <p class="text-center m-0 about-text-content">데이터확보 및 전처리</p>
        <p class="text-center about-text-content">백엔드</p>
      </div>
      <div class="col-2 m-1">
        <img class="profile" src="@/assets/about/kimjunho.jpg" alt="">
        <p class="text-center m-0 font-weight-bold about-text-title">김준호</p>
        <p class="text-center m-0 about-text-content">프론트엔드</p>
        <p class="text-center about-text-content">인공지능모델구현</p>
      </div>
      <div class="col-2 m-1 my-auto">
        <img class="profile" src="@/assets/about/result_172852.jpg" alt="">
        <p class="text-center m-0 font-weight-bold about-text-title">염동환</p>
        <p class="text-center m-0 about-text-content">백엔드</p>
        <p class="text-center about-text-content">인공지능모델구현</p>
      </div>
      <div class="col-2 m-1">
        <img class="profile" src="@/assets/about/ByeongjunCho.jpg" alt="">
        <p class="text-center m-0 font-weight-bold about-text-title">조병준</p>
        <p class="text-center m-0 about-text-content">인공지능모델구현</p>
        <p class="text-center about-text-content">AWS환경구축</p>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style scoped>
.profile{
  width: 100%;
}

.about-word >p{
  margin: 0px;
  font-size: 1.2em
}

.about-word{
  margin-bottom: 40px;
}

.about-text-title{
  font-size: 1.1em;
}

.about-text-content{
  font-size: 0.9em;
}
</style>