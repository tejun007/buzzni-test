// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '@mdi/font/css/materialdesignicons.css'

import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import 'babel-polyfill'
import moment from 'moment'
import 'moment/locale/ko'

import Moment from 'vue-moment'
import VueCurrencyFilter from 'vue-currency-filter'

// CSS for vuetify
import 'vuetify/dist/vuetify.min.css'

import router from './router'
import api from './api'

Vue.use(Vuetify, {
  iconfont: 'mdi'
})
moment.locale('ko')
Vue.use(Moment, {
  moment
})
Vue.use(VueCurrencyFilter, {
  symbol: '',
  thousandsSeparator: ',',
  fractionCount: 0,
  fractionSeparator: '',
  symbolPosition: '',
  symbolSpacing: false
})

Vue.config.productionTip = false

Vue.prototype.$API = api

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
})
