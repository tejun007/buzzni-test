<template>
  <v-flex xs12>
    <v-card>
      <v-layout row wrap>
        <v-flex xs4>
          <img class="product-img" :src="goodImgPath"/>
        </v-flex>
        <v-flex xs8>
          <div class="good-genre-time d-flex justify-space-between">
            <div>{{ goodGenre2 }}</div>
            <div>{{ goodBroedcastTime }}</div>
          </div>
          <div class="d-flex">
            {{ goodName }}
          </div>
          <div class="d-flex">
           {{ goodOrgPrice | currency }} 원
          </div>
          <div class="d-flex">
            {{ goodPrice | currency }} 원
          </div>
        </v-flex>
        <v-flex xs12>
          <v-expansion-panel class="goods-in-same-timeline" expand>
            <v-expansion-panel-content>
              <template  v-slot:header style="text-align: center">
                  같은 시간대 판매상품 {{ 0 }}개
              </template>
              <v-card>
                <v-card-text>Some content</v-card-text>
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
    goodGenre2: {
      type: String,
      require: true,
      default: 'mall'
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
    }
  },

  computed: {
    goodBroedcastTime () {
      const dateFormat = 'YYYYMMDD'
      const timeFormat = 'hh:mm'

      let goodStartHourEndAt = this.goodStartTime.length > 3 ? 2 : 1
      let goodEndHourEndAt = this.goodEndTime.length > 3 ? 2 : 1
      return this.$moment(this.goodDate, dateFormat)
        .set({
          hour: this.goodStartTime.substring(0, goodStartHourEndAt),
          second: this.goodStartTime.substring(goodStartHourEndAt)
        }).format(timeFormat) +
        ' ~ ' +
        this.$moment(this.goodDate, dateFormat)
          .set({
            hour: this.goodEndTime.substring(0, goodEndHourEndAt),
            second: this.goodEndTime.substring(goodEndHourEndAt)
          }).format(timeFormat)
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
</style>
