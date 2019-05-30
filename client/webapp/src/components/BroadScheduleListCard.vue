<template>
  <v-list subheader>
    <v-subheader>편성표 시간</v-subheader>
    <v-flex>
      <broadcast-schedule-list-card-detail />
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
