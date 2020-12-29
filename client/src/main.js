import Vue from 'vue';

import Vuecidity from 'vuecidity';
import { IconsPlugin, BootstrapVue } from 'bootstrap-vue';

import { library } from "@fortawesome/fontawesome-svg-core";
import { faLink, faUser, faPowerOff, faNotesMedical, faBoxes, faChartBar, 
  faPrescriptionBottle, faCogs, faHome, faArrowLeft } 
  from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { dom } from '@fortawesome/fontawesome-svg-core'

import 'vuecidity/dist/lib/vuecidity.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.min.css';

import App from './App.vue';
import router from './router';
import { Auth0Plugin } from './auth';
import HighlightJs from './directives/highlight';
import { domain, clientId, audience } from '../auth_config.json';

Vue.config.productionTip = false;

Vue.use(Vuecidity);
Vue.use(IconsPlugin);
Vue.use(BootstrapVue);
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

Vue.directive('highlightjs', HighlightJs);

library.add(faLink, faUser, faPowerOff, faNotesMedical, faBoxes, 
  faChartBar, faPrescriptionBottle, faCogs, faHome, faArrowLeft);
Vue.component('font-awesome-icon', FontAwesomeIcon);
dom.watch();

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
