<template>
  <v-app>
    <SideBar>
      <div class="container">
        <!-- 上方資訊欄 -->
        <div class="item infobar">
          <DialogBox>
            <template #content>
              <p>{{ geminiComment }}</p>
            </template>
          </DialogBox>
          <v-avatar color="red">
            <span class="text-h5">CJ</span>
          </v-avatar>
        </div>

        <!-- 日曆與顏色圓圈 -->
        <div>
          <keep-alive>
            <CalenderView @update:date="fetchColorForDate" />
          </keep-alive>

          <div class="color-circle-wrapper">
            <ColorCircle :date="parentPickedDate" :color="color" :text="text" />
          </div>
        </div>

        <!-- 日記區塊 -->
        <div class="journal">
          <h2>Date: {{ parentPickedDate }} </h2>
          <v-textarea
            label="Input"
            variant="outlined"
            style="height: 300px"
            v-model="journalText"
          ></v-textarea>
          <v-btn 
            :disabled="isLoading"  
            class="submit-button" 
            color="white" 
            @click="submitJournal"
          >
            <span v-if="isLoading">Submitting...</span>
            <span v-else>Submit</span>
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

const userStore = useUserStore();
const userId = ref(null);
const isLoading = ref(false);

const parentPickedDate = ref("");
const journalText = ref("");
const color = ref("");
const text = ref("");
const geminiComment = ref("");

// 預設為今天
onMounted(() => {
  userStore.loadUserId();
  userId.value = userStore.userId;

  if (!userId.value) {
    alert("用戶尚未登入");
  }

  const today = new Date();
  parentPickedDate.value = today.toISOString().split("T")[0];
  fetchColorForDate(parentPickedDate.value);
});

const fetchColorForDate = async (selectedDate) => {
  parentPickedDate.value = selectedDate;
  try {
    isLoading.value = true;
    const response = await api.get(`/api/mood_tree_color/${userId.value}/${selectedDate}`);
    const data = response.data;

    if (response.status !== 200 || !data?.hex || !data?.content_text) {
      alert("尚未填寫顏色資料！");
      return;
    }

    color.value = response.data.hex;
    text.value = response.data.content_text;
    localStorage.setItem("lastColor", color.value);
    localStorage.setItem("lastText", text.value);
  } catch (error) {
    console.error("獲取顏色失敗:", error);
    alert("今天還沒留下日記唷！");
  } finally {
    isLoading.value = false;
  }
};

const submitJournal = async () => {
  try {
    if (!journalText.value) {
      alert("請記錄些東西再送出吧");
      return;
    }
    isLoading.value = true;

    const formData = new FormData();
    formData.append("user_id", userId.value);
    formData.append("entry_date", parentPickedDate.value);
    formData.append("content_text", journalText.value);
    formData.append("mood_icon_code", "string");

    const response = await api.post("/api/Post_diary_entry", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    if (response.data.status === "success") {
      color.value = response.data.diary_entry.hex_color_code;
      geminiComment.value = response.data.gemini_comment;
      text.value = journalText.value;
      localStorage.setItem("lastColor", color.value);
      alert("日記上傳成功");
    } else {
      alert("發生錯誤：" + response.data.message);
    }
  } catch (error) {
    console.error("發生錯誤:", error);
    alert("發生錯誤，請稍後再試");
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.container {
  display: grid;
  margin-top: 30px;
  grid-template-columns: auto auto;
  grid-template-rows: auto;
  gap: 40px;
}

.item {
  grid-column: 2;
  align-self: center;
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
  width: 130px;
  align-self: flex-end;
  color: #1976d2;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.square-card[data-v-19047e93] {
  width: 450px;
  height: 280px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.color-circle-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

/* 👉 手機版排版調整 */
@media (max-width: 768px) {
  .container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 0 16px;
  }

  .item {
    grid-column: auto;
    align-self: stretch;
  }

  .infobar {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .journal {
    min-height: auto;
  }

  .submit-button {
    width: 100%;
  }

  .square-card[data-v-19047e93] {
    width: 100%;
    height: auto;
  }

  .color-circle-wrapper {
    margin-top: 0;
    overflow-x: auto;
    max-width: 100%;
  }
}
</style>
