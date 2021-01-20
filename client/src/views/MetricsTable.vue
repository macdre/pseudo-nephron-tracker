<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Tables"/>
          <vc-card-text>
            <b-row class="my-1">
              <b-col :span="24">
                <b-table
                  id="my-table" :items="metricItems" :fields="metricsFields" 
                  :per-page="perPage" :current-page="currentPage" small>
                </b-table>
                <b-pagination
                  v-model="currentPage" :total-rows="rows" :per-page="perPage" 
                  aria-controls="my-table" align="center">
                </b-pagination>
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
  name: "metrics-table",
  data() {
    return {
      perPage: 10,
      currentPage: 1,
      metricItems: "",
      metricsFields: ['entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 'initial_drain'],
      quantity: 9999
    };
  },
  computed: {
    rows() {
      return this.metricItems.length
    }
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