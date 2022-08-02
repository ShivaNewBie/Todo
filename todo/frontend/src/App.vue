<template>
  <Navbar />
  <router-view />
</template>

<script>
import { axios } from "@/common/api.service.js";

import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
  methods: {
    async setUserInfo(){
      try {
        const response = await axios.get('/auth/users/me/')
        const requestUser = response.data['username']
        window.localStorage.setItem('username', requestUser)
        console.log(requestUser)
      } catch (error) {
        console.log(error)
      }
    }
  },
  created(){
    this.setUserInfo()
  }
};
</script>

<style></style>
