(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[5912],{44162:function(e,t,n){"use strict";n.d(t,{HC:function(){return A},Kf:function(){return s},Nk:function(){return p},gE:function(){return b},jv:function(){return f},oh:function(){return l},qn:function(){return d},t1:function(){return h},y9:function(){return m}});var r=n(46313),o=n(23831),c=n(73942),i=n(86422),u=n(49125),a=n(90880),l=68;function d(e,t){var n=(t.theme.borders||o.Z.borders).light,r=(t.theme.monotone||o.Z.monotone).grey500,c=t||{},u=c.isSelected,a=c.theme;return u?n=(a.content||o.Z.content).active:i.tf.TRANSFORMER===e?(n=(a.accent||o.Z.accent).purple,r=(a.accent||o.Z.accent).purpleLight):i.tf.DATA_EXPORTER===e?(n=(a.accent||o.Z.accent).yellow,r=(a.accent||o.Z.accent).yellowLight):i.tf.DATA_LOADER===e?(n=(a.accent||o.Z.accent).blue,r=(a.accent||o.Z.accent).blueLight):i.tf.SCRATCHPAD===e?(n=(a.content||o.Z.content).default,r=(a.accent||o.Z.accent).contentDefaultTransparent):i.tf.SENSOR===e?(n=(a.accent||o.Z.accent).pink,r=(a.accent||o.Z.accent).pinkLight):i.tf.DBT===e&&(n=(a.accent||o.Z.accent).dbt,r=(a.accent||o.Z.accent).dbtLight),{accent:n,accentLight:r}}var s=(0,r.css)([""," "," "," "," ",""],(0,a.eR)(),(function(e){return!e.selected&&!e.hasError&&"\n    border-color: ".concat(d(e.blockType,e).accentLight,";\n  ")}),(function(e){return e.selected&&!e.hasError&&"\n    border-color: ".concat(d(e.blockType,e).accent,";\n  ")}),(function(e){return!e.selected&&e.hasError&&"\n    border-color: ".concat((e.theme.accent||o.Z.accent).negativeTransparent,";\n  ")}),(function(e){return e.selected&&e.hasError&&"\n    border-color: ".concat((e.theme.borders||o.Z.borders).danger,";\n  ")})),p=r.default.div.withConfig({displayName:"indexstyle__ContainerStyle",componentId:"sc-s5rj34-0"})(["border-radius:","px;position:relative;"],c.n_),f=r.default.div.withConfig({displayName:"indexstyle__CodeContainerStyle",componentId:"sc-s5rj34-1"})([""," border-left-style:solid;border-left-width:2px;border-right-style:solid;border-right-width:2px;border-top-left-radius:","px;border-top-right-radius:","px;border-top-style:solid;border-top-width:2px;padding-bottom:","px;padding-top:","px;position:relative;"," "," .line-numbers{opacity:0;}&.selected{.line-numbers{opacity:1 !important;}}"],s,c.n_,c.n_,u.iI,u.iI,(function(e){return"\n    background-color: ".concat((e.theme.background||o.Z.background).codeTextarea,";\n  ")}),(function(e){return!e.hasOutput&&"\n    border-bottom-left-radius: ".concat(c.n_,"px;\n    border-bottom-right-radius: ").concat(c.n_,"px;\n    border-bottom-style: solid;\n    border-bottom-width: 2px;\n  ")})),b=r.default.div.withConfig({displayName:"indexstyle__BlockDivider",componentId:"sc-s5rj34-2"})(["align-items:center;display:flex;height:","px;justify-content:center;position:relative;z-index:10;&:hover{.block-divider-inner{","}}"],2*u.iI,(function(e){return"\n        background-color: ".concat((e.theme.text||o.Z.text).fileBrowser,";\n      ")})),h=r.default.div.withConfig({displayName:"indexstyle__BlockDividerInner",componentId:"sc-s5rj34-3"})(["height 1px;width:100%;position:absolute;z-index:-1;"]),m=r.default.div.withConfig({displayName:"indexstyle__CodeHelperStyle",componentId:"sc-s5rj34-4"})(["margin-bottom:","px;padding-bottom:","px;padding-left:","px;",""],u.cd*u.iI,u.iI,l,(function(e){return"\n    border-bottom: 1px solid ".concat((e.theme.borders||o.Z.borders).medium,";\n  ")})),A=r.default.div.withConfig({displayName:"indexstyle__TimeTrackerStyle",componentId:"sc-s5rj34-5"})(["bottom:","px;left:","px;position:absolute;"],1*u.iI,l)},43032:function(e,t,n){"use strict";n.d(t,{Cl:function(){return u},Nk:function(){return a},ZG:function(){return i}});var r=n(46313),o=n(23831),c=n(49125),i=1.5*c.iI,u=1*i+c.iI/2,a=r.default.div.withConfig({displayName:"indexstyle__ContainerStyle",componentId:"sc-uvd91-0"})([".row:hover{","}"],(function(e){return"\n      background-color: ".concat((e.theme.interactive||o.Z.interactive).hoverBackground,";\n    ")}))},86422:function(e,t,n){"use strict";n.d(t,{$W:function(){return s},DA:function(){return d},HX:function(){return b},J8:function(){return f},Qj:function(){return h},Ut:function(){return v},V4:function(){return g},VZ:function(){return p},dO:function(){return l},f2:function(){return A},iZ:function(){return m},t6:function(){return i},tf:function(){return a}});var r,o,c,i,u=n(82394);!function(e){e.PYTHON="python",e.R="r",e.SQL="sql",e.YAML="yaml"}(i||(i={}));var a,l=(r={},(0,u.Z)(r,i.PYTHON,"PY"),(0,u.Z)(r,i.R,"R"),(0,u.Z)(r,i.SQL,"SQL"),(0,u.Z)(r,i.YAML,"YAML"),r);!function(e){e.CHART="chart",e.DATA_EXPORTER="data_exporter",e.DATA_LOADER="data_loader",e.DBT="dbt",e.SCRATCHPAD="scratchpad",e.SENSOR="sensor",e.TRANSFORMER="transformer"}(a||(a={}));var d,s=[a.CHART,a.DATA_EXPORTER,a.DATA_LOADER,a.SCRATCHPAD,a.SENSOR,a.TRANSFORMER],p=[a.DATA_EXPORTER,a.DATA_LOADER],f=[a.DATA_EXPORTER,a.DATA_LOADER,a.TRANSFORMER],b=[a.DATA_EXPORTER,a.DATA_LOADER,a.DBT,a.TRANSFORMER],h=[a.CHART,a.SCRATCHPAD,a.SENSOR],m=[a.SCRATCHPAD];!function(e){e.EXECUTED="executed",e.FAILED="failed",e.NOT_EXECUTED="not_executed",e.UPDATED="updated"}(d||(d={}));var A=[a.DATA_EXPORTER,a.TRANSFORMER],g=(o={},(0,u.Z)(o,a.DATA_EXPORTER,"Data exporter"),(0,u.Z)(o,a.DATA_LOADER,"Data loader"),(0,u.Z)(o,a.SCRATCHPAD,"Scratchpad"),(0,u.Z)(o,a.SENSOR,"Sensor"),(0,u.Z)(o,a.TRANSFORMER,"Transformer"),o),v=[a.DATA_LOADER,a.TRANSFORMER,a.DATA_EXPORTER];c={},(0,u.Z)(c,a.DATA_EXPORTER,"DE"),(0,u.Z)(c,a.DATA_LOADER,"DL"),(0,u.Z)(c,a.SCRATCHPAD,"SP"),(0,u.Z)(c,a.SENSOR,"SR"),(0,u.Z)(c,a.TRANSFORMER,"TF")},55378:function(e,t,n){"use strict";var r=n(82394),o=n(26304),c=n(82684),i=n(46313),u=n(69898),a=n(31969),l=n(49125),d=n(28598),s=["beforeIcon","children","label","placeholder"];function p(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function f(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?p(Object(n),!0).forEach((function(t){(0,r.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):p(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var b=i.default.select.withConfig({displayName:"Select__SelectStyle",componentId:"sc-q6ezu2-0"})(["",' background-image:url("data:image/svg+xml;utf8,','");background-repeat:no-repeat;background-position:-webkit-calc(100% - ',"px) center;background-position:calc(100% - ","px) center;padding-right:","px;&:hover{cursor:pointer;}"," "," "," ",""],u.p,"\n  <svg width='12' height='12' viewBox='0 0 16 16' xmlns='http://www.w3.org/2000/svg'>\n    <path\n      clip-rule='evenodd'\n      d='M8.0015 11.7109L14.0022 5.71017L12.588 4.29597L7.99485 8.88914L3.40754 4.34482L2 5.76567L8.0015 11.7109Z'\n      fill='%23B4B8C0'\n      fill-rule='evenodd'\n    />\n  </svg>",l.iI,l.iI,2.5*l.iI,(function(e){return!e.hasContent&&!e.showPlaceholder&&"\n    color: ".concat((e.theme.content||a.Z.content).muted,";\n  ")}),(function(e){return e.backgroundColor&&"\n    background-color: ".concat(e.backgroundColor,";\n  ")}),(function(e){return e.color&&"\n    color: ".concat(e.color,";\n  ")}),(function(e){return e.showPlaceholder&&"\n    color: ".concat((e.theme.content||a.Z.content).inverted,";\n  ")})),h=function(e,t){var n=e.beforeIcon,r=e.children,c=e.label,i=e.placeholder,a=(0,o.Z)(e,s);return(0,d.jsx)(u.Z,f(f({},a),{},{beforeIcon:n,input:(0,d.jsxs)(b,f(f({},a),{},{children:[(c||i)&&(0,d.jsx)("option",{disabled:!0,selected:!0,value:"",children:c||i}),r]})),label:c,placeholder:i,ref:t,setContentOnMount:!0,showLabelRequirement:function(e){return!!e.content}}))};t.Z=c.forwardRef(h)},50094:function(e,t,n){"use strict";n.r(t);var r=n(77837),o=n(12757),c=n(82394),i=n(38860),u=n.n(i),a=n(82684),l=n(92083),d=n.n(l),s=n(46313),p=n(21679),f=n(16634),b=n(67971),h=n(87372),m=n(87465),A=n(55378),g=n(86673),v=n(41374),R=n(28799),O=n(23831),T=n(67400),E=n(43032),_=n(92953),Z=n(44162),x=n(24224),D=n(96510),y=n(83455),S=n(28598);function w(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function j(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?w(Object(n),!0).forEach((function(t){(0,c.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):w(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function C(e){var t=e.pipeline,n=(0,a.useContext)(s.ThemeContext),i=(0,a.useState)(null),l=i[0],w=i[1],C=t.uuid,P=v.ZP.pipelines.detail(C).data,k=(0,a.useMemo)((function(){return j(j({},null===P||void 0===P?void 0:P.pipeline),{},{uuid:C})}),[P,C]),L=v.ZP.pipeline_schedules.pipelines.list(C).data,N=(0,a.useMemo)((function(){return null===L||void 0===L?void 0:L.pipeline_schedules}),[L]),I=(0,a.useMemo)((function(){return(0,x.HK)(null===k||void 0===k?void 0:k.blocks,(function(e){return e.uuid}))||{}}),[k]),M=(0,a.useState)(null),H=M[0],X=M[1],B=(0,y.Db)(function(){var e=(0,r.Z)(u().mark((function e(t){var n;return u().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n="".concat((0,R.ZP)(v.x8),"/block_run_count?pipeline_uuid=").concat(C),(t||0===t)&&(n+="&pipeline_schedule_id=".concat(t)),e.abrupt("return",fetch(n,{method:"GET"}));case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),{onSuccess:function(e){return(0,D.wD)(e,{callback:function(e){X(e)}})}}),F=(0,o.Z)(B,1)[0];(0,a.useEffect)((function(){F()}),[F]);var q=((null===H||void 0===H?void 0:H.monitor_stats)||{}).stats,U=(0,a.useMemo)((function(){for(var e=new Date,t=[],n=0;n<90;n++)t.unshift(e.toISOString().split("T")[0]),e.setDate(e.getDate()-1);return t}),[]),Y=(0,a.useMemo)((function(){if(q)return Object.entries(q).reduce((function(e,t){var n=(0,o.Z)(t,2),r=n[0],i=n[1].data,u=U.map((function(e){return j({date:e},i[e]||{})}));return j(j({},e),{},(0,c.Z)({},r,u))}),{})}),[q]),K=(0,a.useMemo)((function(){var e=[];return e.push({bold:!0,label:function(){return"Monitors"}}),e}),[k]);return(0,S.jsx)(m.Z,{breadcrumbs:K,monitorType:_.a.BLOCK_RUNS,pipeline:k,subheader:(0,S.jsx)(b.Z,{children:(0,S.jsxs)(A.Z,{backgroundColor:O.Z.interactive.defaultBackground,label:"Trigger:",onChange:function(e){var t=e.target.value;"initial"!==t?(F(t),w(t)):(F(),w(null))},value:l||"initial",children:[(0,S.jsx)("option",{value:"initial",children:"All"}),N&&N.map((function(e){return(0,S.jsx)("option",{value:e.id,children:e.name})}))]})}),children:(0,S.jsx)(g.Z,{mx:2,children:Y&&Object.entries(Y).map((function(e){var t,r=(0,o.Z)(e,2),c=r[0],i=r[1];return(0,S.jsxs)(g.Z,{mt:3,children:[(0,S.jsxs)(b.Z,{alignItems:"center",children:[(0,S.jsx)(g.Z,{mx:1,children:(0,S.jsx)(f.Z,{color:(0,Z.qn)(null===(t=I[c])||void 0===t?void 0:t.type,{theme:n}).accent,size:E.ZG,square:!0})}),(0,S.jsx)(h.Z,{level:4,children:c})]}),(0,S.jsx)(g.Z,{mt:1,children:(0,S.jsx)(p.Z,{colors:T.BAR_STACK_COLORS,data:i,getXValue:function(e){return e.date},height:200,keys:T.BAR_STACK_STATUSES,margin:{top:10,bottom:30,left:35,right:0},xLabelFormat:function(e){return d()(e).format("MMM DD")}})})]})}))})})}C.getInitialProps=function(){var e=(0,r.Z)(u().mark((function e(t){var n;return u().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=t.query.pipeline,e.abrupt("return",{pipeline:{uuid:n}});case 2:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),t.default=C},83542:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pipelines/[pipeline]/monitors/block-runs",function(){return n(50094)}])}},function(e){e.O(0,[4259,2212,7689,6674,2714,1374,5763,6792,1273,8965,9898,7400,9774,2888,179],(function(){return t=83542,e(e.s=t);var t}));var t=e.O();_N_E=t}]);