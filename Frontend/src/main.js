import Vue from 'vue'
import App from './App.vue'
import VueAxios from 'vue-axios'
import Axios from 'axios'
import VueAgile from 'vue-agile'
import VueGeolocation from 'vue-browser-geolocation';

Vue.use(VueGeolocation);
Vue.use(VueAgile)
Vue.config.productionTip = false
Vue.use(VueAxios, Axios)
document.addEventListener("DOMContentLoaded", async function (event){

new Vue({
  render: h => h(App),
}).$mount('#app')
})
