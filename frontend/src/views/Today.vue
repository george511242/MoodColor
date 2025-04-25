<template>
  <v-app>
    <SideBar>
      <v-container>
        <!-- 放你主頁的內容 -->
        <h1>歡迎！這裡是今天出勤頁面</h1>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";

export default {
  name: "TodayAttendance", // 拼字修正
  components: { SideBar }, // ✅ 正確的結尾
  setup() {},
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
  width: 100%;
  margin: 0 auto;
}
</style>
