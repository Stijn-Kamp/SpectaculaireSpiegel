(function(t){function e(e){for(var a,o,r=e[0],l=e[1],c=e[2],f=0,d=[];f<r.length;f++)o=r[f],Object.prototype.hasOwnProperty.call(s,o)&&s[o]&&d.push(s[o][0]),s[o]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);u&&u(e);while(d.length)d.shift()();return i.push.apply(i,c||[]),n()}function n(){for(var t,e=0;e<i.length;e++){for(var n=i[e],a=!0,r=1;r<n.length;r++){var l=n[r];0!==s[l]&&(a=!1)}a&&(i.splice(e--,1),t=o(o.s=n[0]))}return t}var a={},s={app:0},i=[];function o(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=t,o.c=a,o.d=function(t,e,n){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)o.d(n,a,function(e){return t[e]}.bind(null,a));return n},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],l=r.push.bind(r);r.push=e,r=r.slice();for(var c=0;c<r.length;c++)e(r[c]);var u=l;i.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},1:function(t,e){},2:function(t,e){},"56d7":function(t,e,n){"use strict";n.r(e);n("96cf");var a=n("1da1"),s=(n("e260"),n("e6cf"),n("cca6"),n("a79d"),n("2b0e")),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("HelloWorld",{attrs:{msg:"Wir lieben Spiegels"}})],1)},o=[],r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"flex items-stretch bg-black text-white min-h-screen font-thin"},[n("div",{staticClass:"w-1/2 flex-1"},[n("div",{staticClass:"mb-6",attrs:{id:"weather"}},[n("table",[t._m(0),t._l(t.weather,(function(e,a){return n("tr",{key:"dayReport-"+a},[n("th",{staticClass:"font-thin"},[t._v(" "+t._s(t.WEEKDAYS[(t.today.getDay()+a+t.WEEKDAYS.length-1)%t.WEEKDAYS.length])+" ")]),n("th",["rain"==e.icon?n("i",{staticClass:"fas fa-cloud-rain font-thin"}):"partly-cloudy-day"==e.icon?n("i",{staticClass:"fas fa-cloud-sun"}):"wind"==e.icon?n("i",{staticClass:"fas fa-wind font-thin"}):"cloudy"==e.icon?n("i",{staticClass:"fas fa-cloud font-thin"}):"clear-night"==e.icon?n("i",{staticClass:"fas fa-moon font-thin"}):"clear-day"==e.icon?n("i",{staticClass:"fas fa-sun font-thin"}):"partly-cloudy-night"==e.icon?n("i",{staticClass:"fas fa-cloud-moon font-thin"}):"sleet"==e.icon?n("i",{staticClass:"fas fa-cloud font-thin"}):"snow"==e.icon?n("i",{staticClass:"fas fa-cloud-meatball font-thin"}):"fog"==e.icon?n("i",{staticClass:"fas fa-smog font-thin"}):t._e()]),n("th",{staticClass:"font-thin"},[t._v(t._s(e.tempMin)+"°")]),n("th",{staticClass:"font-thin"},[t._v("/")]),n("th",{staticClass:"font-thin"},[t._v(t._s(e.tempMax)+"°")])])}))],2)]),n("div",{attrs:{id:"calendar"}},[n("table",[t._m(1),t._l(t.calendar,(function(e,a){return n("tr",{key:"event-"+a},[n("th",{staticClass:"font-thin"},[t._v(" "+t._s(e.summary)+" ")]),n("th",{staticClass:"font-thin"},[t._v(" "+t._s(t.get_event_dif(e.startTime))+" ")])])}))],2)])]),n("div",{staticClass:"text-3xl flex flex-col top-0 right-0 mb-6 pr-2",attrs:{id:"clock"}},[n("p",[t._v(t._s(t.today.toDateString()))]),n("p",[t._v(t._s(t.today.toLocaleTimeString()))])]),n("div",{staticClass:"w-full text-center absolute mb-16 px-12 bottom-0",attrs:{id:"news"}},[t.news?n("agile",{attrs:{"nav-buttons":!1,autoplay:!0,"autoplay-speed":1e4,"slides-to-show":1}},t._l(t.news,(function(e,a){return n("div",{key:"newsItem-"+a,staticClass:"slide text-2xl px-3"},[n("a",{attrs:{href:e.url,target:"_blank"}},[t._v(" "+t._s(e.title)+" ")]),n("p",{staticClass:"text-sm text-gray-500"},[t._v(" "+t._s(e.source)+" published "+t._s(t.get_time_diff(t.parse_time(e.time)))+" ago ")])])})),0):t._e()],1),n("div",{staticClass:"w-full text-center absolute mb-16 px-12 top-0 text-sm text-gray-800",attrs:{hidden:!0}},[t._v(" SpectaculaireSpiegel v0.1 ")])])},l=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("thead",[n("tr",[n("th",{staticClass:"text-left font-tiny border-b border-white",attrs:{Colspan:"10"}},[t._v(" WEATHER FORECAST ")])])])},function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("thead",[n("tr",[n("th",{staticClass:"text-left font-tiny border-b border-white",attrs:{colspan:"2"}},[t._v(" CALENDAR ")])])])}],c=n("f7ab"),u=n("bc3a").default,f={name:"SpectaculaireSpiegel",components:{agile:c["a"]},props:{msg:String},data:function(){return{news:null,weather:[],calendar:[],location:[],today:new Date,WEEKDAYS:["Mo","Tu","We","Th","Fr","Sa","Su"]}},created:function(){this.getnews()},mounted:function(){setInterval(this.set_time,1e3),setInterval(this.getnews,6e4)},methods:{set_time:function(){this.today=new Date},get_event_dif:function(t){t=this.parse_time(t);return t>this.today?"in "+this.get_time_diff(t):"has started"},parse_time:function(t){t="undefined"!==typeof t?t:"2014-01-01 01:02:03.123456",t=new Date(t).getTime();return t},get_time_diff:function(t){var e=(new Date).getTime();if(isNaN(t))return"";var n="";if(t>e)var a=t-e;else a=e-t;var s=new Date(a),i=Math.floor(a/1e3/60/1440),o=s.getUTCHours(),r=s.getMinutes();n="";return i?n+=i+(i>1?" Days ":" Day "):((o||n)&&(n+=o+(1!=o?" Hours ":" Hour ")),(r||n)&&(n+=r+(1!=r?" Minutes ":" Minute "))),n},getnews:function(){var t=this,e="http://".concat(window.location.hostname,":8000");console.log(e+"/news"),this.news=null,u.get(e+"/news",{}).then((function(e){console.log(e.data),t.news=e.data})).catch(),u.get(e+"/weather",{}).then((function(e){console.log(e.data),t.weather=e.data})).catch(),u.get(e+"/location",{}).then((function(e){console.log(e.data),t.location=e.data})).catch(),u.get(e+"/calendar",{}).then((function(e){console.log(e.data),t.calendar=e.data})).catch()}}},d=f,h=n("2877"),p=Object(h["a"])(d,r,l,!1,null,null,null),_=p.exports,g={name:"App",components:{HelloWorld:_}},v=g,m=Object(h["a"])(v,i,o,!1,null,null,null),b=m.exports,w=n("a7fe"),y=n.n(w),C=n("bc3a"),x=n.n(C),S=n("ebfd"),E=n.n(S);s["a"].use(E.a),s["a"].use(c["b"]),s["a"].config.productionTip=!1,s["a"].use(y.a,x.a),document.addEventListener("DOMContentLoaded",function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:new s["a"]({render:function(t){return t(b)}}).$mount("#app");case 1:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}())}});
//# sourceMappingURL=app.12e94184.js.map