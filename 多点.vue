<template>
  <div class="grid-container">
    <!-- 输入和按钮 -->
    <div class="input-section">
      <span class="title">多点扫描</span>
      <el-row :gutter="10" align="middle">
        <el-col :span="9">
          <span>x-start</span>
          <el-input-number size="small" v-model="xStart" :min="-99999" :max="99999" :step="1"></el-input-number>
          <el-button @click="adjustValue('xStart', 10)">+10</el-button>
          <el-button @click="adjustValue('xStart', -10)">-10</el-button>
        </el-col>
        <el-col :span="9">
          <span>x-end</span>
          <el-input-number size="small" v-model="xEnd" :min="-99999" :max="99999" :step="1"></el-input-number>
          <el-button @click="adjustValue('xEnd', 10)">+10</el-button>
          <el-button @click="adjustValue('xEnd', -10)">-10</el-button>
        </el-col>
      </el-row>
      <br />
      <el-row :gutter="10" align="middle">
        <el-col :span="9">
          <span>y-start</span>
          <el-input-number size="small" v-model="yStart" :min="-99999" :max="99999" :step="1"></el-input-number>
          <el-button @click="adjustValue('yStart', 10)">+10</el-button>
          <el-button @click="adjustValue('yStart', -10)">-10</el-button>
        </el-col>
        <el-col :span="9">
          <span>y-end</span>
          <el-input-number size="small" v-model="yEnd" :min="-99999" :max="99999" :step="1"></el-input-number>
          <el-button @click="adjustValue('yEnd', 10)">+10</el-button>
          <el-button @click="adjustValue('yEnd', -10)">-10</el-button>
        </el-col>
      </el-row>
      <br />
      <el-row :gutter="10" align="middle">
        <el-col :span="9">
          <span>x-step</span>
          <el-input-number size="small" v-model="xStep" :min="1" :max="99999" :step="1"></el-input-number>
        </el-col>
        <el-col :span="9">
          <span>y-step</span>
          <el-input-number size="small" v-model="yStep" :min="1" :max="99999" :step="1"></el-input-number>
        </el-col>
      </el-row>
      <div class="button-group">
        <el-button type="primary" @click="submitMultiScan">提交</el-button>
      </div>
    </div>

    <!-- 结果显示 -->
    <div class="result-section">
      <h3>图片实时显示</h3>
      <el-carousel indicator-position="outside" v-if="imgList.length > 0">
        <el-carousel-item v-for="(item, index) in imgList" :key="index">
          <img :src="item" alt="" style="width: 100%; height: auto; display: block;" />
        </el-carousel-item>
      </el-carousel>
      <p v-else><el-empty description="暂无图片"></el-empty></p>
    </div>
  </div>
</template>
<script>
export default {
  name: "App",
  data() {
    return {
      xStart: null,
      xEnd: null,
      yStart: null,
      yEnd: null,
      xStep: 1,
      yStep: 1,
      imgList: [], // 图片列表
    };
  },
  methods: {
    adjustValue(key, value) {
      this[key] += value;
    },
    async submitMultiScan() {
      // 示例API调用
      console.log("提交扫描：", {
        xStart: this.xStart,
        xEnd: this.xEnd,
        xStep: this.xStep,
        yStart: this.yStart,
        yEnd: this.yEnd,
        yStep: this.yStep,
      });
    },
    loadImages() {
      // 使用 require.context 动态加载 src/assets 下的所有图片
      const images = require.context("@/assets/", false, /\.(png|jpe?g|gif|svg)$/);
      this.imgList = images.keys().map((key) => images(key));
      console.log("加载的图片列表：", this.imgList);
    },
  },
  mounted() {
    this.loadImages(); // 初始化加载图片
  },
};
</script>
<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.input-section,
.result-section {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
}

.result-section {
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 1.5em;
  margin-bottom: 20px;
}

.button-group {
  margin-top: 20px;
}

.el-carousel__item img {
  width: 100%;
  height: auto;
}
</style>
