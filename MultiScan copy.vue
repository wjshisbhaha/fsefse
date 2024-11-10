<template>
  <div class="grid-item">
    <span class="title">多点扫描</span>
    <el-row :gutter="10" align="middle">
      <el-col :span="12">
        <span>x-start</span>
        <el-input-number size="small" v-model="xStart" :min="-99999" :max="99999" :step="10"></el-input-number>
        <el-button @click="adjustValue('xStart', 10)">+10</el-button>
        <el-button @click="adjustValue('xStart', -10)">-10</el-button>
      </el-col>
      <el-col :span="12">
        <span>x-end</span>
        <el-input-number size="small" v-model="xEnd" :min="-99999" :max="99999" :step="10"></el-input-number>
        <el-button @click="adjustValue('xEnd', 10)">+10</el-button>
        <el-button @click="adjustValue('xEnd', -10)">-10</el-button>
      </el-col>
    </el-row>
    <el-row :gutter="10" align="middle">
      <el-col :span="12">
        <span>y-start</span>
        <el-input-number size="small" v-model="yStart" :min="-99999" :max="99999" :step="10"></el-input-number>
        <el-button @click="adjustValue('yStart', 10)">+10</el-button>
        <el-button @click="adjustValue('yStart', -10)">-10</el-button>
      </el-col>
      <el-col :span="12">
        <span>y-end</span>
        <el-input-number size="small" v-model="yEnd" :min="-99999" :max="99999" :step="10"></el-input-number>
        <el-button @click="adjustValue('yEnd', 10)">+10</el-button>
        <el-button @click="adjustValue('yEnd', -10)">-10</el-button>
      </el-col>
    </el-row>
    <div class="button-group">
      <el-button type="primary" @click="submitMultiScan">提交</el-button>
    </div>
    <div v-if="result" class="result">
      <h3>扫描结果</h3>
      <pre>{{ result }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      xStart: 0,
      xEnd: 0,
      yStart: 0,
      yEnd: 0,
      result: null
    };
  },
  methods: {
    adjustValue(key, amount) {
      this[key] += amount;
    },
    async submitMultiScan() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/two', {
          xStart: this.xStart,
          xEnd: this.xEnd,
          yStart: this.yStart,
          yEnd: this.yEnd
        });
        this.result = response.data.result; // 将结果保存到 data 中
        console.log("单点扫描结果：", response.data.result);
      } catch (error) {
        console.error("请求出错:", error);
      }
    }
  }
};
</script>

<style scoped>
.grid-item {
  background-color: #fff;
  border: 2px solid pink;
  padding: 20px;
}
.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}
.button-group {
  margin-top: 20px;
  text-align: center;
}
.result {
  margin-top: 20px;
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 5px;
}
</style>