// src/router/index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../components/Login.vue'; // 引入主页组件
import SingleScan from '../components/SingleScan.vue';
import MultiScan from '../components/MultiScan.vue';
import DataCenter from '../components/DataCenter.vue';

Vue.use(VueRouter);


const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login // 将主页组件设置为根路径
  },
  {
    path: '/single-scan',
    name: 'SingleScan',
    component: SingleScan
  },
  {
    path: '/multi-scan',
    name: 'MultiScan',
    component: MultiScan
  },
  {
    path: '/data-center',
    name: 'DataCenter',
    component: DataCenter
  },
  {
    path: '*', // 捕获所有未定义路径，重定向到主页
    redirect: '/'
  }
];

const router = new VueRouter({
  routes
});

export default router;
