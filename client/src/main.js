import Vue from 'vue';

import Vuecidity from 'vuecidity';
import { IconsPlugin, BootstrapVue } from 'bootstrap-vue';

import { library } from "@fortawesome/fontawesome-svg-core";
import { faLink, faUser, faPowerOff, faNotesMedical, faBoxes, faChartBar, faRedo, 
  faPrescriptionBottle, faCogs, faHome, faArrowLeft, faArrowRight, faTable, 
  faChartArea, faArrowDown, faArrowUp, faPrint, faFileDownload} 
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
import VueHtmlToPaper from 'vue-html-to-paper';
import VueBlobJsonCsv from 'vue-blob-json-csv';

Vue.config.productionTip = false;
Vue.use(Vuecidity);
Vue.use(IconsPlugin);
Vue.use(BootstrapVue);
Vue.use(VueHtmlToPaper);
Vue.use(VueBlobJsonCsv);
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
  faChartBar, faPrescriptionBottle, faCogs, faHome, faArrowLeft,
  faArrowRight, faTable, faChartArea, faRedo, faArrowDown, faArrowUp,
  faPrint, faFileDownload);
Vue.component('font-awesome-icon', FontAwesomeIcon);
dom.watch();

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
