<template>
  <b-card no-body class="mb-1">

    <b-card-header class="header-padding" header-tag="header" role="tab">
      <b-button class="btn-accordion" block v-b-toggle.accordion-1>Configure Displayed Fields</b-button>
    </b-card-header>

    <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
      <b-card-body>
        <b-row align-v="center">

          <b-col cols="5">
            <b-row class="mb-2" align-h="center">
              <b-list-group class="w-100" style="max-height: 300px; overflow:scroll; -webkit-overflow-scrolling: touch;">
                <b-list-group-item button v-for="field in available_fields" v-bind:key="field" 
                  @click="setSelectedAvail(field, $event)">{{ field }}
                </b-list-group-item>
              </b-list-group>
            </b-row>
          </b-col>

          <b-col cols="2">
            <b-row class="mb-2" align-h="center">
              <b-button class="btn w-75" @click="addField" variant="primary">
                Add <font-awesome-icon icon="arrow-right"/>
              </b-button>
            </b-row>
            <b-row class="mb-2" align-h="center">
              <b-button class="btn w-75" @click="removeField" variant="primary">
                <font-awesome-icon icon="arrow-left"/> Remove
              </b-button>
            </b-row>
            <b-row class="mb-2" align-h="center">
              <b-button class="btn w-75" @click="resetFields" variant="primary">
                Reset <font-awesome-icon icon="redo"/>
              </b-button>
            </b-row>
          </b-col>
          
          <b-col cols="5">
            <b-row class="mb-2" align-h="center">
              <b-button class="btn w-100" @click="moveFieldUp" variant="primary">
                Move Field Up <font-awesome-icon icon="arrow-up"/>
              </b-button>
            </b-row>
            <b-row class="mb-2" align-h="center">
              <b-list-group class="w-100" style="max-height: 200px; overflow:scroll; -webkit-overflow-scrolling: touch;">
                <b-list-group-item button v-for="field in displayed_fields" v-bind:key="field"
                  @click="setSelectedDisp(field, $event)">{{ field }}
                </b-list-group-item>
              </b-list-group>
            </b-row>
            <b-row class="mb-2" align-h="center">
              <b-button class="btn w-100" @click="moveFieldDown" variant="primary">
                Move Field Down <font-awesome-icon icon="arrow-down"/>
              </b-button>
            </b-row>
          </b-col>

        </b-row>

      </b-card-body>
    </b-collapse>
  </b-card>
</template>

<script>
  export default {
    name: "FieldSelector",
    props: [
      'all_fields',
      'default_fields',
      'displayed_fields'
    ],
    data() {
      return {
        available_fields: [],
        selected_field_available: '',
        selected_field_displayed: ''
      };
    },
    computed: {
    },
    methods: {
      arrayMove(arr, old_index, new_index) {
        if (new_index >= arr.length) {
            var k = new_index - arr.length + 1;
            while (k--) {
                arr.push(undefined);
            }
        }
        arr.splice(new_index, 0, arr.splice(old_index, 1)[0]);
        return arr; // for testing
      },
      setSelectedAvail(field, e) {
        const el = e.target;
        var current = document.querySelector('.active');
        if (current) {
            current.classList.remove('active');
        }
        el.classList.add('active');
        this.selected_field_available = field;
        this.selected_field_displayed = null;
      },
      setSelectedDisp(field, e) {
        const el = e.target;
        var current = document.querySelector('.active');
        if (current) {
            current.classList.remove('active');
        }
        el.classList.add('active');
        this.selected_field_displayed = field;
        this.selected_field_available = null;
      },
      addField() {
        if (this.selected_field_available) {
          this.displayed_fields.push(this.selected_field_available);
          this.available_fields.splice(this.available_fields.indexOf(this.selected_field_available), 1);
          this.selected_field_available = null;
          this.available_fields.sort();
          this.$emit("listUpdate", this.displayed_fields);
        }
      },
      removeField() {
        if (this.selected_field_displayed && this.displayed_fields.length > 1) {
          this.available_fields.push(this.selected_field_displayed);
          this.displayed_fields.splice(this.displayed_fields.indexOf(this.selected_field_displayed), 1);
          this.selected_field_displayed = null;
          this.available_fields.sort();
          this.$emit("listUpdate", this.displayed_fields);
        }
      },
      resetFields() {
        this.selected_field_available = null;
        this.selected_field_displayed = null;
        this.displayed_fields = [...this.default_fields];
        this.available_fields = [];
        for (let i=0; i<this.all_fields.length; i++) {
          if (this.displayed_fields.includes(this.all_fields[i]) == false) {
            this.available_fields.push(this.all_fields[i]);
          }
        }
        this.available_fields.sort();
        this.$emit("listUpdate", this.displayed_fields);
      },
      moveFieldUp() {
        if (this.selected_field_displayed) {
          let fieldLocation = this.displayed_fields.indexOf(this.selected_field_displayed);
          if(fieldLocation > 0) {
            // move the field one earlier
            this.arrayMove(this.displayed_fields, fieldLocation, fieldLocation - 1);
            this.$emit("listUpdate", this.displayed_fields);
          }
        }
      },
      moveFieldDown() {
        if (this.selected_field_displayed) {
          let fieldLocation = this.displayed_fields.indexOf(this.selected_field_displayed);
          let listLength = this.displayed_fields.length;
          if(fieldLocation < (listLength - 1)) {
            // move the field one later
            this.arrayMove(this.displayed_fields, fieldLocation, fieldLocation + 1);
            this.$emit("listUpdate", this.displayed_fields);
          }
        }
      }
    },
    beforeMount(){
      this.displayed_fields = [...this.default_fields];
      this.available_fields = [];
      for (let i=0; i<this.all_fields.length; i++) {
        if (this.displayed_fields.includes(this.all_fields[i]) == false) {
          this.available_fields.push(this.all_fields[i]);
        }
      }
      this.available_fields.sort();
    }  
  };
</script>

<style>

.header-padding {
  padding-left: 4px; 
  padding-right: 4px;
  padding-top: 4px; 
  padding-bottom: 4px;
}

.btn { 
  color: #ffffff; 
  background-color: #2196F3; 
  border-color: #2196F3; 
} 

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