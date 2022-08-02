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
      <div v-else>
        <form @submit.prevent="emitUpdateTask">
          <textarea
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            name=""
            id=""
            class="form-control"
            rows="2"
          ></textarea>
          <button type="submit" class="btn btn-danger mt-2 me-2">Save</button>
        </form>
        <button @click="showForm = !showForm" class="btn btn-primary mt-2">
          Cancel
        </button>
      </div>
      <div class="col-md-2 mt-1">
        <button
          @click="showForm = !showForm"
          type="button"
          class="btn btn-primary me-2"
          v-show="showForm === false"
        >
          Edit
        </button>

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
