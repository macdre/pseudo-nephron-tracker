import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Treatment from "../views/Treatment.vue";
import Inventory from "../views/Inventory.vue";
import Metrics from "../views/Metrics.vue";
import Medications from "../views/Medications.vue";
import Setup from "../views/Setup.vue";
import { authGuard } from "../auth";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/profile",
      name: "profile",
      component: Profile,
      beforeEnter: authGuard
    },
    {
      path: "/treatment",
      name: "treatment",
      component: Treatment,
      beforeEnter: authGuard
    },
    {
      path: "/inventory",
      name: "inventory",
      component: Inventory,
      beforeEnter: authGuard
    },
    {
      path: "/metrics",
      name: "metrics",
      component: Metrics,
      beforeEnter: authGuard
    },
    {
      path: "/medications",
      name: "medications",
      component: Medications,
      beforeEnter: authGuard
    },
    {
      path: "/setup",
      name: "setup",
      component: Setup,
      beforeEnter: authGuard
    }
  ]
});

export default router;
