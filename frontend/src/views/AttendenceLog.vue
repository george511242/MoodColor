<template>
  <v-app>
    <SideBar>
      <v-container>
        <!-- 放你主頁的內容 -->
        <h1>歡迎！這裡是出勤報告區</h1>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";

export default {
  name: "AttendenceLog", // 拼字修正
  components: { SideBar }, // ✅ 正確的結尾
  setup() {},
};
</script>
