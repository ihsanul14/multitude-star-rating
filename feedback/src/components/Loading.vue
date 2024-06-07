<template>
  <div class="loading-container">
    <div class='loading-content'>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoadingComponent',
  props:{
    name: String
  }
}
</script>
<style >

.loading-container{
  height: '100vh';
  width: '100vw';
  display:'flex';
  justify-content:'center';
  align-items:'center';
  flex-direction: column;
}
.loading-content {
  border: 8px solid white;
  border-top: 8px solid #828282;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin: auto;
  margin-bottom: 0.5rem;
}


@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
