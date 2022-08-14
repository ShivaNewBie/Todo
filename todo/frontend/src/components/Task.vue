<template>
  <div class="shadow p-3 mb-5 bg-body rounded">
    <div class="d-flex align-items-center">
      <div class="d-inline-block flex-grow-1">
        <div class="task-link">
          <h1
            @click="$emit('update-status', this.task)"
            :class="[task.status ? 'done' : '']"
          >
            {{ task.description }}
          </h1>
        </div>
      </div>

      <div class="d-inline-block">
        <router-link
          class="btn btn-primary me-1"
          :to="{ name: 'task-edit', params: { slug: slug } }"
          >Edit</router-link
        >
      </div>
      <div class="d-inline-block mr-5">
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
    slug: {
      type: String,
      required: true,
    },
    task: {
      type: Object,
      required: true,
    },
  },
  emits: ["delete-task", "update-task", "update-status"],
  methods: {
    emitDeleteTask() {
      this.$emit("delete-task", this.task);
    },
    emitUpdateTask() {
      this.$emit("update-task", this.task);
    },
  },
};
</script>

<style scope>
.done {
  text-decoration: line-through;
}
</style>
