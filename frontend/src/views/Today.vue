<template>
  <v-app>
    <SideBar>
      <v-container>
        <p>state</p>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";
export default {
  name: "MainPage",
  components: {
    SideBar,
  },
  setup() {},
};
</script>

<style scoped></style>
