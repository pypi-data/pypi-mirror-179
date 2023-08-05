import{S as B,i as M,s as L,w as T,b as _,f as g,g as p,x as v,n as b,e as w,a as k,a3 as V,C as z,F as A,a4 as D,a5 as E,I,a6 as j,P as q,c as y,m as C,j as h,k as d,o as H,R as F,T as K,U as N,V as O,D as P,E as Y,K as Z}from"./index.68c8b051.js";import{B as G}from"./BlockLabel.8f427405.js";function J(n){let e,s,t;return{c(){e=T("svg"),s=T("path"),t=T("path"),_(s,"fill","currentColor"),_(s,"d","M17.74 30L16 29l4-7h6a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h9v2H6a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4h20a4 4 0 0 1 4 4v12a4 4 0 0 1-4 4h-4.84Z"),_(t,"fill","currentColor"),_(t,"d","M8 10h16v2H8zm0 6h10v2H8z"),_(e,"xmlns","http://www.w3.org/2000/svg"),_(e,"xmlns:xlink","http://www.w3.org/1999/xlink"),_(e,"aria-hidden","true"),_(e,"role","img"),_(e,"class","iconify iconify--carbon"),_(e,"width","100%"),_(e,"height","100%"),_(e,"preserveAspectRatio","xMidYMid meet"),_(e,"viewBox","0 0 32 32")},m(a,l){g(a,e,l),p(e,s),p(e,t)},p:v,i:v,o:v,d(a){a&&b(e)}}}class Q extends B{constructor(e){super(),M(this,e,null,J,L,{})}}function R(n,e,s){const t=n.slice();return t[9]=e[s],t}function S(n){let e,s=n[9][0]+"",t,a,l,f,r=n[9][1]+"",c,o;return{c(){e=w("div"),a=k(),l=w("div"),f=new V(!1),c=k(),_(e,"data-testid","user"),_(e,"class","px-3 py-2 rounded-[22px] rounded-br-none text-white text-sm chat-message svelte-rct66g"),_(e,"style",t="background-color:"+n[2][0]),f.a=c,_(l,"data-testid","bot"),_(l,"class","px-3 py-2 rounded-[22px] rounded-bl-none place-self-start text-white text-sm chat-message svelte-rct66g"),_(l,"style",o="background-color:"+n[2][1])},m(u,m){g(u,e,m),e.innerHTML=s,g(u,a,m),g(u,l,m),f.m(r,l),p(l,c)},p(u,m){m&1&&s!==(s=u[9][0]+"")&&(e.innerHTML=s),m&4&&t!==(t="background-color:"+u[2][0])&&_(e,"style",t),m&1&&r!==(r=u[9][1]+"")&&f.p(r),m&4&&o!==(o="background-color:"+u[2][1])&&_(l,"style",o)},d(u){u&&b(e),u&&b(a),u&&b(l)}}}function W(n){let e,s,t=n[0],a=[];for(let l=0;l<t.length;l+=1)a[l]=S(R(n,t,l));return{c(){e=w("div"),s=w("div");for(let l=0;l<a.length;l+=1)a[l].c();_(s,"class","flex flex-col items-end space-y-4 p-3"),_(e,"class","overflow-y-auto h-[40vh]")},m(l,f){g(l,e,f),p(e,s);for(let r=0;r<a.length;r+=1)a[r].m(s,null);n[4](e)},p(l,[f]){if(f&5){t=l[0];let r;for(r=0;r<t.length;r+=1){const c=R(l,t,r);a[r]?a[r].p(c,f):(a[r]=S(c),a[r].c(),a[r].m(s,null))}for(;r<a.length;r+=1)a[r].d(1);a.length=t.length}},i:v,o:v,d(l){l&&b(e),z(a,l),n[4](null)}}}function X(n,e,s){let t,{value:a}=e,{style:l={}}=e,f,r;const c=A();D(()=>{r=f&&f.offsetHeight+f.scrollTop>f.scrollHeight-20}),E(()=>{r&&f.scrollTo(0,f.scrollHeight)});function o(i){return i in j?j[i].primary:i}function u(){return l.color_map?[o(l.color_map[0]),o(l.color_map[1])]:["#fb923c","#9ca3af"]}function m(i){I[i?"unshift":"push"](()=>{f=i,s(1,f)})}return n.$$set=i=>{"value"in i&&s(0,a=i.value),"style"in i&&s(3,l=i.style)},n.$$.update=()=>{n.$$.dirty&1&&a&&c("change")},s(2,t=u()),[a,f,t,l,m]}class x extends B{constructor(e){super(),M(this,e,X,W,L,{value:0,style:3})}}function U(n){let e,s;return e=new G({props:{show_label:n[5],Icon:Q,label:n[4]||"Chatbot",disable:typeof n[0].container=="boolean"&&!n[0].container}}),{c(){y(e.$$.fragment)},m(t,a){C(e,t,a),s=!0},p(t,a){const l={};a&32&&(l.show_label=t[5]),a&16&&(l.label=t[4]||"Chatbot"),a&1&&(l.disable=typeof t[0].container=="boolean"&&!t[0].container),e.$set(l)},i(t){s||(h(e.$$.fragment,t),s=!0)},o(t){d(e.$$.fragment,t),s=!1},d(t){H(e,t)}}}function $(n){let e,s,t,a,l;const f=[n[6]];let r={};for(let o=0;o<f.length;o+=1)r=F(r,f[o]);e=new K({props:r});let c=n[5]&&U(n);return a=new x({props:{style:n[0],value:n[3]}}),a.$on("change",n[8]),{c(){y(e.$$.fragment),s=k(),c&&c.c(),t=k(),y(a.$$.fragment)},m(o,u){C(e,o,u),g(o,s,u),c&&c.m(o,u),g(o,t,u),C(a,o,u),l=!0},p(o,u){const m=u&64?N(f,[O(o[6])]):{};e.$set(m),o[5]?c?(c.p(o,u),u&32&&h(c,1)):(c=U(o),c.c(),h(c,1),c.m(t.parentNode,t)):c&&(P(),d(c,1,1,()=>{c=null}),Y());const i={};u&1&&(i.style=o[0]),u&8&&(i.value=o[3]),a.$set(i)},i(o){l||(h(e.$$.fragment,o),h(c),h(a.$$.fragment,o),l=!0)},o(o){d(e.$$.fragment,o),d(c),d(a.$$.fragment,o),l=!1},d(o){H(e,o),o&&b(s),c&&c.d(o),o&&b(t),H(a,o)}}}function ee(n){let e,s;return e=new q({props:{padding:!1,elem_id:n[1],visible:n[2],$$slots:{default:[$]},$$scope:{ctx:n}}}),{c(){y(e.$$.fragment)},m(t,a){C(e,t,a),s=!0},p(t,[a]){const l={};a&2&&(l.elem_id=t[1]),a&4&&(l.visible=t[2]),a&633&&(l.$$scope={dirty:a,ctx:t}),e.$set(l)},i(t){s||(h(e.$$.fragment,t),s=!0)},o(t){d(e.$$.fragment,t),s=!1},d(t){H(e,t)}}}function te(n,e,s){let{elem_id:t=""}=e,{visible:a=!0}=e,{value:l=[]}=e,{style:f={}}=e,{label:r}=e,{show_label:c=!0}=e,{color_map:o={}}=e,{loading_status:u}=e;function m(i){Z.call(this,n,i)}return n.$$set=i=>{"elem_id"in i&&s(1,t=i.elem_id),"visible"in i&&s(2,a=i.visible),"value"in i&&s(3,l=i.value),"style"in i&&s(0,f=i.style),"label"in i&&s(4,r=i.label),"show_label"in i&&s(5,c=i.show_label),"color_map"in i&&s(7,o=i.color_map),"loading_status"in i&&s(6,u=i.loading_status)},n.$$.update=()=>{n.$$.dirty&129&&!f.color_map&&Object.keys(o).length&&s(0,f.color_map=o,f)},[f,t,a,l,r,c,u,o,m]}class le extends B{constructor(e){super(),M(this,e,te,ee,L,{elem_id:1,visible:2,value:3,style:0,label:4,show_label:5,color_map:7,loading_status:6})}}var ne=le;const oe=["static"],ie=n=>({type:"Array<[string, string]>",description:"Represents list of message pairs of chat message.",example_data:n.value??[["Hi","Hello"],["1 + 1","2"]]});export{ne as Component,ie as document,oe as modes};
//# sourceMappingURL=index.05edb9d4.js.map
