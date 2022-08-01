<template>
  <div class="container">
    <div class="shadow p-3 mb-5 bg-body rounded">
      <h1>{{ task.description }}</h1>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Task",
  data() {
    return {
      task: {},
    };
  },
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  methods: {
    async getTask() {
      let endpoint = `/api/v1/tasks/${this.slug}/`;

      try {
        const response = await axios.get(endpoint);
        this.task = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getTask();
  },
};
</script>
