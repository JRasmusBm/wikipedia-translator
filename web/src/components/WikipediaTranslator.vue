<template>
  <header><h1>Wikipedia Translator</h1></header>
  <main>
    <form @submit="submit">
      <label class="wide">
        <span>Enter the term you want to translate:</span>
        <input type="text" v-model="query" />
      </label>
      <label>
        <span>From</span>
        <select v-model="from">
          <option value="en">English</option>
          <option value="se">Swedish</option>
        </select>
      </label>
      <label>
        <span>To</span>
        <select v-model="to">
          <option value="se">Swedish</option>
          <option value="en">English</option>
        </select>
      </label>
      <label v-if="result" class="wide">
        <span>Result:</span>
        <output name="result">{{ result }}</output>
      </label>
    </form>
  </main>
  <footer>Made by @JRasmusBm</footer>
</template>

<script lang="ts">
import { defineComponent, ref, unref } from "vue";
import * as translateUtils from "../utils/translate";

export default defineComponent({
  setup() {
    const query = ref<string>("");
    const from = ref<translateUtils.Language>("en");
    const to = ref<translateUtils.Language>("se");
    const result = ref<null | string>(null);

    function submit(e: Event) {
      e.preventDefault();

      translateUtils
        .translate({
          query: unref(query),
          from: unref(from),
          to: unref(to),
        })
        .then((value) => {
          result.value = value;
        });
    }

    return {
      query,
      from,
      to,
      submit,
      result,
    };
  },
});
</script>

<style scoped>
header {
  height: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

main {
  height: calc(100vh - 6rem);
  display: grid;
  grid-template-columns: auto 30rem auto;
  grid-template-rows: 2fr auto 3fr;
}

main form {
  grid-column: 2;
  grid-row: 2;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 1rem;
}

main form span {
  display: block;
  padding: 1rem;
}

main form label.wide {
  grid-column: 1 /-1;
}

main form input,
main form select,
main form output {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 4rem;
  width: 100%;
  border-radius: 1rem;
  font-size: 2rem;
  text-align: center;
  text-align-last: center;
  -moz-text-align-last: center;
  border: 2px solid var(--color);
  background: var(--search-background);
  color: var(--color);
}

footer {
  height: 2rem;
  width: 100%;
  position: fixed;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
