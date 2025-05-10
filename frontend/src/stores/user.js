import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    userId: null,
  }),
  actions: {
    setUserId(id) {
      this.userId = id;
    },
  },
});
