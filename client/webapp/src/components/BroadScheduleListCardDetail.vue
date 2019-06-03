<template>
  <v-flex xs12>
    <v-card>
      <v-layout row wrap>
        <v-flex xs4>
          <img class="product-img" :src="goodImgPath"/>
        </v-flex>
        <v-flex class="pr-2 pl-2" xs8>
          <div class="good-genre-time d-flex justify-space-between">
            <div>{{ goodMallName }}</div>
            <div>{{ goodBroedcastTime }}</div>
          </div>
          <div class="d-flex">
            {{ goodName }}
          </div>
          <div class="d-flex org-good-price" v-if="goodOrgPrice !== goodPrice">
           {{ goodOrgPrice | currency }} 원
          </div>
          <div class="d-flex good-price">
            {{ goodPrice | currency }} 원
          </div>
        </v-flex>
        <v-flex xs12 v-if="goodsOnSameTimeline">
          <v-expansion-panel class="goods-in-same-timeline" expand>
            <v-expansion-panel-content>
              <template  v-slot:header style="text-align: center">
                  같은 시간대 판매상품 {{ goodsOnSameTimeline.length }}개
              </template>
              <v-card v-for="(good, index) in goodsOnSameTimeline"
                      v-bind:key="good.mall_name +'-'+ good.start_time + '-' + index">
                <v-card-text>
                  <v-layout>
                    <v-flex xs2>
                      <img class="good-on-same-timeline-img" :src="good.img"/>
                    </v-flex>
                    <v-flex xs10>
                      <div class="d-flex">
                        {{ good.name }}
                      </div>
                      <div class="d-flex org-good-price" v-if="good.org_price !== good.price">
                        {{ good.org_price | currency }} 원
                      </div>
                      <div class="d-flex good-price">
                        {{ good.price | currency }} 원
                      </div>
                    </v-flex>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-flex>
      </v-layout>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: 'BroadcastScheduleListCardDetail',

  props: {
    goodImgPath: {
      type: String,
      require: true,
      default: 'static/img/logo.png'
    },
    goodMallName: {
      type: String,
      require: true,
      default: 'mall'
    },
    goodCate1: {
      type: String,
      require: true,
      default: '카테고리'
    },
    goodDate: {
      type: String,
      require: true,
      default: '20171125'
    },
    goodStartTime: {
      type: String,
      require: true,
      default: '100'
    },
    goodEndTime: {
      type: String,
      require: true,
      default: '200'
    },
    goodName: {
      type: String,
      require: true,
      default: '상품 이름'
    },
    goodOrgPrice: {
      type: Number,
      require: true,
      default: 10000
    },
    goodPrice: {
      type: Number,
      require: true,
      default: 7000
    },
    goodsOnSameTimeline: {
      type: Array,
      require: false
    }
  },

  computed: {
    goodBroedcastTime () {
      const dateFormat = 'YYYYMMDD'
      const timeFormat = 'HH:mm'

      const goodStartHourEndAt = this.goodStartTime.length > 3 ? 2 : 1
      const goodEndHourEndAt = this.goodEndTime.length > 3 ? 2 : 1

      const startHour = this.goodStartTime.length < 3 ? '00' : this.goodStartTime.substring(0, goodStartHourEndAt)
      const startMinute = this.goodStartTime.length < 3 ? this.goodStartTime : this.goodStartTime.substring(goodStartHourEndAt)
      const endHour = this.goodEndTime.length < 3 ? '00' : this.goodEndTime.substring(0, goodEndHourEndAt)
      const endMinute = this.goodEndTime.length < 3 ? this.goodEndTime : this.goodEndTime.substring(goodEndHourEndAt)

      return this.$moment(this.goodDate, dateFormat)
        .set({ hour: startHour, minute: startMinute }).format(timeFormat) +
        ' ~ ' +
        this.$moment(this.goodDate, dateFormat)
          .set({hour: endHour, minute: endMinute}).format(timeFormat)
    }
  }
}
</script>

<style>
  .goods-in-same-timeline .v-expansion-panel__container .v-expansion-panel__header {
    justify-content: center;
  }
</style>

<style scoped>
.product-img {
  width: 100px;
}

.good-genre-time {
  width: 100%;
}

.org-good-price {
  font-size: 12px;
  color: #b0bec5;
  opacity: 0.7;
}

.good-price {
  color: #d50000;
}

.good-on-same-timeline-img {
  width: 50px;
}
</style>
