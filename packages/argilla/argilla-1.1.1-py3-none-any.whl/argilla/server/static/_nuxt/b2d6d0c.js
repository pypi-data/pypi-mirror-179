(window.webpackJsonp=window.webpackJsonp||[]).push([[60],{758:function(e,n,t){var content=t(814);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("24aedcee",content,!0,{sourceMap:!1})},813:function(e,n,t){"use strict";t(758)},814:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.pill[data-v-69bac0c3]{display:flex;align-items:center;width:auto;background:rgba(0,0,0,0);height:40px;line-height:40px;color:#fff;border-radius:10px;padding:8px 16px;font-size:14px;font-size:.875rem;border:1px solid rgba(0,0,0,0);margin:3.5px;font-weight:500}.pill[data-v-69bac0c3]{border:1px solid #e6e6e6;color:rgba(0,0,0,.6);line-height:1.4em}.pill__container[data-v-69bac0c3]{display:flex;margin-bottom:1em}.pill__text[data-v-69bac0c3]{display:inline-block;max-width:200px;text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.pill__score[data-v-69bac0c3]{margin-left:1em}.pill.active[data-v-69bac0c3]{background:#f4f5f6}',""]),e.exports=d},826:function(e,n,t){"use strict";t.r(n);t(97),t(98);var r={props:{label:{type:Object,required:!0},predictedAs:{type:Array},showScore:{type:Boolean,default:!1},annotationLabels:{type:Array,default:function(){return[]}}},methods:{isPredictedAs:function(label){return this.predictedAs?this.predictedAs.includes(label.class):null}}},o=(t(813),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return n("div",[n("p",{class:["pill",e.isPredictedAs(e.label)?"active":""],attrs:{title:e.label.class}},[n("span",{staticClass:"pill__text"},[e._v(e._s(e.label.class)+" ")]),e._v(" "),e.showScore?n("span",{staticClass:"pill__score"},[n("span",{staticClass:"radio-data__score"},[e._v(e._s(e._f("percent")(e.label.score)))])]):e._e()])])}),[],!1,null,"69bac0c3",null);n.default=component.exports}}]);