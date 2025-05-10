<template>
  <v-app :style="{ backgroundColor: red }">
    <SideBar>
      <div class="container">
        <div class="item infobar">
          <DialogBox>
            <template #content>
              <p>Here is some custom content for the dialog.</p>
            </template>
          </DialogBox>
          <v-avatar color="red">
            <span class="text-h5">CJ</span>
          </v-avatar>
        </div>
        <div>
          <CalenderView @update:date="parentPickedDate = $event" />
          <div class="color-circle-wrapper">
            <ColorCircle :date="parentPickedDate" :color="color" />
          </div>
        </div>

        <div class="journal">
          <h2>Date: {{ parentPickedDate }} userID{{ userId }}</h2>
          <v-textarea
            label="Input"
            variant="outlined"
            style="height: 300px"
            v-model="journalText"
          ></v-textarea>
          <v-btn class="submit-button" color="white" @click="submitJournal">
            Submit
          </v-btn>
        </div>
      </div>
    </SideBar>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from "vue";
import SideBar from "../components/SideBar.vue";
import CalenderView from "../components/Calender.vue";
import DialogBox from "../components/Dialogs.vue";
import ColorCircle from "../components/ColorCircle.vue";
import api from "@/api";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore(); // 使用 Pinia store
const userId = ref(null); // 用來存儲 userId

const parentPickedDate = ref(""); // 用戶選的日期
const journalText = ref(""); // 用戶輸入的日記內容

const color = ref("");

onMounted(() => {
  userStore.loadUserId(); // 確保讀取 userId
  userId.value = userStore.userId; // 從 store 獲取 userId

  if (!userId.value) {
    alert("用戶尚未登入");
  }
});

//將日記送出
const submitJournal = async () => {
  try {
    if (!journalText.value) {
      alert("請記錄些東西再送出吧");
      return;
    }
    const formData = new FormData();
    formData.append("user_id", userId.value);
    formData.append("entry_date", parentPickedDate.value);
    formData.append("content_text", journalText.value);
    formData.append("mood_icon_code", "string");

    const response = await api.post("/api/Post_diary_entry", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    if (response.data.status === "success") {
      color.value = response.data.diary_entry.hex_color_code;
      console.log("color get:", color); // ← 加這一行來觀察
      alert("日記上傳成功");
    } else {
      alert("發生錯誤：" + response.data.message);
    }
  } catch (error) {
    console.error("發生錯誤:", error);
    alert("發生錯誤，請稍後再試");
  }
};
</script>

<style scoped>
.container {
  display: grid;
  margin-top: 30px;
  grid-template-columns: auto auto; /* 設定列 (column) 大小 */
  grid-template-rows: auto auto auto;
  gap: 40px;
}
.item {
  grid-column: 2; /* 放在第 2 欄 */
  align-self: center; /* 垂直置中（可選） */
}
.infobar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}
.journal {
  display: flex;
  flex-direction: column;
  min-height: 600px;
}
.submit-button {
  width: 100px; /* 控制寬度 */
  align-self: flex-end; /* 靠右（若 journal 是 flex）*/
  color: #1976d2; /* 按鈕文字為 Vuetify 藍色 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 可選的陰影效果 */
}
.color-circle-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.square-card[data-v-19047e93] {
  width: 80%;
  height: 250px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
</style>

<style>
/* 這邊是 global 的，不加 scoped，這樣才能作用到 .v-application */

.v-container {
  margin-left: auto; /* 設定左邊邊距 */
  margin-right: auto;
}
</style>
