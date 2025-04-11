import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);

// 获取环境变量中的 backend URL
// const backendUrl = process.env.VUE_APP_BACKEND_URL || "http://localhost:3000"; // 如果环境变量不存在，使用默认的地址

app.config.globalProperties.$backendUrl = "http://localhost:3000"; // 設定全域變數

// 挂载到 #app
app.mount("#app");
