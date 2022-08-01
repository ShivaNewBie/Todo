<template>
  <div class="container">
    <div v-for="task in tasks" :key="task.slug">
      <div class="shadow p-3 mb-5 bg-body rounded">
        <router-link :to="{ name: 'task', params: { slug: task.slug } }"
          ><h1>{{ task.description }}</h1></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";

export default {
  name: "HomeView",
  data() {
    return {
      tasks: [],
    };
  },
  components: {},
  methods: {
    async getTasks() {
      let endpoint = "/api/v1/tasks/";

      try {
        const response = await axios.get(endpoint);
        this.tasks = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
