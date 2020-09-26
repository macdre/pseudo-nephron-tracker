<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <vc-card-title color="primary" :dark="false">
            <span class="body=2 vc-block">Home</span>
          </vc-card-title>
          <vc-card-text>
            <vc-layout v-resize="resize" :class="['align-center', 'mx-0']">
              <menu-card v-for="card in cards" v-bind:key="card.id" v-bind:card="card"/>      
            </vc-layout>
          </vc-card-text>
        </vc-card>
      </vc-col>
    </vc-layout>
  </b-container>
</template>

<script>

import MenuCard from "../components/MenuCard";

export default {
  name: "HomeContent",
  components: {
    MenuCard
  },
  data() {
    return {
      cards: [
        { id: 1, routerLink: "/treatment", iconName: "fa-notes-medical", cardTitle: "Record Treatment" },
        { id: 2, routerLink: "/inventory", iconName: "fa-boxes", cardTitle: "Manage Inventory" },
        { id: 3, routerLink: "/metrics", iconName: "fa-chart-bar", cardTitle: "Explore Metrics" },
        { id: 4, routerLink: "/setup", iconName: "fa-cogs", cardTitle: "Configure Templates" }
      ]
    }
  }
};
</script>
