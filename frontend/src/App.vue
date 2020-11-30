<template>
  <v-app>
    <v-navigation-drawer :width="400" app>
      <TreeView />
    </v-navigation-drawer>
    <v-main>
      <Similarities />
    </v-main>
  </v-app>
</template>

<script>
import TreeView from "./components/TreeView";
import Similarities from "./components/Similarities.vue";

export default {
  name: "App",

  components: {
    TreeView,
    Similarities,
  },

  data: () => ({
    //
  }),
};
</script>
