<template>
    <div class="home">
      <Rating :key="modalKey" v-show="isClicked" @close-pop-up="handleClicked"/>
      <div v-show="!isClicked" class="button-container" @click="handleClicked">
        <div class="button">
            Pop-up
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Rating from '@/components/Rating.vue';

  export default {
    name: 'HomeComponent',
    components: {
      Rating
    },
    data(){
        return {
            isClicked: false,
            modalKey: 0
        }
    },
    methods:{
    handleClicked(){
      this.isClicked = !this.isClicked
      this.modalKey += 1
    }
    }
  }
  </script>
  
  <style>
  .home {
    width: 100%;
    height: 100%
  }

  .button-container{
  position: relative;
  margin: auto;
  display: flex;
  flex-direction: column;
  width: 80px;
}

.button{
  display: flex;
  background: #2F80ED;
  border-radius: 4px;
  justify-content: center;
  padding: 0.5rem;
  color: white;
  font-weight: 600;
  margin-top: 1rem;
}

.button:hover{
  cursor: pointer, auto;
}
  </style>
  