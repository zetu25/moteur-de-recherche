import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        selection: [],
        res: [],
        results: "",
    },
    mutations: {
        change(state,query) {
            state.selection = query
        },
        clear(state){
            state.selection = []
            state.res = []
            state.results = ""
        },
        change_results(state,results){
            state.results = results
        }
    },
    getters: {
        requete(state){
            return state.selection;
        },
        res(state){
            return state.res
        },
        results(state){
            return state.results
        }
    }
});

export default store;