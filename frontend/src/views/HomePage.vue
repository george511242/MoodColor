<template>
  <v-app>
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
            <ColorCircle :date="parentPickedDate" />
          </div>
        </div>

        <div class="journal">
          <h2>Date: {{ parentPickedDate }} userID{{ userId }}</h2>
          <v-textarea
            label="Input"
            variant="outlined"
            style="height: 300px"
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
import { ref, onMounted, computed } from "vue";
import SideBar from "../components/SideBar.vue";
import CalenderView from "../components/Calender.vue";
import DialogBox from "../components/Dialogs.vue";
import ColorCircle from "../components/ColorCircle.vue";

import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
const userId = computed(() => userStore.userId);

const parentPickedDate = ref(""); // Reactive reference

onMounted(() => {
  console.log("userId from Pinia:", userId);
});
</script>

<style scoped>
.container {
  display: grid;

  grid-template-columns: auto auto; /* 設定列 (column) 大小 */
  grid-template-rows: auto auto auto;
  gap: 10px;
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
