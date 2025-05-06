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
        <CalenderView @update:date="parentPickedDate = $event" />
        <div class="journal">
          <h2>Date: {{ parentPickedDate }}</h2>
          <v-textarea
            label="Input"
            variant="outlined"
            style="height: 600px"
          ></v-textarea>
        </div>
      </div>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";
import CalenderView from "../components/Calender.vue";
import DialogBox from "../components/Dialogs.vue";
import { ref } from "vue";

export default {
  name: "MainPage",
  components: {
    SideBar,
    CalenderView,
    DialogBox,
  },
  setup() {
    const parentPickedDate = ref(""); // Initialize parentPickedDate as a reactive reference

    return {
      parentPickedDate, // Expose to template for binding
    };
  },
};
</script>

<style scoped>
.container {
  display: grid;

  grid-template-columns: auto auto; /* 設定列 (column) 大小 */
  grid-template-rows: auto auto auto;
  gap: 15px;
}
.item {
  grid-column: 2; /* 放在第 2 欄 */

  align-self: center; /* 垂直置中（可選） */
}
.infobar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 30%;
}
.journal {
  display: flex;
  flex-direction: column;
}
</style>
