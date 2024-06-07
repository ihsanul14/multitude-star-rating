<template>
  <div>
    <div class="pop-up" @click="handleClosed"></div>
    <div v-show="data.error !== null" class="exception-box w3-animate-top">
      <div class="exception-box-header">!! Error !!</div>
      <div class="exception-box-message">{{data.error}}</div>
    </div>
    <div v-show="!data.isLoading && !isSubmit && data.error === null" class="rating w3-animate-top">
      <div class="progress-box">
        <div class="progress-bar" :style="{width: parseRatingsToProgress()}"></div>  
      </div>
      <div class="rating-header">How would you rate your satisfaction with out product?</div>
      <br />
      <div class="rating-box">
        <div v-for="(v,i) in data.data" :key="i" class="rating-box-option">
          <div @click="handleClicked(i);handleSubmit(i)" class="rating-box-option-data">
            <div class="rating-box-option-data-icon">
              <svg v-show="v.isClicked" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="#707271">
                <path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/>
              </svg>
              <svg v-show="!v.isClicked" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="#707271">
                <path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/>
              </svg>
            </div>
            <div class="rating-box-option-data-text">
              {{v.score}}
            </div>
          </div>
        </div>
      </div>
      <div class="rating-caption">
        <div class="rating-caption-text">Very dissatisfied</div>
        <div class="rating-caption-text" style="text-align: right;">Very satisfied</div>
      </div>
    </div>
    <div v-show="isSubmit" style="position: absolute;margin: 0;top: 50%; bottom: 50%;left: 50%;right: 50%;">
      <Loading />
    </div>
  </div>
</template>

<script>
import { handleClicked, getRating, submit } from './script'
import Loading from '@/components/Loading.vue'

export default {
  name: 'RatingComponent',
  components: {
    Loading
  },
  data(){
    return {
      data: {
          data : [
            {
              isClicked: false,
              score: 1
            },
            {
              isClicked: false,
              score: 2
            },
            {
              isClicked: false,
              score: 3
            },
            {
              isClicked: false,
              score: 4
            },
            {
              isClicked: false,
              score: 5
            },
          ],
          rating: 0,
          isLoading: true,
          error: null
        },
        isClicked: false,
        isSubmit: false
      }
  },
  mounted(){
    getRating(this.data)
  },
  methods:{
    handleClicked(target){
      handleClicked(this.data.data, target)
    },
    handleClosed(){
      this.$emit('close-pop-up')
    },
    handleSubmit(i){
      const payload = {
        rating: parseInt(this.data.data[i].score)
      }
      this.isSubmit = true
      setTimeout(()=> {
        submit(payload, this.data)
        this.data.isLoading = false
        this.handleClosed()
      }, 1000)
    },
  },
  computed:{
    parseRatingsToProgress(){
      return function(){
        return `${100 * this.data.rating/5}%`
      }
    }
  }
}
</script>

<style scoped>
.pop-up{
  position: absolute;
  opacity: 60%;
  background: black;
  height: 100%;
  width: 100%;
}
.rating{
  position: absolute;
  top: 2rem;
  left: 0;
  right: 0;
  margin: auto;
  border-radius: 8px;
  max-width: 320px;
  max-height: 50vh;
  background: #f2f2f2;
  padding: 2rem;
}

.progress-box{
  border-radius: 1rem; 
  background: grey;
  margin-bottom: 1rem;
}

.progress-bar{
  border-radius: 1rem;
  padding: 0.2rem 0;
  background: #5F14ED;
}

.rating-header{
  font-weight: 600;
  font-size: 20px;
  text-align: left;
}

.rating-box{
  display: flex;
  margin-bottom: 1rem;
  gap: 0.5rem
}

.rating-box-option{
  flex: 1;
}

.rating-box-option-data{
  display: flex;
  flex-direction: column;
  gap: 0.5rem
}


.rating-box-option-data-icon{
  flex: 1;
}

.rating-box-option-data-text{
  flex: 1;
}

.rating-caption{
  display: flex;
  gap: 1rem
}

.rating-caption-text{
  flex: 1;
  text-align: left;
  font-size: 14px;
}

.exception-box{
  position: absolute;
  top: 0;
  bottom: 50%;
  left: 0;
  right: 0;
  margin: auto;
  border-radius: 8px;
  max-width: 320px;
  max-height: 14vh;
  background: #f2f2f2;
  padding: 1rem;
}

.exception-box-header{
  color: red;
  font-size: 24px;
  font-weight: 600;
  padding-bottom: 1rem;
}

.exception-box-message{
  font-size: 18px;
  font-weight: 500;
}
</style>
