<template>
  <div class="login-page" style="text-align: center; margin-top: 100px">
    <h2>Login Page</h2>
    <button @click="goToTodo">登入</button>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  name: "UserLogin", // 建議用多字名稱
  setup() {
    const router = useRouter();

    function goToTodo() {
      router.push("/todo");
    }

    return {
      goToTodo,
    };
  },
};
</script>
