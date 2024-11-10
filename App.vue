<template>
  <div id="app">
    <el-container class="home-container">
      <el-header style="text-align: center;">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
          </el-submenu>
          <el-menu-item index="3" disabled>消息中心</el-menu-item>
          <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu>
      </el-header>

      <el-container>
        <el-aside width="200px" class="full-height">
          <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" @select="navigate">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>导航一</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="/single-scan">单点扫描</el-menu-item>
                <el-menu-item index="/multi-scan">多点扫描</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="/data-center">
              <i class="el-icon-document"></i>
              <span slot="title">数据中心</span>
            </el-menu-item>
          </el-menu>
        </el-aside> 

        <!-- 通过 router-view 动态渲染不同页面组件 -->
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import SingleScan from './components/SingleScan.vue';
import MultiScan from './components/MultiScan.vue';
export default {
  name: 'App',
  data() {
    return {
      activeIndex: "1",
    };
  },
  methods: {
    handleSelect(key) {
      this.activeIndex = key;
      console.log("Selected menu item:", key);
    },
    navigate(path) {
      this.$router.push(path); // 使用 Vue Router 跳转
    }
  }
};
</script>

<style scoped>
.home-container {
  height: 100vh;
}

.el-aside {
  background-color: #545c64;
  color: #fff;
}

.full-height {
  height: 100%;
}

.el-header {
  background-color: #545c64;
  color: #ffffff;
  text-align: center;
}

.el-main {
  padding: 20px;
  background-color: beige;
}
</style>
