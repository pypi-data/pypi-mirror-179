(window.webpackJsonp=window.webpackJsonp||[]).push([[95,56,59],{1027:function(e,n,t){"use strict";t.r(n);t(15);var r={props:{dataset:{type:Object,required:!0}},computed:{availableHelpInfo:function(){return this.dataset.results.records.some((function(e){return e.explanation}))},task:function(){return this.dataset.task}}},o=(t(939),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return n("div",{staticClass:"dataset-options"},[e.availableHelpInfo?n("dataset-option-help-info",{staticClass:"dataset-options__item",attrs:{task:e.task}}):e._e()],1)}),[],!1,null,"2bf076e0",null);n.default=component.exports;installComponents(component,{DatasetOptionHelpInfo:t(883).default})},1150:function(e,n,t){"use strict";t.r(n);t(47),t(41),t(57),t(31),t(58);var r=t(1),o=t(22),c=t(60),l=(t(32),t(42),t(75),t(53),t(15),t(195),t(196),t(197),t(198),t(199),t(200),t(201),t(202),t(203),t(204),t(205),t(206),t(207),t(208),t(209),t(210),t(211),t(52),t(48),t(39),t(99));function d(object,e){var n=Object.keys(object);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(object);e&&(t=t.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),n.push.apply(n,t)}return n}function h(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?d(Object(source),!0).forEach((function(n){Object(o.a)(e,n,source[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):d(Object(source)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(source,n))}))}return e}var f={props:{dataset:{type:Object,required:!0}},computed:{isMultiLabel:function(){return this.dataset.isMultiLabel},isRuleListView:function(){var e;return(null===(e=this.dataset.viewSettings)||void 0===e?void 0:e.visibleRulesList)||!1},availableLabels:function(){var e=this.dataset.results.records[0],n=e&&e.prediction?e.prediction.labels.map((function(label){return label.class})):[];return n=Array.from(new Set([].concat(Object(c.a)(n),Object(c.a)(this.dataset.labels))))},viewMode:function(){return this.dataset.viewSettings.viewMode},allowLabelCreation:function(){return!this.dataset.settings.label_schema}},methods:h(h({},Object(l.b)({updateRecords:"entities/datasets/updateRecords",discard:"entities/datasets/discardAnnotations",validate:"entities/datasets/validateAnnotations"})),{},{onSelectLabels:function(e,n){var t=this;return Object(r.a)(regeneratorRuntime.mark((function r(){var o;return regeneratorRuntime.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return o=n.map((function(n){var t=e.map((function(label){return{class:label,score:1}}));return h(h({},n),{},{annotation:{labels:t}})})),r.next=3,t.validate({dataset:t.dataset,agent:t.$auth.user.username,records:o});case 3:case"end":return r.stop()}}),r)})))()},onDiscard:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.discard({dataset:n.dataset,records:e});case 2:case"end":return t.stop()}}),t)})))()},onValidate:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r=e.filter((function(e){return e.annotation||e.predicted_as||e.multi_label})),t.next=3,n.validate({dataset:n.dataset,agent:n.$auth.user.username,records:r.map((function(e){var n={};n.labels=e.predicted_as.map((function(e){return{class:e,score:1}}));var t={labels:[]};return h(h({},e),{},{annotation:h({},e.annotation||n||t)})}))});case 3:case"end":return t.stop()}}),t)})))()},onNewLabel:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.dataset.$dispatch("setLabels",{dataset:n.dataset,labels:Object(c.a)(new Set([].concat(Object(c.a)(n.dataset.labels),[e])))});case 2:case"end":return t.stop()}}),t)})))()}})},m=t(51),component=Object(m.a)(f,(function(){var e=this,n=e._self._c;return n("div",{staticClass:"header__filters"},[e.dataset.viewSettings.visibleRulesList?e._e():n("filters-area",{attrs:{dataset:e.dataset}},[n("dataset-options",{attrs:{dataset:e.dataset}})],1),e._v(" "),n("global-actions",{attrs:{dataset:e.dataset}},[n("validate-discard-action",{attrs:{dataset:e.dataset},on:{"discard-records":e.onDiscard,"validate-records":e.onValidate},scopedSlots:e._u([{key:"first",fn:function(t){return[n("annotation-label-selector",{class:"validate-discard-actions__select",attrs:{"multi-label":e.isMultiLabel,options:e.availableLabels},on:{selected:function(n){return e.onSelectLabels(n,t.selectedRecords)}}})]}}])}),e._v(" "),e.allowLabelCreation?n("create-new-action",{on:{"new-label":e.onNewLabel}}):e._e()],1)],1)}),[],!1,null,"55a60404",null);n.default=component.exports;installComponents(component,{DatasetOptions:t(1027).default,FiltersArea:t(824).default,AnnotationLabelSelector:t(1134).default,ValidateDiscardAction:t(961).default,CreateNewAction:t(886).default,GlobalActions:t(825).default})},756:function(e,n,t){var content=t(810);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("5433e122",content,!0,{sourceMap:!1})},757:function(e,n,t){var content=t(812);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("41985aef",content,!0,{sourceMap:!1})},788:function(e,n,t){var content=t(855);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("045ccdb2",content,!0,{sourceMap:!1})},789:function(e,n,t){var content=t(857);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("0dd0b378",content,!0,{sourceMap:!1})},809:function(e,n,t){"use strict";t(756)},810:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.container[data-v-762d2ffa]{margin:0 auto;padding:4em}.container[data-v-762d2ffa]{padding-right:126px;transition:padding .25s linear .2s}@media(min-width: 1101px){.--metrics .container[data-v-762d2ffa]{padding-right:375px;transition:padding .25s linear}}.container[data-v-762d2ffa]{padding-top:0;padding-bottom:0;margin-left:0}.filters[data-v-762d2ffa]{color:rgba(0,0,0,.6)}.filters__row[data-v-762d2ffa]{display:flex;align-items:center}.filters__content[data-v-762d2ffa]{padding:32px 0;position:relative;width:100%}.filters__block[data-v-762d2ffa]{display:flex;align-items:center;width:calc(100% - 300px)}.filters__searchbar[data-v-762d2ffa]{margin-right:8px;width:100%}@media(min-width: 1101px){.filters__searchbar[data-v-762d2ffa]{margin-right:16px}}',""]),e.exports=d},811:function(e,n,t){"use strict";t(757)},812:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.container[data-v-7804c1b2]{margin:0 auto;padding:4em}.container[data-v-7804c1b2]{padding-right:126px;transition:padding .25s linear .2s}@media(min-width: 1101px){.--metrics .container[data-v-7804c1b2]{padding-right:375px;transition:padding .25s linear}}.container[data-v-7804c1b2]{margin:0 auto auto 0;padding-top:0;padding-bottom:0;padding-left:4em}.global-actions[data-v-7804c1b2]{display:flex;align-items:center;width:100%;text-align:left;padding:1em 16px;background:#fff;border-radius:10px;position:relative;box-shadow:0 1px 2px 0 rgba(185,185,185,.5);margin-bottom:16px}',""]),e.exports=d},824:function(e,n,t){"use strict";t.r(n);t(47),t(41),t(57),t(58);var r=t(1),o=t(22),c=(t(32),t(49),t(192),t(39),t(15),t(52),t(31),t(99));function l(object,e){var n=Object.keys(object);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(object);e&&(t=t.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),n.push.apply(n,t)}return n}function d(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?l(Object(source),!0).forEach((function(n){Object(o.a)(e,n,source[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):l(Object(source)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(source,n))}))}return e}var h={props:{dataset:{type:Object,default:function(){return{}}}},data:function(){return{sortable:{type:Boolean,default:!1},sortBy:"gold",sortByDir:"desc",sortOptions:[{filter:"annotated_as",text:"Annotated as",range:["A","Z"]},{filter:"predicted_as",text:"Predicted as",range:["A","Z"]},{filter:"score",text:"Score",range:["0","1"]}]}},computed:{viewMode:function(){return this.dataset.viewSettings.viewMode}},methods:d(d({},Object(c.b)({search:"entities/datasets/search"})),{},{onTextQuerySearch:function(text){""===text&&(text=void 0),this.search({dataset:this.dataset,query:{text:text}})},onApplyFilter:function(e){var filter=e.filter,n=e.values;Array.isArray(n)&&!n.length&&(n=void 0),this.search({dataset:this.dataset,query:Object(o.a)({},filter,n)})},onApplyMetaFilter:function(e){var filter=e.filter,n=e.values;this.search({dataset:this.dataset,query:{metadata:Object(o.a)({},filter,n)}})},onRemoveAllMetadataFilters:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r={},e.forEach((function(e){return r[e.key]=[]})),t.next=4,n.search({dataset:n.dataset,query:{metadata:r}});case 4:case"end":return t.stop()}}),t)})))()},onRemoveFiltersByGroup:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r={},e.forEach((function(e){return r[e.key]="score"===e.key?void 0:[]})),t.next=4,n.search({dataset:n.dataset,query:r});case 4:case"end":return t.stop()}}),t)})))()},onApplySortBy:function(e){var n=this;return Object(r.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.search({dataset:n.dataset,query:n.dataset.query,sort:e});case 2:case"end":return t.stop()}}),t)})))()}})},f=(t(809),t(51)),component=Object(f.a)(h,(function(){var e=this,n=e._self._c;return n("div",{staticClass:"filters__content"},[n("div",{staticClass:"container"},[n("div",{staticClass:"filters__row"},[n("div",{staticClass:"filters__block"},[n("search-bar",{staticClass:"filters__searchbar",attrs:{dataset:e.dataset},on:{submit:e.onTextQuerySearch}}),e._v(" "),n("filters-list",{attrs:{dataset:e.dataset},on:{applyFilter:e.onApplyFilter,applyMetaFilter:e.onApplyMetaFilter,applySortBy:e.onApplySortBy,removeAllMetadataFilters:e.onRemoveAllMetadataFilters,removeFiltersByGroup:e.onRemoveFiltersByGroup}})],1),e._v(" "),e._t("default")],2)])])}),[],!1,null,"762d2ffa",null);n.default=component.exports;installComponents(component,{SearchBar:t(884).default,FiltersList:t(885).default})},825:function(e,n,t){"use strict";t.r(n);var r={props:{dataset:{type:Object,required:!0}},data:function(){return{}},computed:{annotationEnabled:function(){return"annotate"===this.dataset.viewSettings.viewMode}}},o=(t(811),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return e.annotationEnabled?n("div",{staticClass:"container"},[n("div",{staticClass:"global-actions"},[e._t("default")],2)]):e._e()}),[],!1,null,"7804c1b2",null);n.default=component.exports},853:function(e,n,t){var content=t(940);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,t(125).default)("1236a6d6",content,!0,{sourceMap:!1})},854:function(e,n,t){"use strict";t(788)},855:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.dataset-option__button[data-v-59379e6d]{padding:0;color:#3e5cc9}.dataset-option__button[data-v-59379e6d]:hover,.dataset-option__button.--active[data-v-59379e6d]{color:#2e48a6}',""]),e.exports=d},856:function(e,n,t){"use strict";t(789)},857:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.new-label[data-v-6027f973]{width:180px;border-radius:5px;box-shadow:0 8px 20px 0 rgba(0,0,0,.2);padding:16px;position:absolute;top:-1em;background:#fff;text-align:left}.new-label__close[data-v-6027f973]{position:absolute;top:1.2em;right:1em;cursor:pointer;height:12px;width:12px;stroke:rgba(0,0,0,.6);stroke-width:1}.new-label__input[data-v-6027f973]{border:0;outline:none;padding-right:2em;width:100%}.new-label__button[data-v-6027f973]{margin-top:2em;margin-bottom:0 !important}.new-label__main-button[data-v-6027f973]{margin-bottom:0 !important;margin-right:0;margin-left:auto}.new-label__container[data-v-6027f973]{text-align:right;position:relative;margin-right:0;margin-left:auto;width:180px}',""]),e.exports=d},883:function(e,n,t){"use strict";t.r(n);var r={props:{task:{type:String,required:!0}},data:function(){return{visible:!1}},computed:{currentTaskHelpInfo:function(){return"".concat(this.task,"HelpInfo")},buttonClass:function(){return this.visible?"--active":null}},methods:{showHelpInfo:function(){this.visible=!this.visible},close:function(){this.visible=!1}}},o=(t(854),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return n("div",[n("base-button",{staticClass:"dataset-option__button",class:e.buttonClass,attrs:{title:"Info"},on:{click:function(n){return e.showHelpInfo()}}},[n("svgicon",{attrs:{name:"support",width:"18",height:"18"}}),e._v("Help")],1),e._v(" "),n(e.currentTaskHelpInfo,{tag:"component",attrs:{visible:e.visible},on:{"on-close":function(n){return e.close()}}})],1)}),[],!1,null,"59379e6d",null);n.default=component.exports;installComponents(component,{BaseButton:t(722).default})},886:function(e,n,t){"use strict";t.r(n);t(212);var r={props:{text:{type:String,required:!1,default:"Create label"}},data:function(){return{label:void 0,showLabelCreation:!1}},methods:{createNewLabel:function(label){label&&label.trim()&&(this.$emit("new-label",label),this.reset())},openLabelCreation:function(){var e=this;this.showLabelCreation=!0,this.$nextTick((function(){e.$refs.labelCreation.focus()}))},reset:function(){this.label=void 0,this.showLabelCreation=!1}}},o=(t(856),t(51)),component=Object(o.a)(r,(function(){var e=this,n=e._self._c;return n("div",{staticClass:"new-label__container"},[e.showLabelCreation?n("div",{staticClass:"new-label"},[n("input",{directives:[{name:"model",rawName:"v-model",value:e.label,expression:"label"}],ref:"labelCreation",staticClass:"new-label__input",attrs:{autofocus:"",type:"text",placeholder:"New label"},domProps:{value:e.label},on:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.createNewLabel(e.label)},input:function(n){n.target.composing||(e.label=n.target.value)}}}),e._v(" "),n("svgicon",{staticClass:"new-label__close",attrs:{name:"close"},on:{click:function(n){return e.reset()}}}),e._v(" "),n("base-button",{staticClass:"new-label__button primary small",attrs:{disabled:!e.label},on:{click:function(n){return e.createNewLabel(e.label)}}},[e._v("Create")])],1):n("base-button",{staticClass:"new-label__main-button primary light small",on:{click:function(n){return e.openLabelCreation()}}},[e._v(e._s(e.text))])],1)}),[],!1,null,"6027f973",null);n.default=component.exports;installComponents(component,{BaseButton:t(722).default})},939:function(e,n,t){"use strict";t(853)},940:function(e,n,t){var r=t(124),o=t(150),c=t(151),l=t(152),d=r(!1),h=o(c),f=o(l);d.push([e.i,'/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */@font-face{font-family:"raptor_v2_premiumbold";src:url('+h+') format("woff2"),url('+f+') format("woff");font-weight:normal;font-style:normal}/*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n *//*!\n * coding=utf-8\n * Copyright 2021-present, the Recognai S.L. team.\n *\n * Licensed under the Apache License, Version 2.0 (the "License");\n * you may not use this file except in compliance with the License.\n * You may obtain a copy of the License at\n *\n *     http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing, software\n * distributed under the License is distributed on an "AS IS" BASIS,\n * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n * See the License for the specific language governing permissions and\n * limitations under the License.\n */.dataset-options[data-v-2bf076e0]{display:flex;align-items:center;gap:8px;margin-left:auto}.dataset-options__item[data-v-2bf076e0]{display:flex;align-items:center}',""]),e.exports=d}}]);