<template>
  <b-container fluid>
    <h1 center class="my-5 text-center">Treatment</h1>

    <h3 center class="my-5 text-center">Welcome {{ $auth.user.name }}!</h3>

    <b-row class="my-1">
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Patient Vitals"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <b-form-group
            label-cols-sm="3"
            label="Treatment Date:"
            label-align-sm="right"
            label-for="entry_date"
          >
            <b-form-input id="entry_date" placeholder="2020-01-01"></b-form-input>
          </b-form-group>

          <b-form-group
            label-cols-sm="3"
            label="Systolic Pressure:"
            label-align-sm="right"
            label-for="systolic_pressure"
          >
            <b-form-input id="systolic_pressure" placeholder="150"></b-form-input>
          </b-form-group>

          <b-form-group
            label-cols-sm="3"
            label="Diastolic Pressure:"
            label-align-sm="right"
            label-for="diastolic_pressure"
          >
            <b-form-input id="diastolic_pressure" placeholder="100"></b-form-input>
          </b-form-group>

          <b-form-group
            label-cols-sm="3"
            label="Weight:"
            label-align-sm="right"
            label-for="weight_in_kg"
          >
            <b-form-input id="weight_in_kg" placeholder="250"></b-form-input>
          </b-form-group>
      
          <b-button @click="submitPatientVitals" small color="primary">Submit Patient Vitals</b-button>
          <p>{{ apiMessage }}</p>
        </b-form-group>
      </b-card>
    </b-row> 
  </b-container>
</template>

<script>
import axios from "axios";

export default {
  name: "treatment",
  data() {
    return {
      apiMessage: "",
      entry_date: "",
      systolic_pressure: "",
      diastolic_pressure: "",
      weight_in_kg: ""
    };
  },
  methods: {
    async submitPatientVitals() {
      var sub_array = this.$auth.user.sub.split("|");
      if (sub_array.length == 2) {
        var user_id = sub_array[1];

        var patient_vitals = {
          user_id: user_id,
          entry_date: this.entry_date,
          systolic_pressure: this.systolic_pressure,
          diastolic_pressure: this.diastolic_pressure,
          weight_in_kg: this.weight_in_kg
        };

        // Get the access token from the auth wrapper
        const token = await this.$auth.getTokenSilently();
        // Use Axios to make a call to the API
        const { data } = await axios.post("/v1/patient_vitals", {
          headers: {
            // send the access token through the 'Authorization' header
            Authorization: `Bearer ${token}`    
          },
          params: {
            patient_vitals: patient_vitals
          }
        });
        this.apiMessage = data;
      }
    }
  }
};
</script>