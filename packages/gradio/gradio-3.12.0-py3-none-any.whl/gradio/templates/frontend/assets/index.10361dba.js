import{S as fe,i as ce,s as de,e as E,b as y,d as D,f as C,a8 as ye,l as F,n as H,A as ge,a as j,x as X,K as Ae,I as P,t as _e,h as he,a3 as rt,B as at,g as T,O as x,c as Z,m as G,L as $,j as V,k as Y,o as Q,F as qe,aa as N,w as ve,D as ie,ab as se,ac as ue,E as oe,R as it,T as st,U as ut,V as ot}from"./index.68c8b051.js";import{U as ft}from"./Upload.c4127bdc.js";import{d as ct}from"./dsv.7fe76a93.js";var De=Object.prototype.hasOwnProperty;function ee(n,e){var t,l;if(n===e)return!0;if(n&&e&&(t=n.constructor)===e.constructor){if(t===Date)return n.getTime()===e.getTime();if(t===RegExp)return n.toString()===e.toString();if(t===Array){if((l=n.length)===e.length)for(;l--&&ee(n[l],e[l]););return l===-1}if(!t||typeof n=="object"){l=0;for(t in n)if(De.call(n,t)&&++l&&!De.call(e,t)||!(t in e)||!ee(n[t],e[t]))return!1;return Object.keys(e).length===l}}return n!==n&&e!==e}function Le(n){let e,t,l;return{c(){e=E("input"),y(e,"class","absolute outline-none inset-2 bg-transparent border-0 translate-x-px flex-1 "),y(e,"tabindex","-1"),D(e,"translate-x-px",!n[3]),D(e,"font-bold",n[3])},m(a,i){C(a,e,i),ye(e,n[0]),n[8](e),t||(l=[F(e,"input",n[7]),F(e,"keydown",n[6]),F(e,"blur",ht)],t=!0)},p(a,i){i&1&&e.value!==a[0]&&ye(e,a[0]),i&8&&D(e,"translate-x-px",!a[3]),i&8&&D(e,"font-bold",a[3])},d(a){a&&H(e),n[8](null),t=!1,ge(l)}}}function dt(n){let e;return{c(){e=_e(n[0])},m(t,l){C(t,e,l)},p(t,l){l&1&&he(e,t[0])},d(t){t&&H(e)}}}function gt(n){let e,t;return{c(){e=new rt(!1),t=at(),e.a=t},m(l,a){e.m(n[0],l,a),C(l,t,a)},p(l,a){a&1&&e.p(l[0])},d(l){l&&H(t),l&&e.d()}}}function _t(n){let e,t,l,a,i=n[2]&&Le(n);function _(s,g){return s[4]==="markdown"||s[4]==="html"?gt:dt}let h=_(n),o=h(n);return{c(){i&&i.c(),e=j(),t=E("span"),o.c(),y(t,"tabindex","-1"),y(t,"role","button"),y(t,"class","p-2 outline-none border-0 flex-1"),D(t,"opacity-0",n[2]),D(t,"pointer-events-none",n[2])},m(s,g){i&&i.m(s,g),C(s,e,g),C(s,t,g),o.m(t,null),l||(a=F(t,"dblclick",n[5]),l=!0)},p(s,[g]){s[2]?i?i.p(s,g):(i=Le(s),i.c(),i.m(e.parentNode,e)):i&&(i.d(1),i=null),h===(h=_(s))&&o?o.p(s,g):(o.d(1),o=h(s),o&&(o.c(),o.m(t,null))),g&4&&D(t,"opacity-0",s[2]),g&4&&D(t,"pointer-events-none",s[2])},i:X,o:X,d(s){i&&i.d(s),s&&H(e),s&&H(t),o.d(),l=!1,a()}}}const ht=({currentTarget:n})=>n.setAttribute("tabindex","-1");function bt(n,e,t){let{edit:l}=e,{value:a=""}=e,{el:i}=e,{header:_=!1}=e,{datatype:h="str"}=e;function o(c){Ae.call(this,n,c)}function s(c){Ae.call(this,n,c)}function g(){a=this.value,t(0,a)}function w(c){P[c?"unshift":"push"](()=>{i=c,t(1,i)})}return n.$$set=c=>{"edit"in c&&t(2,l=c.edit),"value"in c&&t(0,a=c.value),"el"in c&&t(1,i=c.el),"header"in c&&t(3,_=c.header),"datatype"in c&&t(4,h=c.datatype)},[a,i,l,_,h,o,s,g,w]}class ze extends fe{constructor(e){super(),ce(this,e,bt,_t,de,{edit:2,value:0,el:1,header:3,datatype:4})}}function Me(n,e,t){const l=n.slice();return l[52]=e[t],l[54]=t,l}function Te(n,e,t){const l=n.slice();return l[55]=e[t].value,l[56]=e[t].id,l[57]=e,l[58]=t,l}function Ee(n,e,t){const l=n.slice();return l[55]=e[t].value,l[56]=e[t].id,l[59]=e,l[54]=t,l}function Be(n){let e,t;return{c(){e=E("p"),t=_e(n[1]),y(e,"class","text-gray-600 text-[0.855rem] mb-2 block dark:text-gray-200 relative z-40")},m(l,a){C(l,e,a),T(e,t)},p(l,a){a[0]&2&&he(t,l[1])},d(l){l&&H(e)}}}function Re(n){let e,t;return{c(){e=E("caption"),t=_e(n[1]),y(e,"class","sr-only")},m(l,a){C(l,e,a),T(e,t)},p(l,a){a[0]&2&&he(t,l[1])},d(l){l&&H(e)}}}function Ce(n,e){let t,l,a,i,_,h,o,s,g,w,c,b=e[56],f,v,O;function u(S){e[30](S,e[56])}function p(){return e[31](e[56])}let M={value:e[55],edit:e[13]===e[56],header:!0};e[10][e[56]].input!==void 0&&(M.el=e[10][e[56]].input),a=new ze({props:M}),P.push(()=>x(a,"el",u)),a.$on("keydown",e[21]),a.$on("dblclick",p);function m(){return e[32](e[54])}const R=()=>e[33](t,b),z=()=>e[33](null,b);return{key:n,first:null,c(){t=E("th"),l=E("div"),Z(a.$$.fragment),_=j(),h=E("div"),o=ve("svg"),s=ve("path"),w=j(),y(s,"d","M4.49999 0L8.3971 6.75H0.602875L4.49999 0Z"),y(o,"width","1em"),y(o,"height","1em"),y(o,"class","fill-current text-[10px]"),y(o,"viewBox","0 0 9 7"),y(o,"fill","none"),y(o,"xmlns","http://www.w3.org/2000/svg"),y(h,"class",g="flex flex-none items-center justify-center p-2 cursor-pointer leading-snug transform transition-all "+(e[12]!==e[54]?"text-gray-200 hover:text-gray-500":"text-orange-500")+" "+(e[12]===e[54]&&e[11]==="des"?"-scale-y-[1]":"")),D(h,"text-gray-200",e[12]!==e[54]),y(l,"class","min-h-[2.3rem] flex outline-none"),y(t,"class","p-0 relative focus-within:ring-1 ring-orange-500 ring-inset outline-none"),y(t,"aria-sort",c=e[15](e[55],e[12],e[11])),D(t,"bg-orange-50",e[13]===e[56]),D(t,"dark:bg-transparent",e[13]===e[56]),D(t,"rounded-tl-lg",e[54]===0),D(t,"rounded-tr-lg",e[54]===e[8].length-1),this.first=t},m(S,B){C(S,t,B),T(t,l),G(a,l,null),T(l,_),T(l,h),T(h,o),T(o,s),T(t,w),R(),f=!0,v||(O=F(h,"click",m),v=!0)},p(S,B){e=S;const I={};B[0]&256&&(I.value=e[55]),B[0]&8448&&(I.edit=e[13]===e[56]),!i&&B[0]&1280&&(i=!0,I.el=e[10][e[56]].input,$(()=>i=!1)),a.$set(I),(!f||B[0]&6400&&g!==(g="flex flex-none items-center justify-center p-2 cursor-pointer leading-snug transform transition-all "+(e[12]!==e[54]?"text-gray-200 hover:text-gray-500":"text-orange-500")+" "+(e[12]===e[54]&&e[11]==="des"?"-scale-y-[1]":"")))&&y(h,"class",g),B[0]&6400&&D(h,"text-gray-200",e[12]!==e[54]),(!f||B[0]&6400&&c!==(c=e[15](e[55],e[12],e[11])))&&y(t,"aria-sort",c),b!==e[56]&&(z(),b=e[56],R()),B[0]&8448&&D(t,"bg-orange-50",e[13]===e[56]),B[0]&8448&&D(t,"dark:bg-transparent",e[13]===e[56]),B[0]&256&&D(t,"rounded-tl-lg",e[54]===0),B[0]&256&&D(t,"rounded-tr-lg",e[54]===e[8].length-1)},i(S){f||(V(a.$$.fragment,S),f=!0)},o(S){Y(a.$$.fragment,S),f=!1},d(S){S&&H(t),Q(a),z(),v=!1,O()}}}function He(n,e){let t,l,a,i,_,h=e[56],o,s,g;function w(m){e[34](m,e[55],e[57],e[58])}function c(m){e[35](m,e[56])}let b={edit:e[6]===e[56],datatype:Array.isArray(e[0])?e[0][e[58]]:e[0]};e[55]!==void 0&&(b.value=e[55]),e[10][e[56]].input!==void 0&&(b.el=e[10][e[56]].input),a=new ze({props:b}),P.push(()=>x(a,"value",w)),P.push(()=>x(a,"el",c));const f=()=>e[36](t,h),v=()=>e[36](null,h);function O(){return e[37](e[56])}function u(){return e[38](e[56])}function p(){return e[39](e[56])}function M(...m){return e[40](e[54],e[58],e[56],...m)}return{key:n,first:null,c(){t=E("td"),l=E("div"),Z(a.$$.fragment),y(l,"class","min-h-[2.3rem] h-full outline-none flex items-center"),D(l,"border-transparent",e[7]!==e[56]),y(t,"tabindex","0"),y(t,"class","outline-none focus-within:ring-1 ring-orange-500 ring-inset focus-within:bg-orange-50 dark:focus-within:bg-gray-800 group-last:first:rounded-bl-lg group-last:last:rounded-br-lg relative"),this.first=t},m(m,R){C(m,t,R),T(t,l),G(a,l,null),f(),o=!0,s||(g=[F(t,"touchstart",O,{passive:!0}),F(t,"click",u),F(t,"dblclick",p),F(t,"keydown",M)],s=!0)},p(m,R){e=m;const z={};R[0]&576&&(z.edit=e[6]===e[56]),R[0]&513&&(z.datatype=Array.isArray(e[0])?e[0][e[58]]:e[0]),!i&&R[0]&512&&(i=!0,z.value=e[55],$(()=>i=!1)),!_&&R[0]&1536&&(_=!0,z.el=e[10][e[56]].input,$(()=>_=!1)),a.$set(z),R[0]&640&&D(l,"border-transparent",e[7]!==e[56]),h!==e[56]&&(v(),h=e[56],f())},i(m){o||(V(a.$$.fragment,m),o=!0)},o(m){Y(a.$$.fragment,m),o=!1},d(m){m&&H(t),Q(a),v(),s=!1,ge(g)}}}function Oe(n,e){let t,l=[],a=new Map,i,_,h=e[52];const o=s=>s[56];for(let s=0;s<h.length;s+=1){let g=Te(e,h,s),w=o(g);a.set(w,l[s]=He(w,g))}return{key:n,first:null,c(){t=E("tr");for(let s=0;s<l.length;s+=1)l[s].c();i=j(),y(t,"class","group border-b dark:border-gray-700 last:border-none divide-x dark:divide-gray-700 space-x-4 odd:bg-gray-50 dark:odd:bg-gray-900 group focus:bg-gradient-to-b focus:from-blue-100 dark:focus:from-blue-900 focus:to-blue-50 dark:focus:to-gray-900 focus:odd:bg-white"),this.first=t},m(s,g){C(s,t,g);for(let w=0;w<l.length;w+=1)l[w].m(t,null);T(t,i),_=!0},p(s,g){e=s,g[0]&460481&&(h=e[52],ie(),l=se(l,g,o,1,e,h,a,t,ue,He,i,Te),oe())},i(s){if(!_){for(let g=0;g<h.length;g+=1)V(l[g]);_=!0}},o(s){for(let g=0;g<l.length;g+=1)Y(l[g]);_=!1},d(s){s&&H(t);for(let g=0;g<l.length;g+=1)l[g].d()}}}function mt(n){let e,t,l,a,i=[],_=new Map,h,o,s=[],g=new Map,w,c=n[1]&&n[1].length!==0&&Re(n),b=n[8];const f=u=>u[56];for(let u=0;u<b.length;u+=1){let p=Ee(n,b,u),M=f(p);_.set(M,i[u]=Ce(M,p))}let v=n[9];const O=u=>u[52];for(let u=0;u<v.length;u+=1){let p=Me(n,v,u),M=O(p);g.set(M,s[u]=Oe(M,p))}return{c(){e=E("table"),c&&c.c(),t=j(),l=E("thead"),a=E("tr");for(let u=0;u<i.length;u+=1)i[u].c();h=j(),o=E("tbody");for(let u=0;u<s.length;u+=1)s[u].c();y(a,"class","border-b dark:border-gray-700 divide-x dark:divide-gray-700 text-left"),y(l,"class","sticky top-0 left-0 right-0 bg-white shadow-sm z-10"),y(o,"class","overflow-y-scroll"),y(e,"class","table-auto font-mono w-full text-gray-900 text-sm transition-opacity overflow-hidden"),D(e,"opacity-40",n[14])},m(u,p){C(u,e,p),c&&c.m(e,null),T(e,t),T(e,l),T(l,a);for(let M=0;M<i.length;M+=1)i[M].m(a,null);T(e,h),T(e,o);for(let M=0;M<s.length;M+=1)s[M].m(o,null);w=!0},p(u,p){u[1]&&u[1].length!==0?c?c.p(u,p):(c=Re(u),c.c(),c.m(e,t)):c&&(c.d(1),c=null),p[0]&3718400&&(b=u[8],ie(),i=se(i,p,f,1,u,b,_,a,ue,Ce,null,Ee),oe()),p[0]&460481&&(v=u[9],ie(),s=se(s,p,O,1,u,v,g,o,ue,Oe,null,Me),oe()),p[0]&16384&&D(e,"opacity-40",u[14])},i(u){if(!w){for(let p=0;p<b.length;p+=1)V(i[p]);for(let p=0;p<v.length;p+=1)V(s[p]);w=!0}},o(u){for(let p=0;p<i.length;p+=1)Y(i[p]);for(let p=0;p<s.length;p+=1)Y(s[p]);w=!1},d(u){u&&H(e),c&&c.d();for(let p=0;p<i.length;p+=1)i[p].d();for(let p=0;p<s.length;p+=1)s[p].d()}}}function Se(n){let e,t,l=n[3][1]==="dynamic"&&Fe(n),a=n[2][1]==="dynamic"&&Ue(n);return{c(){e=E("div"),l&&l.c(),t=j(),a&&a.c(),y(e,"class","flex justify-end space-x-1 pt-2 text-gray-800")},m(i,_){C(i,e,_),l&&l.m(e,null),T(e,t),a&&a.m(e,null)},p(i,_){i[3][1]==="dynamic"?l?l.p(i,_):(l=Fe(i),l.c(),l.m(e,t)):l&&(l.d(1),l=null),i[2][1]==="dynamic"?a?a.p(i,_):(a=Ue(i),a.c(),a.m(e,null)):a&&(a.d(1),a=null)},d(i){i&&H(e),l&&l.d(),a&&a.d()}}}function Fe(n){let e,t,l;return{c(){e=E("button"),e.innerHTML='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1 group-hover:text-orange-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M24.59 16.59L17 24.17V4h-2v20.17l-7.59-7.58L6 18l10 10l10-10l-1.41-1.41z"></path></svg>New row',y(e,"class","!flex-none gr-button group")},m(a,i){C(a,e,i),t||(l=F(e,"click",n[43]),t=!0)},p:X,d(a){a&&H(e),t=!1,l()}}}function Ue(n){let e,t,l;return{c(){e=E("button"),e.innerHTML=`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1 group-hover:text-orange-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="m18 6l-1.43 1.393L24.15 15H4v2h20.15l-7.58 7.573L18 26l10-10L18 6z"></path></svg>
					New column`,y(e,"class","!flex-none gr-button group")},m(a,i){C(a,e,i),t||(l=F(e,"click",n[23]),t=!0)},p:X,d(a){a&&H(e),t=!1,l()}}}function pt(n){let e,t,l,a,i,_,h,o,s,g=n[1]&&n[1].length!==0&&Be(n);function w(f){n[41](f)}let c={flex:!1,center:!1,boundedheight:!1,disable_click:!0,$$slots:{default:[mt]},$$scope:{ctx:n}};n[14]!==void 0&&(c.dragging=n[14]),a=new ft({props:c}),P.push(()=>x(a,"dragging",w)),a.$on("load",n[42]);let b=n[4]&&Se(n);return{c(){e=E("div"),g&&g.c(),t=j(),l=E("div"),Z(a.$$.fragment),_=j(),b&&b.c(),y(l,"class","scroll-hide overflow-hidden rounded-lg relative border transition-colors overflow-x-scroll"),D(l,"border-green-400",n[14]),D(l,"whitespace-nowrap",!n[5]),D(e,"mt-6",n[1]&&n[1].length!==0)},m(f,v){C(f,e,v),g&&g.m(e,null),T(e,t),T(e,l),G(a,l,null),T(e,_),b&&b.m(e,null),h=!0,o||(s=[F(window,"click",n[24]),F(window,"touchstart",n[24])],o=!0)},p(f,v){f[1]&&f[1].length!==0?g?g.p(f,v):(g=Be(f),g.c(),g.m(e,t)):g&&(g.d(1),g=null);const O={};v[0]&32707|v[1]&536870912&&(O.$$scope={dirty:v,ctx:f}),!i&&v[0]&16384&&(i=!0,O.dragging=f[14],$(()=>i=!1)),a.$set(O),v[0]&16384&&D(l,"border-green-400",f[14]),v[0]&32&&D(l,"whitespace-nowrap",!f[5]),f[4]?b?b.p(f,v):(b=Se(f),b.c(),b.m(e,null)):b&&(b.d(1),b=null),v[0]&2&&D(e,"mt-6",f[1]&&f[1].length!==0)},i(f){h||(V(a.$$.fragment,f),h=!0)},o(f){Y(a.$$.fragment,f),h=!1},d(f){f&&H(e),g&&g.d(),Q(a),b&&b.d(),o=!1,ge(s)}}}function kt(n,e){return e.filter(t);function t(l){var a=-1;return n.split(`
`).every(i);function i(_){if(!_)return!0;var h=_.split(l).length;return a<0&&(a=h),a===h&&h>1}}}function wt(n){const e=atob(n.split(",")[1]),t=n.split(",")[0].split(":")[1].split(";")[0],l=new ArrayBuffer(e.length),a=new Uint8Array(l);for(let i=0;i<e.length;i++)a[i]=e.charCodeAt(i);return new Blob([l],{type:t})}function yt(n,e,t){let{datatype:l}=e,{label:a=null}=e,{headers:i=[]}=e,{values:_=[[]]}=e,{col_count:h}=e,{row_count:o}=e,{editable:s=!0}=e,{wrap:g=!1}=e;const w=qe();let c=!1,b=!1,f={};function v(r){let d=r||[];if(h[1]==="fixed"&&d.length<h[0]){const k=Array(h[0]-d.length).fill("").map((A,L)=>`${L+d.length}`);d=d.concat(k)}return!d||d.length===0?Array(h[0]).fill(0).map((k,A)=>{const L=`h-${A}`;return t(10,f[L]={cell:null,input:null},f),{id:L,value:JSON.stringify(A+1)}}):d.map((k,A)=>{const L=`h-${A}`;return t(10,f[L]={cell:null,input:null},f),{id:L,value:k??""}})}function O(r){const d=r.length>0?r.length:o[0];return Array(o[1]==="fixed"||d<o[0]?o[0]:d).fill(0).map((k,A)=>Array(h[1]==="fixed"?h[0]:r[0].length).fill(0).map((L,q)=>{const K=`${A}-${q}`;return t(10,f[K]={input:null,cell:null},f),{value:r?.[A]?.[q]??"",id:K}}))}let u=v(i),p;async function M(){typeof c=="string"?(await N(),f[c]?.input?.focus()):typeof b=="string"&&(await N(),f[b]?.input?.focus())}let m=[[]],R;function z(r,d,k){if(!d)return"none";if(i[d]===r){if(k==="asc")return"ascending";if(k==="des")return"descending"}}function S(r){return m.reduce((d,k,A)=>{const L=k.reduce((q,K,re)=>r===K.id?re:q,-1);return L===-1?d:[A,L]},[-1,-1])}async function B(r,d){if(!s||c===r)return;if(d){const[A,L]=S(r);t(9,m[A][L].value="",m)}t(6,c=r),await N();const{input:k}=f[r];k?.focus()}async function I(r,d,k,A){let L;switch(r.key){case"ArrowRight":if(c)break;r.preventDefault(),L=m[d][k+1],t(7,b=L?L.id:b);break;case"ArrowLeft":if(c)break;r.preventDefault(),L=m[d][k-1],t(7,b=L?L.id:b);break;case"ArrowDown":if(c)break;r.preventDefault(),L=m[d+1],t(7,b=L?L[k].id:b);break;case"ArrowUp":if(c)break;r.preventDefault(),L=m[d-1],t(7,b=L?L[k].id:b);break;case"Escape":if(!s)break;r.preventDefault(),t(7,b=c),t(6,c=!1);break;case"Enter":if(!s)break;if(r.preventDefault(),r.shiftKey){le(d),await N();const[nt]=S(A);t(7,b=m[nt+1][k].id)}else c===A?t(6,c=!1):B(A);break;case"Backspace":if(!s)break;c||(r.preventDefault(),t(9,m[d][k].value="",m));break;case"Delete":if(!s)break;c||(r.preventDefault(),t(9,m[d][k].value="",m));break;case"Tab":let q=r.shiftKey?-1:1,K=m[d][k+q],re=m?.[d+q]?.[q>0?0:u.length-1],ae=K||re;ae&&(r.preventDefault(),t(7,b=ae?ae.id:b)),t(6,c=!1);break;default:(!c||c&&c!==A)&&r.key.length===1&&B(A,!0);break}}async function be(r){c!==r&&b!==r&&(t(6,c=!1),t(7,b=r))}async function me(r,d){if(d==="edit"&&typeof r=="string"&&(await N(),f[r].input?.focus()),d==="edit"&&typeof r=="boolean"&&typeof b=="string"){let k=f[b]?.cell;await N(),k?.focus()}if(d==="select"&&typeof r=="string"){const{cell:k}=f[r];await N(),k?.focus()}}let J,W;function Ne(r,d){d==="asc"?t(9,m=m.sort((k,A)=>k[r].value<A[r].value?-1:1)):d==="des"&&t(9,m=m.sort((k,A)=>k[r].value>A[r].value?-1:1))}function pe(r){typeof W!="number"||W!==r?(t(11,J="asc"),t(12,W=r)):J==="asc"?t(11,J="des"):J==="des"&&t(11,J="asc"),Ne(r,J)}let U;function ke(){if(typeof b=="string"){const r=f[b].input?.value;if(u.find(d=>d.id===b)){let d=u.find(k=>k.id===b);r&&(d.value=r)}else r&&u.push({id:b,value:r})}}async function te(r,d){!s||h[1]!=="dynamic"||c===r||(t(13,U=r),await N(),f[r].input?.focus(),d&&f[r].input?.select())}function je(r){if(!!s)switch(r.key){case"Escape":case"Enter":case"Tab":r.preventDefault(),t(7,b=U),t(13,U=!1),ke();break}}function le(r){o[1]==="dynamic"&&(m.splice(r?r+1:m.length,0,Array(m[0].length).fill(0).map((d,k)=>{const A=`${m.length}-${k}`;return t(10,f[A]={cell:null,input:null},f),{id:A,value:""}})),t(9,m),t(27,_),t(29,R),t(26,i))}async function Ke(){if(h[1]!=="dynamic")return;for(let d=0;d<m.length;d++){const k=`${d}-${m[d].length}`;t(10,f[k]={cell:null,input:null},f),m[d].push({id:k,value:""})}const r=`h-${u.length}`;t(10,f[r]={cell:null,input:null},f),u.push({id:r,value:`Header ${u.length+1}`}),t(9,m),t(27,_),t(29,R),t(26,i),t(8,u),t(26,i),t(28,p),t(27,_),await N(),te(r,!0)}function Ve(r){typeof c=="string"&&f[c]&&f[c].cell!==r.target&&!f[c].cell?.contains(r?.target)&&t(6,c=!1),typeof U=="string"&&f[U]&&f[U].cell!==r.target&&!f[U].cell?.contains(r.target)&&(t(7,b=U),t(13,U=!1),ke(),t(13,U=!1))}function we(r){const d=new FileReader;function k(A){if(!A?.target?.result||typeof A.target.result!="string")return;const[L]=kt(A.target.result,[",","	"]),[q,...K]=ct(L).parseRows(A.target.result);t(8,u=v(h[1]==="fixed"?q.slice(0,h[0]):q)),t(27,_=K),d.removeEventListener("loadend",k)}d.addEventListener("loadend",k),d.readAsText(r)}let ne=!1;function Ye(r,d){n.$$.not_equal(f[d].input,r)&&(f[d].input=r,t(10,f))}const Ie=r=>te(r),Je=r=>pe(r);function Pe(r,d){P[r?"unshift":"push"](()=>{f[d].cell=r,t(10,f)})}function Ze(r,d,k,A){k[A].value=r,t(9,m),t(27,_),t(29,R),t(26,i)}function Ge(r,d){n.$$.not_equal(f[d].input,r)&&(f[d].input=r,t(10,f))}function Qe(r,d){P[r?"unshift":"push"](()=>{f[d].cell=r,t(10,f)})}const We=r=>B(r),Xe=r=>be(r),xe=r=>B(r),$e=(r,d,k,A)=>I(A,r,d,k);function et(r){ne=r,t(14,ne)}const tt=r=>we(wt(r.detail.data)),lt=()=>le();return n.$$set=r=>{"datatype"in r&&t(0,l=r.datatype),"label"in r&&t(1,a=r.label),"headers"in r&&t(26,i=r.headers),"values"in r&&t(27,_=r.values),"col_count"in r&&t(2,h=r.col_count),"row_count"in r&&t(3,o=r.row_count),"editable"in r&&t(4,s=r.editable),"wrap"in r&&t(5,g=r.wrap)},n.$$.update=()=>{n.$$.dirty[0]&201326592&&(_&&!Array.isArray(_)?(t(26,i=_.headers),t(27,_=_.data.length===0?[Array(i.length).fill("")]:_.data)):_===null?t(27,_=[Array(i.length).fill("")]):(t(27,_),t(26,i))),n.$$.dirty[0]&335544320&&(ee(i,p)||(t(8,u=v(i)),t(28,p=i),M())),n.$$.dirty[0]&671088640&&(ee(_,R)||(t(9,m=O(_)),t(29,R=_),M())),n.$$.dirty[0]&768&&u&&w("change",{data:m.map(r=>r.map(({value:d})=>d)),headers:u.map(r=>r.value)}),n.$$.dirty[0]&64&&me(c,"edit"),n.$$.dirty[0]&128&&me(b,"select")},[l,a,h,o,s,g,c,b,u,m,f,J,W,U,ne,z,B,I,be,pe,te,je,le,Ke,Ve,we,i,_,p,R,Ye,Ie,Je,Pe,Ze,Ge,Qe,We,Xe,xe,$e,et,tt,lt]}class At extends fe{constructor(e){super(),ce(this,e,yt,pt,de,{datatype:0,label:1,headers:26,values:27,col_count:2,row_count:3,editable:4,wrap:5},null,[-1,-1])}}function vt(n){let e,t,l,a,i;const _=[n[10]];let h={};for(let o=0;o<_.length;o+=1)h=it(h,_[o]);return t=new st({props:h}),a=new At({props:{label:n[7],row_count:n[6],col_count:n[5],values:n[0],headers:n[1],editable:n[4]==="dynamic",wrap:n[8],datatype:n[9]}}),a.$on("change",n[12]),{c(){e=E("div"),Z(t.$$.fragment),l=j(),Z(a.$$.fragment),y(e,"id",n[2]),y(e,"class","relative overflow-hidden"),D(e,"!hidden",!n[3])},m(o,s){C(o,e,s),G(t,e,null),T(e,l),G(a,e,null),i=!0},p(o,[s]){const g=s&1024?ut(_,[ot(o[10])]):{};t.$set(g);const w={};s&128&&(w.label=o[7]),s&64&&(w.row_count=o[6]),s&32&&(w.col_count=o[5]),s&1&&(w.values=o[0]),s&2&&(w.headers=o[1]),s&16&&(w.editable=o[4]==="dynamic"),s&256&&(w.wrap=o[8]),s&512&&(w.datatype=o[9]),a.$set(w),(!i||s&4)&&y(e,"id",o[2]),s&8&&D(e,"!hidden",!o[3])},i(o){i||(V(t.$$.fragment,o),V(a.$$.fragment,o),i=!0)},o(o){Y(t.$$.fragment,o),Y(a.$$.fragment,o),i=!1},d(o){o&&H(e),Q(t),Q(a)}}}function Dt(n,e,t){let{headers:l=[]}=e,{elem_id:a=""}=e,{visible:i=!0}=e,{value:_={data:[["","",""]],headers:["1","2","3"]}}=e,{mode:h}=e,{col_count:o}=e,{row_count:s}=e,{label:g=null}=e,{wrap:w}=e,{datatype:c}=e;const b=qe();let{loading_status:f}=e;async function v(u){t(0,_=u),await N(),b("change",u)}const O=({detail:u})=>v(u);return n.$$set=u=>{"headers"in u&&t(1,l=u.headers),"elem_id"in u&&t(2,a=u.elem_id),"visible"in u&&t(3,i=u.visible),"value"in u&&t(0,_=u.value),"mode"in u&&t(4,h=u.mode),"col_count"in u&&t(5,o=u.col_count),"row_count"in u&&t(6,s=u.row_count),"label"in u&&t(7,g=u.label),"wrap"in u&&t(8,w=u.wrap),"datatype"in u&&t(9,c=u.datatype),"loading_status"in u&&t(10,f=u.loading_status)},[_,l,a,i,h,o,s,g,w,c,f,v,O]}class Lt extends fe{constructor(e){super(),ce(this,e,Dt,vt,de,{headers:1,elem_id:2,visible:3,value:0,mode:4,col_count:5,row_count:6,label:7,wrap:8,datatype:9,loading_status:10})}}var Bt=Lt;const Rt=["static","dynamic"],Ct=n=>({type:" { data: Array<Array<string | number>>; headers: Array<string> }",description:"hex color code",example_data:n.value??"#000000"});export{Bt as Component,Ct as document,Rt as modes};
//# sourceMappingURL=index.10361dba.js.map
