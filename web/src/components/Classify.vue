<template lang="html">
  <div class="content-centered">
    <h3>Classify an image now:</h3>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="classifyImageInputGroup"
            label-for="image_url"
            description="We currently support JPEG, PNG and GIF image formats">
            <b-form-input id="classifyImageInputForm"
                type="text"
                v-model="form.image_url"
                required
                placeholder="Paste an image link">
            </b-form-input>
        </b-form-group>
        <b-button type="reset" variant="warning">Reset</b-button>
        <button-spinner
            type="submit"
            id="classifyButton"
            :is-loading="classify_button_laoding"
            :disabled="classify_button_laoding"
            :status="classify_button_status">
            <span>{{this.classify_button_text}}</span>
        </button-spinner>
    </b-form>
    <div>
        <b-modal id="modal-center"
            ref="classificationModal"
            title="Classification"
            centered
            ok-only
            ok-variant="success">
                <b-container class="bv-example-row">
                    <b-row>
                        <b-col class="text-sm-right"><b>Result</b></b-col>
                        <b-col class="text-sm-left">{{this.classification}}</b-col>
                    </b-row>
                    <b-row>
                        <b-col class="text-sm-right"><b>Confidence</b></b-col>
                        <b-col class="text-sm-left">{{this.confidence}}</b-col>
                    </b-row>
                    <b-row>
                        <b-col class="text-sm-right"><b>Processing time</b></b-col>
                        <b-col class="text-sm-left">{{this.processing_time}}</b-col>
                    </b-row>
                </b-container>
        </b-modal>
    </div>
  </div>
</template>

<style lang="scss">
  #classifyButton {
    color: #fff;
    background-color: #28a745;
    border-color: #28a745;
    margin: 1px;
  }
</style>

<script>
import axios from 'axios';
export default {
  data () {
    return {
      form: {
        image_url: 'https://s3.amazonaws.com/gumgum-interviews/ml-engineer/cat.jpg',
      },
      classification: null,
      confidence: null,
      processing_time: null,
      show: true,
      classify_button_status: '',
      classify_button_laoding: false,
      classify_button_text: "Classify!",
    }
  },
  methods: {
    onSubmit (evt) {
      this.classify_button_laoding = true
      this.classify_button_text = "Thinking.."
      evt.preventDefault();
      axios({
        method: 'post',
        url: 'http://localhost:8000/classify-image',
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
        crossdomain: true,
        data: {
          image_url: this.form.image_url,
        },
      })
      .then(response => {
        this.classify_button_laoding = false
        this.classify_button_text = "Classify!"
        this.classification = response.data.classification,
        this.confidence = (response.data.confidence*100).toFixed(2) + '%',
        this.processing_time = response.data.processing_time.toFixed(3) + 's'
        this.$refs.classificationModal.show()
      })
      .catch( error => {
        console.log('-----error-------');
        console.log(error)
      })
    },
    onReset (evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.image_url = '';
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => { this.show = true });
    }
  }
}
</script>
