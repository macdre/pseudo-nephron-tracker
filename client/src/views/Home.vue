<template>
  <b-container fluid>
    <div>
      <hero v-if="!$auth.isAuthenticated && !$auth.loading"/>
      <home-content v-if="$auth.isAuthenticated"/>
    </div>
</template>

<script>
import Hero from "../components/Hero";
import HomeContent from "../components/HomeContent";

export default {
  name: "home",
  components: {
    Hero,
    HomeContent
  }
};
</script>
