import Vue from 'vue';
import { router } from './js/helpers';
import { store } from './js/store';
import App from './js/App.vue';

// setup fake backend
import { configureFakeBackend } from './js/helpers';
configureFakeBackend();

new Vue({
  App,
  router,
  store,
  render: h => h(App)
}).$mount('#app');
