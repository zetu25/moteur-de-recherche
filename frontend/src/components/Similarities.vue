<template>
  <v-container>
    <v-toolbar color="blue" dark>
      <v-toolbar-title>Similarity measures</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-divider vertical></v-divider>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn text @click="get_cosine_similarity"> Cosine Similarity </v-btn>

        <v-divider vertical></v-divider>

        <v-btn text @click="get_semantic_path_similarity"> Semantic PathLength </v-btn>

        <v-divider vertical></v-divider>

        <v-btn text> Semantic Content Similarity </v-btn>
      </v-toolbar-items>
    </v-toolbar>
 
    <v-list>
      <v-list-item
        v-model="results"
        v-for="article in results"
        :key="article.title"
      >
        <v-list-item-content>
          
            <v-list-item-title
              :disabled="false"
              v-text="article.score"
            ></v-list-item-title>

            <v-list-item-title
              :disabled="false"
              v-text="article.title"
            ></v-list-item-title>
          
        </v-list-item-content>
      </v-list-item>
    </v-list>
  
  </v-container>
</template>

<script>
import store from "../store/store.js";
import axios from "axios";

export default {
  name: "Similarities",
  data: () => ({
    results: store.state.results,
  }),
  methods: {
    get_cosine_similarity() {
      this.selection.forEach((element) => {
        this.res.push(element.name);
      });
      axios
        .post("http://localhost:5000/cosine-similarity", {
          entities: this.res,
        })
        .then((response) => {
          this.results = response.data;
          
          store.commit("clear");
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    get_semantic_path_similarity(){
      this.selection.forEach((element) => {
        this.res.push(element.name);
      });
      axios
        .post("http://localhost:5000/semantic-path-length", {
          entities: this.res,
        })
        .then((response) => {
          store.commit("clear");
          this.results = response.data;
          console.log(this.results)
          
        })
        .catch((e) => {
          this.errors.push(e);
        });
    }
  },
  computed: {
    selection() {
      return store.getters.requete;
    },
    res() {
      return store.getters.res;
    },
  },
};
</script>

<style>
</style>