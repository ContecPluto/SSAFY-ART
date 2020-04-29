import jwtDecode from 'jwt-decode'
import cookie from '@/js/cookie.js'
const state = {
  token: null,
  user: 'User',
}

const getters = {
  isLoggedIn: function(state) {
    return state.token ? true : false
  },
  requestHeader: function(state) {
    return {
      headers: {
        Authorization: 'JWT ' + state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  },
  user: function(state) {
    return state.user
  },
}

// 상태(토큰)을 받아와서 state를 update
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading: function(state, status) {
    state.loading = status
  },
  setUser: function(state, user) {
    state.user = user
  },
}

const actions = {
  login: function(options, flag) {
    if (flag == true) {
      options.commit('setToken', cookie.token())
      options.commit('setUser', cookie.cookieInfo())
    } else {
      options.commit('setToken', null)
      options.commit('setUser', null) 
    }
  },
  logout: function(options) {
    options.commit('setToken', null)
    options.commit('setUser', null) 
  },
}

export default {
  state,
  mutations,
  actions,
  getters,
}