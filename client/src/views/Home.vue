<template>
  <b-container fluid fill-height class='px-0'>
    <div class="text-center hero" v-if="!$auth.isAuthenticated && !$auth.loading">
      <img class="mb-3 app-logo" src="/logo.png" alt="Pseudo Nephron logo" width="80" />
      <h1 class="mb-4">Pseudo-Nephron Project</h1>
    </div>
 
    <div v-if="$auth.isAuthenticated">
      <vc-layout class="align-center mx-0" spacing="8">
        <vc-col :span="24">
          <vc-card class="elevation-3">
            <card-title-nav title="Home"/>
            <vc-card-text class="pa-2">
              <vc-layout :class="['align-center', 'mx-0']">
                <menu-card v-for="card in cards" v-bind:key="card.id" v-bind:card="card"/>      
              </vc-layout>
            </vc-card-text>
          </vc-card>
        </vc-col>
      </vc-layout>
    </div>
  </b-container>
</template>

<script>
import MenuCard from "../components/MenuCard";
import CardTitleNav from "../components/CardTitleNav";

export default {
  name: "home",
  components: {
    MenuCard,
    CardTitleNav
  },
  data() {
    return {
      cards: [
        { id: 1, routerLink: "/treatment", iconName: "fa-notes-medical", cardTitle: "Record Treatment" },
        { id: 2, routerLink: "/inventory", iconName: "fa-boxes", cardTitle: "Manage Inventory" },
        { id: 3, routerLink: "/metrics-menu", iconName: "fa-chart-bar", cardTitle: "Explore Metrics" },
        { id: 4, routerLink: "/setup", iconName: "fa-cogs", cardTitle: "Configure Templates" },
        { id: 5, routerLink: "/medications", iconName: "fa-prescription-bottle", cardTitle: "Manage Medications" }
      ]
    }
  }
};
</script>
