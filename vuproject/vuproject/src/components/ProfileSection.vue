<template>
    <div class="profile">
      <h2>我的</h2>
      <p>欢迎, {{ username }}</p>
      <button @click="logout">退出登录</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "用户", // 这里可以用后端返回的用户名
      };
    },
    methods: {
      logout() {
        fetch("http://127.0.0.1:8000/api/person/logout/", {
          method: "POST",
          credentials: "include",
        })
          .then(() => {
            alert("退出成功");
            window.location.href = "/";
            this.$store.dispatch("checkLoginStatus");
          })
          .catch(error => console.error("退出失败", error));
      }
    }
  };
  </script>
  