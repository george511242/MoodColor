<template>
  <v-app>
    <SideBar>
      <v-container>
        <!-- 放你主頁的內容 -->
        <h1>歡迎！這裡裡是詳細的歷史紀錄區</h1>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";

export default {
  name: "MyTeam",
  components: { SideBar }, // ✅ 正確的結尾
  setup() {},
};
</script>