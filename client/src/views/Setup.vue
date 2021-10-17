<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Setup"/>

          <vc-card-text>
            
            <b-row class="my-1">
              <b-col sm="3">
                <div class="my-2">
                  <b-button @click="callApi" small color="primary">Get Test</b-button>
                </div>
                <p>{{ apiMessage1 }}</p>
              </b-col>
            </b-row>

            <b-row class="my-1">
              <b-col sm="3">
                <b-form-input
                  v-model="user_id"
                  label="User ID"
                  placeholder="123"
                ></b-form-input>
              </b-col>
              <b-col sm="3">
                <b-form-input
                  v-model="quantity"
                  label="Quantity"
                  placeholder="1"
                ></b-form-input>
              </b-col>
              <b-col sm="3">
                <b-button @click="getPatientVitals" small color="primary">Get Patient Vitals</b-button>
                <p>{{ apiMessage2 }}</p>
              </b-col>
            </b-row>
    
          </vc-card-text>
        </vc-card>
      </vc-col>
    </vc-layout>
  </b-container>
</template>

<script>
import axios from "axios";
import CardTitleNav from "../components/CardTitleNav";

export default {
  components: {
    CardTitleNav
  },
  name: "inventory",
  data() {
    return {
      apiMessage1: "",
      apiMessage2: "",
      user_id: "",
      quantity: ""
    };
  },
  methods: {
    async callApi() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      // Use Axios to make a call to the API
      const { data } = await axios.get("/v1/test", {
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        }
      });
      this.apiMessage1 = data;
    },
    async getPatientVitals() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      // Use Axios to make a call to the API
      const { data } = await axios.get("/v1/patient_vitals", {
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        },
        params: {
          user_id: this.user_id,
          quantity: this.quantity
        }
      });
      this.apiMessage2 = data;
    }
  }
};
</script>