(self["webpackChunkjupyterlab_link_share"] = self["webpackChunkjupyterlab_link_share"] || []).push([["lib_index_js"],{

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
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
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyterlab_link_share', endPoint);
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

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _retrolab_application__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @retrolab/application */ "webpack/sharing/consume/default/@retrolab/application/@retrolab/application");
/* harmony import */ var _retrolab_application__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_retrolab_application__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");







/**
 * The command IDs used by the plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.share = 'link-share:share';
})(CommandIDs || (CommandIDs = {}));
/**
 * Plugin to share the URL of the running Jupyter Server
 */
const plugin = {
    id: 'jupyterlab-link-share:plugin',
    autoStart: true,
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.IMainMenu, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator, _retrolab_application__WEBPACK_IMPORTED_MODULE_1__.IRetroShell],
    activate: (app, palette, menu, translator, retroShell) => {
        const { commands } = app;
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.nullTranslator).load('jupyterlab');
        commands.addCommand(CommandIDs.share, {
            label: trans.__('Share Jupyter Server Link'),
            execute: async () => {
                let results;
                const isRunningUnderJupyterhub = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('hubUser') !== '';
                if (isRunningUnderJupyterhub) {
                    // We are running on a JupyterHub, so let's just use the token set in PageConfig.
                    // Any extra servers running on the server will still need to use this token anyway,
                    // as all traffic (including any to jupyter-server-proxy) needs this token.
                    results = [{ token: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getToken() }];
                }
                else {
                    results = await (0,_handler__WEBPACK_IMPORTED_MODULE_6__.requestAPI)('servers');
                }
                const links = results.map(server => {
                    if (retroShell) {
                        // On retrolab, take current URL and set ?token to it
                        const url = new URL(location.href);
                        url.searchParams.set('token', server.token);
                        return url.toString();
                    }
                    else {
                        // On JupyterLab, let PageConfig.getUrl do its magic.
                        // Handles workspaces, single document mode, etc
                        return _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.normalize(`${_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({
                            workspace: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.defaultWorkspace
                        })}?token=${server.token}`);
                    }
                });
                const entries = document.createElement('div');
                links.map(link => {
                    const p = document.createElement('p');
                    const text = document.createElement('input');
                    text.readOnly = true;
                    text.value = link;
                    text.addEventListener('click', e => {
                        e.target.select();
                    });
                    text.style.width = '100%';
                    p.appendChild(text);
                    entries.appendChild(p);
                });
                // Warn users of the security implications of using this link
                // FIXME: There *must* be a better way to create HTML
                const warning = document.createElement('div');
                const warningHeader = document.createElement('h3');
                warningHeader.innerText = trans.__('Security warning!');
                warning.appendChild(warningHeader);
                const messages = [
                    'Anyone with this link has full access to your notebook server, including all your files!',
                    'Please be careful who you share it with.'
                ];
                if (isRunningUnderJupyterhub) {
                    messages.push(
                    // You can restart the server to revoke the token in a JupyterHub
                    'To revoke access, go to File -> Hub Control Panel, and restart your server');
                }
                else {
                    messages.push(
                    // Elsewhere, you *must* shut down your server - no way to revoke it
                    'Currently, there is no way to revoke access other than shutting down your server');
                }
                messages.map(m => {
                    warning.appendChild(document.createTextNode(trans.__(m)));
                    warning.appendChild(document.createElement('br'));
                });
                entries.appendChild(warning);
                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
                    title: trans.__('Share Jupyter Server Link'),
                    body: new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Widget({ node: entries }),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton({ label: trans.__('Cancel') }),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({
                            label: trans.__('Copy Link'),
                            caption: trans.__('Copy the link to the Jupyter Server')
                        })
                    ]
                });
                if (result.button.accept) {
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Clipboard.copyToSystem(links[0]);
                }
            }
        });
        if (palette) {
            palette.addItem({
                command: CommandIDs.share,
                category: trans.__('Server')
            });
        }
        if (menu) {
            // Create a menu
            const shareMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Menu({ commands });
            shareMenu.title.label = trans.__('Share');
            menu.addMenu(shareMenu, { rank: 10000 });
            // Add the command to the menu
            shareMenu.addItem({ command: CommandIDs.share });
        }
    }
};
const plugins = [plugin];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.ed516e2055e3d514e2ff.js.map