import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "../views/UserLogin.vue"; // 確保這裡是引入 UserLogin

import MainPage from "../views/Today.vue";

import analysis from "../views/Analysis.vue";

const routes = [
  { path: "/", name: "UserLogin", component: UserLogin }, // 使用 UserLogin 組件
  { path: "/home", name: "MainPage", component: MainPage },
  { path: "/analysis", name: " analysis", component: analysis },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
