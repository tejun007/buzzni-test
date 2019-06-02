<template>
  <v-list subheader>
    <v-flex>
      <div>
        <div>
          01월 01일 수요일
        </div>
        <div>
          오늘 오전 12시
        </div>
      </div>

      <v-flex>
        <broadcast-schedule-list-card-detail />
      </v-flex>

    </v-flex>
  </v-list>
</template>

<script>
import BroadcastScheduleListCardDetail from './BroadScheduleListCardDetail'
export default {
  name: 'BroadcastScheduleListCard',
  components: {BroadcastScheduleListCardDetail}
}
</script>

<style scoped>

</style>
