// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '@mdi/font/css/materialdesignicons.css'

import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import 'babel-polyfill'

import Moment from 'vue-moment'
import VueCurrencyFilter from 'vue-currency-filter'

// CSS for vuetify
import 'vuetify/dist/vuetify.min.css'

import router from './router'

Vue.use(Vuetify, {
  iconfont: 'mdi'
})
Vue.use(Moment)
Vue.use(VueCurrencyFilter, {
  symbol: '',
  thousandsSeparator: ',',
  fractionCount: 0,
  fractionSeparator: '',
  symbolPosition: '',
  symbolSpacing: false
})
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
})
