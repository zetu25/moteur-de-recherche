<template>
  <v-container>
    <!-- <v-select
      v-model="selectionType"
      :items="['leaf', 'independent']"
      label="Selection type"
    ></v-select> -->
    <!-- <v-col> -->
    <v-col>
      <v-btn class="ma-2" outlined color="indigo" @click="clear"> Clear </v-btn>
      <v-treeview
        v-model="selection"
        :items="items"
        :selection-type="selectionType"
        selectable
        return-object
        @update:active="onUpdate"
      ></v-treeview>
    </v-col>
    <v-col>
    </v-col>
  </v-container>
</template>

<script>
import data_ontology from "..\\store\\ontology.json";
import store from "../store/store.js";

export default {
  name: "TreeView",
  data: () => ({
    selectionType: "independent",
    selection: store.state.selection,
    items: [data_ontology]
  }),
  watch: {
    selection() {
      this.onUpdate();
    }
  },
  methods: {
    onUpdate() {
      store.commit('clear');
      // console.log("There we are")
      // console.log(this.selection)
      store.commit("change", this.selection);
    },
    clear() {
      store.commit("clear");
      this.selection = store.getters.selection
    }
  }
};
</script>

<style>
</style>