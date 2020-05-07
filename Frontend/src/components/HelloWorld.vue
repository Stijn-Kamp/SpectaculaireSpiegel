<template>
  <div class="flex items-stretch bg-black text-white min-h-screen font-normal">
    <div id="side-bar" class="w-1/2 flex-1">
      <div id="weather" class="mb-6">
        <table>
          <thead>
            <tr>
              <th
                Colspan="10"
                class="text-left font-tiny border-b border-white"
              >
                WEATHER FORECAST
              </th>
            </tr>
          </thead>
          <tr
            v-for="(dayReport, index) in weather"
            :key="'dayReport-' + index"
          >
            <th class="font-normal">
              {{ WEEKDAYS[((today.getDay() + index) + WEEKDAYS.length - 1) % WEEKDAYS.length]}}
            </th>
            <th>
              <i
                v-if="dayReport.icon == 'rain'"
                class="fas fa-cloud-rain font-normal"
              /> 
              <i
                v-else-if="dayReport.icon == 'partly-cloudy-day'"
                class="fas fa-cloud-sun"
              />
              <i
                v-else-if="dayReport.icon == 'wind'"
                class="fas fa-wind font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'cloudy'"
                class="fas fa-cloud font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'clear-night'"
                class="fas fa-moon font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'clear-day'"
                class="fas fa-sun font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'partly-cloudy-night'"
                class="fas fa-cloud-moon font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'sleet'"
                class="fas fa-cloud font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'snow'"
                class="fas fa-cloud-meatball font-normal"
              />
              <i
                v-else-if="dayReport.icon == 'fog'"
                class="fas fa-smog font-normal"
              />
            </th>
              
            <th class="font-normal">{{ dayReport.tempMin }}°</th>
            <th class="font-normal">/</th>
            <th class="font-normal">{{ dayReport.tempMax }}°</th>
          </tr>
        </table>
      </div>

      <div id="calendar">
        <table>
          <thead>
            <tr>
              <th
              colspan="2"
              class="text-left font-tiny border-b border-white"
              >
                CALENDAR
              </th>
            </tr>
          </thead>
          <tr
          v-for="(event, index) in calendar"
          :key="'event-' + index"
          >
            <th class="font-normal">
              {{ event.summary }}
            </th>
            <th class="font-normal">
              {{ get_event_dif(event.startTime) }}
            </th>
          </tr>
        </table>
      </div>
    </div>

    <div id="clock" class="text-3xl flex flex-col top-0 right-0 mb-6 pr-2">
      <p>{{ today.toDateString() }}</p>
      <p>{{ today.toLocaleTimeString() }}</p>
    </div>

    <div id="news" class="w-full text-center absolute mb-16 px-12 bottom-0">
      <agile
        v-if="news"
        :nav-buttons="false"
        :autoplay="true"
        :autoplay-speed="10000"
        :slides-to-show="1"
      >
        <div id="newsItem"
          v-for="(newsItem, index) in news"
          :key="'newsItem-' + index"
          class="slide text-2xl px-3"
        >
          <a
            :href="newsItem.url"
            target="_blank"
          >
            {{ newsItem.title }}
          </a>
          <p class="font-light text-sm text-gray-500">
            {{ newsItem.source }} published {{ get_time_diff(parse_time(newsItem.time)) }} ago
          </p>
        </div>
      </agile>
    </div>
    <div :hidden='true' class="w-full text-center absolute mb-16 px-12 top-0 text-sm text-gray-800">
      SpectaculaireSpiegel v1.1
    </div>
  </div>
</template>

<script>
const axios = require('axios').default;

import { VueAgile } from 'vue-agile'
export default {
  name: 'SpectaculaireSpiegel',
  	components: {
		agile: VueAgile
  },
  props: {
    msg: String,
   
  },
  
  data: () => ({
    //https://codepen.io/gau/pen/LjQwGp Clock
    news: null,
    weather: [],
    calendar: [],
    location: [],

    today: new Date(),
    WEEKDAYS: [
      'Mo',
      'Tu',
      'We',
      'Th',
      'Fr',
      'Sa',
      'Su'
    ]
    
  }),
  created(){
        this.getnews()
  },
  mounted() 
  {
    var tmrTime = setInterval(this.set_time, 1000)
    var tmrUpdate = setInterval(this.getnews, 60000)

  },

  methods:{

    set_time()
    {
      this.today = new Date()
    },
    get_event_dif( datetime )
    {
      var datetime = this.parse_time(datetime)
      if(datetime > this.today) return "in " + this.get_time_diff(datetime)
      else return "has started"
    },
    parse_time( datetime )
    {
      var datetime = typeof datetime !== 'undefined' ? datetime : "2014-01-01 01:02:03.123456";
      var datetime = new Date( datetime ).getTime();
      return datetime
    } 
    ,
    get_time_diff( datetime )
    {
        var now = new Date().getTime();

        if( isNaN(datetime) ) return "";
        
        var time = ""

        if (datetime > now) 
        {
          var milisec_diff = datetime - now;
        }
        else
        {
          var milisec_diff = now - datetime
        }
        var date_diff = new Date( milisec_diff );

        var days = Math.floor(milisec_diff / 1000 / 60 / (60 * 24));
        var hours = date_diff.getUTCHours()
        var minutes = date_diff.getMinutes()
        var time = ""
        if(days) time += days + (days > 1 ? " Days " : " Day ") 
        else{
        if(hours || time) time += hours + (hours != 1 ? " Hours " : " Hour ") 
        if(minutes || time) time += minutes + (minutes != 1 ? " Minutes " : " Minute ")
        
            //return time ? 'Starts in ' + time : ' Has started'
        }
        return time
        //return time ? 'Starts in ' + time : ' Has started'
        //return days + " Days "+ date_diff.getHours() + " Hours " + date_diff.getMinutes() + " Minutes " + date_diff.getSeconds() + " Seconds " +  date_diff.getMilliseconds() + " Miliseconds";
    },
    getnews(){
      const baseUrl = `http://192.168.178.116:8000` //${window.location.hostname}
      console.log(baseUrl+'/news')

      this.news = null
      axios.get(baseUrl+'/news',{

      }).then(response => {
        console.log(response.data);
        this.news = response.data;

      }).catch()

      axios.get(baseUrl+'/weather',{

      }).then(response => {
        console.log(response.data);
        this.weather = response.data;
      }).catch()

    
            axios.get(baseUrl+'/location',{

      }).then(response => {
        console.log(response.data);
        this.location = response.data;
      }).catch()

            axios.get(baseUrl+'/calendar',{

      }).then(response => {
        console.log(response.data);
        this.calendar = response.data;
      }).catch()

    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
