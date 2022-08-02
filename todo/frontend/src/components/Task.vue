<template>
  <div class="shadow p-3 mb-5 bg-body rounded">
    <div class="row">
      <div v-if="showForm === false" class="col-md-10">
        <router-link
          class="task-link"
          :to="{ name: 'task', params: { slug: slug } }"
          ><h1>{{ task.description }}</h1></router-link
        >
      </div>

      <div class="col-md-2 mt-1">
        <router-link
          class="btn btn-primary"
          :to="{ name: 'task-edit', params: { slug: slug } }"
          >Edit</router-link
        >

        <button
          v-show="!showForm"
          @click="emitDeleteTask"
          type="button"
          class="btn btn-danger"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "TaskDetail",
  data() {
    return {
      showForm: false,
      description: null,
    };
  },
  props: {
    modelValue: {
      type: String,
    },
    slug: {
      type: String,
      required: true,
    },
    task: {
      type: Object,
      required: true,
    },
  },
  emits: ["update:modelValue", "delete-task", "update-task"],
  methods: {
    emitDeleteTask() {
      this.$emit("delete-task", this.task);
    },
    emitUpdateTask() {
      this.showForm = false;
      this.$emit("update-task", this.task);
    },
  },
};
</script>
