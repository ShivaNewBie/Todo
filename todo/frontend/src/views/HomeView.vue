<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="newTask"
        class="form-control mt-2"
        rows="1"
        placeholder="Enter Task"
      ></textarea>
      <button type="submit" class="btn btn-success mt-2 mb-2">Enter</button>
    </form>
    <Task
      v-for="task in tasks"
      :key="task.slug"
      :task="task"
      :slug="task.slug"
      @delete-task="deleteTask"
      @update-task="updateTask"
      v-model="description"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";

import Task from "@/components/Task.vue";

export default {
  name: "HomeView",
  data() {
    return {
      tasks: [],
      newTask: null,
      editTask: null,
      error: null,
      description: null,
    };
  },
  components: {
    Task,
  },
  props: {
    slug: {
      type: String,
    },
  },
  methods: {
    async getTasks() {
      let endpoint = "/api/v1/tasks/";

      try {
        const response = await axios.get(endpoint);
        this.tasks.push(...response.data);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async deleteTask(task) {
      let endpoint = `/api/v1/tasks/${task.slug}/`;
      try {
        await axios.delete(endpoint);
        this.tasks.splice(this.tasks.indexOf(task), 1); //changes the contents of an array by removing or replacing existing elements and/or adding new elements in place
      } catch (error) {
        console.log(error);
      }
    },
    async updateTask(task) {
      let endpoint = `/api/v1/tasks/${task.slug}/`;

      try {
        const response = await axios.put(endpoint, {
          description: this.description,
        });
        this.tasks.unshift(response.data);

        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async onSubmit() {
      if (!this.newTask) {
        this.error = "You can't enter an empty task";
        return;
      }
      let endpoint = "/api/v1/tasks/";

      try {
        const response = await axios.post(endpoint, {
          description: this.newTask,
        });
        this.tasks.unshift(response.data);
        this.description = null;
        if (this.error) {
          this.error = null;
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  async beforeRouteEnter(to, from, next) {
    // if the component is used to update a question
    // get the question's data from the REST API
    if (to.params.slug !== undefined && to.params.slug !== "") {
      const endpoint = `/api/v1/tasks/${to.params.slug}/`;
      console.log("testing");
      try {
        const response = await axios.get(endpoint);
        return next((vm) => (vm.description = response.data.description));
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    } else {
      return next();
    }
  },
  created() {
    this.getTasks();
  },
};
</script>

<style>
.task-link {
  font-weight: 400;
  color: black;
  text-decoration: none;
}

.task-link:hover {
  color: #343a40;
}
</style>
