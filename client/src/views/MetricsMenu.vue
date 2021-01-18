<template>
  <b-container fluid fill-height class='px-0'>
    <vc-layout v-resize="resize" class="align-center mx-0" spacing="8">
      <vc-col :span="24">
        <vc-card class="elevation-3">
          <card-title-nav title="Metrics Menu"/>
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
import CardTitleNav from "../components/CardTitleNav";

export default {
  components: {
    CardTitleNav,
    MenuCard
  },
  name: "metrics-menu",
  data() {
    return {
      cards: [
        { id: 1, routerLink: "/metrics-table", iconName: "fa-table", cardTitle: "Tables" },
        { id: 2, routerLink: "/metrics-graph", iconName: "fa-chart-area", cardTitle: "Graphs" }
      ]
    }
  }
};
</script>