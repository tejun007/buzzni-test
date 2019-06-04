<template>
  <v-card>
    <v-toolbar class="tool-bar" color="teal" dark fixed>

      <v-toolbar-title class="text-xs-center">방송 편성표</v-toolbar-title>
      <v-spacer></v-spacer>

    </v-toolbar>
    <v-layout align-center class="timeline-header-layout pl-2 pr-2" wrap>
      <v-flex sm12 xs12>
        <v-select
          :items="filters.dates"
          height="30"
          label="날짜"
          v-model="selectedFilters.date"
        >
        </v-select>
      </v-flex>
      <v-flex class="pr-1" sm6 xs6>
        <v-select
          :items="filters.mallNames"
          label="쇼핑사"
          multiple
          v-model="selectedFilters.mallNames"
        >
          <template v-slot:selection="{ item, index }">
            <span class="selected-item-span" v-if="index === 0">{{ item }}</span>
            <span
              class="grey--text caption"
              v-if="index === 1"
            >(+{{ selectedFilters.mallNames.length - 1 }} others)</span>
          </template>
          <template v-slot:prepend-item>
            <v-list-tile
              @click="toggleMallNamesSelection"
              ripple
            >
              <v-list-tile-action>
                <v-icon :color="selectedFilters.mallNames.length > 0 ? 'indigo darken-4' : ''">
                  {{ mallNamesSelectIcon }}
                </v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Select All</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider class="mt-2"></v-divider>
          </template>
        </v-select>
      </v-flex>
      <v-flex class="pl-1" sm6 xs6>
        <v-select
          :items="filters.cate1s"
          label="카테고리"
          multiple
          v-model="selectedFilters.cate1s"
        >
          <template v-slot:selection="{ item, index }">
            <span class="selected-item-span" v-if="index === 0">{{ item }}</span>
            <span
              class="grey--text caption"
              v-if="index === 1"
            >(+{{ selectedFilters.cate1s.length - 1 }} others)</span>
          </template>
          <template v-slot:prepend-item>
            <v-list-tile
              @click="toggleCate1sSelection"
              ripple
            >
              <v-list-tile-action>
                <v-icon :color="selectedFilters.cate1s.length > 0 ? 'indigo darken-4' : ''">
                  {{ cate1sSelectIcon }}
                </v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Select All</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider class="mt-2"></v-divider>
          </template>
        </v-select>
      </v-flex>
    </v-layout>
    <v-list class="timeline-goods-list" id="timelineGoodsList">
      <v-progress-circular
        v-show="!timelineGoodsLoaded && (scrollDirection === 'init' || scrollDirection === 'up')"
        :size="40"
        :width="4"
        color="red"
        indeterminate
      ></v-progress-circular>
      <v-flex v-bind:key="startDateHour"
              v-for="(goodsByStartDateHour, startDateHour) in timelineGoods">
        <v-flex :id="startDateHour">
          <div id="liveDiv" class="datetime-wrapper" v-if="startDateHour === currentDateTime">
            <div class="d-flex justify-center">
              <div class="live-text-div">LIVE</div>
            </div>
          </div>
          <div class="datetime-wrapper" v-else>
            <div v-if="Object.keys(timelineGoods)[Object.keys(timelineGoods).indexOf(startDateHour)-1]">
              <div v-if="$moment(startDateHour, 'YYYYMMDD_H').format('YYYYMMDD') !== $moment(Object.keys(timelineGoods)[Object.keys(timelineGoods).indexOf(startDateHour)-1], 'YYYYMMDD_H').format('YYYYMMDD')">
                {{ $moment(startDateHour, 'YYYYMMDD_H').format('MMM Do dddd') }}
              </div>
            </div>
            <div class="d-flex justify-center">
              <div class="hour-text-div">
                {{ $moment(startDateHour, 'YYYYMMDD_H').format('a h') }}시
              </div>
            </div>
          </div>
        </v-flex>

        <broadcast-schedule-list-card
          :goods-by-star-date-hour="goodsByStartDateHour"
          :start-date-hour="startDateHour"/>
      </v-flex>
      <v-progress-circular
        v-show="!timelineGoodsLoaded && scrollDirection === 'down'"
        :size="40"
        :width="4"
        color="red"
        indeterminate
      ></v-progress-circular>
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
      currentDate: '20171125',
      currentTime: '1300',
      timelineGoods: null,
      loadingTimelineGoods: false,
      savedTopGoodElementId: '',
      scrollPosition: 0,
      scrollDirection: 'down',
      startDateOfTopGood: '20171125',
      startTimeOfTopGood: '1300',
      nextDateOfBottomGood: '20171125',
      nextStartTimeOfBottomGood: '1700',
      goToOptions: {
        duration: 300,
        offset: 0,
        easing: 'linear'
      },
      filters: {
        dates: [],
        mallNames: [],
        cate1s: []
      },
      selectedFilters: {
        date: '20171125',
        mallNames: [],
        cate1s: []
      }
    }
  },

  computed: {
    timelineGoodsLoaded () {
      return this.loadingTimelineGoods === false
    },
    currentDateTime () {
      return this.currentDate + '_' + this.currentTime
    },
    currentDateHour () {
      return this.currentDate + '_' + this.currentHour
    },
    currentHour () {
      const currentStartHourEndAt = this.currentTime.length > 3 ? 2 : 1
      return this.currentTime.substring(0, currentStartHourEndAt)
    },
    selectAllMallNames () {
      return this.selectedFilters.mallNames.length === this.filters.mallNames.length
    },
    selectSomeMallNames () {
      return this.selectedFilters.mallNames.length > 0 && !this.selectAllMallNames
    },
    mallNamesSelectIcon () {
      if (this.selectAllMallNames) return 'mdi-close-box'
      if (this.selectSomeMallNames) return 'mdi-minus-box'
      return 'mdi-checkbox-blank-outline'
    },
    selectAllCate1s () {
      return this.selectedFilters.cate1s.length === this.filters.cate1s.length
    },
    selectSomeCate1s () {
      return this.selectedFilters.cate1s.length > 0 && !this.selectAllCate1s
    },
    cate1sSelectIcon () {
      if (this.selectAllCate1s) return 'mdi-close-box'
      if (this.selectSomeCate1s) return 'mdi-minus-box'
      return 'mdi-checkbox-blank-outline'
    }
  },

  watch: {
    selectedFilters: {
      handler (newVal) {
        const date = newVal.date
        const startTime = '000'
        const scrollDirection = 'init'
        const mallNames = newVal.mallNames.join('|') || ''
        const cate1s = newVal.cate1s.join('|') || ''

        // init this.timelineGoods
        this.timelineGoods = null
        this.fetchTimelineGoods(date, startTime, scrollDirection, mallNames, cate1s)
      },
      deep: true
    }
  },

  created () {
    const date = this.selectedFilters.date
    const startTime = this.startTimeOfTopGood

    this.scrollDirection = 'init'
    this.scrollPosition = 0

    this.fetchTimelineFilters()
    this.fetchTimelineGoods(date, startTime, this.scrollDirection)
    window.addEventListener('scroll', this.handleScroll)
  },

  destroyed () {
    delete window.savedScrollY
    window.removeEventListener('scroll', this.handleScroll)
  },

  methods: {
    goToLivePosition () {
      setTimeout(() => {
        if (this.scrollDirection === 'init') {
          if (document.getElementById('liveDiv')) {
            console.log('get here')
            let liveDiv = document.getElementById('liveDiv')
            liveDiv.scrollIntoView()
            console.log('get here1')
            console.log('this.scrollPosition', this.scrollPosition)
            console.log('liveDiv.offsetTop', liveDiv.offsetTop - 200)
            window.scrollTo(0, liveDiv.offsetTop - 200)
          }
          this.scrollDirection = ''
        }
      }, 1000)
    },
    toggleMallNamesSelection () {
      this.$nextTick(() => {
        if (this.selectAllMallNames) {
          this.selectedFilters.mallNames = []
        } else {
          this.selectedFilters.mallNames = this.filters.mallNames.slice()
        }
      })
    },
    toggleCate1sSelection () {
      this.$nextTick(() => {
        if (this.selectAllCate1s) {
          this.selectedFilters.cate1s = []
        } else {
          console.log(this.filters.cate1s.slice())
          this.selectedFilters.cate1s = this.filters.cate1s.slice()
        }
      })
    },
    handleScroll () {
      const mallNames = this.selectedFilters.mallNames.join('|') || ''
      const cate1s = this.selectedFilters.cate1s.join('|') || ''

      // check if page hits the top of the page
      if (window.scrollY <= this.scrollPosition) {
        const topOfWindow = window.pageYOffset === 0
        if (topOfWindow) {
          this.scrollDirection = 'up'
          if (!this.loadingTimelineGoods) {
            // save currentTopGood's element id to keep the position of the scroll, even when contents are updated
            let startDateTime = this.$moment(`${this.startDateOfTopGood} ${this.startTimeOfTopGood}`, 'YYYYMMDD Hmm')
            this.savedTopGoodElementId = startDateTime.format('YYYYMMDD_H')

            this.fetchTimelineGoods(
              this.startDateOfTopGood,
              this.startTimeOfTopGood,
              this.scrollDirection,
              mallNames,
              cate1s
            )
            setTimeout(() => {
              // load saved currentTopGood's element id to keep the current scroll position
              const elementOfTopGood = document.getElementById(this.savedTopGoodElementId)
              window.scrollTo(0, elementOfTopGood.offsetTop - 200)
            })
          }
        }
      }

      // check if page hits the bottom of the page
      if (window.scrollY > this.scrollPosition) {
        const bottomOfWindow = window.pageYOffset + window.innerHeight === document.documentElement.offsetHeight
        if (bottomOfWindow) {
          this.scrollDirection = 'down'
          if (!this.loadingTimelineGoods) {
            console.log('scroll DOWN & touch bottom')
            this.fetchTimelineGoods(
              this.nextDateOfBottomGood,
              this.nextStartTimeOfBottomGood,
              this.scrollDirection,
              mallNames,
              cate1s
            )
          }
        }
      }
      this.scrollPosition = window.scrollY
    },
    fetchTimelineFilters () {
      this.$API.timeline.filters()
        .then((response) => {
          if (response.data.success) {
            this.filters.dates = response.data.timeline_filters.dates
            this.filters.mallNames = response.data.timeline_filters.mall_names
            this.filters.cate1s = response.data.timeline_filters.cate1s
          }
        })
        .catch((error) => {
          console.log(error)
          this.filters.mallNames = []
          this.filters.cate1s = []
        })
    },
    fetchTimelineGoods (date, startTime, scrollDirection, mallNames, cate1s) {
      this.loadingTimelineGoods = true

      this.$API.timeline.goods(date, startTime, scrollDirection, mallNames, cate1s)
        .then((response) => {
          if (response.data.success) {
            let timelineGoods = {}
            response.data.timeline_goods.forEach((e) => {
              const mallNameStartTimeKey = e.mall_name + '_' + e.start_time

              let goodStartHourEndAt = e.start_time.length > 3 ? 2 : 1
              let hour = e.start_time.length < 3 ? '0' : e.start_time.substring(0, goodStartHourEndAt)
              let dateHourKey = e.date + '_' + hour

              if (parseInt(e.date) === parseInt(this.currentDate) &&
                  parseInt(e.start_time) <= parseInt(this.currentTime) &&
                  parseInt(e.end_time) >= parseInt(this.currentTime)) {
                dateHourKey = this.currentDateTime
              }

              if (timelineGoods[dateHourKey] === undefined) {
                timelineGoods[dateHourKey] = {}
              }
              if (timelineGoods[dateHourKey][mallNameStartTimeKey] === undefined) {
                timelineGoods[dateHourKey][mallNameStartTimeKey] = {}
              }
              if (timelineGoods[dateHourKey][mallNameStartTimeKey]['mainGood'] === undefined) {
                timelineGoods[dateHourKey][mallNameStartTimeKey]['mainGood'] = e
              } else {
                if (timelineGoods[dateHourKey][mallNameStartTimeKey]['goodsOnSameTimeline'] === undefined) {
                  timelineGoods[dateHourKey][mallNameStartTimeKey]['goodsOnSameTimeline'] = []
                }
                timelineGoods[dateHourKey][mallNameStartTimeKey]['goodsOnSameTimeline'].push(e)
              }
            })

            if (this.timelineGoods === null) {
              this.timelineGoods = {}
            }
            if (scrollDirection === 'down') {
              this.timelineGoods = Object.assign(this.timelineGoods, timelineGoods)
            } else {
              this.timelineGoods = Object.assign(timelineGoods, this.timelineGoods)
            }
            if (Object.keys(this.timelineGoods).length > 0) {
              // get first good's start_hour
              const timelineGoodsDateHours = Object.keys(this.timelineGoods)
              const dateHoursOfBottomGood = timelineGoodsDateHours[timelineGoodsDateHours.length - 1]
              const startTimeOfBottomGood = this.$moment(dateHoursOfBottomGood, 'YYYYMMDD H')
              const nextStartTimeOfBottomGood = startTimeOfBottomGood.add(1, 'hours')

              this.startDateOfTopGood = timelineGoodsDateHours[0].split('_')[0]
              this.startTimeOfTopGood = timelineGoodsDateHours[0].split('_')[1] + '00'
              this.nextDateOfBottomGood = nextStartTimeOfBottomGood.format('YYYYMMDD')
              this.nextStartTimeOfBottomGood = nextStartTimeOfBottomGood.format('H') + '00'
            }
          } else {
            if (Object.keys(this.timelineGoods).length > 0) {
              // get first good's start_hour
              if (scrollDirection === 'down') {
                let nextDateTime = this.$moment(`${this.nextDateOfBottomGood} ${this.nextStartTimeOfBottomGood}`, 'YYYYMMDD Hmm')
                nextDateTime = nextDateTime.add(4, 'hours')

                this.nextDateOfBottomGood = nextDateTime.format('YYYYMMDD')
                this.nextStartTimeOfBottomGood = nextDateTime.format('H') + '00'
              } else {
                let startDateTime = this.$moment(`${this.startDateOfTopGood} ${this.startTimeOfTopGood}`, 'YYYYMMDD Hmm')
                startDateTime = startDateTime.subtract(4, 'hours')

                this.startDateOfTopGood = startDateTime.format('YYYYMMDD')
                this.startTimeOfTopGood = startDateTime.format('H') + '00'
              }
            }
          }
          this.loadingTimelineGoods = false
        })
        .catch((error) => {
          console.log(error)
          this.loadingTimelineGoods = false
        })
        .then(() => {
          this.goToLivePosition()
        })
    }
  }
}
</script>

<style scoped>
  .tool-bar {
    z-index: 3;
  }

  .selected-item-span {
    font-size: 14px;
  }

  .timeline-header-layout {
    position: fixed;
    padding-top: 60px;
    background: white;
    z-index: 2;
  }

  .timeline-goods-list {
    padding-top: 200px;
  }

  .live-text-div {
    max-width: 100px;
    text-align: center;
    border-radius: 10px;
    color: #ffffff;
    background-color: #d50000;
  }

  .datetime-wrapper {
    padding-bottom: 10px;
    padding-top: 5px;
  }

  .hour-text-div {
    max-width: 100px;
    text-align: center;
    border-radius: 10px;
    color: #fff;
    background-color: #b0bec5;
  }
</style>
