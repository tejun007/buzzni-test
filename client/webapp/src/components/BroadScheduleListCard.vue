<template>
  <v-list subheader>
      <v-flex v-for="(goods, goodsMallStartTime) in goodsByStarDateHour "
              v-bind:key="goodsMallStartTime">
        <broadcast-schedule-list-card-detail
          :good-mall-name="goods.mainGood.mall_name"
          :good-name="goods.mainGood.name"
          :good-img-path="goods.mainGood.img"
          :good-cate1="goods.mainGood.cate1"
          :good-date="goods.mainGood.date"
          :good-start-time="goods.mainGood.start_time"
          :good-end-time="goods.mainGood.end_time"
          :good-org-price="goods.mainGood.org_price"
          :good-price="goods.mainGood.price"
          :goods-on-same-timeline="goods.goodsOnSameTimeline"
        />
      </v-flex>
  </v-list>
</template>

<script>
import BroadcastScheduleListCardDetail from './BroadScheduleListCardDetail'
export default {
  name: 'BroadcastScheduleListCard',

  components: {BroadcastScheduleListCardDetail},

  props: {
    startDateHour: {
      type: String,
      required: true
    },
    goodsByStarDateHour: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
