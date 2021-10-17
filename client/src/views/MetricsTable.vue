<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Tables"/>
          <vc-card-text class="pa-2">

            <b-row class="my-1">
              <b-col :span="24">
                <field-selector 
                  v-bind:all_fields="all_metrics_fields"
                  v-bind:default_fields="default_metrics_fields"
                  v-bind:displayed_fields="displayed_metrics_fields"
                  @listUpdate="updateList"
                />
              </b-col>
            </b-row>

            <b-row class="my-1">
              <b-col cols="3">
                <b-card no-body class="mb-1 cmd-btn">
                  <b-button class="btn w-100" @click="print" variant="primary">
                    Print <font-awesome-icon icon="print"/>
                  </b-button>
                </b-card>
              </b-col>

              <b-col cols="6"></b-col>

              <b-col cols="3">
                <b-card no-body class="mb-1 cmd-btn">
                  <b-button class="btn w-100" @click="doExport" variant="primary">
                    Export Raw Data <font-awesome-icon icon="file-download"/>
                  </b-button>
                  <vue-blob-json-csv
                    @success="handleSuccess"
                    @error="handleError"
                    tag-name="div"
                    file-type="csv"
                    file-name="metric_items"
                    title="Download"
                    :data="metric_items"
                    confirm="Are you sure you want to download the metrics?"
                    hidden
                    ref="export"
                  >
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
                    <b-row align-v="center">
                        <b-col cols="12">
                          <b-row class="mb-2" align-h="center">
                            <div class="text-danger">
                              <self-building-square-spinner :animation-duration="6000" :size="50" color="#2196f3"/>
                              <strong>Loading...</strong>
                            </div>
                          </b-row>
                        </b-col>
                  </template>
                </b-table>
                <b-pagination
                  v-model="current_page" :total-rows="rows" :per-page="per_page" 
                  aria-controls="my-table" align="center">
                </b-pagination>
              </b-col>
            </b-row>

            <div v-show="seen" id="printMe">
              <b-row class="my-1">
                <b-col :span="24">
                  <b-table id="my-table-2" :items="metric_items" :fields="displayed_metrics_fields" small/>
                </b-col>
              </b-row>
            </div>

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
import FieldSelector from "../components/FieldSelector";

export default {
  components: {
    CardTitleNav,
    SelfBuildingSquareSpinner,
    FieldSelector
  },
  name: "metrics-table",
  data() {
    return {
      is_busy: true,
      per_page: 10,
      current_page: 1,
      metric_items: '',
      all_metrics_fields: ['entry_date', 'user_id', 'entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 
        'initial_drain', 'total_uf', 'average_dwell', 'added_lost_dwell_type', 'added_lost_dwell_value', 'drain_color', 
        'drain_clarity', 'fibrin_present', 'exit_color', 'exit_sensitivity', 'exit_condition', 'bowel_obs', 'treatment_problems', 
        'comments'],
      default_metrics_fields: ['entry_date', 'systolic_pressure', 'diastolic_pressure', 'weight_in_kg', 'initial_drain'],
      displayed_metrics_fields: [],
      quantity: 9999,
      seen: false
    };
  },
  computed: {
    rows() {
      return this.metric_items.length
    }
  },
  methods: {
    updateList(updatedList) {
      this.displayed_metrics_fields = updatedList;
    },
    doExport() {
      this.$refs.export.handleDownload();
    },
    async print () {
      const vueHtmlToPaperOptions = {
        name: '_blank',
        specs: [
          'fullscreen=yes',
          'titlebar=yes',
          'scrollbars=yes'
        ],
        styles: [
          'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
          'https://unpkg.com/kidlat-css/css/kidlat.css',
          'landscape.css'
        ],
        timeout: 1000, // default timeout before the print window appears
        autoClose: false, // if false, the window will not close after printing
        windowTitle: window.document.title, // override the window title
      };
      await this.$htmlToPaper('printMe', vueHtmlToPaperOptions);
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
    this.displayed_metrics_fields = [...this.default_metrics_fields];
    this.getPatientVitals();
  }
};
</script>

<style scoped>

.cmd-btn {
  padding-left: 4px; 
  padding-right: 4px;
}

.btn { 
  color: #ffffff; 
  background-color: #2196F3; 
  border-color: #2196F3; 
} 

.self-building-square-spinner {
  margin-right: 15px;
  margin-left: 20px;
  margin-top: 25px;
}

</style>