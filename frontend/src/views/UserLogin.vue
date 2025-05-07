<template>
  <SideBar>
    <div class="login-page" style="text-align: center; margin-top: 60px">
      <img :src="logo" alt="Logo" style="width: 100px; height: 100px" />
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
  </SideBar>
</template>

<script>
import { useRouter } from "vue-router";

import SideBar from "../components/SideBar.vue";
import logo from "@/assets/logo.png";

export default {
  name: "UserLogin",
  components: {
    SideBar, // ✅ 在這裡註冊才會生效
  },

  setup() {
    const router = useRouter();

    function goToTodo() {
      router.push("/home");
    }

    return {
      goToTodo,
      logo,
    };
  },
};
</script>

<style scoped>
h2 {
  margin: 10px auto;
  font-size: 30px;
}

.login-page {
  display: flex;
  flex-direction: column;
  align-items: center; /* 這樣內容（input, button）就會置中 */
  margin-top: 0px;
}
.centered-input {
  max-width: 500px;
  width: 500px;
  margin: 0 auto;
}
</style>
