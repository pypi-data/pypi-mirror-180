(self["webpackChunkpyannotebook"] = self["webpackChunkpyannotebook"] || []).push([["lib_widget_js"],{

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// MIT License
//
// Copyright (c) 2022- CNRS
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

// MIT License
//
// Copyright (c) 2022- CNRS
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LabelsView = exports.LabelsModel = exports.WavesurferView = exports.WavesurferModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
const wavesurfer_js_1 = __importDefault(__webpack_require__(/*! wavesurfer.js */ "webpack/sharing/consume/default/wavesurfer.js/wavesurfer.js"));
const regions_1 = __importDefault(__webpack_require__(/*! wavesurfer.js/src/plugin/regions */ "./node_modules/wavesurfer.js/src/plugin/regions/index.js"));
const minimap_1 = __importDefault(__webpack_require__(/*! wavesurfer.js/src/plugin/minimap */ "./node_modules/wavesurfer.js/src/plugin/minimap/index.js"));
class WavesurferModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: WavesurferModel.model_name, _model_module: WavesurferModel.model_module, _model_module_version: WavesurferModel.model_module_version, _view_name: WavesurferModel.view_name, _view_module: WavesurferModel.view_module, _view_module_version: WavesurferModel.view_module_version });
    }
}
exports.WavesurferModel = WavesurferModel;
WavesurferModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
WavesurferModel.model_name = 'WavesurferModel';
WavesurferModel.model_module = version_1.MODULE_NAME;
WavesurferModel.model_module_version = version_1.MODULE_VERSION;
WavesurferModel.view_name = 'WavesurferView';
WavesurferModel.view_module = version_1.MODULE_NAME;
WavesurferModel.view_module_version = version_1.MODULE_VERSION;
class WavesurferView extends base_1.DOMWidgetView {
    to_blob(b64) {
        // https://stackoverflow.com/questions/27980612/converting-base64-to-blob-in-javascript
        // https://ionic.io/blog/converting-a-base64-string-to-a-blob-in-javascript
        const byteString = atob(b64.split(',')[1]);
        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }
        return new Blob([ab], { type: 'audio/x-wav' });
    }
    render() {
        this.wavesurfer_minimap = document.createElement('div');
        this.wavesurfer_container = document.createElement('div');
        this.el.appendChild(this.wavesurfer_minimap);
        this.el.appendChild(this.wavesurfer_container);
        this._wavesurfer = wavesurfer_js_1.default.create({
            container: this.wavesurfer_container,
            barGap: 1,
            barHeight: 1,
            // barMinHeight: null,
            barRadius: 2,
            barWidth: 2,
            scrollParent: true,
            minPxPerSec: 20,
            plugins: [
                regions_1.default.create({
                    regionsMinLength: 0,
                    /** Enable creating regions by dragging with the mouse. */
                    dragSelection: true,
                    /** Regions that should be added upon initialisation. */
                    regions: undefined,
                    /** The sensitivity of the mouse dragging (default: 2). */
                    slop: 2,
                    /** Snap the regions to a grid of the specified multiples in seconds? */
                    snapToGridInterval: undefined,
                    /** Shift the snap-to-grid by the specified seconds. May also be negative. */
                    snapToGridOffset: undefined,
                    /** Maximum number of regions that may be created by the user at one time. */
                    maxRegions: undefined,
                    /** Allows custom formating for region tooltip. */
                    formatTimeCallback: undefined,
                    /** from container edges' Optional width for edgeScroll to start (default: 5% of viewport width). */
                    edgeScrollWidth: undefined,
                }),
                minimap_1.default.create({
                    container: this.wavesurfer_minimap,
                    waveColor: '#777',
                    progressColor: '#222',
                    height: 20,
                }),
            ],
        });
        this._wavesurfer.on('region-update-end', this.on_region_update_end.bind(this));
        this._wavesurfer.on('region-created', this.on_region_created.bind(this));
        this._wavesurfer.on('audioprocess', this.on_audioprocess.bind(this));
        this._wavesurfer.on('seek', this.on_seek.bind(this));
        this._wavesurfer.on('finish', this.on_finish.bind(this));
        this._wavesurfer.on('region-click', this.on_region_click.bind(this));
        this._wavesurfer.on('zoom', this.on_zoom.bind(this));
        this.update_audio();
        this.model.on('change:audio', this.update_audio, this);
        this.model.on('change:regions', this.update_regions, this);
        this.model.on('change:colors', this.update_colors, this);
        this.model.on('change:overlap', this.update_overlap, this);
        this.model.on('change:playing', this.update_playing, this);
        this.model.on('change:time', this.update_time, this);
        this.model.on('change:active_region', this.update_active_region, this);
        this.model.on('change:zoom', this.update_zoom, this);
        // this._wavesurfer.zoom();
    }
    push_regions() {
        const regions = this._wavesurfer.regions.list;
        const region_ids = Object.keys(regions);
        const _regions = [];
        for (const region_id of region_ids) {
            const region = regions[region_id];
            _regions.push({
                start: region.start,
                end: region.end,
                id: region_id,
                label: region.attributes.label,
            });
        }
        this._syncing_regions = true;
        this.model.set('regions', _regions);
        this.touch();
        this._syncing_regions = false;
    }
    update_audio() {
        const blob = this.to_blob(this.model.get('audio'));
        this._wavesurfer.loadBlob(blob);
        this._wavesurfer.clearRegions();
    }
    update_regions() {
        if (this._syncing_regions) {
            return;
        }
        const regions = this.model.get('regions');
        this._adding_regions = true;
        this._wavesurfer.clearRegions();
        for (const region of regions) {
            this._wavesurfer.addRegion({
                start: region.start,
                end: region.end,
                id: region.id,
                attributes: { label: region.label },
            });
        }
        this._adding_regions = false;
        this.update_colors();
        this.update_active_region();
        this.update_overlap();
        this.update_label_visibility();
    }
    update_colors() {
        const regions = this.model.get('regions');
        const colors = this.model.get('colors');
        const wavesurfer_regions = this._wavesurfer.regions.list;
        for (const region of regions) {
            wavesurfer_regions[region['id']].element.style.backgroundColor =
                colors[region['label']];
        }
    }
    update_active_region() {
        const regions = this.model.get('regions');
        const active_region = this.model.get('active_region');
        const wavesurfer_regions = this._wavesurfer.regions.list;
        for (const region of regions) {
            if (region['id'] === active_region) {
                wavesurfer_regions[region['id']].element.classList.add('wavesurfer-region-active');
            }
            else {
                wavesurfer_regions[region['id']].element.classList.remove('wavesurfer-region-active');
            }
        }
    }
    update_overlap() {
        const regions = this.model.get('regions');
        const overlap = this.model.get('overlap');
        const wavesurfer_regions = this._wavesurfer.regions.list;
        for (const region of regions) {
            const wavesurfer_region = wavesurfer_regions[region['id']].element;
            for (const class_name of wavesurfer_region.className.split(' ')) {
                if (class_name.startsWith('wavesurfer-region-overlapping')) {
                    wavesurfer_region.classList.remove(class_name);
                }
            }
            if (region.id in overlap) {
                wavesurfer_region.classList.add('wavesurfer-region-overlapping-' +
                    overlap[region.id].level +
                    '-' +
                    overlap[region.id].num_levels);
            }
        }
    }
    update_label_visibility() {
        const regions = this.model.get('regions');
        const wavesurfer_regions = this._wavesurfer.regions.list;
        for (const region of regions) {
            const wavesurfer_region = wavesurfer_regions[region['id']].element;
            const tag = wavesurfer_region.querySelector('.wavesurfer-region-tag');
            if (tag !== null) {
                tag.style.display =
                    tag.getBoundingClientRect().width >
                        0.9 * wavesurfer_region.getBoundingClientRect().width
                        ? 'none'
                        : 'inline';
            }
        }
    }
    update_playing() {
        if (this.model.get('playing')) {
            this._wavesurfer.play();
        }
        else {
            this._wavesurfer.pause();
        }
    }
    update_time() {
        if (!this.model.get('playing')) {
            this._wavesurfer.setCurrentTime(this.model.get('time'));
        }
    }
    update_zoom() {
        const zoom = this.model.get('zoom');
        this._wavesurfer.zoom(zoom);
        this.update_colors();
        this.update_label_visibility();
    }
    // FIXME: find correct type for `created_region`
    on_region_created(created_region) {
        let label;
        if ('label' in created_region.attributes) {
            label = created_region.attributes.label;
        }
        else {
            label = this.model.get('active_label');
            created_region.attributes.label = label;
        }
        const tag = document.createElement('span');
        tag.textContent = label.toUpperCase();
        tag.classList.add('wavesurfer-region-tag');
        const r = created_region.element;
        r.appendChild(tag);
        if (!this._adding_regions) {
            this.model.set('active_region', created_region.id);
            this.touch();
        }
    }
    // FIXME: find correct type for `created_region`
    on_region_update_end(updated_region) {
        const wavesurfer_regions = this._wavesurfer.regions.list;
        const region_ids = Object.keys(wavesurfer_regions);
        const regions = [];
        for (const region_id of region_ids) {
            const region = wavesurfer_regions[region_id];
            regions.push({
                start: region.start,
                end: region.end,
                id: region_id,
                label: region.attributes.label,
            });
        }
        this._syncing_regions = true;
        this.model.set('regions', regions);
        this.touch();
        this._syncing_regions = false;
        this.update_active_region();
        this.update_colors();
        this.update_overlap();
        this.update_label_visibility();
    }
    on_audioprocess() {
        this.model.set('time', this._wavesurfer.getCurrentTime());
        this.touch();
    }
    on_seek(progress) {
        this.model.set('time', this._wavesurfer.getCurrentTime());
        this.touch();
    }
    on_zoom(minPxPerSec) {
        console.log('minPxPerSec', minPxPerSec);
        this.update_label_visibility();
    }
    on_finish() {
        this.model.set('playing', false);
        this.touch();
    }
    // FIXME: find correct type for `region`
    on_region_click(region) {
        let active_region;
        if (region.id === this.model.get('active_region')) {
            active_region = '';
        }
        else {
            active_region = region.id;
        }
        this.model.set('active_region', active_region);
        this.touch();
    }
}
exports.WavesurferView = WavesurferView;
class LabelsModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: LabelsModel.model_name, _model_module: LabelsModel.model_module, _model_module_version: LabelsModel.model_module_version, _view_name: LabelsModel.view_name, _view_module: LabelsModel.view_module, _view_module_version: LabelsModel.view_module_version });
    }
}
exports.LabelsModel = LabelsModel;
LabelsModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
LabelsModel.model_name = 'LabelsModel';
LabelsModel.model_module = version_1.MODULE_NAME;
LabelsModel.model_module_version = version_1.MODULE_VERSION;
LabelsModel.view_name = 'LabelsView';
LabelsModel.view_module = version_1.MODULE_NAME;
LabelsModel.view_module_version = version_1.MODULE_VERSION;
class LabelsView extends base_1.DOMWidgetView {
    render() {
        this.container = document.createElement('div');
        this.el.appendChild(this.container);
        this.update_labels();
        this.model.on('change:labels', this.update_labels, this);
        this.model.on('change:colors', this.update_labels, this);
        this.model.on('change:active_label', this.update_labels, this);
    }
    update_labels() {
        const labels = this.model.get('labels');
        const colors = this.model.get('colors');
        const active_label = this.model.get('active_label');
        this.container.textContent = '';
        for (const idx of Object.keys(labels)) {
            const button = document.createElement('button');
            button.style.backgroundColor = colors[idx];
            button.classList.add('label-button');
            if (idx === active_label) {
                button.classList.add('label-button-active');
            }
            const shortcut = document.createElement('span');
            shortcut.style.backgroundColor = 'white';
            shortcut.classList.add('label-shortcut');
            if (idx === active_label) {
                shortcut.classList.add('label-button-active');
            }
            shortcut.textContent = idx.toUpperCase();
            button.appendChild(shortcut);
            const label = document.createElement('input');
            label.classList.add('label-input');
            label.value = labels[idx];
            label.addEventListener('keypress', this.save_label_on_enter(label, idx));
            button.appendChild(label);
            button.addEventListener('click', this.activate(idx));
            this.container.appendChild(button);
        }
    }
    activate(idx) {
        return (event) => {
            this.model.set('active_label', idx);
            this.touch();
        };
    }
    save_label_on_enter(label, idx) {
        return (event) => {
            if (event.key === 'Enter') {
                event.preventDefault();
                const new_labels = Object();
                const old_labels = this.model.get('labels');
                for (const i in old_labels) {
                    if (i === idx) {
                        new_labels[i] = label.value;
                    }
                    else {
                        new_labels[i] = old_labels[i];
                    }
                }
                this.model.set('labels', new_labels);
                this.touch();
            }
        };
    }
}
exports.LabelsView = LabelsView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".wavesurfer-handle {\n  border-width: 1px;\n  opacity: 50%;\n}\n\n.wavesurfer-region {\n  opacity: 80%;\n  top: 10% !important;\n  height: 80% !important;\n}\n\n.wavesurfer-region-active {\n  background: repeating-linear-gradient(\n    45deg,\n    transparent,\n    transparent 10px,\n    #ffffff 10px,\n    #ffffff 15px\n  );\n  z-index: 1000 !important;\n}\n\n.wavesurfer-region-overlapping-1-1 {\n  top: 10% !important;\n  height: 80% !important;\n}\n\n.wavesurfer-region-overlapping-1-2 {\n  top: 10% !important;\n  height: 70% !important;\n}\n\n.wavesurfer-region-overlapping-2-2 {\n  top: 20% !important;\n  height: 70% !important;\n}\n\n.wavesurfer-region-overlapping-1-3 {\n  top: 10% !important;\n  height: 60% !important;\n}\n\n.wavesurfer-region-overlapping-2-3 {\n  top: 20% !important;\n  height: 60% !important;\n}\n\n.wavesurfer-region-overlapping-3-3 {\n  top: 30% !important;\n  height: 60% !important;\n}\n\n.wavesurfer-region-overlapping-1-4 {\n  top: 10% !important;\n  height: 50% !important;\n}\n\n.wavesurfer-region-overlapping-2-4 {\n  top: 20% !important;\n  height: 50% !important;\n}\n\n.wavesurfer-region-overlapping-3-4 {\n  top: 30% !important;\n  height: 50% !important;\n}\n\n.wavesurfer-region-overlapping-4-4 {\n  top: 40% !important;\n  height: 50% !important;\n}\n\n.wavesurfer-region-tag {\n  padding-left: 4px;\n  padding-top: 4px;\n  opacity: 100%;\n}\n\n.label-button {\n  padding-left: 5px;\n  padding-right: 5px;\n  padding-top: 5px;\n  padding-bottom: 5px;\n  border-width: 0px;\n  margin-right: 5px;\n  margin-bottom: 5px;\n}\n\n.label-shortcut {\n  background-color: white;\n  /* margin-top: 5px; */\n  padding-left: 5px;\n  padding-right: 5px;\n  margin-right: 5px;\n}\n\n.label-button-active {\n  border-style: solid;\n  border-width: 1px;\n  border-color: black;\n}\n\n.label-input {\n  background: transparent;\n  border-width: 0px;\n  border-style: solid;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"pyannotebook","version":"0.1.0","description":"pyannote jupyter widget","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/pyannote/pyannotebook","bugs":{"url":"https://github.com/pyannote/pyannotebook/issues"},"license":"BSD-3-Clause","author":{"name":"Hervé Bredin","email":"herve@niderb.fr"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/pyannote/pyannotebook"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf pyannotebook/labextension","clean:nbextension":"rimraf pyannotebook/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6","wavesurfer.js":"6.4"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/wavesurfer.js":"^6.0.3","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"pyannotebook/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.5aab188af617c8480816.js.map