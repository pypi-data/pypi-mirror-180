(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[8662],{62976:function(e,n,t){"use strict";t.d(n,{Z:function(){return R}});var r=t(82394),i=t(77555),o=t(82684),u=t(10919),l=t(12691),c=t.n(l),d=t(34376),s=t.n(d),a=t(46313),p=t(63068),f=t(44628),h=t(6508),m=t(67971),v=t(19711),g=t(23831),b=t(31969),y=function(){var e=document.createElement("div");e.setAttribute("style","width: 100px; height: 100px; overflow: scroll; position:absolute; top:-9999px;"),document.body.appendChild(e);var n=e.offsetWidth-e.clientWidth;return document.body.removeChild(e),n},x=t(2005),O=t(31012),j=t(37391),w=t(6753),Z=t(49125),k=t(69345),P=t(24224),C=t(28598);function E(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function _(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?E(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):E(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var D=2*Z.iI+O.dN,I=20*Z.iI,S=a.default.div.withConfig({displayName:"DataTable__Styles",componentId:"sc-1arr863-0"})([""," "," "," .body > div{","}.table{border-spacing:0;display:inline-block;"," "," "," "," .tr{.td.td-index-column{","}}.th{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;","}.th,.td{"," font-family:",";margin:0;","}.td{padding:","px;}&.sticky{overflow:auto;}.header{overflow:hidden;}}"],(function(e){return e.disableScrolling&&"\n    overflow: hidden;\n  "}),(function(e){return e.height&&"\n    height: ".concat(e.height,"px;\n  ")}),(function(e){return e.maxHeight&&"\n    max-height: ".concat(e.maxHeight,"px;\n  ")}),j.w5,(function(e){return!e.noBorderBottom&&"\n      border-bottom: 1px solid ".concat((e.theme.borders||b.Z.borders).medium,";\n    ")}),(function(e){return!e.noBorderLeft&&"\n      border-left: 1px solid ".concat((e.theme.borders||b.Z.borders).medium,";\n    ")}),(function(e){return!e.noBorderRight&&"\n      border-right: 1px solid ".concat((e.theme.borders||b.Z.borders).medium,";\n    ")}),(function(e){return!e.noBorderTop&&"\n      border-top: 1px solid ".concat((e.theme.borders||b.Z.borders).medium,";\n    ")}),(function(e){return"\n          color: ".concat((e.theme.content||b.Z.content).default,";\n        ")}),(function(e){return"\n        height: ".concat(e.columnHeaderHeight||D,"px;\n      ")}),O.iD,x.ry,(function(e){return"\n        background-color: ".concat((e.theme.background||b.Z.background).table,";\n        border-bottom: 1px solid ").concat((e.theme.borders||b.Z.borders).medium,";\n        border-right: 1px solid ").concat((e.theme.borders||b.Z.borders).medium,";\n      ")}),1*Z.iI);function N(e){var n=e.original,t=8.5*Math.max.apply(Math,(0,i.Z)(n.map((function(e){return(null===e||void 0===e?void 0:e.length)||0})))),r=Math.ceil(t/(I-2*Z.iI));return Math.max(r,1)*O.dN+2*Z.iI}function H(e){var n=e.columnHeaderHeight,t=e.columns,r=e.data,l=e.disableScrolling,d=e.height,O=e.index,j=e.invalidValues,E=e.maxHeight,S=e.numberOfIndexes,H=e.previewIndexes,R=e.renderColumnHeader,M=e.width,B=(0,o.useContext)(a.ThemeContext),T=(0,o.useRef)(null),A=(0,o.useRef)(null);(0,o.useEffect)((function(){var e=function(e){var n;null===T||void 0===T||null===(n=T.current)||void 0===n||n.scroll(e.target.scrollLeft,0)};return A&&A.current.addEventListener("scroll",e),function(){var n;null===A||void 0===A||null===(n=A.current)||void 0===n||n.removeEventListener("scroll",e)}}),[T,A]);var L=(0,o.useMemo)((function(){return O&&r&&O.length===r.length}),[r,O]),V=(0,o.useMemo)((function(){var e=[];return(0,P.w6)(S).forEach((function(n,t){var o=8.7*String(null===r||void 0===r?void 0:r.length).length;if(L){var u=O.map((function(e){return S>=2?String(e[t]).length:String(e).length}));o=8.7*Math.max.apply(Math,(0,i.Z)(u))}e.push(o+2*Z.iI)})),e}),[r,O,S,L]),U=t.map((function(e){return null===e||void 0===e?void 0:e.Header})).slice(1),F=(0,o.useMemo)((function(){return y()}),[]),W=(0,o.useMemo)((function(){var e=M-(Math.max.apply(Math,(0,i.Z)(V))+1.5*Z.iI+F),n=t.length-1,r=I;return r*n<e&&(r=e/n),{width:r}}),[t,V,F,M]),q=(0,f.useTable)({columns:t,data:r,defaultColumn:W},f.useBlockLayout,h.useSticky),G=q.getTableBodyProps,z=q.getTableProps,J=q.headerGroups,Y=q.prepareRow,X=q.rows,K=s().query.slug,$=void 0===K?[]:K,Q=new Set((null===H||void 0===H?void 0:H.removedRows)||[]),ee=(0,o.useCallback)((function(e){var n=e.index,t=e.style,r=X[n];Y(r);var i=r.original,l=Q.has(n);return(0,C.jsx)("div",_(_({},r.getRowProps({style:_(_({},t),{},{width:"auto"})})),{},{className:"tr",children:r.cells.map((function(e,t){var r,d=t<=S-1,s=e.getCellProps(),a=e.column.id,p=null===j||void 0===j||null===(r=j[a])||void 0===r?void 0:r.includes(n),f=_({},s.style);d&&(f.fontFamily=x.Vp,f.left=0,f.position="sticky",f.textAlign=O?"right":"center",f.width=V[t]);var h,g=i[t-S],y=U.indexOf(a);if(p&&(f.color=b.Z.interactive.dangerBorder),l&&(f.backgroundColor=b.Z.background.danger),Array.isArray(g)||"object"===typeof g)try{g=JSON.stringify(g)}catch(Z){g="Error: cannot display value"}return d&&(L?(h=O[n],Array.isArray(h)&&(h=h[t])):h=e.render("Cell")),(0,o.createElement)("div",_(_({},s),{},{className:"td ".concat(d?"td-index-column":""),key:"".concat(t,"-").concat(g),style:f}),h,!d&&(0,C.jsxs)(m.Z,{justifyContent:"space-between",children:[(0,C.jsxs)(v.ZP,{danger:p,default:!0,wordBreak:!0,children:[!0===g&&"true",!1===g&&"false",(null===g||"null"===g)&&"null",!0!==g&&!1!==g&&null!==g&&"null"!==g&&g]}),p&&(0,C.jsx)(c(),{as:(0,k.o_)(w.mW,y),href:"/datasets/[...slug]",passHref:!0,children:(0,C.jsx)(u.Z,{danger:!0,children:"View all"})})]}))}))}))}),[O,j,V,S,Y,X,$]),ne=(0,o.useMemo)((function(){var e;return E?(e=(0,P.Sm)(X.map(N)),e+=n||D):(e=d,e-=n||D),e}),[n,N,d,E,X]),te=(0,o.useMemo)((function(){return(0,C.jsx)(p.S_,{estimatedItemSize:D,height:ne,itemCount:null===X||void 0===X?void 0:X.length,itemSize:function(e){return N(X[e])},outerRef:A,style:{maxHeight:E,pointerEvents:l?"none":null},children:ee})}),[ne,A,ee,X]);return(0,C.jsx)("div",_(_({},z()),{},{className:"table sticky",style:{width:M},children:(0,C.jsxs)("div",_(_({},G()),{},{className:"body",children:[(0,C.jsx)("div",{className:"header",ref:T,children:J.map((function(e,n){return(0,o.createElement)("div",_(_({},e.getHeaderGroupProps()),{},{className:"tr",key:"".concat(e.id,"_").concat(n)}),e.headers.map((function(e,n){var t,r=n<=S-1,i=e.getHeaderProps(),u=_({},i.style);return r?(u.fontFamily=x.Vp,u.left=0,u.position="sticky",u.textAlign="center",u.width=V[n],u.minWidth=V[n]):R?t=R(e,n-S,{width:W.width}):(t=e.render("Header"),u.color=(B||g.Z).content.default,u.padding=1*Z.iI,u.minWidth=W.width),(0,o.createElement)("div",_(_({},i),{},{className:"th",key:e.id,style:u,title:r?"Row number":void 0}),t)})))}))}),te]}))}))}var R=function(e){var n=e.columnHeaderHeight,t=e.columns,i=e.disableScrolling,u=e.height,l=e.index,c=e.invalidValues,d=e.maxHeight,s=e.noBorderBottom,a=e.noBorderLeft,p=e.noBorderRight,f=e.noBorderTop,h=e.previewIndexes,m=e.renderColumnHeader,v=e.rows,g=e.width,b=(0,o.useMemo)((function(){return null!==l&&void 0!==l&&l.length&&Array.isArray(l[0])?l[0].length:1}),[l]),y=(0,o.useMemo)((function(){return(0,P.w6)(b).map((function(e,n){return{Header:(0,P.w6)(n+1).map((function(){return" "})).join(" "),accessor:function(e,n){return n},sticky:"left"}})).concat(null===t||void 0===t?void 0:t.map((function(e){return{Header:String(e),accessor:String(e)}})))}),[t,b]);return(0,o.useMemo)((function(){return null===v||void 0===v?void 0:v.map((function(e){return e.reduce((function(e,n,i){return _(_({},e),{},(0,r.Z)({},t[i],n))}),{})}))}),[t,v]),(0,C.jsx)(S,{columnHeaderHeight:n,disableScrolling:i,height:u,maxHeight:d,noBorderBottom:s,noBorderLeft:a,noBorderRight:p,noBorderTop:f,children:(0,C.jsx)(H,{columnHeaderHeight:n,columns:y,data:v,disableScrolling:i,height:u,index:l,invalidValues:c,maxHeight:d,numberOfIndexes:b,previewIndexes:h,renderColumnHeader:m,width:g})})}},27125:function(e,n,t){"use strict";var r=t(82684),i=t(12691),o=t.n(i),u=t(34376),l=t.n(u),c=t(46313),d=t(66050),s=t(60328),a=t(16634),p=t(10919),f=t(98781),h=t(86673),m=t(17903),v=t(19711),g=t(10503),b=t(49125),y=t(44162),x=t(24224),O=t(28598);n.Z=function(e){var n=e.blockRuns,t=e.onClickRow,i=e.pipeline,u=e.selectedRun,j=(0,r.useContext)(c.ThemeContext),w=(i||{}).uuid,Z=(0,r.useMemo)((function(){return i.blocks||[]}),[i]),k=(0,r.useMemo)((function(){return(0,x.HK)(Z,(function(e){return e.uuid}))}),[Z]);return(0,O.jsx)(m.Z,{columnFlex:[null,1,3,2,null,null],columns:[{uuid:"Date"},{uuid:"Status"},{uuid:"Trigger"},{uuid:"Block"},{uuid:"Completed"},{uuid:"Logs"}],isSelectedRow:function(e){return n[e].id===(null===u||void 0===u?void 0:u.id)},onClickRow:t,rows:null===n||void 0===n?void 0:n.map((function(e){var n,t,r,u=e.block_uuid,c=e.completed_at,m=e.created_at,x=e.id,Z=e.pipeline_schedule_id,P=e.pipeline_schedule_name,C=e.status,E=u;if(f.q.INTEGRATION===i.type){var _=E.split(":");E=_[0],t=_[1],r=_[2]}return[(0,O.jsx)(v.ZP,{monospace:!0,default:!0,children:m}),(0,O.jsx)(v.ZP,{danger:d.V.FAILED===C,default:d.V.CANCELLED===C,info:d.V.INITIAL===C,monospace:!0,success:d.V.COMPLETED===C,warning:d.V.RUNNING===C,children:C}),(0,O.jsx)(o(),{as:"/pipelines/".concat(w,"/triggers/").concat(Z),href:"/pipelines/[pipeline]/triggers/[...slug]",passHref:!0,children:(0,O.jsx)(p.Z,{bold:!0,sameColorAsText:!0,children:P})}),(0,O.jsx)(o(),{as:"/pipelines/".concat(w,"/edit?block_uuid=").concat(E),href:"/pipelines/[pipeline]/edit",passHref:!0,children:(0,O.jsxs)(p.Z,{bold:!0,sameColorAsText:!0,verticalAlignContent:!0,children:[(0,O.jsx)(a.Z,{color:(0,y.qn)(null===(n=k[E])||void 0===n?void 0:n.type,{theme:j}).accent,size:1.5*b.iI,square:!0}),(0,O.jsx)(h.Z,{mr:1}),(0,O.jsxs)(v.ZP,{monospace:!0,children:[E,t&&": ",t&&(0,O.jsx)(v.ZP,{default:!0,inline:!0,monospace:!0,children:t}),r>=0&&": ",r>=0&&(0,O.jsx)(v.ZP,{default:!0,inline:!0,monospace:!0,children:r})]})]})}),(0,O.jsx)(v.ZP,{monospace:!0,default:!0,children:c||"-"}),(0,O.jsx)(s.Z,{default:!0,iconOnly:!0,noBackground:!0,onClick:function(){return l().push("/pipelines/".concat(w,"/logs?block_run_id[]=").concat(x))},children:(0,O.jsx)(g.B4,{default:!0,size:2*b.iI})})]})),uuid:"block-runs"})}},64155:function(e,n,t){"use strict";t.d(n,{Eh:function(){return c},ht:function(){return s},t0:function(){return d}});var r=t(46313),i=t(82386),o=t(32151),u=t(31012),l=t(49125),c=(l.iI,o.O$+3*l.iI+u.dN),d=r.default.div.withConfig({displayName:"indexstyle__SidekickContainerStyle",componentId:"sc-15ofupc-0"})(["position:relative;width:fit-content;"," ",""],(function(e){return"\n    height: calc(100vh - ".concat(i.uX,"px - ").concat(e.heightOffset,"px);\n  ")}),(function(e){return e.fullWidth&&"\n    width: 100%;\n  "})),s=r.default.div.withConfig({displayName:"indexstyle__PaddingContainerStyle",componentId:"sc-15ofupc-1"})(["padding:","px;",""],2*l.iI,(function(e){return e.noPadding&&"\n    padding: 0;\n  "}))},19395:function(e,n,t){"use strict";t.d(n,{IJ:function(){return s},eI:function(){return a},gU:function(){return f},tL:function(){return p},vJ:function(){return h}});var r,i,o=t(82394),u=t(92083),l=t.n(u);function c(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function d(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?c(Object(t),!0).forEach((function(n){(0,o.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):c(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e){return null===e||void 0===e?void 0:e.reduce((function(e,n){var t=n.block_uuid,r=n.completed_at,i=n.started_at,u=n.status,c=null;i&&r&&(c=l()(r).valueOf()-l()(i).valueOf());return d(d({},e),{},(0,o.Z)({},t,{runtime:c,status:u}))}),{})}function a(e){if(!e)return null;var n=new Date(l()(e).valueOf()),t=Date.UTC(n.getFullYear(),n.getMonth(),n.getDate(),n.getHours(),n.getMinutes(),n.getSeconds());return new Date(t)}!function(e){e.DAY="day",e.HOUR="hour",e.MINUTE="minute",e.SECOND="second"}(i||(i={}));var p=(r={},(0,o.Z)(r,i.DAY,86400),(0,o.Z)(r,i.HOUR,3600),(0,o.Z)(r,i.MINUTE,60),(0,o.Z)(r,i.SECOND,1),r);function f(e){var n=i.SECOND,t=e;return e%86400===0?(t/=86400,n=i.DAY):e%3600===0?(t/=3600,n=i.HOUR):e%60===0&&(t/=60,n=i.MINUTE),{time:t,unit:n}}function h(e,n){return e*p[n]}},47409:function(e,n,t){"use strict";t.d(n,{D:function(){return u},V:function(){return o}});var r,i=t(82394),o=t(66050).V,u=(r={},(0,i.Z)(r,o.CANCELLED,"Cancelled"),(0,i.Z)(r,o.COMPLETED,"Done"),(0,i.Z)(r,o.FAILED,"Failed"),(0,i.Z)(r,o.INITIAL,"Ready"),(0,i.Z)(r,o.RUNNING,"Running"),r)},23588:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return B}});var r=t(77837),i=t(12757),o=t(82394),u=t(38860),l=t.n(u),c=t(82684),d=t(83455),s=t(27125),a=t(60328),p=t(34744),f=t(87372),h=t(38965),m=t(47409),v=t(86673),g=t(41374),b=t(26304),y=t(62976),x=t(86532),O=t(67971),j=t(54283),w=t(19711),Z=t(64155),k=t(19395),P=t(28598),C=["blockRuns","columns","height","heightOffset","loadingData","pipeline","renderColumnHeader","rows","selectedRun"];function E(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function _(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?E(Object(t),!0).forEach((function(n){(0,o.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):E(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var D=t(59920),I=t(49125),S=t(96510),N=t(66653);function H(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function R(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?H(Object(t),!0).forEach((function(n){(0,o.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):H(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function M(e){var n,t=e.pipeline,r=e.pipelineRun,o=(0,c.useState)(),u=o[0],l=o[1],E=t.uuid,H=g.ZP.pipelines.detail(E).data,M=(0,c.useMemo)((function(){return R(R({},null===H||void 0===H?void 0:H.pipeline),{},{uuid:E})}),[H,E]),B=g.ZP.pipeline_runs.detail(r.id,{},{refreshInterval:3e3,revalidateOnFocus:!0}).data,T=(0,c.useMemo)((function(){return null===B||void 0===B?void 0:B.pipeline_run}),[B]),A=(0,d.Db)(g.ZP.pipeline_runs.useUpdate(null===T||void 0===T?void 0:T.id),{onSuccess:function(e){return(0,S.wD)(e,{onErrorCallback:function(e){var n=e.error,t=n.errors,r=n.message;console.log(t,r)}})}}),L=(0,i.Z)(A,2),V=L[0],U=L[1].isLoading,F=g.ZP.outputs.block_runs.list(null===u||void 0===u?void 0:u.id),W=F.data,q=F.loading,G=(F.mutate,((null===W||void 0===W||null===(n=W.outputs)||void 0===n?void 0:n[0])||{}).sample_data),z=(0,c.useMemo)((function(){return null===T||void 0===T?void 0:T.block_runs}),[T]),J=((null===G||void 0===G?void 0:G.columns)||[]).slice(0,40),Y=(null===G||void 0===G?void 0:G.rows)||[],X=(0,c.useMemo)((function(){return(0,P.jsx)(s.Z,{blockRuns:z,onClickRow:function(e){return l((function(n){var t=z[e];return(null===n||void 0===n?void 0:n.id)!==t.id?t:null}))},pipeline:M,selectedRun:u})}),[z,M,u]);return(0,P.jsxs)(h.Z,{buildSidekick:function(e){return function(e){var n=e.blockRuns,t=e.columns,r=e.height,i=e.heightOffset,o=e.loadingData,u=e.pipeline,l=e.renderColumnHeader,c=e.rows,d=e.selectedRun,s=_({},(0,b.Z)(e,C));s.blockStatus=(0,k.IJ)(n);var a=(0,P.jsx)(P.Fragment,{children:c&&c.length>0?(0,P.jsx)(y.Z,{columnHeaderHeight:l?Z.Eh:0,columns:t,height:r-i-90,noBorderBottom:!0,noBorderLeft:!0,noBorderRight:!0,renderColumnHeader:l,rows:c}):(0,P.jsx)(v.Z,{ml:2,children:(0,P.jsx)(w.ZP,{children:"This block run has no output"})})});return(0,P.jsxs)(P.Fragment,{children:[!d&&(0,P.jsx)(x.Z,_(_({},s),{},{height:r,heightOffset:i||0,pipeline:u})),d&&(0,P.jsxs)(P.Fragment,{children:[(0,P.jsx)(v.Z,{pl:2,py:3,style:{position:"fixed"},children:(0,P.jsx)(f.Z,{level:4,muted:!0,children:"Block Output"})}),(0,P.jsxs)("div",{style:{position:"relative",top:"75px"},children:[o&&(0,P.jsx)(v.Z,{mt:2,children:(0,P.jsx)(O.Z,{alignItems:"center",fullWidth:!0,justifyContent:"center",children:(0,P.jsx)(j.Z,{color:"white",large:!0})})}),!o&&a]})]})]})}(R(R({},e),{},{blockRuns:z,columns:J,loadingData:q,rows:Y,selectedRun:u}))},breadcrumbs:[{label:function(){return"Runs"},linkProps:{as:"/pipelines/".concat(E,"/runs"),href:"/pipelines/[pipeline]/runs"}},{label:function(){return null===T||void 0===T?void 0:T.execution_date}}],pageName:D.M.RUNS,pipeline:M,subheader:(null===T||void 0===T?void 0:T.status)&&T.status!==m.V.COMPLETED&&(0,P.jsx)(a.Z,{danger:!0,loading:U,onClick:function(e){(0,N.j)(e),V({pipeline_run:{action:"retry_blocks"}})},outline:!0,children:"Retry incomplete blocks"}),title:function(e){var n=e.name;return"".concat(n," runs")},uuid:"".concat(D.M.RUNS,"_").concat(E,"_").concat(null===T||void 0===T?void 0:T.id),children:[(0,P.jsx)(v.Z,{mt:I.cd,px:I.cd,children:(0,P.jsx)(f.Z,{level:5,children:"Block runs"})}),(0,P.jsx)(p.Z,{light:!0,mt:I.cd,short:!0}),X]})}M.getInitialProps=function(){var e=(0,r.Z)(l().mark((function e(n){var t,r,i;return l().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.query,r=t.pipeline,i=t.run,e.abrupt("return",{pipeline:{uuid:r},pipelineRun:{id:i}});case 2:case"end":return e.stop()}}),e)})));return function(n){return e.apply(this,arguments)}}();var B=M},39525:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pipelines/[pipeline]/runs/[run]",function(){return t(23588)}])}},function(e){e.O(0,[4259,2212,7689,6674,4804,1774,3668,2125,1374,5763,6792,1273,8965,2151,5703,9774,2888,179],(function(){return n=39525,e(e.s=n);var n}));var n=e.O();_N_E=n}]);