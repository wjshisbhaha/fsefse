// src/router/index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../components/Login.vue'; // 确保路径正确

Vue.use(VueRouter);

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/',
    redirect: '/login' // 重定向到 /login
  }
];

const router = new VueRouter({
  routes
});

export default router;