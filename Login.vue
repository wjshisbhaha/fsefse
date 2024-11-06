<template>
  <el-container class="home-container">
    <el-header style="text-align: center;">
      <div>
        <span>电商系统</span>
      </div>
    </el-header>
    <el-container>
      <!--  ce -->
      <el-aside width="200px" class="full-height">
        <el-menu
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">

      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航一</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
          <el-menu-item index="2-4">选项4</el-menu-item>
          <el-menu-item index="2-5">选项5</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航二</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
          <el-menu-item index="2-4">选项4</el-menu-item>
          <el-menu-item index="2-5">选项5</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航三</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1">选项1</el-menu-item>
          <el-menu-item index="3-2">选项2</el-menu-item>
          <el-menu-item index="3-3">选项3</el-menu-item>
          <el-menu-item index="3-4">选项4</el-menu-item>
          <el-menu-item index="3-5">选项5</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="4">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航四</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="4-1">选项1</el-menu-item>
          <el-menu-item index="4-2">选项2</el-menu-item>
          <el-menu-item index="4-3">选项3</el-menu-item>
          <el-menu-item index="4-4">选项4</el-menu-item>
          <el-menu-item index="4-5">选项5</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-menu-item index="2" disabled>
        <i class="el-icon-menu"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="4" disabled>
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>
    </el-menu>
      </el-aside>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {

};
</script>

<style scoped>
.home-container {
  height: 100vh; /* 使容器高度为视口高度 */
}

.el-header {
  background-color: red;
  text-align: center;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #ffff;
  > div {
    display: flex;
    align-items: center;
  }
}

.el-aside {
  background-color: #545c64;
  /* height: 100%; 确保左侧栏填满高度 
  flex-shrink: 0; 确保 Aside 不被压缩 */
}

.el-main {
  background-color: red;
  /* flex-grow: 1; 确保 Main 区域占据剩余空间 */
}
</style>