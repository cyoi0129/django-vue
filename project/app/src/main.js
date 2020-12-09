import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'
import Vuex from 'vuex'
import 'es6-promise/auto'

Vue.config.productionTip = false
Vue.use(Vuex)

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')