(window.webpackJsonp=window.webpackJsonp||[]).push([[118],{1012:function(e,n,t){"use strict";t.r(n);t(47),t(41),t(39),t(15),t(57),t(31),t(58);var r=t(22),o=t(1),c=(t(59),t(32),t(99));t(895),t(896);function l(object,e){var n=Object.keys(object);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(object);e&&(t=t.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),n.push.apply(n,t)}return n}function h(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?l(Object(source),!0).forEach((function(n){Object(r.a)(e,n,source[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):l(Object(source)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(source,n))}))}return e}var d={data:function(){return{visibleSelector:!1,appVersion:void 0}},computed:{user:function(){return this.$auth.user}},fetch:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return n.next=2,e.getAppVersion();case 2:e.appVersion=n.sent;case 3:case"end":return n.stop()}}),n)})))()},methods:h(h({},Object(c.b)({getAppVersion:"entities/rubrix-info/getAppVersion"})),{},{firstChar:function(e){return e.slice(0,2)},showSelector:function(){this.visibleSelector=!this.visibleSelector},close:function(){this.visibleSelector=!1},logout:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return n.next=2,e.$auth.logout();case 2:return n.next=4,e.$auth.strategy.token.reset();case 4:case"end":return n.stop()}}),n)})))()}})},f=(t(897),t(51)),component=Object(f.a)(d,(function(){var e=this,n=e._self._c;return e.$auth.loggedIn?n("div",{directives:[{name:"click-outside",rawName:"v-click-outside",value:e.close,expression:"close"}],staticClass:"user"},[n("a",{staticClass:"user__button",attrs:{href:"#"},on:{click:function(n){return n.preventDefault(),e.showSelector.apply(null,arguments)}}},[e._v("\n    "+e._s(e.firstChar(e.user.username))+"\n  ")]),e._v(" "),e.visibleSelector&&e.user?n("div",{staticClass:"user__content"},[n("p",{staticClass:"user__name"},[e._v(e._s(e.user.username))]),e._v(" "),n("p",{staticClass:"user__mail"},[e._v(e._s(e.user.email))]),e._v(" "),n("a",{staticClass:"user__link",attrs:{href:"https://docs.argilla.io/en/latest/",target:"_blank"}},[n("svgicon",{attrs:{width:"16",height:"16",name:"external"}}),e._v(" View docs\n    ")],1),e._v(" "),n("a",{staticClass:"user__link",attrs:{href:"#"},on:{click:function(n){return n.preventDefault(),e.logout.apply(null,arguments)}}},[n("svgicon",{attrs:{width:"16",heigth:"16",name:"log-out"}}),e._v(" Log out\n    ")],1),e._v(" "),n("span",{staticClass:"copyright"},[e._v("© 2022 Argilla ("+e._s(e.appVersion)+")")])]):e._e()]):e._e()}),[],!1,null,null,null);n.default=component.exports},828:function(e,n,t){var content=t(898);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("60b22f6c",content,!0,{sourceMap:!1})},895:function(e,n,t){t(153).register({external:{width:41,height:40,viewBox:"0 0 41 40",data:'<path pid="0" d="M23.57 26.615l2.651 2.652 9.279-9.28-9.279-9.278-2.65 2.651 4.683 4.684H12.998A7.498 7.498 0 005.5 25.542v3.75h3.75v-3.75a3.75 3.75 0 013.748-3.75h15.395l-4.823 4.823z" _fill="#000"/>'}})},896:function(e,n,t){t(153).register({"log-out":{width:41,height:40,viewBox:"0 0 41 40",data:'<path pid="0" d="M26.012 32.65h6.325a3.163 3.163 0 003.163-3.162V10.512a3.163 3.163 0 00-3.163-3.163h-6.325v3.163h6.325v18.976h-6.325v3.163z" _fill="#000"/><path pid="1" d="M17.587 28.515l-2.245-2.226 6.197-6.25H7.081a1.581 1.581 0 110-3.164H21.57l-6.295-6.24 2.227-2.246 10.106 10.02-10.02 10.106z" _fill="#000"/>'}})},897:function(e,n,t){"use strict";t(828)},898:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),h=r(!1),d=o(c),f=o(l);h.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+d+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.user__button{height:34px;width:34px;line-height:34px;display:block;text-align:center;text-transform:uppercase;border-radius:50%;text-decoration:none;font-weight:500;font-size:16px;font-size:1rem}.user{position:relative;z-index:3}.user__button{background:#ff675f;transform:scale3d(1, 1, 1) translateZ(0);transition:all .2s ease-in-out;color:#fff;will-change:auto}.user__button:hover{transform:scale3d(1.05, 1.05, 1.05) translateZ(0);transition:all .2s ease-in-out;outline:0;border:none}.user__content{position:absolute;top:3.8em;right:-0.5em;padding-top:1.5em;background:#212121;border-radius:5px;font-size:14px;font-size:.875rem;font-weight:400;color:#fff;box-shadow:0 8px 20px 0 rgba(0,0,0,.2);min-width:260px}.user__content:after{position:absolute;top:-10px;right:1em;content:"";display:block;width:0;height:0;border-style:solid;border-width:0 10px 10px 10px;border-color:rgba(0,0,0,0) rgba(0,0,0,0) #212121 rgba(0,0,0,0)}.user__content a{text-decoration:none}.user__name{font-size:16px;font-size:1rem;margin:0 1.5em .3em 1.5em;font-weight:600}.user__mail{margin:0 1.5em 2em 1.5em;color:#f8c0a7}.user__link{display:flex;align-items:center;margin:.5em 1.5em 1.5em 1.5em;color:#fff}.user__link:hover{color:#e6e6e6}.user__link:hover .svg-icon{fill:#e6e6e6}.user__link .svg-icon{margin-right:.5em}.copyright{display:block;font-size:11px;font-size:.6875rem;font-weight:400;line-height:1em;margin-top:1.5em;padding:1em;background:rgba(0,0,0,.6);text-align:right;border-bottom-right-radius:5px;border-bottom-left-radius:5px}',""]),e.exports=h}}]);