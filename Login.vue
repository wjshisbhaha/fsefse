<template>
  <el-container class="home-container">
    <el-header style="text-align: center;">
      <div>
        <span>电商系统</span>
      </div>
    </el-header>
    <el-container>
      <!-- 左侧导航栏 -->
      <el-aside width="200px" class="full-height">
        <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
              <el-menu-item index="1-3">选项3</el-menu-item>
              <el-menu-item index="1-4">选项4</el-menu-item>
              <el-menu-item index="1-5">选项5</el-menu-item>
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
        </el-menu>
      </el-aside>

      <!-- 主内容区 -->
      <el-main>
        <!-- 单点扫描 -->
        <el-row :gutter="20">
          <el-col :span="18">
            <div class="grid-item">
              <span class="title">单点扫描</span>
              <el-row :gutter="10" align="middle">
                <el-col :span="12">
                  <span>x-start</span>
                  <el-input-number size="small" v-model="singleScan.xStart" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('singleScan', 'xStart', 10)">+10</el-button>
                  <el-button @click="adjustValue('singleScan', 'xStart', -10)">-10</el-button>
                </el-col>
                <el-col :span="12">
                  <span>x-end</span>
                  <el-input-number size="small" v-model="singleScan.xEnd" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('singleScan', 'xEnd', 10)">+10</el-button>
                  <el-button @click="adjustValue('singleScan', 'xEnd', -10)">-10</el-button>
                </el-col>
              </el-row>
              <div class="button-group">
                <el-button type="primary" @click="submitSingleScan">提交</el-button>
              </div>
            </div>
          </el-col>
        </el-row>

        <!-- 多点扫描 -->
        <el-row :gutter="20">
          <el-col :span="18">
            <div class="grid-item">
              <span class="title">多点扫描</span>
              <el-row :gutter="10" align="middle">
                <el-col :span="12">
                  <span>x-start</span>
                  <el-input-number size="small" v-model="multiScan.xStart" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('multiScan', 'xStart', 10)">+10</el-button>
                  <el-button @click="adjustValue('multiScan', 'xStart', -10)">-10</el-button>
                </el-col>
                <el-col :span="12">
                  <span>x-end</span>
                  <el-input-number size="small" v-model="multiScan.xEnd" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('multiScan', 'xEnd', 10)">+10</el-button>
                  <el-button @click="adjustValue('multiScan', 'xEnd', -10)">-10</el-button>
                </el-col>
              </el-row>
              <el-row :gutter="10" align="middle">
                <el-col :span="12">
                  <span>y-start</span>
                  <el-input-number size="small" v-model="multiScan.yStart" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('multiScan', 'yStart', 10)">+10</el-button>
                  <el-button @click="adjustValue('multiScan', 'yStart', -10)">-10</el-button>
                </el-col>
                <el-col :span="12">
                  <span>y-end</span>
                  <el-input-number size="small" v-model="multiScan.yEnd" :min="-99999" :max="99999" :step="10"></el-input-number>
                  <el-button @click="adjustValue('multiScan', 'yEnd', 10)">+10</el-button>
                  <el-button @click="adjustValue('multiScan', 'yEnd', -10)">-10</el-button>
                </el-col>
              </el-row>
              <div class="button-group">
                <el-button type="primary" @click="submitMultiScan">提交</el-button>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      singleScan: {
        xStart: 0,
        xEnd: 0,
      },
      multiScan: {
        xStart: 0,
        xEnd: 0,
        yStart: 0,
        yEnd: 0,
      },
    };
  },
  methods: {
    adjustValue(region, key, amount) {
      this[region][key] += amount;
    },
    async submitSingleScan() {
      const { xStart, xEnd } = this.singleScan;
      try {
        const response = await axios.post('http://localhost:5000/process', {
          xStart,
          xEnd
        });
        console.log("单点扫描结果：", response.data.result);
      } catch (error) {
        this.handleError(error);
      }
    },
    async submitMultiScan() {
      const { xStart, xEnd, yStart, yEnd } = this.multiScan;
      try {
        const response = await axios.post('http://localhost:5000/process', {
          xStart,
          xEnd,
          yStart,
          yEnd
        });
        console.log("多点扫描结果：", response.data.result);
      } catch (error) {
        this.handleError(error);
      }
    },
    handleError(error) {
      if (error.response) {
        // 服务器返回响应码范围在2xx之外
        console.error("服务器返回错误:", error.response.data);
        console.error("状态码:", error.response.status);
        console.error("响应头:", error.response.headers);
      } else if (error.request) {
        // 请求已发出，但没有收到响应
        console.error("请求发出，但没有响应:", error.request);
      } else {
        // 其他错误
        console.error("请求出错:", error.message);
      }
      console.error("完整错误对象:", error);
    }
  }
};
</script>

<style scoped>
.home-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.el-header {
  background-color: red;
  text-align: center;
  color: #ffffff;
  padding: 20px 0;
  font-size: 20px;
}

.el-container {
  flex-grow: 1;
  display: flex;
}

.el-aside {
  background-color: #545c64;
  color: #fff;
}

.el-main {
  background-color: beige;
  padding: 20px;
}

.grid-item {
  background-color: #fff;
  text-align: left;
  border: 2px solid pink;
  padding: 20px;
  font-size: 16px;
  height: auto;
  display: flex;
  flex-direction: column;
}

.grid-item .title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.el-input-number {
  width: 120px;
  margin-right: 10px;
}

.button-group {
  margin-top: 10px;
}

.el-button {
  margin-right: 5px;
}
</style>