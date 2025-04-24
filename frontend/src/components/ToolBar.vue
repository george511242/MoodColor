<template>
  <v-app-bar :elevation="2" class="custom-bar" extension-height="80px">
    <v-img
      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROTxcu9w5BKsCZKZHy2Yw8MJAnV6l-9mYp0g&s"
      max-width="40"
      max-height="32"
      class="ml-2"
      contain
    ></v-img>

    <v-title class="custom-title">HR-In-Out System</v-title>

    <v-spacer></v-spacer>

    <v-app-bar-nav-icon class="nav-icon-center"></v-app-bar-nav-icon>
  </v-app-bar>
</template>

<style scoped>
.custom-bar {
  display: flex;
  align-items: center;
  padding: 10px;
}

.custom-title {
  margin-left: 10px;
  font-size: 20px;
  font-weight: 600;
}

.nav-icon-center {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
