<template>
  <WikipediaTranslator />
</template>

<script lang="ts">
import { defineComponent } from "vue";

import WikipediaTranslator from "./components/WikipediaTranslator.vue";

export default defineComponent({
  name: "App",
  components: {
    WikipediaTranslator,
  },
});
</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  --background: #272914;
  --color: #f8f4e3;
  --search-border: #d5573b;
  --search-background: #648844;
}

@media (prefers-color-scheme: light) {
  body {
    --background: #f8f4e3;
    --color: #272914;
    --search-border: #d5573b;
    --search-background: #648844;
  }
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: var(--background);
  color: var(--color);
  min-width: 100vw;
  min-height: 100vh;
}
</style>
