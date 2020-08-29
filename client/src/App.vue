<template>
  <div id="app" class="d-flex flex-column h-100">
    <nav-bar />
    <b-container fluid>
      <error />
      <div class="mt-5">
        <router-view />
      </div>
    </b-container>
    <footer class="bg-light text-center p-3">
      <div class="logo"></div>
      <p>
        This is an app that allows a patient to track their dialysis treatments electronically.
      </p>
    </footer>
  </div>
</template>

<script>
import NavBar from "./components/NavBar";
import Error from "./components/Error";

export default {
  components: {
    NavBar,
    Error
  }
};
</script>
