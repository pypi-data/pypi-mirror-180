"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1374],{41374:function(t,e,r){r.d(e,{x8:function(){return V},ZP:function(){return et}});var n=r(82394),o=r(77837),c=r(12757),u=r(38860),a=r.n(u),i=(r(83455),r(96040)),s=r(55056),l=r.n(s),p=r(59e3),f=r(554);function d(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function v(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?d(Object(r),!0).forEach((function(e){(0,n.Z)(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):d(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var h="DELETE",g="GET",y="POST",b="PUT";function O(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=e.body,o=(e.ctx,e.method),u=void 0===o?g:o,a=e.query,i=void 0===a?{}:a,s=(e.token,{"Content-Type":"application/json"}),l={method:u};if(r){var d=r.file;if(d){d.name,d.size,d.type;var h=new FormData,y=Object.keys(r).filter((function(t){return"file"!==t}))[0];h.set("json_root_body",JSON.stringify((0,n.Z)({api_key:f.env.NEXT_PUBLIC_API_KEY},y,r[y]))),h.append("file",d),l.body=h,delete s["Content-Type"]}else l.body=JSON.stringify(v(v({},r),{},{api_key:f.env.NEXT_PUBLIC_API_KEY}))}l.headers=new Headers(s);var b=v(v({},(0,p.iV)(t)),i);f.env.NEXT_PUBLIC_API_KEY&&(b.api_key=f.env.NEXT_PUBLIC_API_KEY);var O=Object.entries(b).reduce((function(t,e){var r=(0,c.Z)(e,2),n=r[0],o=r[1];return t.concat("".concat(n,"=").concat(o))}),[]).join("&");return{data:l,headers:s,method:u,queryString:O,url:t.split("?")[0]}}function m(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=O(t,e),n=r.data,o=r.queryString,c=r.url,u=o?"".concat(c,"?").concat(o):c;return fetch(u,n)}function w(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=O(t,e),n=r.data,o=r.headers,c=r.method,u=r.queryString,a=r.url,i=u?"".concat(a,"?").concat(u):a;return l().request({data:n.body,headers:o,method:c,onUploadProgress:null===e||void 0===e?void 0:e.onUploadProgress,url:i})}function j(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return m(t,e).then((function(t){return t.clone().json()}))}var P=r(28799);function _(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function x(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?_(Object(r),!0).forEach((function(e){(0,n.Z)(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):_(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}function k(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};return w((0,P.Q2)(t),x(x({},r),{},{body:e,method:y}))}function E(t,e,r,n){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{},c=(0,P.Q2)(e,r,t);return w(c,x(x({},o),{},{body:n,method:y}))}function Z(t,e,r,n,o){var c=arguments.length>5&&void 0!==arguments[5]?arguments[5]:{},u=(0,P.Q2)(e,r,t,n);return w(u,x(x({},c),{},{body:o,method:b}))}function D(t,e,r){var n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{};return m((0,P.Q2)(e,r),{ctx:t,query:n,method:g})}function A(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};return m((0,P.Q2)(e),{ctx:t,query:r,method:g})}function C(t,e,r,n){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{};return m((0,P.Q2)(r,n,e),{ctx:t,query:o,method:g})}function S(t,e,r){var n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},o=(0,P.Q2)(t,e,null,null,n);return w(o,{body:r,method:b})}function Q(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},o=(0,i.ZP)(e?(0,P.Q2)(t,e):null,(function(t){return j(t,{method:g,query:r})}),n),c=o.data,u=o.error,a=o.mutate;return{data:c,error:u,mutate:a}}function U(t,e,r,n){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{},c=arguments.length>5&&void 0!==arguments[5]?arguments[5]:{},u=arguments.length>6?arguments[6]:void 0,a=(0,i.ZP)(e&&(n?(0,P.Q2)(r,n,t,e,o,u):null),(function(t){return j(t,{method:g,query:o})}),c),s=a.data,l=a.error,p=a.mutate;return{data:s,error:l,mutate:p}}function T(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};return m((0,P.Q2)(t,e),{query:r,method:h})}function q(t,e,r,n){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{};return m((0,P.Q2)(e,r,t,n),{query:o,method:h})}function I(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},o=n.pauseFetch,c=void 0!==o&&o,u=(0,i.ZP)(c?null:(0,P.Q2)(t,null,null,null,e),(function(t){return j(t)}),r),a=u.data,s=u.error,l=u.mutate;return{data:a,error:s,loading:!a&&!s,mutate:l}}function L(t,e,r){var n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{},c=(0,i.ZP)(r?(0,P.Q2)(e,r,t,null,n):null,(function(t){return j(t)}),o),u=c.data,a=c.error,s=c.mutate;return{data:u,error:a,loading:!u&&!a,mutate:s}}function N(t,e,r,n){return m((0,P.Q2)(e,r),{ctx:t,body:n,method:b})}var B=r(96510);function K(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function H(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?K(Object(r),!0).forEach((function(e){(0,n.Z)(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):K(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var R="blocks",M="block_runs",X="clusters",Y="feature_sets",F="integration_sources",J="kernels",V="monitor_stats",z="outputs",G="pipelines",W="pipeline_runs",$="pipeline_schedules",tt={};[["execute",G],["autocomplete_items"],[M],[R],[R,G],[R,G,"analyses"],[R,G,z],[X],["columns",Y],["data_providers"],["downloads",Y],["event_matchers"],["event_rules"],[Y],["files"],["file_contents"],["instances",X],["integration_destinations"],["integration_samples",F],[F],["integration_source_streams"],[J],["interrupt",J],["restart",J],["logs",G],[V],[z,M],[G],[W],[W,$],[$],[$,G],["projects"],["status"],["variables",G],["versions",Y],["widgets",G]].forEach((function(t){var e=(0,c.Z)(t,4),r=e[0],n=e[1],u=e[2],i=e[3];tt[r]||(tt[r]={deleteAsync:function(){var t=(0,o.Z)(a().mark((function t(e){var n;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,T(r,e);case 2:return n=t.sent,t.next=5,(0,B.pr)(n);case 5:return t.abrupt("return",t.sent);case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),detail:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},n=arguments.length>2?arguments[2]:void 0;return Q(r,t,e,H(H({},i),n))},detailAsync:function(){var t=(0,o.Z)(a().mark((function t(e,n){var o,c,u=arguments;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return o=u.length>2&&void 0!==u[2]?u[2]:{},t.next=3,D(e,r,n,o);case 3:return c=t.sent,t.next=6,(0,B.pr)(c);case 6:return t.abrupt("return",t.sent);case 7:case"end":return t.stop()}}),t)})));return function(e,r){return t.apply(this,arguments)}}(),updateAsync:function(){var t=(0,o.Z)(a().mark((function t(e,n,o){var c;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,N(e,r,n,o);case 2:return c=t.sent,t.next=5,(0,B.pr)(c);case 5:return t.abrupt("return",t.sent);case 6:case"end":return t.stop()}}),t)})));return function(e,r,n){return t.apply(this,arguments)}}(),useUpdate:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return function(){var n=(0,o.Z)(a().mark((function n(o){return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return n.abrupt("return",S(r,t,o,e));case 1:case"end":return n.stop()}}),n)})));return function(t){return n.apply(this,arguments)}}()}}),u?(tt[r][n][u]={},tt[r][n][u].detail=function(t,e,o,c){return U(r,e,n,t,o,H(H({},i),c),u)}):n?(tt[r][n]={},tt[r][n].useCreate=function(t,e){return function(){var c=(0,o.Z)(a().mark((function o(c){return a().wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return o.abrupt("return",E(r,n,t,c,e));case 1:case"end":return o.stop()}}),o)})));return function(t){return c.apply(this,arguments)}}()},tt[r][n].useCreateWithParentIdLater=function(t){return function(){var e=(0,o.Z)(a().mark((function e(o){return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",E(r,n,o.parentId,o.body,t));case 1:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()},tt[r][n].useUpdate=function(t,e,c){return function(){var u=(0,o.Z)(a().mark((function o(u){return a().wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return o.abrupt("return",Z(r,n,t,e,u,c));case 1:case"end":return o.stop()}}),o)})));return function(t){return u.apply(this,arguments)}}()},tt[r][n].useDelete=function(t,e,c){return(0,o.Z)(a().mark((function o(){var u;return a().wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return o.next=2,q(r,n,t,e,c);case 2:return u=o.sent,o.next=5,(0,B.pr)(u);case 5:return o.abrupt("return",o.sent);case 6:case"end":return o.stop()}}),o)})))},tt[r][n].listAsync=function(){var t=(0,o.Z)(a().mark((function t(e,o){var c,u,i=arguments;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return c=i.length>2&&void 0!==i[2]?i[2]:{},t.next=3,C(e,r,n,o,c);case 3:return u=t.sent,t.next=6,(0,B.pr)(u);case 6:return t.abrupt("return",t.sent);case 7:case"end":return t.stop()}}),t)})));return function(e,r){return t.apply(this,arguments)}}(),tt[r][n].list=function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},o=arguments.length>2?arguments[2]:void 0;return L(r,n,t,e,H(H({},i),o))},tt[r][n].detail=function(t,e,o,c){return U(r,e,n,t,o,H(H({},i),c))}):(tt[r].create=function(){var t=(0,o.Z)(a().mark((function t(e,n){var o;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,k(r,e,n);case 2:return o=t.sent,t.next=5,(0,B.pr)(o);case 5:return t.abrupt("return",t.sent);case 6:case"end":return t.stop()}}),t)})));return function(e,r){return t.apply(this,arguments)}}(),tt[r].useCreate=function(t){return function(){var e=(0,o.Z)(a().mark((function e(n){return a().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",k(r,n,t));case 1:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()},tt[r].useDelete=function(t,e){return(0,o.Z)(a().mark((function n(){var o;return a().wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return n.next=2,T(r,t,e);case 2:return o=n.sent,n.next=5,(0,B.pr)(o);case 5:return n.abrupt("return",n.sent);case 6:case"end":return n.stop()}}),n)})))},tt[r].listAsync=function(){var t=(0,o.Z)(a().mark((function t(e){var n,o,c=arguments;return a().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n=c.length>1&&void 0!==c[1]?c[1]:{},t.next=3,A(e,r,n);case 3:return o=t.sent,t.next=6,(0,B.pr)(o);case 6:return t.abrupt("return",t.sent);case 7:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),tt[r].list=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},e=arguments.length>1?arguments[1]:void 0,n=arguments.length>2?arguments[2]:void 0;return I(r,t,H(H({},i),e),n)})}));var et=tt},96510:function(t,e,r){r.d(e,{QZ:function(){return l},nU:function(){return i},pr:function(){return s},qQ:function(){return f},wD:function(){return d}});var n=r(77555),o=r(82394),c=r(12757);function u(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function a(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?u(Object(r),!0).forEach((function(e){(0,o.Z)(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):u(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}function i(t){var e=t.error,r=e.code,n=e.errors,o=e.message,u=e.type,i=[];return i=n?null!==n&&void 0!==n&&n.__all__?null===n||void 0===n?void 0:n.__all__:Array.isArray(n)?n:Object.entries(n).reduce((function(t,e){var r=(0,c.Z)(e,2),n=r[0],o=r[1];return t.concat("".concat(n,": ").concat(o[0]))}),[]):e.messages,a(a({},e),{},{code:r,errors:n,message:o,messages:i,type:u})}function s(t){return t.data?Promise.resolve(t.data):t.json?t.json():void 0}function l(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=i(t),o=r.code,c=r.errors,u=r.exception,a=r.message,s=r.messages,l=[];if(a)l.push.apply(l,(0,n.Z)(a.split("\n")));else if((null===s||void 0===s?void 0:s.length)>=1)l.push.apply(l,(0,n.Z)(s));else{var p=e.errorMessage||(null===s||void 0===s?void 0:s[0])||c;p&&l.push(p)}return u&&l.push(u),{code:o,messages:l}}function p(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=e.acceptErrorStatuses,n=void 0===r?[]:r,o=e.callback,c=e.onErrorCallback,u=(e.successMessage,t.error);if(u&&!n.includes(null===u||void 0===u?void 0:u.code)){var a=l(t);return null===c||void 0===c||c(t,a),a}return null===o||void 0===o?void 0:o(t)}function f(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=t.errors,n=t.message,o=t.response,c=a({error:{code:null===o||void 0===o?void 0:o.status,messages:[r||n]}},null===o||void 0===o?void 0:o.data),u=e.callback;return null===u||void 0===u||u(c),l(c,e)}function d(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return t.status?s(t).then((function(t){return p(t,e)})):p(t,e)}},28799:function(t,e,r){r.d(e,{Ib:function(){return u},Q2:function(){return a}});var n=r(59e3);function o(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"localhost",r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"6789",n=e;return t&&(n=window.location.hostname),n===e?n="".concat(n,":").concat(r):t&&window.location.port&&(n="".concat(n,":").concat(window.location.port)),n}function c(){var t="localhost",e="/CLOUD_NOTEBOOK_BASE_PATH_PLACEHOLDER_",r=o(true,t,"6789"),n=function(t,e){var r,n="http://";return e!==(arguments.length>2&&void 0!==arguments[2]?arguments[2]:"localhost")&&(n="https://",!t||null!==(r=window.location.protocol)&&void 0!==r&&r.match(/https/)||(n="http://")),n}(true,r,t),c="";return e.includes("CLOUD_NOTEBOOK_BASE_PATH_PLACEHOLDER")||(c=e),"".concat(n).concat(r).concat(c,"/api")}function u(){var t,e="ws://";return null!==(t=window.location.protocol)&&void 0!==t&&t.match(/https/)&&(e="wss://"),"".concat(e).concat(o(true,"localhost","6789"),"/websocket/")}function a(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null,r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:null,o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:null,u=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{},a=arguments.length>5&&void 0!==arguments[5]?arguments[5]:null,i="".concat(c(),"/").concat(t);return e&&(i="".concat(i,"/").concat(e)),r&&(i="".concat(i,"/").concat(r)),o&&(i="".concat(i,"/").concat(o)),a&&(i="".concat(i,"/").concat(a)),Object.values(u||{}).length>=1&&(i="".concat(i,"?").concat((0,n.uM)(u))),i}e.ZP=a},59e3:function(t,e,r){r.d(e,{iV:function(){return o},uM:function(){return c}});var n=r(12757);r(34376);function o(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null,e={},r=t;if(t||(r=window.location.search),r){var o=new URLSearchParams(r.split("?").slice(1).join(""));Array.from(o.keys()).forEach((function(t){var r=t.match(/\[\]/),c=o.getAll(t);if(1!==c.length||r)e[t]=c;else{var u=(0,n.Z)(c,1);e[t]=u[0]}}))}return e}function c(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return Object.entries(t).reduce((function(t,e){var r=(0,n.Z)(e,2),o=r[0],c=r[1];if(Array.isArray(c)){var u=o;return u.match(/\[\]/)||(u="".concat(u,"[]")),t.concat(c.map((function(t){return"".concat(u,"=").concat(encodeURIComponent(t))})))}return t.concat("".concat(o,"=").concat(encodeURIComponent(c)))}),[]).join("&")}}}]);