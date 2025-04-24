<template>
  <ToolBar />
  <div class="login-page" style="text-align: center; margin-top: 100px">
    <img
      src="https://upload.wikimedia.org/wikipedia/zh/thumb/8/83/Taiwan_Semiconductor_Manufacturing_Co_logo.svg/1200px-Taiwan_Semiconductor_Manufacturing_Co_logo.svg.png"
      alt="TSMC Logo"
      style="max-width: 100px; max-height: 100px"
      class="login-icon"
    />
    <h2>Login</h2>
    <v-text-field
      clearable
      label="Account"
      variant="outlined"
      class="centered-input"
    />
    <v-text-field
      clearable
      label="Password"
      variant="outlined"
      class="centered-input"
    />

    <v-btn height:20px variant="tonal" @click="goToTodo"> Submit </v-btn>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import ToolBar from "../components/ToolBar.vue";

export default {
  name: "UserLogin",
  components: {
    ToolBar, // ✅ 在這裡註冊才會生效
  },
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

<style scoped>
h2 {
  margin: 10px auto;
  font-size: 30px;
}
.login-icon {
  margin-top: 20px;
}
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center; /* 這樣內容（input, button）就會置中 */
  margin-top: 0px;
}
.centered-input {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
}
</style>
