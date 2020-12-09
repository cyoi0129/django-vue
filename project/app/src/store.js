import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export default new Vuex.Store({
  state: {
    accounts: {},
    list: {}
   },
   mutations: {
    mutateAccount(state, payload) {
     state.accounts = payload;
    },
    mutateList(state, payload) {
      state.list = payload;
    },
    mutateItem(state, item){
      if (item.status) {
        state.list[item.id].status = 'done'
      } else {
        state.list[item.id].status = 'tbd'
      }
      state.list[item.id].comment = item.comment
      state.list[item.id].score = item.score
    },
   },
   actions: {
    commitAccount(store) {
      // API for test usage
      // const url = 'https://jsondata.okiba.me/v1/json/XVuI1201208064227'
      // Use the following to switch to PROD
      const url = '/api/accounts/?format=json'
     return axios.get(url)
      .then(response => {
       store.commit('mutateAccount', response.data)
      })
    },
   commitList(store, account) {
    // API for test usage
    // const url = 'https://jsondata.okiba.me/v1/json/yvN4L201208041033'
    // Use the following to switch to PROD
    const url = '/api/entries/?format=json&reporter=' + account
    console.log(account)
    return axios.get(url)
     .then(response => {
      store.commit('mutateList', response.data)
     })
   },
   commitItem(store, item){
      store.commit('mutateItem', item)
      let status = 'tbd'
      if (item.status) {
        status = 'done'
      } else {
        status = 'tbd'
      }
      axios.put('/api/entries/' + item.id + '/', { status: status, comment: item.comment, score: item.score })
      .then(console.log('scuessed!'))
      .catch((error) =>{ console.log(error) })
   }
  },
   getters: {
    getAccount: (state) => state.accounts,
    getList: (state) => state.list,
    getDetail(state) {
      return id => {
        return state.list[id]
      }
    },
  }
})