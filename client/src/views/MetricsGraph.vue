<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Graphs"/>
          <vc-card-text class="pa-2">

            <b-row class="my-1">
              <b-col :span="24">
                <field-selector 
                  v-bind:all_fields="all_metrics_fields"
                  v-bind:default_fields="default_metrics_fields"
                  v-bind:displayed_fields="displayed_fields"
                  @listUpdate="updateList"
                />
              </b-col>
            </b-row>

            <b-row class="my-1">
              <b-col :span="24">
                <line-chart v-if="metric_items"
                  v-bind:graph_data="metric_items"
                  v-bind:column_list="displayed_fields"
                  v-bind:date_field_name="date_field_name">
                </line-chart>
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
import LineChart from "../components/LineChart";
import FieldSelector from "../components/FieldSelector";

export default {
  components: {
    CardTitleNav,
    LineChart,
    FieldSelector
  },
  name: "metrics-graph",
  data() {
    return {
      metric_items: null,
      all_metrics_fields: ['systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 
        'initial_drain', 'total_uf', 'average_dwell', 'added_lost_dwell_type', 'added_lost_dwell_value'],
      default_metrics_fields: ['systolic_pressure','diastolic_pressure'],
      displayed_fields: ['systolic_pressure','diastolic_pressure'],
      date_field_name: 'entry_date',
      quantity: 10
    };
  },
  computed: {
  },
  methods: {
    updateList(updatedList) {
      this.displayed_fields = updatedList;
    },
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
    this.displayed_fields = [...this.default_metrics_fields];
    this.getPatientVitals();
  },
};
</script>