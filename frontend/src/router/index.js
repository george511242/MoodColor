import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "../views/UserLogin.vue"; // 確保這裡是引入 UserLogin
import TodayAttendence from "../views/Today.vue";
// import HomeView from "../views/HomeView.vue";

const routes = [
  { path: "/", name: "UserLogin", component: UserLogin }, // 使用 UserLogin 組件
  { path: "/today", name: "TodayAttendence", component: TodayAttendence },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
