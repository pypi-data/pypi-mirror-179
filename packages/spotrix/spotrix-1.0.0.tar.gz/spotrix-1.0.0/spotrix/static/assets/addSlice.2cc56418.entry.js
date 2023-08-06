/******/ (function(modules) { // webpackBootstrap
/******/ 	// install a JSONP callback for chunk loading
/******/ 	function webpackJsonpCallback(data) {
/******/ 		var chunkIds = data[0];
/******/ 		var moreModules = data[1];
/******/ 		var executeModules = data[2];
/******/
/******/ 		// add "moreModules" to the modules object,
/******/ 		// then flag all "chunkIds" as loaded and fire callback
/******/ 		var moduleId, chunkId, i = 0, resolves = [];
/******/ 		for(;i < chunkIds.length; i++) {
/******/ 			chunkId = chunkIds[i];
/******/ 			if(Object.prototype.hasOwnProperty.call(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 				resolves.push(installedChunks[chunkId][0]);
/******/ 			}
/******/ 			installedChunks[chunkId] = 0;
/******/ 		}
/******/ 		for(moduleId in moreModules) {
/******/ 			if(Object.prototype.hasOwnProperty.call(moreModules, moduleId)) {
/******/ 				modules[moduleId] = moreModules[moduleId];
/******/ 			}
/******/ 		}
/******/ 		if(parentJsonpFunction) parentJsonpFunction(data);
/******/
/******/ 		while(resolves.length) {
/******/ 			resolves.shift()();
/******/ 		}
/******/
/******/ 		// add entry modules from loaded chunk to deferred list
/******/ 		deferredModules.push.apply(deferredModules, executeModules || []);
/******/
/******/ 		// run deferred modules when all chunks ready
/******/ 		return checkDeferredModules();
/******/ 	};
/******/ 	function checkDeferredModules() {
/******/ 		var result;
/******/ 		for(var i = 0; i < deferredModules.length; i++) {
/******/ 			var deferredModule = deferredModules[i];
/******/ 			var fulfilled = true;
/******/ 			for(var j = 1; j < deferredModule.length; j++) {
/******/ 				var depId = deferredModule[j];
/******/ 				if(installedChunks[depId] !== 0) fulfilled = false;
/******/ 			}
/******/ 			if(fulfilled) {
/******/ 				deferredModules.splice(i--, 1);
/******/ 				result = __webpack_require__(__webpack_require__.s = deferredModule[0]);
/******/ 			}
/******/ 		}
/******/
/******/ 		return result;
/******/ 	}
/******/
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// object to store loaded and loading chunks
/******/ 	// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 	// Promise = chunk loading, 0 = chunk loaded
/******/ 	var installedChunks = {
/******/ 		"addSlice": 0
/******/ 	};
/******/
/******/ 	var deferredModules = [];
/******/
/******/ 	// script path function
/******/ 	function jsonpScriptSrc(chunkId) {
/******/ 		return __webpack_require__.p + "" + ({}[chunkId]||chunkId) + "." + "2cc56418" + ".chunk.js"
/******/ 	}
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/ 	// This file contains only the entry chunk.
/******/ 	// The chunk loading function for additional chunks
/******/ 	__webpack_require__.e = function requireEnsure(chunkId) {
/******/ 		var promises = [];
/******/
/******/
/******/ 		// JSONP chunk loading for javascript
/******/
/******/ 		var installedChunkData = installedChunks[chunkId];
/******/ 		if(installedChunkData !== 0) { // 0 means "already installed".
/******/
/******/ 			// a Promise means "currently loading".
/******/ 			if(installedChunkData) {
/******/ 				promises.push(installedChunkData[2]);
/******/ 			} else {
/******/ 				// setup Promise in chunk cache
/******/ 				var promise = new Promise(function(resolve, reject) {
/******/ 					installedChunkData = installedChunks[chunkId] = [resolve, reject];
/******/ 				});
/******/ 				promises.push(installedChunkData[2] = promise);
/******/
/******/ 				// start chunk loading
/******/ 				var script = document.createElement('script');
/******/ 				var onScriptComplete;
/******/
/******/ 				script.charset = 'utf-8';
/******/ 				script.timeout = 120;
/******/ 				if (__webpack_require__.nc) {
/******/ 					script.setAttribute("nonce", __webpack_require__.nc);
/******/ 				}
/******/ 				script.src = jsonpScriptSrc(chunkId);
/******/
/******/ 				// create error before stack unwound to get useful stacktrace later
/******/ 				var error = new Error();
/******/ 				onScriptComplete = function (event) {
/******/ 					// avoid mem leaks in IE.
/******/ 					script.onerror = script.onload = null;
/******/ 					clearTimeout(timeout);
/******/ 					var chunk = installedChunks[chunkId];
/******/ 					if(chunk !== 0) {
/******/ 						if(chunk) {
/******/ 							var errorType = event && (event.type === 'load' ? 'missing' : event.type);
/******/ 							var realSrc = event && event.target && event.target.src;
/******/ 							error.message = 'Loading chunk ' + chunkId + ' failed.\n(' + errorType + ': ' + realSrc + ')';
/******/ 							error.name = 'ChunkLoadError';
/******/ 							error.type = errorType;
/******/ 							error.request = realSrc;
/******/ 							chunk[1](error);
/******/ 						}
/******/ 						installedChunks[chunkId] = undefined;
/******/ 					}
/******/ 				};
/******/ 				var timeout = setTimeout(function(){
/******/ 					onScriptComplete({ type: 'timeout', target: script });
/******/ 				}, 120000);
/******/ 				script.onerror = script.onload = onScriptComplete;
/******/ 				document.head.appendChild(script);
/******/ 			}
/******/ 		}
/******/ 		return Promise.all(promises);
/******/ 	};
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/static/assets/";
/******/
/******/ 	// on error function for async loading
/******/ 	__webpack_require__.oe = function(err) { console.error(err); throw err; };
/******/
/******/ 	var jsonpArray = window["webpackJsonp"] = window["webpackJsonp"] || [];
/******/ 	var oldJsonpFunction = jsonpArray.push.bind(jsonpArray);
/******/ 	jsonpArray.push = webpackJsonpCallback;
/******/ 	jsonpArray = jsonpArray.slice();
/******/ 	for(var i = 0; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]);
/******/ 	var parentJsonpFunction = oldJsonpFunction;
/******/
/******/
/******/ 	// add entry module to deferred list
/******/ 	deferredModules.push([10,"vendors","mathjs","thumbnail",3,4]);
/******/ 	// run deferred modules when ready
/******/ 	return checkDeferredModules();
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/addSlice/AddSliceContainer.tsx":
/*!********************************************!*\
  !*** ./src/addSlice/AddSliceContainer.tsx ***!
  \********************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* WEBPACK VAR INJECTION */(function(module) {/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return AddSliceContainer; });\n/* harmony import */ var _babel_runtime_corejs3_core_js_stable_json_stringify__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime-corejs3/core-js-stable/json/stringify */ \"./node_modules/@babel/runtime-corejs3/core-js-stable/json/stringify.js\");\n/* harmony import */ var _babel_runtime_corejs3_core_js_stable_json_stringify__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_corejs3_core_js_stable_json_stringify__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @babel/runtime-corejs3/core-js-stable/instance/bind */ \"./node_modules/@babel/runtime-corejs3/core-js-stable/instance/bind.js\");\n/* harmony import */ var _babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var src_components_Button__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/components/Button */ \"./src/components/Button/index.tsx\");\n/* harmony import */ var src_components__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! src/components */ \"./src/components/index.ts\");\n/* harmony import */ var _superset_ui_core__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @superset-ui/core */ \"./node_modules/@superset-ui/core/esm/style/index.js\");\n/* harmony import */ var _superset_ui_core__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @superset-ui/core */ \"./node_modules/@emotion/react/dist/emotion-react.browser.esm.js\");\n/* harmony import */ var _superset_ui_core__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @superset-ui/core */ \"./node_modules/@superset-ui/core/esm/translation/TranslatorSingleton.js\");\n/* harmony import */ var src_components_Form__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! src/components/Form */ \"./src/components/Form/index.tsx\");\n/* harmony import */ var src_explore_components_controls_VizTypeControl_VizTypeGallery__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! src/explore/components/controls/VizTypeControl/VizTypeGallery */ \"./src/explore/components/controls/VizTypeControl/VizTypeGallery.tsx\");\n/* harmony import */ var src_common_components__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! src/common/components */ \"./src/common/components/index.tsx\");\n(function () {var enterModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.enterModule : undefined;enterModule && enterModule(module);})();var __signature__ = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default.signature : function (a) {return a;}; /**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\n\n\n\n\nconst ESTIMATED_NAV_HEIGHT = '56px';\nconst APP_HEADER_HEIGHT = '47px';\nconst APP_NAV_WIDTH = '60px';\nconst StyledContainer = _superset_ui_core__WEBPACK_IMPORTED_MODULE_5__[\"styled\"].div`\n  ${({ theme }) => `\n    flex: 1 1 auto;\n    display: flex;\n    flex-direction: column;\n    justify-content: space-between;\n    width: calc(100vw - ${APP_NAV_WIDTH});\n    max-width: ${src_explore_components_controls_VizTypeControl_VizTypeGallery__WEBPACK_IMPORTED_MODULE_9__[\"MAX_ADVISABLE_VIZ_GALLERY_WIDTH\"]}px;\n    max-height: calc(100vh - ${ESTIMATED_NAV_HEIGHT} - ${APP_HEADER_HEIGHT});\n    border-radius: ${theme.gridUnit}px;\n    background-color: ${theme.colors.grayscale.light5};\n    margin-left: auto;\n    margin-right: auto;\n    padding-left: ${theme.gridUnit * 4}px;\n    padding-right: ${theme.gridUnit * 4}px;\n    padding-bottom: ${theme.gridUnit * 4}px;\n\n    h3 {\n      padding-bottom: ${theme.gridUnit * 3}px;\n    }\n\n    & .dataset {\n      display: flex;\n      flex-direction: row;\n      align-items: center;\n\n      & > div {\n        min-width: 200px;\n        width: 300px;\n      }\n\n      & > span {\n        color: ${theme.colors.grayscale.light1};\n        margin-left: ${theme.gridUnit * 4}px;\n        margin-top: ${theme.gridUnit * 6}px;\n      }\n    }\n  `}\n`;\nconst cssStatic = _superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"css\"]`\n  flex: 0 0 auto;\n`;\nconst StyledVizTypeGallery = Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_5__[\"styled\"])(src_explore_components_controls_VizTypeControl_VizTypeGallery__WEBPACK_IMPORTED_MODULE_9__[\"default\"])`\n  ${({ theme }) => `\n    border: 1px solid ${theme.colors.grayscale.light2};\n    border-radius: ${theme.gridUnit}px;\n    margin: ${theme.gridUnit * 3}px 0px;\n    flex: 1 1 auto;\n  `}\n`;\nclass AddSliceContainer extends react__WEBPACK_IMPORTED_MODULE_2___default.a.PureComponent {\n  constructor(props) {var _context, _context2, _context3;\n    super(props);\n    this.state = {\n      visType: null };\n\n    this.changeDatasource = _babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1___default()(_context = this.changeDatasource).call(_context, this);\n    this.changeVisType = _babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1___default()(_context2 = this.changeVisType).call(_context2, this);\n    this.gotoSlice = _babel_runtime_corejs3_core_js_stable_instance_bind__WEBPACK_IMPORTED_MODULE_1___default()(_context3 = this.gotoSlice).call(_context3, this);\n  }\n  exploreUrl() {\n    const formData = encodeURIComponent(_babel_runtime_corejs3_core_js_stable_json_stringify__WEBPACK_IMPORTED_MODULE_0___default()({\n      viz_type: this.state.visType,\n      datasource: this.state.datasourceValue }));\n\n    return `/spotrix/explore/?form_data=${formData}`;\n  }\n  gotoSlice() {\n    window.location.href = this.exploreUrl();\n  }\n  changeDatasource(value) {\n    this.setState({\n      datasourceValue: value,\n      datasourceId: value.split('__')[0] });\n\n  }\n  changeVisType(visType) {\n    this.setState({ visType });\n  }\n  isBtnDisabled() {\n    return !(this.state.datasourceId && this.state.visType);\n  }\n  render() {\n    return Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(StyledContainer, null,\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_common_components__WEBPACK_IMPORTED_MODULE_10__[\"Row\"], { align: \"middle\" },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_common_components__WEBPACK_IMPORTED_MODULE_10__[\"Col\"], { md: 16, xs: 16 },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(\"h3\", null, Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Create a new chart'))),\n\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_common_components__WEBPACK_IMPORTED_MODULE_10__[\"Col\"], { md: 8, xs: 8, style: { textAlign: 'right' } },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_components_Button__WEBPACK_IMPORTED_MODULE_3__[\"default\"], { css: [\n      cssStatic,\n      _superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"css\"]`\n                  align-self: flex-end;\n                `,  false ? undefined : \";label:AddSliceContainer;\",  false ? undefined : \"/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9Vc2Vycy9hZG1pbi9HaXQvUHVibGljL3Nwb3RyaXgvc3BvdHJpeC1mcm9udGVuZC9zcmMvYWRkU2xpY2UvQWRkU2xpY2VDb250YWluZXIudHN4Il0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQXFIb0IiLCJmaWxlIjoiL1VzZXJzL2FkbWluL0dpdC9QdWJsaWMvc3BvdHJpeC9zcG90cml4LWZyb250ZW5kL3NyYy9hZGRTbGljZS9BZGRTbGljZUNvbnRhaW5lci50c3giLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIExpY2Vuc2VkIHRvIHRoZSBBcGFjaGUgU29mdHdhcmUgRm91bmRhdGlvbiAoQVNGKSB1bmRlciBvbmVcbiAqIG9yIG1vcmUgY29udHJpYnV0b3IgbGljZW5zZSBhZ3JlZW1lbnRzLiAgU2VlIHRoZSBOT1RJQ0UgZmlsZVxuICogZGlzdHJpYnV0ZWQgd2l0aCB0aGlzIHdvcmsgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb25cbiAqIHJlZ2FyZGluZyBjb3B5cmlnaHQgb3duZXJzaGlwLiAgVGhlIEFTRiBsaWNlbnNlcyB0aGlzIGZpbGVcbiAqIHRvIHlvdSB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGVcbiAqIFwiTGljZW5zZVwiKTsgeW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZVxuICogd2l0aCB0aGUgTGljZW5zZS4gIFlvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdFxuICpcbiAqICAgaHR0cDovL3d3dy5hcGFjaGUub3JnL2xpY2Vuc2VzL0xJQ0VOU0UtMi4wXG4gKlxuICogVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLFxuICogc29mdHdhcmUgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW5cbiAqIFwiQVMgSVNcIiBCQVNJUywgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZXG4gKiBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLiAgU2VlIHRoZSBMaWNlbnNlIGZvciB0aGVcbiAqIHNwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhbmQgbGltaXRhdGlvbnNcbiAqIHVuZGVyIHRoZSBMaWNlbnNlLlxuICovXG5pbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IEJ1dHRvbiBmcm9tICdzcmMvY29tcG9uZW50cy9CdXR0b24nO1xuaW1wb3J0IHsgU2VsZWN0IH0gZnJvbSAnc3JjL2NvbXBvbmVudHMnO1xuaW1wb3J0IHsgY3NzLCBzdHlsZWQsIHQgfSBmcm9tICdAc3VwZXJzZXQtdWkvY29yZSc7XG5pbXBvcnQgeyBGb3JtTGFiZWwgfSBmcm9tICdzcmMvY29tcG9uZW50cy9Gb3JtJztcbmltcG9ydCBWaXpUeXBlR2FsbGVyeSwgeyBNQVhfQURWSVNBQkxFX1ZJWl9HQUxMRVJZX1dJRFRILCB9IGZyb20gJ3NyYy9leHBsb3JlL2NvbXBvbmVudHMvY29udHJvbHMvVml6VHlwZUNvbnRyb2wvVml6VHlwZUdhbGxlcnknO1xuaW1wb3J0IHsgQ29sLCBSb3cgfSBmcm9tICdzcmMvY29tbW9uL2NvbXBvbmVudHMnO1xuY29uc3QgRVNUSU1BVEVEX05BVl9IRUlHSFQgPSAnNTZweCc7XG5jb25zdCBBUFBfSEVBREVSX0hFSUdIVCA9ICc0N3B4JztcbmNvbnN0IEFQUF9OQVZfV0lEVEggPSAnNjBweCc7XG5jb25zdCBTdHlsZWRDb250YWluZXIgPSBzdHlsZWQuZGl2IGBcbiAgJHsoeyB0aGVtZSB9KSA9PiBgXG4gICAgZmxleDogMSAxIGF1dG87XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgICB3aWR0aDogY2FsYygxMDB2dyAtICR7QVBQX05BVl9XSURUSH0pO1xuICAgIG1heC13aWR0aDogJHtNQVhfQURWSVNBQkxFX1ZJWl9HQUxMRVJZX1dJRFRIfXB4O1xuICAgIG1heC1oZWlnaHQ6IGNhbGMoMTAwdmggLSAke0VTVElNQVRFRF9OQVZfSEVJR0hUfSAtICR7QVBQX0hFQURFUl9IRUlHSFR9KTtcbiAgICBib3JkZXItcmFkaXVzOiAke3RoZW1lLmdyaWRVbml0fXB4O1xuICAgIGJhY2tncm91bmQtY29sb3I6ICR7dGhlbWUuY29sb3JzLmdyYXlzY2FsZS5saWdodDV9O1xuICAgIG1hcmdpbi1sZWZ0OiBhdXRvO1xuICAgIG1hcmdpbi1yaWdodDogYXV0bztcbiAgICBwYWRkaW5nLWxlZnQ6ICR7dGhlbWUuZ3JpZFVuaXQgKiA0fXB4O1xuICAgIHBhZGRpbmctcmlnaHQ6ICR7dGhlbWUuZ3JpZFVuaXQgKiA0fXB4O1xuICAgIHBhZGRpbmctYm90dG9tOiAke3RoZW1lLmdyaWRVbml0ICogNH1weDtcblxuICAgIGgzIHtcbiAgICAgIHBhZGRpbmctYm90dG9tOiAke3RoZW1lLmdyaWRVbml0ICogM31weDtcbiAgICB9XG5cbiAgICAmIC5kYXRhc2V0IHtcbiAgICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgICBmbGV4LWRpcmVjdGlvbjogcm93O1xuICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcblxuICAgICAgJiA+IGRpdiB7XG4gICAgICAgIG1pbi13aWR0aDogMjAwcHg7XG4gICAgICAgIHdpZHRoOiAzMDBweDtcbiAgICAgIH1cblxuICAgICAgJiA+IHNwYW4ge1xuICAgICAgICBjb2xvcjogJHt0aGVtZS5jb2xvcnMuZ3JheXNjYWxlLmxpZ2h0MX07XG4gICAgICAgIG1hcmdpbi1sZWZ0OiAke3RoZW1lLmdyaWRVbml0ICogNH1weDtcbiAgICAgICAgbWFyZ2luLXRvcDogJHt0aGVtZS5ncmlkVW5pdCAqIDZ9cHg7XG4gICAgICB9XG4gICAgfVxuICBgfVxuYDtcbmNvbnN0IGNzc1N0YXRpYyA9IGNzcyBgXG4gIGZsZXg6IDAgMCBhdXRvO1xuYDtcbmNvbnN0IFN0eWxlZFZpelR5cGVHYWxsZXJ5ID0gc3R5bGVkKFZpelR5cGVHYWxsZXJ5KSBgXG4gICR7KHsgdGhlbWUgfSkgPT4gYFxuICAgIGJvcmRlcjogMXB4IHNvbGlkICR7dGhlbWUuY29sb3JzLmdyYXlzY2FsZS5saWdodDJ9O1xuICAgIGJvcmRlci1yYWRpdXM6ICR7dGhlbWUuZ3JpZFVuaXR9cHg7XG4gICAgbWFyZ2luOiAke3RoZW1lLmdyaWRVbml0ICogM31weCAwcHg7XG4gICAgZmxleDogMSAxIGF1dG87XG4gIGB9XG5gO1xuZXhwb3J0IGRlZmF1bHQgY2xhc3MgQWRkU2xpY2VDb250YWluZXIgZXh0ZW5kcyBSZWFjdC5QdXJlQ29tcG9uZW50IHtcbiAgICBjb25zdHJ1Y3Rvcihwcm9wcykge1xuICAgICAgICBzdXBlcihwcm9wcyk7XG4gICAgICAgIHRoaXMuc3RhdGUgPSB7XG4gICAgICAgICAgICB2aXNUeXBlOiBudWxsLFxuICAgICAgICB9O1xuICAgICAgICB0aGlzLmNoYW5nZURhdGFzb3VyY2UgPSB0aGlzLmNoYW5nZURhdGFzb3VyY2UuYmluZCh0aGlzKTtcbiAgICAgICAgdGhpcy5jaGFuZ2VWaXNUeXBlID0gdGhpcy5jaGFuZ2VWaXNUeXBlLmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMuZ290b1NsaWNlID0gdGhpcy5nb3RvU2xpY2UuYmluZCh0aGlzKTtcbiAgICB9XG4gICAgZXhwbG9yZVVybCgpIHtcbiAgICAgICAgY29uc3QgZm9ybURhdGEgPSBlbmNvZGVVUklDb21wb25lbnQoSlNPTi5zdHJpbmdpZnkoe1xuICAgICAgICAgICAgdml6X3R5cGU6IHRoaXMuc3RhdGUudmlzVHlwZSxcbiAgICAgICAgICAgIGRhdGFzb3VyY2U6IHRoaXMuc3RhdGUuZGF0YXNvdXJjZVZhbHVlLFxuICAgICAgICB9KSk7XG4gICAgICAgIHJldHVybiBgL3Nwb3RyaXgvZXhwbG9yZS8/Zm9ybV9kYXRhPSR7Zm9ybURhdGF9YDtcbiAgICB9XG4gICAgZ290b1NsaWNlKCkge1xuICAgICAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9IHRoaXMuZXhwbG9yZVVybCgpO1xuICAgIH1cbiAgICBjaGFuZ2VEYXRhc291cmNlKHZhbHVlKSB7XG4gICAgICAgIHRoaXMuc2V0U3RhdGUoe1xuICAgICAgICAgICAgZGF0YXNvdXJjZVZhbHVlOiB2YWx1ZSxcbiAgICAgICAgICAgIGRhdGFzb3VyY2VJZDogdmFsdWUuc3BsaXQoJ19fJylbMF0sXG4gICAgICAgIH0pO1xuICAgIH1cbiAgICBjaGFuZ2VWaXNUeXBlKHZpc1R5cGUpIHtcbiAgICAgICAgdGhpcy5zZXRTdGF0ZSh7IHZpc1R5cGUgfSk7XG4gICAgfVxuICAgIGlzQnRuRGlzYWJsZWQoKSB7XG4gICAgICAgIHJldHVybiAhKHRoaXMuc3RhdGUuZGF0YXNvdXJjZUlkICYmIHRoaXMuc3RhdGUudmlzVHlwZSk7XG4gICAgfVxuICAgIHJlbmRlcigpIHtcbiAgICAgICAgcmV0dXJuICg8U3R5bGVkQ29udGFpbmVyPlxuICAgICAgICA8Um93IGFsaWduPVwibWlkZGxlXCI+XG4gICAgICAgICAgPENvbCBtZD17MTZ9IHhzPXsxNn0+XG4gICAgICAgICAgICA8aDM+e3QoJ0NyZWF0ZSBhIG5ldyBjaGFydCcpfTwvaDM+XG4gICAgICAgICAgPC9Db2w+XG4gICAgICAgICAgPENvbCBtZD17OH0geHM9ezh9IHN0eWxlPXt7IHRleHRBbGlnbjogJ3JpZ2h0JyB9fT5cbiAgICAgICAgICAgIDxCdXR0b24gY3NzPXtbXG4gICAgICAgICAgICAgICAgY3NzU3RhdGljLFxuICAgICAgICAgICAgICAgIGNzcyBgXG4gICAgICAgICAgICAgICAgICBhbGlnbi1zZWxmOiBmbGV4LWVuZDtcbiAgICAgICAgICAgICAgICBgLFxuICAgICAgICAgICAgXX0gYnV0dG9uU3R5bGU9XCJwcmltYXJ5XCIgZGlzYWJsZWQ9e3RoaXMuaXNCdG5EaXNhYmxlZCgpfSBvbkNsaWNrPXt0aGlzLmdvdG9TbGljZX0+XG4gICAgICAgICAgICAgIHt0KCdDcmVhdGUgbmV3IGNoYXJ0Jyl9XG4gICAgICAgICAgICA8L0J1dHRvbj5cbiAgICAgICAgICA8L0NvbD5cbiAgICAgICAgPC9Sb3c+XG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF0YXNldFwiPlxuICAgICAgICAgIDxTZWxlY3QgYXV0b0ZvY3VzIGFyaWFMYWJlbD17dCgnRGF0YXNldCcpfSBuYW1lPVwic2VsZWN0LWRhdGFzb3VyY2VcIiBoZWFkZXI9ezxGb3JtTGFiZWwgcmVxdWlyZWQ+e3QoJ0Nob29zZSBhIGRhdGFzZXQnKX08L0Zvcm1MYWJlbD59IG9uQ2hhbmdlPXt0aGlzLmNoYW5nZURhdGFzb3VyY2V9IG9wdGlvbnM9e3RoaXMucHJvcHMuZGF0YXNvdXJjZXN9IHBsYWNlaG9sZGVyPXt0KCdDaG9vc2UgYSBkYXRhc2V0Jyl9IHNob3dTZWFyY2ggdmFsdWU9e3RoaXMuc3RhdGUuZGF0YXNvdXJjZVZhbHVlfS8+XG4gICAgICAgICAgPHNwYW4+XG4gICAgICAgICAgICB7dCgnSW5zdHJ1Y3Rpb25zIHRvIGFkZCBhIGRhdGFzZXQgYXJlIGF2YWlsYWJsZSBpbiB0aGUgU3BvdHJpeCB0dXRvcmlhbC4nKX17JyAnfVxuICAgICAgICAgICAgPGEgaHJlZj1cImh0dHBzOi8vY2l1c2ppLmdpdGJvb2suaW8vc3BvdHJpeC9jcmVhdGluZy1jaGFydHMvY3JlYXRpbmcteW91ci1jaGFydHNcIiByZWw9XCJub29wZW5lciBub3JlZmVycmVyXCIgdGFyZ2V0PVwiX2JsYW5rXCI+XG4gICAgICAgICAgICAgIDxpIGNsYXNzTmFtZT1cImZhIGZhLWV4dGVybmFsLWxpbmtcIi8+XG4gICAgICAgICAgICA8L2E+XG4gICAgICAgICAgPC9zcGFuPlxuICAgICAgICA8L2Rpdj5cbiAgICAgICAgPFN0eWxlZFZpelR5cGVHYWxsZXJ5IG9uQ2hhbmdlPXt0aGlzLmNoYW5nZVZpc1R5cGV9IHNlbGVjdGVkVml6PXt0aGlzLnN0YXRlLnZpc1R5cGV9Lz5cbiAgICAgIDwvU3R5bGVkQ29udGFpbmVyPik7XG4gICAgfVxufVxuIl19 */\"],\n      buttonStyle: \"primary\", disabled: this.isBtnDisabled(), onClick: this.gotoSlice },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Create new chart')))),\n\n\n\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(\"div\", { className: \"dataset\" },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_components__WEBPACK_IMPORTED_MODULE_4__[\"Select\"], { autoFocus: true, ariaLabel: Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Dataset'), name: \"select-datasource\", header: Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(src_components_Form__WEBPACK_IMPORTED_MODULE_8__[\"FormLabel\"], { required: true }, Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Choose a dataset')), onChange: this.changeDatasource, options: this.props.datasources, placeholder: Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Choose a dataset'), showSearch: true, value: this.state.datasourceValue }),\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(\"span\", null,\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_7__[\"t\"])('Instructions to add a dataset are available in the Spotrix tutorial.'), ' ',\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(\"a\", { href: \"https://ciusji.gitbook.io/spotrix/creating-charts/creating-your-charts\", rel: \"noopener noreferrer\", target: \"_blank\" },\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(\"i\", { className: \"fa fa-external-link\" })))),\n\n\n\n    Object(_superset_ui_core__WEBPACK_IMPORTED_MODULE_6__[\"jsx\"])(StyledVizTypeGallery, { onChange: this.changeVisType, selectedViz: this.state.visType }));\n\n  } // @ts-ignore\n  __reactstandin__regenerateByEval(key, code) {// @ts-ignore\n    this[key] = eval(code);}};(function () {var reactHotLoader = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default : undefined;if (!reactHotLoader) {return;}reactHotLoader.register(ESTIMATED_NAV_HEIGHT, \"ESTIMATED_NAV_HEIGHT\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(APP_HEADER_HEIGHT, \"APP_HEADER_HEIGHT\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(APP_NAV_WIDTH, \"APP_NAV_WIDTH\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(StyledContainer, \"StyledContainer\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(cssStatic, \"cssStatic\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(StyledVizTypeGallery, \"StyledVizTypeGallery\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");reactHotLoader.register(AddSliceContainer, \"AddSliceContainer\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/AddSliceContainer.tsx\");})();;(function () {var leaveModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.leaveModule : undefined;leaveModule && leaveModule(module);})();\n/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./../../node_modules/webpack/buildin/harmony-module.js */ \"./node_modules/webpack/buildin/harmony-module.js\")(module)))//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvYWRkU2xpY2UvQWRkU2xpY2VDb250YWluZXIudHN4LmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL2FkZFNsaWNlL0FkZFNsaWNlQ29udGFpbmVyLnRzeD80MDc2Il0sInNvdXJjZXNDb250ZW50IjpbIi8qKlxuICogTGljZW5zZWQgdG8gdGhlIEFwYWNoZSBTb2Z0d2FyZSBGb3VuZGF0aW9uIChBU0YpIHVuZGVyIG9uZVxuICogb3IgbW9yZSBjb250cmlidXRvciBsaWNlbnNlIGFncmVlbWVudHMuICBTZWUgdGhlIE5PVElDRSBmaWxlXG4gKiBkaXN0cmlidXRlZCB3aXRoIHRoaXMgd29yayBmb3IgYWRkaXRpb25hbCBpbmZvcm1hdGlvblxuICogcmVnYXJkaW5nIGNvcHlyaWdodCBvd25lcnNoaXAuICBUaGUgQVNGIGxpY2Vuc2VzIHRoaXMgZmlsZVxuICogdG8geW91IHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZVxuICogXCJMaWNlbnNlXCIpOyB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlXG4gKiB3aXRoIHRoZSBMaWNlbnNlLiAgWW91IG1heSBvYnRhaW4gYSBjb3B5IG9mIHRoZSBMaWNlbnNlIGF0XG4gKlxuICogICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjBcbiAqXG4gKiBVbmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsXG4gKiBzb2Z0d2FyZSBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhblxuICogXCJBUyBJU1wiIEJBU0lTLCBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTllcbiAqIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuICBTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZVxuICogc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZCBsaW1pdGF0aW9uc1xuICogdW5kZXIgdGhlIExpY2Vuc2UuXG4gKi9cbmltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgQnV0dG9uIGZyb20gJ3NyYy9jb21wb25lbnRzL0J1dHRvbic7XG5pbXBvcnQgeyBTZWxlY3QgfSBmcm9tICdzcmMvY29tcG9uZW50cyc7XG5pbXBvcnQgeyBjc3MsIHN0eWxlZCwgdCB9IGZyb20gJ0BzdXBlcnNldC11aS9jb3JlJztcbmltcG9ydCB7IEZvcm1MYWJlbCB9IGZyb20gJ3NyYy9jb21wb25lbnRzL0Zvcm0nO1xuXG5pbXBvcnQgVml6VHlwZUdhbGxlcnksIHtcbiAgTUFYX0FEVklTQUJMRV9WSVpfR0FMTEVSWV9XSURUSCxcbn0gZnJvbSAnc3JjL2V4cGxvcmUvY29tcG9uZW50cy9jb250cm9scy9WaXpUeXBlQ29udHJvbC9WaXpUeXBlR2FsbGVyeSc7XG5pbXBvcnQgeyBDb2wsIFJvdyB9IGZyb20gJ3NyYy9jb21tb24vY29tcG9uZW50cyc7XG5cbmludGVyZmFjZSBEYXRhc291cmNlIHtcbiAgbGFiZWw6IHN0cmluZztcbiAgdmFsdWU6IHN0cmluZztcbn1cblxuZXhwb3J0IHR5cGUgQWRkU2xpY2VDb250YWluZXJQcm9wcyA9IHtcbiAgZGF0YXNvdXJjZXM6IERhdGFzb3VyY2VbXTtcbn07XG5cbmV4cG9ydCB0eXBlIEFkZFNsaWNlQ29udGFpbmVyU3RhdGUgPSB7XG4gIGRhdGFzb3VyY2VJZD86IHN0cmluZztcbiAgZGF0YXNvdXJjZVR5cGU/OiBzdHJpbmc7XG4gIGRhdGFzb3VyY2VWYWx1ZT86IHN0cmluZztcbiAgdmlzVHlwZTogc3RyaW5nIHwgbnVsbDtcbn07XG5cbmNvbnN0IEVTVElNQVRFRF9OQVZfSEVJR0hUID0gJzU2cHgnO1xuY29uc3QgQVBQX0hFQURFUl9IRUlHSFQgPSAnNDdweCc7XG5jb25zdCBBUFBfTkFWX1dJRFRIID0gJzYwcHgnO1xuXG5jb25zdCBTdHlsZWRDb250YWluZXIgPSBzdHlsZWQuZGl2YFxuICAkeyh7IHRoZW1lIH0pID0+IGBcbiAgICBmbGV4OiAxIDEgYXV0bztcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIHdpZHRoOiBjYWxjKDEwMHZ3IC0gJHtBUFBfTkFWX1dJRFRIfSk7XG4gICAgbWF4LXdpZHRoOiAke01BWF9BRFZJU0FCTEVfVklaX0dBTExFUllfV0lEVEh9cHg7XG4gICAgbWF4LWhlaWdodDogY2FsYygxMDB2aCAtICR7RVNUSU1BVEVEX05BVl9IRUlHSFR9IC0gJHtBUFBfSEVBREVSX0hFSUdIVH0pO1xuICAgIGJvcmRlci1yYWRpdXM6ICR7dGhlbWUuZ3JpZFVuaXR9cHg7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJHt0aGVtZS5jb2xvcnMuZ3JheXNjYWxlLmxpZ2h0NX07XG4gICAgbWFyZ2luLWxlZnQ6IGF1dG87XG4gICAgbWFyZ2luLXJpZ2h0OiBhdXRvO1xuICAgIHBhZGRpbmctbGVmdDogJHt0aGVtZS5ncmlkVW5pdCAqIDR9cHg7XG4gICAgcGFkZGluZy1yaWdodDogJHt0aGVtZS5ncmlkVW5pdCAqIDR9cHg7XG4gICAgcGFkZGluZy1ib3R0b206ICR7dGhlbWUuZ3JpZFVuaXQgKiA0fXB4O1xuXG4gICAgaDMge1xuICAgICAgcGFkZGluZy1ib3R0b206ICR7dGhlbWUuZ3JpZFVuaXQgKiAzfXB4O1xuICAgIH1cblxuICAgICYgLmRhdGFzZXQge1xuICAgICAgZGlzcGxheTogZmxleDtcbiAgICAgIGZsZXgtZGlyZWN0aW9uOiByb3c7XG4gICAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuXG4gICAgICAmID4gZGl2IHtcbiAgICAgICAgbWluLXdpZHRoOiAyMDBweDtcbiAgICAgICAgd2lkdGg6IDMwMHB4O1xuICAgICAgfVxuXG4gICAgICAmID4gc3BhbiB7XG4gICAgICAgIGNvbG9yOiAke3RoZW1lLmNvbG9ycy5ncmF5c2NhbGUubGlnaHQxfTtcbiAgICAgICAgbWFyZ2luLWxlZnQ6ICR7dGhlbWUuZ3JpZFVuaXQgKiA0fXB4O1xuICAgICAgICBtYXJnaW4tdG9wOiAke3RoZW1lLmdyaWRVbml0ICogNn1weDtcbiAgICAgIH1cbiAgICB9XG4gIGB9XG5gO1xuXG5jb25zdCBjc3NTdGF0aWMgPSBjc3NgXG4gIGZsZXg6IDAgMCBhdXRvO1xuYDtcblxuY29uc3QgU3R5bGVkVml6VHlwZUdhbGxlcnkgPSBzdHlsZWQoVml6VHlwZUdhbGxlcnkpYFxuICAkeyh7IHRoZW1lIH0pID0+IGBcbiAgICBib3JkZXI6IDFweCBzb2xpZCAke3RoZW1lLmNvbG9ycy5ncmF5c2NhbGUubGlnaHQyfTtcbiAgICBib3JkZXItcmFkaXVzOiAke3RoZW1lLmdyaWRVbml0fXB4O1xuICAgIG1hcmdpbjogJHt0aGVtZS5ncmlkVW5pdCAqIDN9cHggMHB4O1xuICAgIGZsZXg6IDEgMSBhdXRvO1xuICBgfVxuYDtcblxuZXhwb3J0IGRlZmF1bHQgY2xhc3MgQWRkU2xpY2VDb250YWluZXIgZXh0ZW5kcyBSZWFjdC5QdXJlQ29tcG9uZW50PFxuICBBZGRTbGljZUNvbnRhaW5lclByb3BzLFxuICBBZGRTbGljZUNvbnRhaW5lclN0YXRlXG4+IHtcbiAgY29uc3RydWN0b3IocHJvcHM6IEFkZFNsaWNlQ29udGFpbmVyUHJvcHMpIHtcbiAgICBzdXBlcihwcm9wcyk7XG4gICAgdGhpcy5zdGF0ZSA9IHtcbiAgICAgIHZpc1R5cGU6IG51bGwsXG4gICAgfTtcblxuICAgIHRoaXMuY2hhbmdlRGF0YXNvdXJjZSA9IHRoaXMuY2hhbmdlRGF0YXNvdXJjZS5iaW5kKHRoaXMpO1xuICAgIHRoaXMuY2hhbmdlVmlzVHlwZSA9IHRoaXMuY2hhbmdlVmlzVHlwZS5iaW5kKHRoaXMpO1xuICAgIHRoaXMuZ290b1NsaWNlID0gdGhpcy5nb3RvU2xpY2UuYmluZCh0aGlzKTtcbiAgfVxuXG4gIGV4cGxvcmVVcmwoKSB7XG4gICAgY29uc3QgZm9ybURhdGEgPSBlbmNvZGVVUklDb21wb25lbnQoXG4gICAgICBKU09OLnN0cmluZ2lmeSh7XG4gICAgICAgIHZpel90eXBlOiB0aGlzLnN0YXRlLnZpc1R5cGUsXG4gICAgICAgIGRhdGFzb3VyY2U6IHRoaXMuc3RhdGUuZGF0YXNvdXJjZVZhbHVlLFxuICAgICAgfSksXG4gICAgKTtcbiAgICByZXR1cm4gYC9zcG90cml4L2V4cGxvcmUvP2Zvcm1fZGF0YT0ke2Zvcm1EYXRhfWA7XG4gIH1cblxuICBnb3RvU2xpY2UoKSB7XG4gICAgd2luZG93LmxvY2F0aW9uLmhyZWYgPSB0aGlzLmV4cGxvcmVVcmwoKTtcbiAgfVxuXG4gIGNoYW5nZURhdGFzb3VyY2UodmFsdWU6IHN0cmluZykge1xuICAgIHRoaXMuc2V0U3RhdGUoe1xuICAgICAgZGF0YXNvdXJjZVZhbHVlOiB2YWx1ZSxcbiAgICAgIGRhdGFzb3VyY2VJZDogdmFsdWUuc3BsaXQoJ19fJylbMF0sXG4gICAgfSk7XG4gIH1cblxuICBjaGFuZ2VWaXNUeXBlKHZpc1R5cGU6IHN0cmluZyB8IG51bGwpIHtcbiAgICB0aGlzLnNldFN0YXRlKHsgdmlzVHlwZSB9KTtcbiAgfVxuXG4gIGlzQnRuRGlzYWJsZWQoKSB7XG4gICAgcmV0dXJuICEodGhpcy5zdGF0ZS5kYXRhc291cmNlSWQgJiYgdGhpcy5zdGF0ZS52aXNUeXBlKTtcbiAgfVxuXG4gIHJlbmRlcigpIHtcbiAgICByZXR1cm4gKFxuICAgICAgPFN0eWxlZENvbnRhaW5lcj5cbiAgICAgICAgPFJvdyBhbGlnbj1cIm1pZGRsZVwiPlxuICAgICAgICAgIDxDb2wgbWQ9ezE2fSB4cz17MTZ9PlxuICAgICAgICAgICAgPGgzPnt0KCdDcmVhdGUgYSBuZXcgY2hhcnQnKX08L2gzPlxuICAgICAgICAgIDwvQ29sPlxuICAgICAgICAgIDxDb2wgbWQ9ezh9IHhzPXs4fSBzdHlsZT17eyB0ZXh0QWxpZ246ICdyaWdodCcgfX0+XG4gICAgICAgICAgICA8QnV0dG9uXG4gICAgICAgICAgICAgIGNzcz17W1xuICAgICAgICAgICAgICAgIGNzc1N0YXRpYyxcbiAgICAgICAgICAgICAgICBjc3NgXG4gICAgICAgICAgICAgICAgICBhbGlnbi1zZWxmOiBmbGV4LWVuZDtcbiAgICAgICAgICAgICAgICBgLFxuICAgICAgICAgICAgICBdfVxuICAgICAgICAgICAgICBidXR0b25TdHlsZT1cInByaW1hcnlcIlxuICAgICAgICAgICAgICBkaXNhYmxlZD17dGhpcy5pc0J0bkRpc2FibGVkKCl9XG4gICAgICAgICAgICAgIG9uQ2xpY2s9e3RoaXMuZ290b1NsaWNlfVxuICAgICAgICAgICAgPlxuICAgICAgICAgICAgICB7dCgnQ3JlYXRlIG5ldyBjaGFydCcpfVxuICAgICAgICAgICAgPC9CdXR0b24+XG4gICAgICAgICAgPC9Db2w+XG4gICAgICAgIDwvUm93PlxuICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImRhdGFzZXRcIj5cbiAgICAgICAgICA8U2VsZWN0XG4gICAgICAgICAgICBhdXRvRm9jdXNcbiAgICAgICAgICAgIGFyaWFMYWJlbD17dCgnRGF0YXNldCcpfVxuICAgICAgICAgICAgbmFtZT1cInNlbGVjdC1kYXRhc291cmNlXCJcbiAgICAgICAgICAgIGhlYWRlcj17PEZvcm1MYWJlbCByZXF1aXJlZD57dCgnQ2hvb3NlIGEgZGF0YXNldCcpfTwvRm9ybUxhYmVsPn1cbiAgICAgICAgICAgIG9uQ2hhbmdlPXt0aGlzLmNoYW5nZURhdGFzb3VyY2V9XG4gICAgICAgICAgICBvcHRpb25zPXt0aGlzLnByb3BzLmRhdGFzb3VyY2VzfVxuICAgICAgICAgICAgcGxhY2Vob2xkZXI9e3QoJ0Nob29zZSBhIGRhdGFzZXQnKX1cbiAgICAgICAgICAgIHNob3dTZWFyY2hcbiAgICAgICAgICAgIHZhbHVlPXt0aGlzLnN0YXRlLmRhdGFzb3VyY2VWYWx1ZX1cbiAgICAgICAgICAvPlxuICAgICAgICAgIDxzcGFuPlxuICAgICAgICAgICAge3QoXG4gICAgICAgICAgICAgICdJbnN0cnVjdGlvbnMgdG8gYWRkIGEgZGF0YXNldCBhcmUgYXZhaWxhYmxlIGluIHRoZSBTcG90cml4IHR1dG9yaWFsLicsXG4gICAgICAgICAgICApfXsnICd9XG4gICAgICAgICAgICA8YVxuICAgICAgICAgICAgICBocmVmPVwiaHR0cHM6Ly9jaXVzamkuZ2l0Ym9vay5pby9zcG90cml4L2NyZWF0aW5nLWNoYXJ0cy9jcmVhdGluZy15b3VyLWNoYXJ0c1wiXG4gICAgICAgICAgICAgIHJlbD1cIm5vb3BlbmVyIG5vcmVmZXJyZXJcIlxuICAgICAgICAgICAgICB0YXJnZXQ9XCJfYmxhbmtcIlxuICAgICAgICAgICAgPlxuICAgICAgICAgICAgICA8aSBjbGFzc05hbWU9XCJmYSBmYS1leHRlcm5hbC1saW5rXCIgLz5cbiAgICAgICAgICAgIDwvYT5cbiAgICAgICAgICA8L3NwYW4+XG4gICAgICAgIDwvZGl2PlxuICAgICAgICA8U3R5bGVkVml6VHlwZUdhbGxlcnlcbiAgICAgICAgICBvbkNoYW5nZT17dGhpcy5jaGFuZ2VWaXNUeXBlfVxuICAgICAgICAgIHNlbGVjdGVkVml6PXt0aGlzLnN0YXRlLnZpc1R5cGV9XG4gICAgICAgIC8+XG4gICAgICA8L1N0eWxlZENvbnRhaW5lcj5cbiAgICApO1xuICB9XG59XG4iXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBaUJBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBR0E7QUFrQkE7QUFDQTtBQUNBO0FBRUE7QUFDQTs7Ozs7QUFLQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFHQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7Ozs7Ozs7Ozs7Ozs7QUFjQTtBQUNBO0FBQ0E7OztBQUdBO0FBQ0E7QUFFQTs7QUFFQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUVBO0FBSUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTs7QUFFQTtBQUVBO0FBSUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBV0E7QUFDQTtBQUdBO0FBS0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBS0E7QUEvRkE7QUFBQTtBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/addSlice/AddSliceContainer.tsx\n");

/***/ }),

/***/ "./src/addSlice/App.tsx":
/*!******************************!*\
  !*** ./src/addSlice/App.tsx ***!
  \******************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* WEBPACK VAR INJECTION */(function(module) {/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var react_hot_loader_root__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-hot-loader/root */ \"./node_modules/react-hot-loader/root.js\");\n/* harmony import */ var react_hot_loader_root__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_hot_loader_root__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _superset_ui_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @superset-ui/core */ \"./node_modules/@emotion/react/dist/emotion-element-4fbd89c5.browser.esm.js\");\n/* harmony import */ var _setup_setupApp__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../setup/setupApp */ \"./src/setup/setupApp.ts\");\n/* harmony import */ var _setup_setupPlugins__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../setup/setupPlugins */ \"./src/setup/setupPlugins.ts\");\n/* harmony import */ var _components_DynamicPlugins__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../components/DynamicPlugins */ \"./src/components/DynamicPlugins/index.tsx\");\n/* harmony import */ var _AddSliceContainer__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./AddSliceContainer */ \"./src/addSlice/AddSliceContainer.tsx\");\n/* harmony import */ var _featureFlags__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../featureFlags */ \"./src/featureFlags.ts\");\n/* harmony import */ var _preamble__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../preamble */ \"./src/preamble.ts\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @emotion/react */ \"./node_modules/@emotion/react/dist/emotion-react.browser.esm.js\");\n(function () {var enterModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.enterModule : undefined;enterModule && enterModule(module);})();var __signature__ = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default.signature : function (a) {return a;}; /**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\n\n\n\n\n\n\nObject(_setup_setupApp__WEBPACK_IMPORTED_MODULE_3__[\"default\"])();\nObject(_setup_setupPlugins__WEBPACK_IMPORTED_MODULE_4__[\"default\"])();\nconst addSliceContainer = document.getElementById('app');\nconst bootstrapData = JSON.parse((addSliceContainer == null ? void 0 : addSliceContainer.getAttribute('data-bootstrap')) || '{}');\nObject(_featureFlags__WEBPACK_IMPORTED_MODULE_7__[\"initFeatureFlags\"])(bootstrapData.common.feature_flags);\nconst App = () => Object(_emotion_react__WEBPACK_IMPORTED_MODULE_9__[\"jsx\"])(_superset_ui_core__WEBPACK_IMPORTED_MODULE_2__[\"a\"], { theme: _preamble__WEBPACK_IMPORTED_MODULE_8__[\"theme\"] },\nObject(_emotion_react__WEBPACK_IMPORTED_MODULE_9__[\"jsx\"])(_components_DynamicPlugins__WEBPACK_IMPORTED_MODULE_5__[\"DynamicPluginProvider\"], null,\nObject(_emotion_react__WEBPACK_IMPORTED_MODULE_9__[\"jsx\"])(_AddSliceContainer__WEBPACK_IMPORTED_MODULE_6__[\"default\"], { datasources: bootstrapData.datasources })));const _default =\n\n\nObject(react_hot_loader_root__WEBPACK_IMPORTED_MODULE_1__[\"hot\"])(App);/* harmony default export */ __webpack_exports__[\"default\"] = (_default);;(function () {var reactHotLoader = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default : undefined;if (!reactHotLoader) {return;}reactHotLoader.register(addSliceContainer, \"addSliceContainer\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/App.tsx\");reactHotLoader.register(bootstrapData, \"bootstrapData\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/App.tsx\");reactHotLoader.register(App, \"App\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/App.tsx\");reactHotLoader.register(_default, \"default\", \"/Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/App.tsx\");})();;(function () {var leaveModule = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.leaveModule : undefined;leaveModule && leaveModule(module);})();\n/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./../../node_modules/webpack/buildin/harmony-module.js */ \"./node_modules/webpack/buildin/harmony-module.js\")(module)))//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvYWRkU2xpY2UvQXBwLnRzeC5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy8uL3NyYy9hZGRTbGljZS9BcHAudHN4P2UwMTIiXSwic291cmNlc0NvbnRlbnQiOlsiLyoqXG4gKiBMaWNlbnNlZCB0byB0aGUgQXBhY2hlIFNvZnR3YXJlIEZvdW5kYXRpb24gKEFTRikgdW5kZXIgb25lXG4gKiBvciBtb3JlIGNvbnRyaWJ1dG9yIGxpY2Vuc2UgYWdyZWVtZW50cy4gIFNlZSB0aGUgTk9USUNFIGZpbGVcbiAqIGRpc3RyaWJ1dGVkIHdpdGggdGhpcyB3b3JrIGZvciBhZGRpdGlvbmFsIGluZm9ybWF0aW9uXG4gKiByZWdhcmRpbmcgY29weXJpZ2h0IG93bmVyc2hpcC4gIFRoZSBBU0YgbGljZW5zZXMgdGhpcyBmaWxlXG4gKiB0byB5b3UgdW5kZXIgdGhlIEFwYWNoZSBMaWNlbnNlLCBWZXJzaW9uIDIuMCAodGhlXG4gKiBcIkxpY2Vuc2VcIik7IHlvdSBtYXkgbm90IHVzZSB0aGlzIGZpbGUgZXhjZXB0IGluIGNvbXBsaWFuY2VcbiAqIHdpdGggdGhlIExpY2Vuc2UuICBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXRcbiAqXG4gKiAgIGh0dHA6Ly93d3cuYXBhY2hlLm9yZy9saWNlbnNlcy9MSUNFTlNFLTIuMFxuICpcbiAqIFVubGVzcyByZXF1aXJlZCBieSBhcHBsaWNhYmxlIGxhdyBvciBhZ3JlZWQgdG8gaW4gd3JpdGluZyxcbiAqIHNvZnR3YXJlIGRpc3RyaWJ1dGVkIHVuZGVyIHRoZSBMaWNlbnNlIGlzIGRpc3RyaWJ1dGVkIG9uIGFuXG4gKiBcIkFTIElTXCIgQkFTSVMsIFdJVEhPVVQgV0FSUkFOVElFUyBPUiBDT05ESVRJT05TIE9GIEFOWVxuICogS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4gIFNlZSB0aGUgTGljZW5zZSBmb3IgdGhlXG4gKiBzcGVjaWZpYyBsYW5ndWFnZSBnb3Zlcm5pbmcgcGVybWlzc2lvbnMgYW5kIGxpbWl0YXRpb25zXG4gKiB1bmRlciB0aGUgTGljZW5zZS5cbiAqL1xuaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IGhvdCB9IGZyb20gJ3JlYWN0LWhvdC1sb2FkZXIvcm9vdCc7XG5pbXBvcnQgeyBUaGVtZVByb3ZpZGVyIH0gZnJvbSAnQHN1cGVyc2V0LXVpL2NvcmUnO1xuaW1wb3J0IHNldHVwQXBwIGZyb20gJy4uL3NldHVwL3NldHVwQXBwJztcbmltcG9ydCBzZXR1cFBsdWdpbnMgZnJvbSAnLi4vc2V0dXAvc2V0dXBQbHVnaW5zJztcbmltcG9ydCB7IER5bmFtaWNQbHVnaW5Qcm92aWRlciB9IGZyb20gJy4uL2NvbXBvbmVudHMvRHluYW1pY1BsdWdpbnMnO1xuaW1wb3J0IEFkZFNsaWNlQ29udGFpbmVyIGZyb20gJy4vQWRkU2xpY2VDb250YWluZXInO1xuaW1wb3J0IHsgaW5pdEZlYXR1cmVGbGFncyB9IGZyb20gJy4uL2ZlYXR1cmVGbGFncyc7XG5pbXBvcnQgeyB0aGVtZSB9IGZyb20gJy4uL3ByZWFtYmxlJztcblxuc2V0dXBBcHAoKTtcbnNldHVwUGx1Z2lucygpO1xuXG5jb25zdCBhZGRTbGljZUNvbnRhaW5lciA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKTtcbmNvbnN0IGJvb3RzdHJhcERhdGEgPSBKU09OLnBhcnNlKFxuICBhZGRTbGljZUNvbnRhaW5lcj8uZ2V0QXR0cmlidXRlKCdkYXRhLWJvb3RzdHJhcCcpIHx8ICd7fScsXG4pO1xuXG5pbml0RmVhdHVyZUZsYWdzKGJvb3RzdHJhcERhdGEuY29tbW9uLmZlYXR1cmVfZmxhZ3MpO1xuXG5jb25zdCBBcHAgPSAoKSA9PiAoXG4gIDxUaGVtZVByb3ZpZGVyIHRoZW1lPXt0aGVtZX0+XG4gICAgPER5bmFtaWNQbHVnaW5Qcm92aWRlcj5cbiAgICAgIDxBZGRTbGljZUNvbnRhaW5lciBkYXRhc291cmNlcz17Ym9vdHN0cmFwRGF0YS5kYXRhc291cmNlc30gLz5cbiAgICA8L0R5bmFtaWNQbHVnaW5Qcm92aWRlcj5cbiAgPC9UaGVtZVByb3ZpZGVyPlxuKTtcblxuZXhwb3J0IGRlZmF1bHQgaG90KEFwcCk7XG4iXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBaUJBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUVBO0FBQ0E7QUFJQTtBQUVBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFHQTtBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/addSlice/App.tsx\n");

/***/ }),

/***/ "./src/addSlice/index.tsx":
/*!********************************!*\
  !*** ./src/addSlice/index.tsx ***!
  \********************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-dom */ \"./node_modules/@hot-loader/react-dom/index.js\");\n/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _App__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./App */ \"./src/addSlice/App.tsx\");\n/* harmony import */ var _emotion_react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @emotion/react */ \"./node_modules/@emotion/react/dist/emotion-react.browser.esm.js\");\nvar __signature__ = typeof reactHotLoaderGlobal !== 'undefined' ? reactHotLoaderGlobal.default.signature : function (a) {return a;}; /**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\nreact_dom__WEBPACK_IMPORTED_MODULE_1___default.a.render(Object(_emotion_react__WEBPACK_IMPORTED_MODULE_3__[\"jsx\"])(_App__WEBPACK_IMPORTED_MODULE_2__[\"default\"], null), document.getElementById('app'));//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvYWRkU2xpY2UvaW5kZXgudHN4LmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL2FkZFNsaWNlL2luZGV4LnRzeD9kNWY5Il0sInNvdXJjZXNDb250ZW50IjpbIi8qKlxuICogTGljZW5zZWQgdG8gdGhlIEFwYWNoZSBTb2Z0d2FyZSBGb3VuZGF0aW9uIChBU0YpIHVuZGVyIG9uZVxuICogb3IgbW9yZSBjb250cmlidXRvciBsaWNlbnNlIGFncmVlbWVudHMuICBTZWUgdGhlIE5PVElDRSBmaWxlXG4gKiBkaXN0cmlidXRlZCB3aXRoIHRoaXMgd29yayBmb3IgYWRkaXRpb25hbCBpbmZvcm1hdGlvblxuICogcmVnYXJkaW5nIGNvcHlyaWdodCBvd25lcnNoaXAuICBUaGUgQVNGIGxpY2Vuc2VzIHRoaXMgZmlsZVxuICogdG8geW91IHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZVxuICogXCJMaWNlbnNlXCIpOyB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlXG4gKiB3aXRoIHRoZSBMaWNlbnNlLiAgWW91IG1heSBvYnRhaW4gYSBjb3B5IG9mIHRoZSBMaWNlbnNlIGF0XG4gKlxuICogICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjBcbiAqXG4gKiBVbmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsXG4gKiBzb2Z0d2FyZSBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhblxuICogXCJBUyBJU1wiIEJBU0lTLCBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTllcbiAqIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuICBTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZVxuICogc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZCBsaW1pdGF0aW9uc1xuICogdW5kZXIgdGhlIExpY2Vuc2UuXG4gKi9cbmltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgUmVhY3RET00gZnJvbSAncmVhY3QtZG9tJztcbmltcG9ydCBBcHAgZnJvbSAnLi9BcHAnO1xuXG5SZWFjdERPTS5yZW5kZXIoPEFwcCAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTtcbiJdLCJtYXBwaW5ncyI6IkFBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFpQkE7QUFDQTtBQUNBO0FBQ0E7QUFFQSIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/addSlice/index.tsx\n");

/***/ }),

/***/ 10:
/*!********************************************************************************************************!*\
  !*** multi webpack-dev-server/client?http://localhost:9000 ./src/preamble.ts ./src/addSlice/index.tsx ***!
  \********************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(/*! webpack-dev-server/client?http://localhost:9000 */"./node_modules/webpack-dev-server/client/index.js?http://localhost:9000");
__webpack_require__(/*! /Users/admin/Git/Public/spotrix/spotrix-frontend/src/preamble.ts */"./src/preamble.ts");
module.exports = __webpack_require__(/*! /Users/admin/Git/Public/spotrix/spotrix-frontend/src/addSlice/index.tsx */"./src/addSlice/index.tsx");


/***/ })

/******/ });