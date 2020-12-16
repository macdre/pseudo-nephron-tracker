<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Treatment"/>
          <vc-card-text>
            <b-form @submit="submitPatientVitals" @reset="onReset">
              <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
                <vc-col :span="8" xs24 sm12 md6>
                  <h5>Vitals</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Treatment Date:"
                    label-align-sm="right"
                    label-for="entry_date"
                  >
                    <b-form-datepicker
                      id="entry_date"
                      today-button
                      reset-button
                      close-button
                      v-model="defaultDate"
                      reset-value="defaultDate"
                      v-if="!isReset"
                    ></b-form-datepicker>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Systolic Pressure:"
                    label-align-sm="right"
                    label-for="systolic_pressure"
                  >
                    <b-form-input v-model.number="systolic_pressure" placeholder=180 type="number"></b-form-input>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Diastolic Pressure:"
                    label-align-sm="right"
                    label-for="diastolic_pressure"
                  >
                    <b-form-input v-model.number="diastolic_pressure" placeholder=130 type="number"></b-form-input>
                  </b-form-group>

                  <b-form-group
                    label-cols-sm="6"
                    label="Weight(kg):"
                    label-align-sm="right"
                    label-for="weight_in_kg"
                  >
                    <b-form-input v-model.number="weight_in_kg" placeholder=300 type="number" ></b-form-input>
                  </b-form-group>
                </vc-col>
                
                <vc-col :span="8" xs24 sm12 md6>
                  <h5>Treatment Details</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Initial Drain:"
                    label-align-sm="right"
                    label-for="initial_drain"
                  >
                    <b-form-input id="initial_drain" placeholder="initial_drain"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Total UF:"
                    label-align-sm="right"
                    label-for="total_uf"
                  >
                    <b-form-input id="total_uf" placeholder="total_uf"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Average Dwell:"
                    label-align-sm="right"
                    label-for="average_dwell"
                  >
                    <b-form-input id="average_dwell" placeholder="average_dwell"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Added/Lost Dwell:"
                    label-align-sm="right"
                    label-for="added_lost_dwell"
                  >
                    <b-form-input id="added_lost_dwell" placeholder="added_lost_dwell"></b-form-input>
                  </b-form-group>
                </vc-col>

                <vc-col :span="8" xs24 sm12 md6>
                  <h5>Drain Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Drain Color:"
                    label-align-sm="right"
                    label-for="drain_color"
                  >
                    <b-form-select id="drain_color" v-model="drain_color" :options="drainColorOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Drain Clarity:"
                    label-align-sm="right"
                    label-for="drain_clarity"
                  >
                    <b-form-select v-model="drain_clarity" :options="drainClarityOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Fibrin Present:"
                    label-align-sm="right"
                    label-for="fibrin_present"
                  >
                    <b-form-select v-model="fibrin_present" :options="fibrinPresentOptions"></b-form-select>
                  </b-form-group>
                </vc-col>

                <vc-col :span="8" xs24 sm12 md6>
                  <h5>Exit and Tunnel Site Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Color:"
                    label-align-sm="right"
                    label-for="exit_color"
                  >
                    <b-form-select v-model="exit_color" :options="exitColorOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Sensitivity:"
                    label-align-sm="right"
                    label-for="exit_sensitivity"
                  >
                    <b-form-select v-model="exit_sensitivity" :options="exitSensitivityOptions"></b-form-select>
                  </b-form-group>
                  <b-form-group
                    label-cols-sm="6"
                    label="Site Condition:"
                    label-align-sm="right"
                    label-for="exit_condition"
                  >
                    <b-form-select v-model="exit_condition" :options="exitConditionOptions"></b-form-select>
                  </b-form-group>                  
                </vc-col>

                <vc-col :span="8" xs24 sm12 md6>
                  <h5>Misc. Observations</h5>
                  <br/>
                  <b-form-group
                    label-cols-sm="6"
                    label="Bowel Observations:"
                    label-align-sm="right"
                    label-for="bowel_obs"
                  >
                    <b-form-select v-model="bowel_obs" :options="bowelObsOptions"></b-form-select>
                  </b-form-group>
                </vc-col>


<!--  
      comments

      problem: yes, no, notes
      -->

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

export default {
  components: { CardTitleNav },
  name: "treatment",
  data() {
    return {
      entry_date: "",
      systolic_pressure: "",
      diastolic_pressure: "",
      weight_in_kg: "",
      defaultDate: moment.utc(new Date()).local().format(),
      isReset: false,
      drain_color: null,
      drain_clarity: null,
      fibrin_present: null,
      exit_color: null,
      exit_sensitivity: null,
      exit_condition: null,
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
      ]
    };
  },
  methods: {
    async submitPatientVitals(e) {
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
    },
    onReset(e) {
      e.preventDefault()
      // Reset our form values
      this.entry_date = moment.utc(new Date()).local().format()
      this.systolic_pressure = ""
      this.diastolic_pressure = ""
      this.weight_in_kg = ""
      this.drain_color = null
      this.drain_clarity = null
      this.fibrin_present = null
      this.exit_color = null
      this.exit_sensitivity = null
      this.exit_condition = null
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.isReset = true
      this.$nextTick(() => {
        this.show = true
        this.isReset = false
      })
    }
  }
};
</script>