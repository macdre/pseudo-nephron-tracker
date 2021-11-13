<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Medications"/>

          <vc-card-text class="pa-2">
            <div>

              <b-row class="my-1">
                <b-col :span="24">
                  <b-table striped hover :items="items" :fields="fields">
                    <template v-slot:cell(name)="row">
                      <b-form-input v-model="row.item.name"/>
                    </template>
                    <template v-slot:cell(dose)="row">
                      <b-form-textarea v-model="row.item.dose"/>
                    </template>
                    <template #cell(-)="data">
                      <b-button @click="removeRow(data.index, $event)" variant="primary">
                        <font-awesome-icon icon="times"/>
                      </b-button>
                    </template>
                  </b-table>
                </b-col>
              </b-row>

              <b-row class="my-1">
                <b-col :span="24">
                  <b-button class="mr-2" @click="addRow" variant="primary">
                    Add <font-awesome-icon icon="plus"/>
                  </b-button>  
                  <b-button class="mr-2" @click="saveSet" variant="primary">
                    Save <font-awesome-icon icon="save"/>
                  </b-button>
                  <b-button class="mr-2" @click="resetAll" variant="danger">
                    Reset <font-awesome-icon icon="dumpster-fire"/>
                  </b-button>
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

export default {
  components: { 
    CardTitleNav
  },
  name: "inventory",
  data() {
    return {
      apiMessage1: "",
      apiMessage2: "",
      user_id: "",
      quantity: "",
      fields: [{key: "name", label: "Name"}, {key: "dose", label: "Dosage"}, "-"],
      default_items: [{ name: "Yellows", dose: "10mg twice daily" }, { name: "Oranges", dose: "200mg once daily" }, { name: "Purples", dose: "idk" },{ name: "Blues", dose: "all of them" }],
      dummy_row: { name: "Yellows", dose: "10mg twice daily" },
      items: []
    };
  },
  methods: {
    removeRow(index, e) {
      this.$delete(this.items, index);
    },
    addRow () {
      this.items.push(this.dummy_row);
    },
    saveSet () {

    },
    resetAll () {

    },
    async callApi() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      // Use Axios to make a call to the API
      const { data } = await axios.get("/v1/test", {
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        }
      });
      this.apiMessage1 = data;
    },
    async getPatientVitals() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      // Use Axios to make a call to the API
      const { data } = await axios.get("/v1/patient_vitals", {
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        },
        params: {
          user_id: this.user_id,
          quantity: this.quantity
        }
      });
      this.apiMessage2 = data;
    }
  },
  beforeMount(){
    this.items = this.default_items;
    //this.getPatientVitals();
  }
};
</script>