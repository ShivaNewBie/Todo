<template>
  <div class="container">
    <h1 class="mb-3 mt-3">Edit Task</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        name=""
        id=""
        class="form-control"
        rows="2"
        v-model="description"
      ></textarea>
      <button type="submit" class="btn btn-success mt-2">Update</button>
    </form>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "TaskEdit",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      description: null,
    };
  },
  methods: {
    onSubmit() {
      let endpoint = `/api/v1/tasks/${this.slug}/`;

      try {
        const response = axios.put(endpoint, {
          description: this.description,
        });
        this.$router.push({
          name: "home",
        });
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
      try {
        const response = await axios.get(endpoint);
        return next(
          (vm) => (
            (vm.description = response.data.description),
            (vm.status = response.data.status)
          )
        );
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    } else {
      return next();
    }
  },
};
</script>
