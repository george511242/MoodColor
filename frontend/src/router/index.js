import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "../views/UserLogin.vue"; // 確保這裡是引入 UserLogin
import Todo from "../views/Todo.vue";

const routes = [
  { path: "/", name: "UserLogin", component: UserLogin }, // 使用 UserLogin 組件
  { path: "/todo", name: "TodoView", component: Todo },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
