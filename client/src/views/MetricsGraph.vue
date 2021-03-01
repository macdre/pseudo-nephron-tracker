<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Graphs"/>
          <vc-card-text>
            <b-row class="my-1">
              <b-col :span="24">
                <D3LineChart :config="chart_config" :datum="metric_items" :key="metric_items"></D3LineChart>
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
import { D3LineChart } from 'vue-d3-charts';

export default {
  components: {
    CardTitleNav,
    D3LineChart
  },
  name: "metrics-graph",
  data() {
    return {
      quantity: 9999,
      chart_config: {
        date: {
          key: "entry_date"
        },
        values: ["entry_date", "systolic_pressure", "diastolic_pressure", "weight_in_kg", "initial_drain"],
        axis: {
          yTitle: "Thingers",
          xTitle: "Thangers"
        }
      },
      metric_items: []
    };
  },
  computed: {
    rows() {
      return this.metric_items.length
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
        this.metric_items = data;
      }
    }
  },
  beforeMount(){
    this.getPatientVitals()
  },
};
</script>