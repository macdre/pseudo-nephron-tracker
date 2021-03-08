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
                      <b-row>
                        <b-col cols="5">
                          <b-list-group style="max-height: 300px; overflow:scroll; -webkit-overflow-scrolling: touch;">
                            <b-list-group-item button>Button item</b-list-group-item>
                            <b-list-group-item button>I am a button</b-list-group-item>                            
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
                          </b-list-group>
                        </b-col>

                        <b-col class="text-center" align-v="center" cols="2">
                          <b-row>
                            <b-button>Add</b-button>
                          </b-row>
                          <b-row>
                            <b-button>Remove</b-button>
                          </b-row>
                          <b-row>
                            <b-button>Reset</b-button>
                          </b-row>
                        </b-col>
                        
                        <b-col cols="5">
                          <b-list-group>
                            <b-list-group-item button>Button item</b-list-group-item>
                            <b-list-group-item button>I am a button</b-list-group-item>
                            <b-list-group-item button disabled>Disabled button</b-list-group-item>
                            <b-list-group-item button>This is a button too</b-list-group-item>
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
                  id="my-table" :items="metric_items" :fields="metrics_fields" 
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
      metric_items: "",
      metrics_fields: ['entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 'initial_drain'],
      quantity: 9999
    };
  },
  computed: {
    rows() {
      return this.metric_items.length
    }
  },
  methods: {
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
    }
  },
  beforeMount(){
    this.getPatientVitals()
  },
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