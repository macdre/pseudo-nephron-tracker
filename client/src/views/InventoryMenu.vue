<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Inventory Menu"/>
          <vc-card-text class="pa-2">
            <vc-layout :class="['align-center', 'mx-0']">
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
import CardTitleNav from "../components/CardTitleNav";

export default {
  components: {
    CardTitleNav,
    MenuCard
  },
  name: "inventory-menu",
  data() {
    return {
      cards: [
        { id: 1, routerLink: "/inventory", iconName: "fa-boxes", cardTitle: "Manage Inventory" },                
        { id: 2, routerLink: "/setup", iconName: "fa-cogs", cardTitle: "Configure Templates" }
      ]
    }
  }
};
</script>