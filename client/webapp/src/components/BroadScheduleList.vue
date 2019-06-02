<template>
  <v-card>
    <v-toolbar color="teal" dark>

      <v-toolbar-title class="text-xs-center">방송 편성표</v-toolbar-title>
      <v-spacer></v-spacer>

    </v-toolbar>

    <v-list>
      <v-flex>
        <broadcast-schedule-list-card />
      </v-flex>
    </v-list>
  </v-card>
</template>

<script>
import BroadcastScheduleListCard from './BroadScheduleListCard'

export default {
  name: 'BroadScheduleList',

  components: {BroadcastScheduleListCard},

  data () {
    return {
      broadcastScheduleList: [
        {

        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
