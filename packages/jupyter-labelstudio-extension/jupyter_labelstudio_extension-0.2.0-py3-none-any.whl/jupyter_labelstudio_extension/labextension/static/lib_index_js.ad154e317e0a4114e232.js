"use strict";
(self["webpackChunkjupyter_labelstudio_extension"] = self["webpackChunkjupyter_labelstudio_extension"] || []).push([["lib_index_js"],{

/***/ "./lib/components/createProject.js":
/*!*****************************************!*\
  !*** ./lib/components/createProject.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CreateProjectInput": () => (/* binding */ CreateProjectInput)
/* harmony export */ });
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");



// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types,@typescript-eslint/ban-ts-comment
// @ts-ignore
const CreateProjectInput = ({ template, updateFunc }) => {
    const [nameValue, setNameValue] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    const [description, setDescription] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    const onNameChange = (e) => setNameValue(e.target.value);
    const onDescriptionChange = (e) => setDescription(e.target.value);
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('count')
            .then((data) => {
            const num = data['project_count'] + 1;
            setNameValue('New Project #' + num.toString());
        })
            .catch(reason => {
            console.error(`The jupyter_labelstudio_extension server extension appears to be missing.\n${reason}`);
        });
    }, []);
    async function handleCreate() {
        try {
            const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('projects', {
                body: JSON.stringify({
                    name: nameValue,
                    config: template,
                    description: description
                }),
                method: 'POST'
            });
            if (updateFunc) {
                updateFunc(reply['id']);
            }
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            document.getElementById('create-project-button').style.display = 'none';
            alert('Successfully create project.');
        }
        catch (reason) {
            console.error(`Error on POST /jupyterlab_labelstudio_extension/projects.\n${reason}`);
            alert('failed to create project.');
        }
    }
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { id: "proj_name", label: "Project Name", variant: "outlined", value: nameValue, onChange: onNameChange, required: true }),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("br", null),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { id: "proj_description", label: "Project Description", value: description, variant: "outlined", onChange: onDescriptionChange }),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("br", null),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Button, { id: "create-project-button", style: { backgroundColor: '#448ef7', color: 'white', marginTop: '2%' }, onClick: handleCreate }, "Create Project")));
};


/***/ }),

/***/ "./lib/components/project.js":
/*!***********************************!*\
  !*** ./lib/components/project.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ProjectPanel": () => (/* binding */ ProjectPanel),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");

// import { config } from 'webpack';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const ProjectPanel = ({ type, updateFunc }) => {
    const [projectNames, setProjectNames] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const [projectIDs, setProjectIDs] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const [isEmpty, setEmpty] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    async function handleCheckProject(projectId) {
        try {
            if (type === 'labeling') {
                const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('current', {
                    body: JSON.stringify({ project_id: projectId }),
                    method: 'POST'
                });
                if (updateFunc) {
                    updateFunc(reply);
                }
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                document.getElementById('project-content').style.display = 'block';
            }
            if (type === 'storage') {
                const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('storage', {
                    body: JSON.stringify({ project_id: projectId }),
                    method: 'POST'
                });
                console.log(reply);
                if (updateFunc) {
                    updateFunc(reply);
                }
                //
                // // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // // @ts-ignore
                // document.getElementById('storage-list').style.display = 'block';
            }
        }
        catch (reason) {
            console.error(`Error on ProjectPanel rendering.\n${reason}`);
        }
    }
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('projects')
            .then(data => {
            // TODO: ignore ts compile, fix this when available
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            setProjectIDs(Object.keys(data));
            setProjectNames(Object.values(data));
            if (Object.keys(data).length === 0) {
                setEmpty(true);
            }
        })
            .catch(reason => {
            console.error(`The jupyter_labelstudio_extension server extension appears to be missing.\n${reason}`);
        });
    }, []);
    // TODO: beautify frontend
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        isEmpty && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { style: { marginLeft: '2%' } },
            ' ',
            "You don't have any project now. Please go to \"create project\" to create one",
            ' ')),
        !isEmpty && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: {
                display: 'flex',
                overflowX: 'scroll',
                width: '95%',
                marginLeft: '2%',
                cursor: 'pointer'
            } }, projectNames.map((src, index) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { key: projectIDs[index], style: {
                width: '300px',
                height: '200px',
                borderRadius: '10px',
                borderStyle: 'solid',
                borderColor: 'black',
                marginLeft: '10px'
            }, onClick: () => handleCheckProject(projectIDs[index]) },
            "Name: ",
            src)))))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ProjectPanel);


/***/ }),

/***/ "./lib/components/storageCard.js":
/*!***************************************!*\
  !*** ./lib/components/storageCard.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "StorageCard": () => (/* binding */ StorageCard)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");



// import { CardContent } from '@material-ui/core';
// import { CardActions } from '@material-ui/core';



const StorageCard = ({ storageID, storageType, storagePath }) => {
    //TODO: add more color set for s3 and google drive
    // const colorSet = {
    //   localfiles: '#47cf73'
    // };
    async function handleSyncStorage() {
        try {
            await (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('sync', {
                body: JSON.stringify({
                    storage_id: storageID,
                    storage_type: storageType
                }),
                method: 'POST'
            });
            alert('successfully sync storage at ' + storageType);
        }
        catch (reason) {
            console.error(`Error on POST /jupyterlab_labelstudio_extension/sync.\n${reason}`);
            //TODO: specific error tip
            alert('Sync error');
        }
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Container, { style: {
            width: '30%',
            margin: '2%',
            padding: '2%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            flexWrap: 'wrap',
            overflow: 'auto'
        } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Card, { style: {
                fontFamily: 'Roboto,sans-serif',
                boxSizing: 'border-box',
                borderRadius: '5px',
                backgroundColor: '#fafafa',
                borderStyle: 'solid',
                borderColor: 'rgba(128,128,128,0.73)',
                margin: '1% 1%',
                overflow: 'auto'
            } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Typography, { style: { margin: '2%' }, variant: "h5", component: "div" }, storageType),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: {
                    backgroundColor: '#448ef7',
                    width: '80%',
                    height: '5px',
                    marginLeft: '10%'
                } }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Typography, { style: {
                    margin: '2%',
                    overflow: 'auto',
                    wordWrap: 'break-word',
                    whiteSpace: 'pre-wrap',
                    textOverflow: 'ellipsis',
                    display: '-webkit-box',
                    lineClamp: 3
                }, variant: "body2" },
                "path:",
                storagePath),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Button, { variant: "contained", style: { color: 'white', backgroundColor: '#448ef7', margin: '4%' }, size: "small", onClick: handleSyncStorage }, "Sync Storage"))));
};


/***/ }),

/***/ "./lib/components/storageTabs.js":
/*!***************************************!*\
  !*** ./lib/components/storageTabs.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "StorageTabs": () => (/* binding */ StorageTabs)
/* harmony export */ });
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");
var __rest = (undefined && undefined.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};







function TabPanel(props) {
    const { children, value, index } = props, other = __rest(props, ["children", "value", "index"]);
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", Object.assign({ role: "tabpanel", hidden: value !== index, id: `simple-tabpanel-${index}`, "aria-labelledby": `simple-tab-${index}` }, other), value === index && (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Box, { sx: { p: 3 } },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Typography, null, children)))));
}
function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        'aria-controls': `simple-tabpanel-${index}`
    };
}
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const StorageTabs = ({ projectID, updateFunc }) => {
    const [localName, setLocalName] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    const [localPath, setLocalPath] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('');
    //TODO: change regex according to tasks type
    const [regex, setRegex] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)('.*(jpe?g|png)');
    const [value, setValue] = react__WEBPACK_IMPORTED_MODULE_1__.useState(0);
    async function handleCheckConnection() {
        console.log(projectID);
        console.log(localName);
        console.log(regex);
        console.log(localPath);
        try {
            const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('validate', {
                body: JSON.stringify({
                    project_id: projectID,
                    storage_name: localName,
                    path: localPath,
                    regex: regex
                }),
                method: 'POST'
            });
            console.log(reply);
            alert('Connection clear. You can click "add storage" to connect the storage.');
        }
        catch (reason) {
            console.error(`Error on POST /jupyterlab_labelstudio_extension/export.\n${reason}`);
            alert('Connection failed. Check if the absolute path and regex is correct, or if the local config is set.');
        }
    }
    async function handleAddLocalStorage() {
        try {
            const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('connect/local', {
                body: JSON.stringify({
                    project_id: projectID,
                    storage_name: localName,
                    path: localPath,
                    regex: regex
                }),
                method: 'POST'
            });
            console.log('reply:', reply);
            alert('Successfully create and sync local storage');
            console.log(updateFunc);
            if (updateFunc) {
                updateFunc(reply);
            }
        }
        catch (reason) {
            console.error(`Error on POST /jupyterlab_labelstudio_extension/connect/local.\n${reason}`);
            alert('Fail to create. Check if the absolute path and regex is correct, or if the local config is set.');
        }
    }
    // eslint-disable-next-line @typescript-eslint/ban-types
    const handleChange = (event, newValue) => {
        setValue(newValue);
    };
    const handleLocalNameChange = (e) => setLocalName(e.target.value);
    const handleLocalPathChange = (e) => setLocalPath(e.target.value);
    const handleRegexChange = (e) => setRegex(e.target.value);
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Box, { sx: { width: '100%' } },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Box, { sx: { borderBottom: 1, borderColor: 'divider' } },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Tabs, { value: value, onChange: handleChange, "aria-label": "basic tabs example", centered: true },
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Tab, Object.assign({ label: "Local" }, a11yProps(0))),
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Tab, Object.assign({ label: "Google Cloud" }, a11yProps(1))))),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(TabPanel, { value: value, index: 0 },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "local_storage_title", label: "Storage Title:", value: localName, onChange: handleLocalNameChange, variant: "outlined" }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "local_path", label: "Absolute Path", value: localPath, onChange: handleLocalPathChange, variant: "outlined", required: true }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "local_regex", label: "File Filter Regex", value: regex, onChange: handleRegexChange, variant: "outlined" }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("br", null),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Button, { variant: "contained", style: { backgroundColor: '#448ef7', color: 'white', margin: '4%' }, onClick: handleCheckConnection }, "Check Connection"),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.Button, { variant: "contained", style: { backgroundColor: '#448ef7', color: 'white', margin: '4%' }, onClick: handleAddLocalStorage }, "Add Storage")),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(TabPanel, { value: value, index: 1 },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "gc_storage_title", label: "Storage Title:", variant: "outlined" }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "gc_bucket_name", label: "Bucket Name", variant: "outlined", required: true }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("br", null),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "gc_regex", label: "File Filter Regex", variant: "outlined", required: true }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_0__.TextField, { style: { margin: '1%' }, id: "gc_credentials", label: "Google Application Credentials", variant: "outlined" }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("br", null))));
};


/***/ }),

/***/ "./lib/export.js":
/*!***********************!*\
  !*** ./lib/export.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");


// eslint-disable-next-line @typescript-eslint/naming-convention
// export interface UserInformation {
//   user: string;
//   apiKey: string;
// }
var ExportFormat;
(function (ExportFormat) {
    ExportFormat[ExportFormat["JSON"] = 0] = "JSON";
    ExportFormat[ExportFormat["CSV"] = 1] = "CSV";
})(ExportFormat || (ExportFormat = {}));
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const ExportPanel = (props) => {
    // const [userInfo, setUserInfo] = useState(props);
    const { projectID } = props;
    const [currentFormat, setFormat] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(ExportFormat[0]);
    async function exportAPI() {
        //TODO: add more export format
        try {
            const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('export', {
                body: JSON.stringify({
                    project_id: projectID,
                    format: currentFormat
                }),
                method: 'POST'
            });
            console.log(reply);
            alert('Successfully export annotation file');
        }
        catch (reason) {
            console.error(`Error on POST /jupyterlab_labelstudio_extension/export.\n${reason}`);
            alert('Failed to export.You could try another export format.');
        }
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: { marginLeft: '2%' } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "radio", name: "type", value: "JSON", id: "exportJSON", onChange: () => {
                setFormat(ExportFormat[0]);
            }, defaultChecked: true }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("label", { htmlFor: "exportJSON" }, "JSON"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "radio", name: "type", value: "CSV", id: "exportCSV", onChange: () => {
                setFormat(ExportFormat[1]);
            } }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("label", { htmlFor: "exportCSV" }, "CSV"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("br", null),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { onClick: exportAPI }, "Export")));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ExportPanel);


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyter-labelstudio-extension', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _labelling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./labelling */ "./lib/labelling.js");



// import {ImportWidget} from "./import"
// import { PageConfig } from '@jupyterlab/coreutils';
// import { logoIcon } from "./style/icon"
/**
 * The command IDs used by the react-widget plugin.
 */
// eslint-disable-next-line @typescript-eslint/no-unused-vars
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'create-labelstudio-widget';
    CommandIDs.importData = 'import';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the jupyter_labelstudio_extension extension.
 */
const plugin = {
    id: 'LabelStudio:plugin',
    autoStart: true,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__.ILauncher],
    activate: async (app, launcher) => {
        console.log('JupyterLab extension jupyter_labelstudio_extension is activated!');
        const { commands } = app;
        const command = CommandIDs.create;
        commands.addCommand(command, {
            caption: 'Create an LabelStudio widget',
            label: 'LabelStudio Extension',
            // TODO: add ICON
            execute: () => {
                const content = new _labelling__WEBPACK_IMPORTED_MODULE_2__.LabelStudioWidget();
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
                widget.title.label = 'LabelStudio Extension';
                widget.title.icon = 'logo-icon';
                app.shell.add(widget, 'main');
            }
        });
        if (launcher) {
            launcher.add({ command });
        }
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/instruction.js":
/*!****************************!*\
  !*** ./lib/instruction.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ InstructionPage)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function InstructionPage() {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: { marginLeft: '2%' } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", null, "Label Studio Setup Instruction"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null,
            ' ',
            "It seems you haven't setup a label-studio server on localhost, please follow the instruction here to launch the label-studio server on http://localhost:8080 with one .ipynb notebook: ",
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("link", null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("br", null)));
}


/***/ }),

/***/ "./lib/labelProject.js":
/*!*****************************!*\
  !*** ./lib/labelProject.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _components_project__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./components/project */ "./lib/components/project.js");
/* harmony import */ var _export__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./export */ "./lib/export.js");
/* harmony import */ var label_studio__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! label-studio */ "webpack/sharing/consume/default/label-studio/label-studio");
/* harmony import */ var label_studio__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(label_studio__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var label_studio_build_static_css_main_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! label-studio/build/static/css/main.css */ "./node_modules/label-studio/build/static/css/main.css");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");







// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const ProjectUI = () => {
    const [currentID, setID] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(-1);
    const [tasks, setTasks] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)([{}]);
    // const [currentTask, setCurrentTask] = useState({});
    const [currentIndex, setCurrentIndex] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(0);
    const [currentConfig, setCurrentConfig] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)('');
    const [currentPanel, setCurrentPanel] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)({
        config: '',
        task: {}
    });
    const onClickPrevMission = () => {
        if (currentIndex > 0) {
            setCurrentPanel({
                config: currentConfig,
                task: tasks[currentIndex - 1]
            });
            setCurrentIndex(currentIndex - 1);
        }
    };
    const onClickNextMission = () => {
        if (currentIndex < tasks.length - 1) {
            setCurrentPanel({
                config: currentConfig,
                task: tasks[currentIndex + 1]
            });
            setCurrentIndex(currentIndex + 1);
        }
    };
    const updateCurrentPanel = (data) => {
        //TODO: fixed URL(changes to default URL)
        //TODO: change data type to json object
        const tasks_raw = data['current_tasks'];
        for (let i = 0; i < tasks_raw.length; i++) {
            const image_path = tasks_raw[i]['data']['image'];
            const base_url = 'http://localhost:8080';
            tasks_raw[i]['data']['image'] = base_url + image_path;
        }
        setTasks(tasks_raw);
        setCurrentConfig(data['current_view']);
        setCurrentPanel({
            config: data['current_view'],
            task: tasks_raw[0]
        });
        setCurrentIndex(0);
        //TODO: error handle
        setID(data['id']);
        // console.log('current task: ', tasks_raw[0]);
        // console.log('current config: ', currentConfig);
    };
    const updateCurrentTask = (task, base_url) => {
        const image_path = task['data']['image'];
        task['data']['image'] = base_url + image_path;
        const new_tasks = [...tasks];
        new_tasks[currentIndex] = task;
        setTasks(new_tasks);
        setCurrentPanel({
            config: currentConfig,
            task: task
        });
    };
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        if (currentID >= 0) {
            new (label_studio__WEBPACK_IMPORTED_MODULE_0___default())('label-studio', {
                config: currentPanel.config,
                interfaces: [
                    'panel',
                    'update',
                    'submit',
                    'controls',
                    'infobar',
                    'topbar',
                    'instruction',
                    'side-column',
                    'annotations:history',
                    'annotations:tabs',
                    'annotations:menu',
                    'annotations:current',
                    'annotations:add-new',
                    'annotations:delete',
                    'annotations:view-all',
                    'edit-history'
                ],
                user: {
                    pk: 1,
                    firstName: 'Test',
                    lastName: 'Account'
                },
                task: currentPanel.task,
                //TODO: any type modification
                onLabelStudioLoad: function (LS) {
                    const c = LS.annotationStore.addAnnotation({
                        userGenerate: true
                    });
                    LS.annotationStore.selectAnnotation(c.id);
                },
                onSubmitAnnotation: async function (LS, annotation) {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-ignore
                    //TODO: change it to better
                    const id = currentPanel.task['id'];
                    // const annotation = annotation.serializeAnnotation();
                    try {
                        const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)('submit', {
                            body: JSON.stringify({
                                project_id: currentID,
                                task_id: id,
                                annotation_result: annotation.serializeAnnotation()
                            }),
                            method: 'POST'
                        });
                        const update_task = reply['updated_task'];
                        updateCurrentTask(update_task, 'http://localhost:8080');
                    }
                    catch (reason) {
                        console.error(`Error on POST /jupyterlab_labelstudio_extension/submit.\n${reason}`);
                    }
                },
                onUpdateAnnotation: async function (LS, annotation) {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-ignore
                    //TODO: change it to better
                    const task_id = currentPanel.task['id'];
                    const annotation_id = annotation.pk;
                    const annotation_result = annotation.serializeAnnotation();
                    try {
                        const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)('update', {
                            body: JSON.stringify({
                                project_id: currentID,
                                task_id: task_id,
                                annotation_id: annotation_id,
                                annotation_result: annotation_result
                            }),
                            method: 'POST'
                        });
                        const update_task = reply['updated_task'];
                        updateCurrentTask(update_task, 'http://localhost:8080');
                    }
                    catch (reason) {
                        console.error(`Error on POST /jupyterlab_labelstudio_extension/update.\n${reason}`);
                    }
                },
                onDeleteAnnotation: async function (LS, annotation) {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-ignore
                    //TODO: change it to better
                    const task_id = currentPanel.task['id'];
                    const annotation_id = annotation.pk;
                    //TODO: delete post
                    try {
                        const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)('delete', {
                            body: JSON.stringify({
                                project_id: currentID,
                                task_id: task_id,
                                annotation_id: annotation_id
                            }),
                            method: 'POST'
                        });
                        const update_task = reply['updated_task'];
                        updateCurrentTask(update_task, 'http://localhost:8080');
                    }
                    catch (reason) {
                        console.error(`Error on POST /jupyterlab_labelstudio_extension/delete.\n${reason}`);
                    }
                }
            });
        }
    }, [currentPanel, currentID]);
    //TODO: potential bug test for boundary tasks
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Choose Project"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_components_project__WEBPACK_IMPORTED_MODULE_5__["default"], { type: "labeling", updateFunc: updateCurrentPanel }),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "project-content", style: { display: 'none' } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Labeling"),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Button, { variant: "contained", style: { color: 'white', backgroundColor: '#448ef7', margin: '4%' }, onClick: onClickPrevMission, disabled: currentIndex === 0 }, "Last"),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Button, { variant: "contained", style: { color: 'white', backgroundColor: '#448ef7', margin: '4%' }, onClick: onClickNextMission, disabled: currentIndex === tasks.length - 1 }, "Next"),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("br", null),
            currentID >= 0 && react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { id: "label-studio" }, " "),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Export"),
            currentID >= 0 && react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_export__WEBPACK_IMPORTED_MODULE_6__["default"], { projectID: currentID }))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ProjectUI);


/***/ }),

/***/ "./lib/labelling.js":
/*!**************************!*\
  !*** ./lib/labelling.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LabelStudioWidget": () => (/* binding */ LabelStudioWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var label_studio_build_static_css_main_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! label-studio/build/static/css/main.css */ "./node_modules/label-studio/build/static/css/main.css");
/* harmony import */ var _instruction__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./instruction */ "./lib/instruction.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _template__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./template */ "./lib/template.js");
/* harmony import */ var _labelProject__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./labelProject */ "./lib/labelProject.js");
/* harmony import */ var _storageManagement__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./storageManagement */ "./lib/storageManagement.js");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");




// import {Route} from "react-router-dom"
// import {useNavigate} from "react-router"







// Single label
function LabelStudioUI() {
    const [page, setPage] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)('create');
    const onClickCreate = () => {
        setPage('create');
    };
    const onClickLabel = () => {
        setPage('label');
    };
    const onClickStorage = () => {
        setPage('storage');
    };
    const showCreateProjectUI = () => {
        if (page === 'create') {
            return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_template__WEBPACK_IMPORTED_MODULE_4__.TemplateUI, null);
        }
    };
    const showLabelingProjectUI = () => {
        if (page === 'label') {
            return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_labelProject__WEBPACK_IMPORTED_MODULE_5__["default"], null);
        }
    };
    const showStorageUI = () => {
        if (page === 'storage') {
            return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_storageManagement__WEBPACK_IMPORTED_MODULE_6__.StorageUI, null);
        }
    };
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { flexGrow: 1 } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.AppBar, { position: "static", style: { backgroundColor: '#448ef7' } },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Toolbar, null,
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Button, { style: { color: 'white' }, onClick: onClickCreate },
                        ' ',
                        "Create Project"),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Button, { style: { color: 'white' }, onClick: onClickLabel },
                        ' ',
                        "Label Project"),
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_3__.Button, { style: { color: 'white' }, onClick: onClickStorage },
                        ' ',
                        "Storage Management")))),
        showCreateProjectUI(),
        showLabelingProjectUI(),
        showStorageUI()));
}
const LabelStudioComponent = () => {
    const [connected, setConnected] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(false);
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        (0,_handler__WEBPACK_IMPORTED_MODULE_7__.requestAPI)('connect')
            .then((data) => {
            if (data['status'] === 'UP') {
                console.log('status is up');
                setConnected(true);
            }
            else {
                console.log('status is down');
                setConnected(false);
            }
        })
            .catch(reason => {
            console.log('status error');
            setConnected(false);
        });
    }, []);
    return react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", null, connected ? react__WEBPACK_IMPORTED_MODULE_2___default().createElement(LabelStudioUI, null) : react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_instruction__WEBPACK_IMPORTED_MODULE_8__["default"], null));
};
class LabelStudioWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor() {
        super();
        this.addClass('jp-LabelStudioWidget');
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { height: '100%', width: '100%', overflow: 'scroll' } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(LabelStudioComponent, null)));
    }
}


/***/ }),

/***/ "./lib/storageManagement.js":
/*!**********************************!*\
  !*** ./lib/storageManagement.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "StorageUI": () => (/* binding */ StorageUI)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _components_project__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./components/project */ "./lib/components/project.js");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components_storageCard__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./components/storageCard */ "./lib/components/storageCard.js");
/* harmony import */ var _components_storageTabs__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/storageTabs */ "./lib/components/storageTabs.js");


// import { StorageCard } from './components/storageCard';





const StorageUI = () => {
    const [currentID, setID] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(-1);
    const [storageList, setStorageList] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([
        {
            id: undefined,
            path: undefined,
            type: undefined
        }
    ]);
    const [dialogOpen, setDialogOpen] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const handleOpenDialog = () => {
        setDialogOpen(true);
    };
    const handleClose = () => {
        setDialogOpen(false);
    };
    const updateCurrentPanel = (data) => {
        console.log('data:', data);
        setID(data['id']);
        setStorageList(data['storage_list']);
        handleClose();
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        document.getElementById('storage-list').style.display = 'block';
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h2", { style: { marginLeft: '2%' } }, "Choose Project"),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_project__WEBPACK_IMPORTED_MODULE_2__["default"], { type: "storage", updateFunc: updateCurrentPanel }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { id: "storage-list", style: { display: 'none', marginLeft: '2%' } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h2", null, "Storage List"),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Button, { variant: "contained", style: { backgroundColor: '#448ef7', color: 'white', margin: '4%' }, onClick: handleOpenDialog }, "add storage"),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Dialog, { open: dialogOpen, onClose: handleClose },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.DialogTitle, null, "Link with cloud storage"),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.DialogContent, null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_storageTabs__WEBPACK_IMPORTED_MODULE_3__.StorageTabs, { projectID: currentID, updateFunc: updateCurrentPanel })),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.DialogActions, null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Button, { onClick: handleClose }, "Close"))),
            storageList.length === 0 && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null, " there's no storage for this project, u can try to create one ")),
            storageList.map((src, index) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_storageCard__WEBPACK_IMPORTED_MODULE_4__.StorageCard, { storageID: src['id'], storagePath: src['path'], storageType: src['type'] })))))));
};


/***/ }),

/***/ "./lib/template.js":
/*!*************************!*\
  !*** ./lib/template.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TemplateUI": () => (/* binding */ TemplateUI),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var label_studio_build_static_css_main_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! label-studio/build/static/css/main.css */ "./node_modules/label-studio/build/static/css/main.css");
/* harmony import */ var _uiw_react_codemirror__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @uiw/react-codemirror */ "webpack/sharing/consume/default/@uiw/react-codemirror/@uiw/react-codemirror");
/* harmony import */ var _uiw_react_codemirror__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_uiw_react_codemirror__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _codemirror_lang_html__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @codemirror/lang-html */ "webpack/sharing/consume/default/@codemirror/lang-html/@codemirror/lang-html");
/* harmony import */ var _codemirror_lang_html__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_codemirror_lang_html__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var label_studio__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! label-studio */ "webpack/sharing/consume/default/label-studio/label-studio");
/* harmony import */ var label_studio__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(label_studio__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _components_storageTabs__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./components/storageTabs */ "./lib/components/storageTabs.js");
/* harmony import */ var _components_createProject__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./components/createProject */ "./lib/components/createProject.js");
// import { ReactWidget } from "@jupyterlab/apputils";
// import LabelStudio from "label-studio"


// from :https://github.com/uiwjs/react-codemirror






//BUGS TODO:!! empty error
const TemplatePreview = (props) => {
    const { config } = props;
    // const [renderError,setRenderError]=useState(false);
    // let templateImgURL= "./assets/template.jpg"
    //TODO：Setting States
    (0,react__WEBPACK_IMPORTED_MODULE_2__.useEffect)(() => {
        try {
            new (label_studio__WEBPACK_IMPORTED_MODULE_4___default())('template-preview', {
                config: config,
                interfaces: ['update', 'controls'],
                user: {
                    pk: 1,
                    firstName: 'James',
                    lastName: 'Dean'
                },
                task: {
                    annotations: [],
                    predictions: [],
                    id: 1,
                    data: {
                        image: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.eduwo.com%2Fu%2Fcms%2Fwww%2F201503%2F11151325i4p2.jpg&refer=http%3A%2F%2Fwww.eduwo.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1668566302&t=ce01be687029ada4e4694c44cdb2d34b'
                    }
                },
                onLabelStudioLoad: function (LS) {
                    const c = LS.annotationStore.addAnnotation({
                        userGenerate: true
                    });
                    LS.annotationStore.selectAnnotation(c.id);
                }
            });
        }
        catch (reason) {
            console.error(`Error on rendering with current config.\n${reason}`);
        }
    });
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { flex: '1', width: '45%', height: '500px' }, id: "template-preview" }));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (TemplatePreview);
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
function TemplateUI() {
    // TODO: add react config
    const default_code = `<View>
  <Image name="image" value="$image"/>
  <Choices name="choice" toName="image" showInLine="true">
    <Choice value="Boeing"/>
    <Choice value="Airbus"/>
  </Choices>
</View>
    `;
    const [currentCode, setCode] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(default_code);
    const [currentProject, setCurrentProject] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(-1);
    const onChange = react__WEBPACK_IMPORTED_MODULE_2___default().useCallback((value, viewUpdate) => {
        setCode(value);
    }, []);
    function onClickImageClassification() {
        setCode(`<View>
  <Image name="image" value="$image"/>
  <Choices name="choice" toName="image" showInLine="true">
    <Choice value="Boeing"/>
    <Choice value="Airbus"/>
  </Choices>
</View>
    `);
    }
    function onClickObjectDetection() {
        setCode(`<View>
  <Image name="image" value="$image"/>
  <RectangleLabels name="label" toName="image">
    <Label value="Airplane" background="green"/>
    <Label value="Car" background="blue"/>
  </RectangleLabels>
</View>

    `);
    }
    return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h1", { style: { marginLeft: '2%' } }, "Label Studio Interface"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Choose Tasks"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { marginLeft: '2%' } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("button", { style: { margin: '1%' }, onClick: onClickImageClassification }, "Image Classification"),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("button", { style: { margin: '1%' }, onClick: onClickObjectDetection }, "Object Detection")),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Labeling Template"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: {
                display: 'flex',
                marginLeft: '2%',
                width: '95%',
                marginBottom: '1em'
            } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement((_uiw_react_codemirror__WEBPACK_IMPORTED_MODULE_1___default()), { value: currentCode, height: "500px", style: { width: '50%', fontSize: '20' }, onChange: onChange, extensions: [(0,_codemirror_lang_html__WEBPACK_IMPORTED_MODULE_3__.html)()] }),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(TemplatePreview, { config: currentCode })),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Create Project"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { marginLeft: '2%' } },
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_components_createProject__WEBPACK_IMPORTED_MODULE_5__.CreateProjectInput, { template: currentCode, updateFunc: (data) => {
                    setCurrentProject(data);
                } })),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("h2", { style: { marginLeft: '2%' } }, "Link with Local Storage/Google Cloud"),
        react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { style: { marginLeft: '2%' } }, currentProject >= 0 && react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_components_storageTabs__WEBPACK_IMPORTED_MODULE_6__.StorageTabs, { projectID: currentProject }))));
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.ad154e317e0a4114e232.js.map