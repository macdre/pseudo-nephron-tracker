<template>
  <vc-col :span="6" style="padding: 8px;" xs24 sm12 md6>
    <vc-card tag="router-link" :href="card.routerLink" style="text-decoration: none;"
        :class="`${hover ? 'elevation-24': 'elevation-6'}`" @mouseover.native="hover = true" @mouseleave.native="hover = false">
      <vc-card-media class="pa-0" height="25px"/>
      <vc-card-media class="pa-0" height="120px">
        <vc-icon class="fas" color="primary" size="x-large" style="width: 120px; height: 120px;">{{ card.iconName }}</vc-icon>
      </vc-card-media>
      <vc-card-media class="pa-0" height="25px"/>
      <vc-card-title color="primary" :dark="false">
        <span class="body=2 vc-block">{{ card.cardTitle }}</span>
      </vc-card-title>
    </vc-card>
  </vc-col>
</template>

<script>
  export default {
    name: "MenuCard",
    props: [
      'card'
    ],
    data() {
      return {
        hover: false
      }
    }
  };
</script>