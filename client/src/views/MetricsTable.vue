<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Tables"/>
          <vc-card-text>

            <b-row class="my-1">
              <b-col :span="24">
                <b-card no-body class="mb-1">
                  <b-card-header header-tag="header" class="p-1" role="tab">
                    <b-button class="btn-accordion" block v-b-toggle.accordion-1>Configure Displayed Field</b-button>
                  </b-card-header>
                  <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
                    <b-card-body>
                      <b-row align-v="center">
                        <b-col cols="5">
                          <b-list-group style="max-height: 300px; overflow:scroll; -webkit-overflow-scrolling: touch;">
                            <b-list-group-item button v-for="field in available_metrics_fields" v-bind:key="field" @click="setSelectedAvail(field, $event)">{{ field }}</b-list-group-item>
                          </b-list-group>
                        </b-col>

                        <b-col cols="2">
                          <b-row class="mb-2" align-h="center">
                            <b-button @click="addField" variant="primary">Add</b-button>
                          </b-row>
                          <b-row class="mb-2" align-h="center">
                            <b-button @click="removeField" variant="primary">Remove</b-button>
                          </b-row>
                          <b-row class="mb-2" align-h="center">
                            <b-button @click="resetFields" variant="primary">Reset</b-button>
                          </b-row>
                        </b-col>
                        
                        <b-col cols="5">
                          <b-list-group>
                            <b-list-group-item button v-for="field in displayed_metrics_fields" v-bind:key="field" @click="setSelectedDisp(field)">{{ field }}</b-list-group-item>
                          </b-list-group>
                        </b-col>
                      </b-row>

                    </b-card-body>
                  </b-collapse>
                </b-card>
              </b-col>
            </b-row>

            <b-row class="my-1">
              <b-col :span="24">
                <b-table
                  id="my-table" :items="metric_items" :fields="displayed_metrics_fields" 
                  :per-page="per_page" :current-page="current_page" small
                  :busy="is_busy">
                  <template #table-busy>
                    <div class="text-center text-danger my-2">
                      <self-building-square-spinner class="align-middle" :animation-duration="6000" :size="50" color="#2196f3"/>
                      <strong>Loading...</strong>
                    </div>
                  </template>
                </b-table>
                <b-pagination
                  v-model="current_page" :total-rows="rows" :per-page="per_page" 
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
import { SelfBuildingSquareSpinner  } from 'epic-spinners';

export default {
  components: {
    CardTitleNav,
    SelfBuildingSquareSpinner
  },
  name: "metrics-table",
  data() {
    return {
      is_busy: true,
      per_page: 10,
      current_page: 1,
      metric_items: '',
      all_metrics_fields: ['entry_date', 'user_id', 'entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 'initial_drain', 'total_uf', 'average_dwell', 'added_lost_dwell_type', 'added_lost_dwell_value', 'drain_color', 'drain_clarity', 'fibrin_present', 'exit_color', 'exit_sensitivity', 'exit_condition', 'bowel_obs', 'treatment_problems', 'comments'],
      default_metrics_fields: ['entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 'initial_drain'],
      displayed_metrics_fields: [],
      available_metrics_fields: [],
      selected_field_available: '',
      selected_field_displayed: '',
      quantity: 9999
    };
  },
  computed: {
    rows() {
      return this.metric_items.length
    }
  },
  methods: {
    setSelectedAvail(field, e) {
      const el = e.target;
      var current = document.querySelector('.active');
      if (current) {
          current.classList.remove('active');
      }
      el.classList.add('active');
      this.selected_field_available = field;
    },
    setSelectedDisp(field) {
      this.selected_field_displayed = field;
    },
    addField() {
      if (this.selected_field_available) {
        this.displayed_metrics_fields.push(this.selected_field_available);
        this.available_metrics_fields.splice(this.available_metrics_fields.indexOf(this.selected_field_available), 1);
        this.selected_field_available = '';
        this.getPatientVitals();
      }
    },
    removeField() {
      if (this.selected_field_displayed) {
        this.available_metrics_fields.push(this.selected_field_displayed);
        this.displayed_metrics_fields.splice(this.displayed_metrics_fields.indexOf(this.selected_field_displayed), 1);
        this.selected_field_displayed = '';
        this.getPatientVitals();
      }
    },
    resetFields() {
      this.displayed_metrics_fields = this.default_metrics_fields;
      this.available_metrics_fields = [];
      for (let i=0; i<this.all_metrics_fields.length; i++) {
        if (this.displayed_metrics_fields.includes(this.all_metrics_fields[i]) == false) {
          this.available_metrics_fields.push(this.all_metrics_fields[i]);
        }
      }
      this.selected_field_available = '';
      this.selected_field_displayed = '';
      this.getPatientVitals();
    },
    async getPatientVitals() {
      this.is_busy = true;
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
        this.is_busy = false;
      }
    },
  },
  beforeMount(){
    this.displayed_metrics_fields = this.default_metrics_fields;
    this.available_metrics_fields = [];
    for (let i=0; i<this.all_metrics_fields.length; i++) {
      if (this.displayed_metrics_fields.includes(this.all_metrics_fields[i]) == false) {
        this.available_metrics_fields.push(this.all_metrics_fields[i]);
      }
    }
    this.getPatientVitals();
  }
};
</script>

<style scoped>

.btn-accordion { 
  color: #ffffff; 
  background-color: #2196F3; 
  border-color: #2196F3; 
} 
 
.btn-accordion:hover, 
.btn-accordion:focus, 
.btn-accordion:active, 
.btn-accordion.active, 
.open .dropdown-toggle.btn-accordion { 
  color: #ffffff; 
  background-color: #2196F3; 
  border-color: #2196F3; 
} 
 
.btn-accordion:active, 
.btn-accordion.active, 
.open .dropdown-toggle.btn-accordion { 
  background-image: none; 
} 
 
.btn-accordion.disabled, 
.btn-accordion[disabled], 
fieldset[disabled] .btn-accordion, 
.btn-accordion.disabled:hover, 
.btn-accordion[disabled]:hover, 
fieldset[disabled] .btn-accordion:hover, 
.btn-accordion.disabled:focus, 
.btn-accordion[disabled]:focus, 
fieldset[disabled] .btn-accordion:focus, 
.btn-accordion.disabled:active, 
.btn-accordion[disabled]:active, 
fieldset[disabled] .btn-accordion:active, 
.btn-accordion.disabled.active, 
.btn-accordion[disabled].active, 
fieldset[disabled] .btn-accordion.active { 
  background-color: #2196F3; 
  border-color: #2196F3; 
} 
 
.btn-accordion .badge { 
  color: #2196F3; 
  background-color: #ffffff; 
}

</style>