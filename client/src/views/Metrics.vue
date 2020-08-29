<template>
  <b-container fluid>
    <h1 class="my-5 text-center">Metrics</h1>

    <b-row class="my-1">
      <b-table striped hover :items="metricItems" :fields="metricsFields"></b-table>
    </b-row>
    
  </b-container>
</template>

<script>
import axios from "axios";

export default {
  name: "metrics",
  data() {
    return {
      metricItems: "",
      metricsFields: ['entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg'],
      quantity: 9999
    };
  },
  methods: {
    async getPatientVitals() {
      var sub_array = this.$auth.user.sub.split("|");
      if (sub_array.length == 2) {
        var user_id = sub_array[1];
        // Get the access token from the auth wrapper
        const token = await this.$auth.getTokenSilently();
        // Use Axios to make a call to the API
        const { data } = await axios.get("/v1/patient_vitals", {
          headers: {
            // send the access token through the 'Authorization' header
            Authorization: `Bearer ${token}`    
          },
          params: {
            user_id: user_id,
            quantity: this.quantity
          }
        });
        this.metricItems = data;
      }
    }
  },
  beforeMount(){
    this.getPatientVitals()
  },
};
</script>