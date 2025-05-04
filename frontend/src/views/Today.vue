<template>
  <v-app>
    <SideBar>
      <v-container>
        <v-row>
          <p>a word for you</p>
        </v-row>
        <v-row>
          <v-col cols="6" style="padding: 0 ga-md-6">
            <CalenderView />
          </v-col>

          <v-col>
            <v-textarea
              label="Input"
              variant="outlined"
              style="height: 600px"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <div class="bg-info text-white">第二個欄位</div>
          </v-col>

          <!-- 如果需要你也可以在這裡添加其他欄位 -->
        </v-row>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";
import CalenderView from "../components/Calender.vue";
export default {
  name: "MainPage",
  components: {
    SideBar,
    CalenderView,
  },
  setup() {},
};
</script>

<style scoped></style>
