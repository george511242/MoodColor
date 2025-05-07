<template>
  <v-dialog max-width="500">
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        v-bind="activatorProps"
        color="grey"
        text="A sentence for you today"
        variant="flat"
      ></v-btn>
    </template>

    <template v-slot:default="{ isActive }">
      <v-card title="Dialog">
        <v-card-text>
          <slot name="content" />
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text="Close" @click="isActive.value = false"></v-btn>
        </v-card-actions>
        
      </v-card>
      
    </template>
  </v-dialog>
 
</template>

<script>
export default {
  name: "DialogBox",
};
</script>
