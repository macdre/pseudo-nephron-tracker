import Vue from 'vue';
import { router } from './js/helpers';
import { store } from './js/store';
import App from './js/App';

// setup fake backend
import { configureFakeBackend } from './js/helpers';
configureFakeBackend();

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
