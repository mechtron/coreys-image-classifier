<template>
  <div class="top10">
    <ul class="list-unstyled" v-for="item,index in top10">
      <b-media tag="li">
        <b-img slot="aside" rounded="circle" width="75" height="75" blank-color="#777" alt="img" class="m-1" 
          :src="item.image_url" />
        <h5 class="mt-0 mb-1">#{{index+1}}</h5>
        Request count: {{item.classification_count}}<br/>
        Max processing time: {{item.processing_time_max.toFixed(3)}}s<br/>
        Mean processing time: {{item.processing_time_avg.toFixed(3)}}s<br/>
        Image URL: {{item.image_url}}
      </b-media>
    </ul>
  </div>
</template>

<style lang="scss">
  .top10 {
    margin-top: 80px;
    overflow: shown;
    max-width: 800px;
  }
</style>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      top10: null,
    }
  },
  mounted() {
    axios.get('../api/report')
    .then((response) => {
      console.log(response.data);
      this.fields = response.data;
      this.top10 = response.data;
    })
    .catch(function(error) {
      console.log(error);
    })
    .then(function() {
      // always executed
    });
  }
}
</script>
