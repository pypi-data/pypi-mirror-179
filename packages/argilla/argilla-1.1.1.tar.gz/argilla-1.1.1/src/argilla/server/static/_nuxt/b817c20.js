(window.webpackJsonp=window.webpackJsonp||[]).push([[86,23,41,48,79,119],{1032:function(e,n,t){"use strict";t.r(n);t(59);var r=t(35),o=(t(422),t(155),t(189),{props:{limit:{type:Number,required:!0},object:{type:Object,required:!0},k:{type:String,required:!0}},computed:{sortedObject:function(){return Object.entries(this.object[this.k]).sort((function(e,n){var a=Object(r.a)(e,2)[1];return Object(r.a)(n,2)[1]-a}))}}}),c=(t(957),t(51)),component=Object(c.a)(o,(function(){var e=this,n=e._self._c;return n("ul",{staticClass:"metrics__list"},[e._l(e.sortedObject.slice(0,e.limit),(function(t,r){return n("li",{key:r},[n("label",{staticClass:"metrics__list__name"},[e._v(e._s(t[0]))]),e._v(" "),n("span",{staticClass:"metrics__list__counter"},[e._v("\n      "+e._s(e._f("formatNumber")(t[1]))+"\n    ")])])})),e._v(" "),0!==e.limit&&e.sortedObject.length>3?n("base-button",{staticClass:"secondary light small",on:{click:function(n){return e.$emit("limit",e.k)}}},[e._v(e._s(3===e.limit?"Show more":"Show less"))]):e._e()],2)}),[],!1,null,"58f6f274",null);n.default=component.exports;installComponents(component,{BaseButton:t(722).default})},721:function(e,n,t){var content=t(724);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("5c4c2564",content,!0,{sourceMap:!1})},722:function(e,n,t){"use strict";t.r(n);var r={name:"ReButton",props:{href:String,target:String,rel:String,type:{type:String,default:"button"},loading:Boolean,disabled:Boolean,centered:Boolean,to:String},computed:{newRel:function(){return"_blank"===this.target?this.rel||"noopener":this.rel},buttonClasses:function(){return{button:!0,loading:this.loading,centered:this.centered}}}},o=(t(723),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return e.href?n("a",{class:e.buttonClasses,attrs:{href:e.href,loading:e.loading,disabled:e.disabled,target:e.target,rel:e.newRel},on:{click:function(n){return e.$emit("click",n)}}},[e._t("default")],2):e.to?n("nuxt-link",{class:e.buttonClasses,attrs:{to:e.to,loading:e.loading,disabled:e.disabled},on:{click:function(n){return e.$emit("click",n)}}},[e._t("default")],2):n("button",{class:e.buttonClasses,attrs:{tabindex:"0",loading:e.loading,type:e.type,disabled:e.disabled},on:{click:function(n){return e.$emit("click",n)}}},[e._t("default")],2)}),[],!1,null,"1b8a1f64",null);n.default=component.exports},723:function(e,n,t){"use strict";t(721)},724:function(e,n,t){var r=t(124),o=t(150),c=t(151),d=t(152),l=r(!1),h=o(c),f=o(d);l.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.button[data-v-1b8a1f64]{position:relative;display:flex;align-items:center;gap:8px;min-width:auto;overflow:hidden;user-select:none;outline:0;background:none;border:0;border-radius:6px;font-style:inherit;font-variant:inherit;letter-spacing:inherit;font-weight:500;text-align:center;text-decoration:none;white-space:nowrap;font-size:14px;font-size:.875rem;line-height:14px;padding:12px 24px;transition:all .4s cubic-bezier(0.02, 0.42, 0.01, 0.51);cursor:pointer}.button[data-v-1b8a1f64]:focus{outline:0}.button[data-v-1b8a1f64]::-moz-focus-inner{border:0}[disabled].button[data-v-1b8a1f64]{opacity:.5;cursor:default;pointer-events:none}.small[data-v-1b8a1f64]{font-size:13px;font-size:.8125rem;line-height:13px;padding:9px 18px}.primary[data-v-1b8a1f64]{background-color:#3e5cc9;color:#fff}.primary .svg-icon[data-v-1b8a1f64]{fill:#fff}.primary[data-v-1b8a1f64]:hover,.primary[data-v-1b8a1f64]:active,.primary.active[data-v-1b8a1f64]{background-color:#2e48a6}.primary.outline[data-v-1b8a1f64]{background:none;border:1px solid #3e5cc9;color:#3e5cc9}.primary.outline .svg-icon[data-v-1b8a1f64]{fill:#3e5cc9}.primary.outline[data-v-1b8a1f64]:hover,.primary.outline[data-v-1b8a1f64]:active,.primary.outline.active[data-v-1b8a1f64]{color:#2e48a6;border-color:#2e48a6}.primary.light[data-v-1b8a1f64]{background:rgba(128,128,128,.04);color:#3e5cc9}.primary.light[data-v-1b8a1f64]:hover,.primary.light[data-v-1b8a1f64]:active,.primary.light.active[data-v-1b8a1f64]{background:rgba(0,0,0,.04)}.primary.link[data-v-1b8a1f64]{background:none;color:#3e5cc9}.primary.link[data-v-1b8a1f64]:hover{text-decoration:underline;background:none}.secondary[data-v-1b8a1f64]{background-color:#4d4d4d;color:#fff}.secondary .svg-icon[data-v-1b8a1f64]{fill:#fff}.secondary[data-v-1b8a1f64]:hover,.secondary[data-v-1b8a1f64]:active,.secondary.active[data-v-1b8a1f64]{background-color:#404040}.secondary.outline[data-v-1b8a1f64]{background:none;border:1px solid rgba(0,0,0,.6);color:#4d4d4d}.secondary.light[data-v-1b8a1f64]{background:rgba(128,128,128,.04);color:rgba(0,0,0,.6)}.secondary.light[data-v-1b8a1f64]:hover,.secondary.light[data-v-1b8a1f64]:active,.secondary.light.active[data-v-1b8a1f64]{background:rgba(0,0,0,.04)}.secondary.light .svg-icon[data-v-1b8a1f64]{fill:rgba(0,0,0,.6)}',""]),e.exports=l},876:function(e,n,t){var content=t(958);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("149ba37e",content,!0,{sourceMap:!1})},957:function(e,n,t){"use strict";t(876)},958:function(e,n,t){var r=t(124),o=t(150),c=t(151),d=t(152),l=r(!1),h=o(c),f=o(d);l.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.button[data-v-58f6f274]{margin-top:16px}',""]),e.exports=l}}]);