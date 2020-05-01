<template>
  <div class="frame">
    <img :src="imgPath" alt="Mona Lisa" />
  </div>
</template>

<script>
  export default {
    props:{
      imgPath: {
        type: String
      }
    }
  }
</script>

<style lang="scss" scoped>
img {
  max-height:100%;
  max-width:100%;
}

.frame {
  // margin-bottom: 5px;
  background-color:#ddc;
  border:solid 3vmin #eee;
  border-bottom-color:#fff;
  border-left-color:#eee;
  border-radius:2px;
  border-right-color:#eee;
  border-top-color:#ddd;
  box-shadow:0 0 5px 0 rgba(0,0,0,.25) inset, 0 5px 10px 5px rgba(0,0,0,.25);
  box-sizing:border-box;
  display:inline-block;
  // height:20vh;
  padding:2vmin;
  position:relative;
  text-align:center;
  &:before {
    border-radius:2px;
    bottom:-2vmin;
    box-shadow:0 2px 5px 0 rgba(0,0,0,.25) inset;
    content:"";
    left:-2vmin;
    position:absolute;
    right:-2vmin;
    top:-2vmin;
  }
  &:after {
    border-radius:2px;
    bottom:-2.5vmin;
    box-shadow: 0 2px 5px 0 rgba(0,0,0,.25);
    content:"";
    left:-2.5vmin;
    position:absolute;
    right:-2.5vmin;
    top:-2.5vmin;
  }
}
</style>