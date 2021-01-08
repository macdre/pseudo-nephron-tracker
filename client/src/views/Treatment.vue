<template>
  <b-container id="axiosForm" fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Treatment"/>
          <div class="Center-Container" v-if="loading">
            <div class="Absolute-Center">
              <self-building-square-spinner :animation-duration="6000" :size="100" color="#2196f3"/>
            </div>
          </div>
          <vc-card-text>
            <div class="contact-form-success alert alert-success mt-4" v-if="success">
              <strong>Success!</strong> Your treatment was recorded.
            </div>

            <div class="contact-form-error alert alert-danger mt-4" v-if="error">
              <strong>Error!</strong> There was a problem saving your treatment record.
            </div>

            <b-form @submit.prevent="submitPatientVitals" @reset="onReset">
              <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Vitals</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Treatment Date:"
                    label-align-sm="right"
                    label-for="entry_date"
                  >
                    <b-form-datepicker
                      today-button
                      reset-button
                      close-button
                      id="entry_date"
                      v-model="entry_date"
                      reset-value="entry_date"
                      :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                      locale="en-CA"
                    ></b-form-datepicker>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Systolic Pressure:"
                    label-align-sm="right"
                    label-for="systolic_pressure"
                  >
                    <b-form-input required id="systolic_pressure" v-model.number="systolic_pressure" placeholder="Please Enter" type="number"></b-form-input>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Diastolic Pressure:"
                    label-align-sm="right"
                    label-for="diastolic_pressure"
                  >
                    <b-form-input required id="diastolic_pressure" v-model.number="diastolic_pressure" placeholder="Please Enter" type="number"></b-form-input>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Weight(kg):"
                    label-align-sm="right"
                    label-for="weight_in_kg"
                  >
                    <b-form-input required id="weight_in_kg" v-model.number="weight_in_kg" placeholder="Please Enter" type="number"></b-form-input>
                  </b-form-group>
                </vc-col>
                
                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Treatment Details</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Initial Drain:"
                    label-align-sm="right"
                    label-for="initial_drain"
                  >
                    <b-form-input required id="initial_drain" v-model.number="initial_drain" placeholder="Please Enter" type="number"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Total UF:"
                    label-align-sm="right"
                    label-for="total_uf"
                  >
                    <b-form-input required id="total_uf" v-model.number="total_uf" placeholder="Please Enter" type="number"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Average Dwell:"
                    label-align-sm="right"
                    label-for="average_dwell"
                  >
                    <!-- Hard code the locale to de as it gives us a 24 hour clock that is 0-based -->
                    <b-form-timepicker required id="average_dwell" v-model="average_dwell" locale="de"></b-form-timepicker>
                  </b-form-group>
                  <b-form-row class="justify-content-end">
                    <b-col class="col-auto"><label class="Absolute-Center">Added/Lost Dwell:</label></b-col>
                    <b-col class="col-auto"><b-form-select required id="added_lost_dwell_type" v-model="added_lost_dwell_type" :options="addedLostOptions"/></b-col>
                    <b-col class="col-auto"><b-form-timepicker required id="added_lost_dwell_value" v-model="added_lost_dwell_value" locale="de"/></b-col>
                  </b-form-row>
                </vc-col>

                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Drain Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Drain Color:"
                    label-align-sm="right"
                    label-for="drain_color"
                  >
                    <b-form-select required id="drain_color" v-model="drain_color" :options="drainColorOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Drain Clarity:"
                    label-align-sm="right"
                    label-for="drain_clarity"
                  >
                    <b-form-select required id="drain_clarity" v-model="drain_clarity" :options="drainClarityOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Fibrin Present:"
                    label-align-sm="right"
                    label-for="fibrin_present"
                  >
                    <b-form-select required id="fibrin_present" v-model="fibrin_present" :options="fibrinPresentOptions"></b-form-select>
                  </b-form-group>
                </vc-col>

                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Exit and Tunnel Site Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Color:"
                    label-align-sm="right"
                    label-for="exit_color"
                  >
                    <b-form-select required id="exit_color" v-model="exit_color" :options="exitColorOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Sensitivity:"
                    label-align-sm="right"
                    label-for="exit_sensitivity"
                  >
                    <b-form-select required id="exit_sensitivity" v-model="exit_sensitivity" :options="exitSensitivityOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Site Condition:"
                    label-align-sm="right"
                    label-for="exit_condition"
                  >
                    <b-form-select required id="exit_condition" v-model="exit_condition" :options="exitConditionOptions"></b-form-select>
                  </b-form-group>                  
                </vc-col>

                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Misc. Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Bowel Observations:"
                    label-align-sm="right"
                    label-for="bowel_obs"
                  >
                    <b-form-select required id="bowel_obs" v-model="bowel_obs" :options="bowelObsOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Treatment Problems?"
                    label-align-sm="right"
                    label-for="treatment_problems"
                  >
                    <b-form-select required id="treatment_problems" v-model="treatment_problems" :options="treatProbOptions"></b-form-select>
                  </b-form-group>                  
                </vc-col>
                
                <vc-col :span="12" xs24 sm12 md6>
                  <h5>Notes/Comments</h5>
                  <br/>
                  <b-form-textarea
                    id="comments"
                    v-model="comments"
                    placeholder="Enter Comments..."
                    rows="3"
                    max-rows="6"
                  ></b-form-textarea>
                </vc-col>
              </vc-layout>

              <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
                <vc-col :span="24">
                  <b-button class="mr-2" type="submit" variant="primary">Submit</b-button>
                  <b-button class="mr-2" type="reset" variant="danger">Reset</b-button>
                </vc-col>
              </vc-layout>

            </b-form>
          </vc-card-text>
        </vc-card>
      </vc-col>
    </vc-layout>
  </b-container>
</template>

<script>
import axios from "axios";
import moment from "moment";
import CardTitleNav from "../components/CardTitleNav";
import { SelfBuildingSquareSpinner  } from 'epic-spinners';

export default {
  components: {
    CardTitleNav,
    SelfBuildingSquareSpinner
  },
  name: "treatment",
  data() {
    return {
      success: false,
      error: false,
      loading: false,
      entry_date: moment.utc(new Date()).local().format('YYYY-MM-DD'),
      systolic_pressure: "",
      diastolic_pressure: "",
      weight_in_kg: "",
      initial_drain: "",
      total_uf: "",
      average_dwell: "01:30",
      added_lost_dwell_type: null,
      added_lost_dwell_value: "00:00",
      drain_color: null,
      drain_clarity: null,
      fibrin_present: null,
      exit_color: null,
      exit_sensitivity: null,
      exit_condition: null,
      bowel_obs: null,
      treatment_problems: null,
      comments: null,
      addedLostOptions: [
        { value: null, text: 'Select...' },
        { value: 'added', text: 'Added' },
        { value: 'lost', text: 'Lost' },
      ],
      drainColorOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'no-color', text: 'No Color' },
        { value: 'yellow', text: 'Yellow' },
        { value: 'dark-yellow', text: 'Dark Yellow' },
        { value: 'pink', text: 'Pink' },
        { value: 'red', text: 'Red' }
      ],
      drainClarityOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'clear', text: 'Clear' },
        { value: 'cloudy', text: 'Cloudy' },
        { value: 'very-cloudy', text: 'Very Cloudy' }
      ],
      fibrinPresentOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'no', text: 'No' },
        { value: 'yes', text: 'Yes' }
      ],
      exitColorOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'normal', text: 'Normal' },
        { value: 'redness', text: 'Redness' }
      ],
      exitSensitivityOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'normal', text: 'Normal' },
        { value: 'tender', text: 'Tender' },
        { value: 'painful', text: 'Painful' }
      ],
      exitConditionOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'normal', text: 'Normal' },
        { value: 'swelling', text: 'Swelling' },
        { value: 'discharge', text: 'Discharge' }
      ],
      bowelObsOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'liquid', text: 'Liquid' },
        { value: 'soft', text: 'Soft' },
        { value: 'normal', text: 'Normal' },
        { value: 'hard', text: 'Hard' },
        { value: 'bloody', text: 'Bloody' },
        { value: 'no-stool', text: 'No Stool For Last 24 Hours' }
      ],
      treatProbOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'no', text: 'No' },
        { value: 'yes', text: 'Yes' }
      ]
    };
  },
  methods: {
    async submitPatientVitals(e) {
      console.log("Hitting the submit button!!!!");
      var sub_array = this.$auth.user.sub.split("|");
      if (sub_array.length == 2) {
        var user_id = sub_array[1];

        var patient_vitals = {
          user_id: user_id,
          entry_date: this.entry_date,
          systolic_pressure: this.systolic_pressure,
          diastolic_pressure: this.diastolic_pressure,
          weight_in_kg: this.weight_in_kg,
          initial_drain: this.initial_drain,
          total_uf: this.total_uf,
          average_dwell: this.average_dwell,
          added_lost_dwell_type: this.added_lost_dwell_type,
          added_lost_dwell_value: this.added_lost_dwell_value,
          drain_color: this.drain_color,
          drain_clarity: this.drain_clarity,
          fibrin_present: this.fibrin_present,
          exit_color: this.exit_color,
          exit_sensitivity: this.exit_sensitivity,
          exit_condition: this.exit_condition,
          bowel_obs: this.bowel_obs,
          treatment_problems: this.treatment_problems,
          comments: this.comments
        };
        
        console.log(JSON.stringify(patient_vitals));

        // Get the access token from the auth wrapper
        const token = await this.$auth.getTokenSilently();

        this.loading = true;

        // Use Axios to make a call to the API
        axios
          .post("/v1/patient_vitals", 
            {
              patient_vitals: patient_vitals
            },
            {
              headers: {
                // send the access token through the 'Authorization' header
                Authorization: `Bearer ${token}`    
              }
            }
          )
          .then(res => {
            this.onReset(e);
            this.success = true;
            console.log(res);
          })
          .catch(error => {
            this.error = true;
            console.log(error);
          })
          .finally(() => {
            this.loading = false;
          });                      

        //this.apiMessage = data;
      }
    },
    onReset(e) {
      e.preventDefault()
      // Reset our form values
      this.entry_date = moment.utc(new Date()).local().format('YYYY-MM-DD')
      this.systolic_pressure = ""
      this.diastolic_pressure = ""
      this.weight_in_kg = ""
      this.initial_drain = ""
      this.total_uf = ""
      this.average_dwell = "01:30"
      this.added_lost_dwell_type = null
      this.added_lost_dwell_value = "00:00"
      this.drain_color = null
      this.drain_clarity = null
      this.fibrin_present = null
      this.exit_color = null
      this.exit_sensitivity = null
      this.exit_condition = null
      this.bowel_obs = null
      this.treatment_problems = null
      this.comments = null

      this.success = false
      this.error = false
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
};
</script>

<style scoped>
#axiosForm {
  /* Components Root Element ID */
  position: relative;
}

.Center-Container {
  position: absolute;
  top: 0px;
  right: 0px;
  width: 100%;
  height: 100%;
  background-color: #eceaea;
  background-size: 50px;
  background-repeat: no-repeat;
  background-position: center;
  z-index: 10000000;
  opacity: 0.7;
  filter: alpha(opacity=70);
}

.Absolute-Center {
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  text-align: center;
}
</style>