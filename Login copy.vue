<!-- src/components/Home.vue -->
<template>
    <el-container>
      <el-main>
        <SingleScan />
        <MultiScan />
      </el-main>
    </el-container>
  </template>
  
  <script>
  import SingleScan from './SingleScan.vue';
  import MultiScan from './MultiScan.vue';
  
  export default {
    components: {
      SingleScan,
      MultiScan
    },
    // Vue component (DataCenter.vue or the relevant scan components)
  }
  </script>
  
  <style scoped>
  .el-main {
    padding: 20px;
  }
  </style>
  