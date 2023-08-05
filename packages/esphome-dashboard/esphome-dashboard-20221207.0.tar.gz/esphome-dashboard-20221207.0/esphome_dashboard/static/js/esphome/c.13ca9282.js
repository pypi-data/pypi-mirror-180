import{_ as e,a as t,M as i,b as r,i as o,p as a,d,o as c,q as s,u as n,v as l,R as m,y as h,g as p,f as u,x as b,r as _,n as f,z as g,B as v,A as y,s as w,j as k,C as x,D as S,E as $}from"./index-b2b66d7f.js";import"./c.493fa92b.js";import{F as P,c as C,s as E}from"./c.a6fda5b7.js";import{c as R,o as B}from"./c.9302e097.js";import{s as A,a as T,C as I,b as z,c as O,d as D,e as H}from"./c.0b38eff0.js";import{g as L,c as F,a as N,d as j}from"./c.5644905a.js";import{g as U,f as M}from"./c.a10841c1.js";import{S as W,a as q,c as Y,s as V}from"./c.19b39e1f.js";const G=Symbol("selection controller");class K{constructor(){this.selected=null,this.ordered=null,this.set=new Set}}class J{constructor(e){this.sets={},this.focusedSet=null,this.mouseIsDown=!1,this.updating=!1,e.addEventListener("keydown",(e=>{this.keyDownHandler(e)})),e.addEventListener("mousedown",(()=>{this.mousedownHandler()})),e.addEventListener("mouseup",(()=>{this.mouseupHandler()}))}static getController(e){const t=!("global"in e)||"global"in e&&e.global?document:e.getRootNode();let i=t[G];return void 0===i&&(i=new J(t),t[G]=i),i}keyDownHandler(e){const t=e.target;"checked"in t&&this.has(t)&&("ArrowRight"==e.key||"ArrowDown"==e.key?this.selectNext(t):"ArrowLeft"!=e.key&&"ArrowUp"!=e.key||this.selectPrevious(t))}mousedownHandler(){this.mouseIsDown=!0}mouseupHandler(){this.mouseIsDown=!1}has(e){return this.getSet(e.name).set.has(e)}selectPrevious(e){const t=this.getOrdered(e),i=t.indexOf(e),r=t[i-1]||t[t.length-1];return this.select(r),r}selectNext(e){const t=this.getOrdered(e),i=t.indexOf(e),r=t[i+1]||t[0];return this.select(r),r}select(e){e.click()}focus(e){if(this.mouseIsDown)return;const t=this.getSet(e.name),i=this.focusedSet;this.focusedSet=t,i!=t&&t.selected&&t.selected!=e&&t.selected.focus()}isAnySelected(e){const t=this.getSet(e.name);for(const e of t.set)if(e.checked)return!0;return!1}getOrdered(e){const t=this.getSet(e.name);return t.ordered||(t.ordered=Array.from(t.set),t.ordered.sort(((e,t)=>e.compareDocumentPosition(t)==Node.DOCUMENT_POSITION_PRECEDING?1:0))),t.ordered}getSet(e){return this.sets[e]||(this.sets[e]=new K),this.sets[e]}register(e){const t=e.name||e.getAttribute("name")||"",i=this.getSet(t);i.set.add(e),i.ordered=null}unregister(e){const t=this.getSet(e.name);t.set.delete(e),t.ordered=null,t.selected==e&&(t.selected=null)}update(e){if(this.updating)return;this.updating=!0;const t=this.getSet(e.name);if(e.checked){for(const i of t.set)i!=e&&(i.checked=!1);t.selected=e}if(this.isAnySelected(e))for(const e of t.set){if(void 0===e.formElementTabIndex)break;e.formElementTabIndex=e.checked?0:-1}this.updating=!1}}var Q={NATIVE_CONTROL_SELECTOR:".mdc-radio__native-control"},X={DISABLED:"mdc-radio--disabled",ROOT:"mdc-radio"},Z=function(i){function r(e){return i.call(this,t(t({},r.defaultAdapter),e))||this}return e(r,i),Object.defineProperty(r,"cssClasses",{get:function(){return X},enumerable:!1,configurable:!0}),Object.defineProperty(r,"strings",{get:function(){return Q},enumerable:!1,configurable:!0}),Object.defineProperty(r,"defaultAdapter",{get:function(){return{addClass:function(){},removeClass:function(){},setNativeControlDisabled:function(){}}},enumerable:!1,configurable:!0}),r.prototype.setDisabled=function(e){var t=r.cssClasses.DISABLED;this.adapter.setNativeControlDisabled(e),e?this.adapter.addClass(t):this.adapter.removeClass(t)},r}(i);class ee extends P{constructor(){super(...arguments),this._checked=!1,this.useStateLayerCustomProperties=!1,this.global=!1,this.disabled=!1,this.value="on",this.name="",this.reducedTouchTarget=!1,this.mdcFoundationClass=Z,this.formElementTabIndex=0,this.focused=!1,this.shouldRenderRipple=!1,this.rippleElement=null,this.rippleHandlers=new m((()=>(this.shouldRenderRipple=!0,this.ripple.then((e=>{this.rippleElement=e})),this.ripple)))}get checked(){return this._checked}set checked(e){var t,i;const r=this._checked;e!==r&&(this._checked=e,this.formElement&&(this.formElement.checked=e),null===(t=this._selectionController)||void 0===t||t.update(this),!1===e&&(null===(i=this.formElement)||void 0===i||i.blur()),this.requestUpdate("checked",r),this.dispatchEvent(new Event("checked",{bubbles:!0,composed:!0})))}_handleUpdatedValue(e){this.formElement.value=e}renderRipple(){return this.shouldRenderRipple?h`<mwc-ripple unbounded accent
        .internalUseStateLayerCustomProperties="${this.useStateLayerCustomProperties}"
        .disabled="${this.disabled}"></mwc-ripple>`:""}get isRippleActive(){var e;return(null===(e=this.rippleElement)||void 0===e?void 0:e.isActive)||!1}connectedCallback(){super.connectedCallback(),this._selectionController=J.getController(this),this._selectionController.register(this),this._selectionController.update(this)}disconnectedCallback(){this._selectionController.unregister(this),this._selectionController=void 0}focus(){this.formElement.focus()}createAdapter(){return Object.assign(Object.assign({},p(this.mdcRoot)),{setNativeControlDisabled:e=>{this.formElement.disabled=e}})}handleFocus(){this.focused=!0,this.handleRippleFocus()}handleClick(){this.formElement.focus()}handleBlur(){this.focused=!1,this.formElement.blur(),this.rippleHandlers.endFocus()}setFormData(e){this.name&&this.checked&&e.append(this.name,this.value)}render(){const e={"mdc-radio--touch":!this.reducedTouchTarget,"mdc-ripple-upgraded--background-focused":this.focused,"mdc-radio--disabled":this.disabled};return h`
      <div class="mdc-radio ${u(e)}">
        <input
          tabindex="${this.formElementTabIndex}"
          class="mdc-radio__native-control"
          type="radio"
          name="${this.name}"
          aria-label="${b(this.ariaLabel)}"
          aria-labelledby="${b(this.ariaLabelledBy)}"
          .checked="${this.checked}"
          .value="${this.value}"
          ?disabled="${this.disabled}"
          @change="${this.changeHandler}"
          @focus="${this.handleFocus}"
          @click="${this.handleClick}"
          @blur="${this.handleBlur}"
          @mousedown="${this.handleRippleMouseDown}"
          @mouseenter="${this.handleRippleMouseEnter}"
          @mouseleave="${this.handleRippleMouseLeave}"
          @touchstart="${this.handleRippleTouchStart}"
          @touchend="${this.handleRippleDeactivate}"
          @touchcancel="${this.handleRippleDeactivate}">
        <div class="mdc-radio__background">
          <div class="mdc-radio__outer-circle"></div>
          <div class="mdc-radio__inner-circle"></div>
        </div>
        ${this.renderRipple()}
      </div>`}handleRippleMouseDown(e){const t=()=>{window.removeEventListener("mouseup",t),this.handleRippleDeactivate()};window.addEventListener("mouseup",t),this.rippleHandlers.startPress(e)}handleRippleTouchStart(e){this.rippleHandlers.startPress(e)}handleRippleDeactivate(){this.rippleHandlers.endPress()}handleRippleMouseEnter(){this.rippleHandlers.startHover()}handleRippleMouseLeave(){this.rippleHandlers.endHover()}handleRippleFocus(){this.rippleHandlers.startFocus()}changeHandler(){this.checked=this.formElement.checked}}r([o(".mdc-radio")],ee.prototype,"mdcRoot",void 0),r([o("input")],ee.prototype,"formElement",void 0),r([a()],ee.prototype,"useStateLayerCustomProperties",void 0),r([d({type:Boolean})],ee.prototype,"global",void 0),r([d({type:Boolean,reflect:!0})],ee.prototype,"checked",null),r([d({type:Boolean}),c((function(e){this.mdcFoundation.setDisabled(e)}))],ee.prototype,"disabled",void 0),r([d({type:String}),c((function(e){this._handleUpdatedValue(e)}))],ee.prototype,"value",void 0),r([d({type:String})],ee.prototype,"name",void 0),r([d({type:Boolean})],ee.prototype,"reducedTouchTarget",void 0),r([d({type:Number})],ee.prototype,"formElementTabIndex",void 0),r([a()],ee.prototype,"focused",void 0),r([a()],ee.prototype,"shouldRenderRipple",void 0),r([s("mwc-ripple")],ee.prototype,"ripple",void 0),r([n,d({attribute:"aria-label"})],ee.prototype,"ariaLabel",void 0),r([n,d({attribute:"aria-labelledby"})],ee.prototype,"ariaLabelledBy",void 0),r([l({passive:!0})],ee.prototype,"handleRippleTouchStart",null);const te=_`.mdc-touch-target-wrapper{display:inline}.mdc-radio{padding:calc((40px - 20px) / 2)}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.54)}.mdc-radio .mdc-radio__native-control:enabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__native-control:enabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio .mdc-radio__background::before{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__background::before{top:calc(-1 * (40px - 20px) / 2);left:calc(-1 * (40px - 20px) / 2);width:40px;height:40px}.mdc-radio .mdc-radio__native-control{top:calc((40px - 40px) / 2);right:calc((40px - 40px) / 2);left:calc((40px - 40px) / 2);width:40px;height:40px}@media screen and (forced-colors: active),(-ms-high-contrast: active){.mdc-radio.mdc-radio--disabled [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio.mdc-radio--disabled .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio.mdc-radio--disabled [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio.mdc-radio--disabled .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio.mdc-radio--disabled [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio.mdc-radio--disabled .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:GrayText}}.mdc-radio{display:inline-block;position:relative;flex:0 0 auto;box-sizing:content-box;width:20px;height:20px;cursor:pointer;will-change:opacity,transform,border-color,color}.mdc-radio__background{display:inline-block;position:relative;box-sizing:border-box;width:20px;height:20px}.mdc-radio__background::before{position:absolute;transform:scale(0, 0);border-radius:50%;opacity:0;pointer-events:none;content:"";transition:opacity 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__outer-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;border-width:2px;border-style:solid;border-radius:50%;transition:border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__inner-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;transform:scale(0, 0);border-width:10px;border-style:solid;border-radius:50%;transition:transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__native-control{position:absolute;margin:0;padding:0;opacity:0;cursor:inherit;z-index:1}.mdc-radio--touch{margin-top:4px;margin-bottom:4px;margin-right:4px;margin-left:4px}.mdc-radio--touch .mdc-radio__native-control{top:calc((40px - 48px) / 2);right:calc((40px - 48px) / 2);left:calc((40px - 48px) / 2);width:48px;height:48px}.mdc-radio.mdc-ripple-upgraded--background-focused .mdc-radio__focus-ring,.mdc-radio:not(.mdc-ripple-upgraded):focus .mdc-radio__focus-ring{pointer-events:none;border:2px solid transparent;border-radius:6px;box-sizing:content-box;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);height:100%;width:100%}@media screen and (forced-colors: active){.mdc-radio.mdc-ripple-upgraded--background-focused .mdc-radio__focus-ring,.mdc-radio:not(.mdc-ripple-upgraded):focus .mdc-radio__focus-ring{border-color:CanvasText}}.mdc-radio.mdc-ripple-upgraded--background-focused .mdc-radio__focus-ring::after,.mdc-radio:not(.mdc-ripple-upgraded):focus .mdc-radio__focus-ring::after{content:"";border:2px solid transparent;border-radius:8px;display:block;position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);height:calc(100% + 4px);width:calc(100% + 4px)}@media screen and (forced-colors: active){.mdc-radio.mdc-ripple-upgraded--background-focused .mdc-radio__focus-ring::after,.mdc-radio:not(.mdc-ripple-upgraded):focus .mdc-radio__focus-ring::after{border-color:CanvasText}}.mdc-radio__native-control:checked+.mdc-radio__background,.mdc-radio__native-control:disabled+.mdc-radio__background{transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__outer-circle{transition:border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio--disabled{cursor:default;pointer-events:none}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle{transform:scale(0.5);transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:disabled+.mdc-radio__background,[aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background{cursor:default}.mdc-radio__native-control:focus+.mdc-radio__background::before{transform:scale(1);opacity:.12;transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}:host{display:inline-block;outline:none}.mdc-radio{vertical-align:bottom}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-unchecked-color, rgba(0, 0, 0, 0.54))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}`;let ie=class extends ee{};ie.styles=[te],ie=r([f("mwc-radio")],ie);var re={ROOT:"mdc-form-field"},oe={LABEL_SELECTOR:".mdc-form-field > label"},ae=function(i){function r(e){var o=i.call(this,t(t({},r.defaultAdapter),e))||this;return o.click=function(){o.handleClick()},o}return e(r,i),Object.defineProperty(r,"cssClasses",{get:function(){return re},enumerable:!1,configurable:!0}),Object.defineProperty(r,"strings",{get:function(){return oe},enumerable:!1,configurable:!0}),Object.defineProperty(r,"defaultAdapter",{get:function(){return{activateInputRipple:function(){},deactivateInputRipple:function(){},deregisterInteractionHandler:function(){},registerInteractionHandler:function(){}}},enumerable:!1,configurable:!0}),r.prototype.init=function(){this.adapter.registerInteractionHandler("click",this.click)},r.prototype.destroy=function(){this.adapter.deregisterInteractionHandler("click",this.click)},r.prototype.handleClick=function(){var e=this;this.adapter.activateInputRipple(),requestAnimationFrame((function(){e.adapter.deactivateInputRipple()}))},r}(i);class de extends v{constructor(){super(...arguments),this.alignEnd=!1,this.spaceBetween=!1,this.nowrap=!1,this.label="",this.mdcFoundationClass=ae}createAdapter(){return{registerInteractionHandler:(e,t)=>{this.labelEl.addEventListener(e,t)},deregisterInteractionHandler:(e,t)=>{this.labelEl.removeEventListener(e,t)},activateInputRipple:async()=>{const e=this.input;if(e instanceof P){const t=await e.ripple;t&&t.startPress()}},deactivateInputRipple:async()=>{const e=this.input;if(e instanceof P){const t=await e.ripple;t&&t.endPress()}}}}get input(){var e,t;return null!==(t=null===(e=this.slottedInputs)||void 0===e?void 0:e[0])&&void 0!==t?t:null}render(){const e={"mdc-form-field--align-end":this.alignEnd,"mdc-form-field--space-between":this.spaceBetween,"mdc-form-field--nowrap":this.nowrap};return h`
      <div class="mdc-form-field ${u(e)}">
        <slot></slot>
        <label class="mdc-label"
               @click="${this._labelClick}">${this.label}</label>
      </div>`}click(){this._labelClick()}_labelClick(){const e=this.input;e&&(e.focus(),e.click())}}r([d({type:Boolean})],de.prototype,"alignEnd",void 0),r([d({type:Boolean})],de.prototype,"spaceBetween",void 0),r([d({type:Boolean})],de.prototype,"nowrap",void 0),r([d({type:String}),c((async function(e){var t;null===(t=this.input)||void 0===t||t.setAttribute("aria-label",e)}))],de.prototype,"label",void 0),r([o(".mdc-form-field")],de.prototype,"mdcRoot",void 0),r([g("",!0,"*")],de.prototype,"slottedInputs",void 0),r([o("label")],de.prototype,"labelEl",void 0);const ce=_`.mdc-form-field{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87));display:inline-flex;align-items:center;vertical-align:middle}.mdc-form-field>label{margin-left:0;margin-right:auto;padding-left:4px;padding-right:0;order:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{margin-left:auto;margin-right:0}[dir=rtl] .mdc-form-field>label,.mdc-form-field>label[dir=rtl]{padding-left:0;padding-right:4px}.mdc-form-field--nowrap>label{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.mdc-form-field--align-end>label{margin-left:auto;margin-right:0;padding-left:0;padding-right:4px;order:-1}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{margin-left:0;margin-right:auto}[dir=rtl] .mdc-form-field--align-end>label,.mdc-form-field--align-end>label[dir=rtl]{padding-left:4px;padding-right:0}.mdc-form-field--space-between{justify-content:space-between}.mdc-form-field--space-between>label{margin:0}[dir=rtl] .mdc-form-field--space-between>label,.mdc-form-field--space-between>label[dir=rtl]{margin:0}:host{display:inline-flex}.mdc-form-field{width:100%}::slotted(*){-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;font-family:Roboto, sans-serif;font-family:var(--mdc-typography-body2-font-family, var(--mdc-typography-font-family, Roboto, sans-serif));font-size:0.875rem;font-size:var(--mdc-typography-body2-font-size, 0.875rem);line-height:1.25rem;line-height:var(--mdc-typography-body2-line-height, 1.25rem);font-weight:400;font-weight:var(--mdc-typography-body2-font-weight, 400);letter-spacing:0.0178571429em;letter-spacing:var(--mdc-typography-body2-letter-spacing, 0.0178571429em);text-decoration:inherit;text-decoration:var(--mdc-typography-body2-text-decoration, inherit);text-transform:inherit;text-transform:var(--mdc-typography-body2-text-transform, inherit);color:rgba(0, 0, 0, 0.87);color:var(--mdc-theme-text-primary-on-background, rgba(0, 0, 0, 0.87))}::slotted(mwc-switch){margin-right:10px}[dir=rtl] ::slotted(mwc-switch),::slotted(mwc-switch[dir=rtl]){margin-left:10px}`;let se=class extends de{};se.styles=[ce],se=r([f("mwc-formfield")],se);let ne=class extends w{constructor(){super(...arguments),this._busy=!1,this._board="esp32dev",this._hasWifiSecrets=void 0,this._customBoard="",this._data={ssid:`!secret ${W}`,psk:`!secret ${q}`},this._state=A?"basic_config":"ask_esphome_web",this._installed=!1,this._cleanNameInput=e=>{this._error=void 0;const t=e.target;t.value=C(t.value)},this._cleanNameBlur=e=>{const t=e.target;t.value=E(t.value)},this._cleanSSIDBlur=e=>{const t=e.target;t.value=t.value.trim()}}render(){let e,t,i=!1;return"ask_esphome_web"===this._state?[e,t,i]=this._renderAskESPHomeWeb():"basic_config"===this._state?[e,t,i]=this._renderBasicConfig():"pick_board"===this._state?(e="Select your device type",t=this._renderPickBoard()):"connect_webserial"===this._state?(e="Installation",t=this._renderConnectSerial()):"connecting_webserial"===this._state?(t=this._renderProgress("Connecting"),i=!0):"prepare_flash"===this._state?(t=this._renderProgress("Preparing installation"),i=!0):"flashing"===this._state?(t=void 0===this._writeProgress?this._renderProgress("Erasing"):this._renderProgress(h`
                Installing<br /><br />
                This will take
                ${"esp01_1m"===this._board?"a minute":"2 minutes"}.<br />
                Keep this page visible to prevent slow down
              `,this._writeProgress>3?this._writeProgress:void 0),i=!0):"wait_come_online"===this._state?(t=this._renderProgress("Finding device on network"),i=!0):"done"===this._state&&(t=this._renderDone()),h`
      <mwc-dialog
        open
        heading=${e}
        scrimClickAction
        @closed=${this._handleClose}
        .hideActions=${i}
        >${t}</mwc-dialog
      >
    `}_renderProgress(e,t){return h`
      <div class="center">
        <div>
          <mwc-circular-progress
            active
            ?indeterminate=${void 0===t}
            .progress=${void 0!==t?t/100:void 0}
            density="8"
          ></mwc-circular-progress>
          ${void 0!==t?h`<div class="progress-pct">${t}%</div>`:""}
        </div>
        ${e}
      </div>
    `}_renderMessage(e,t,i){return h`
      <div class="center">
        <div class="icon">${e}</div>
        ${t}
      </div>
      ${i?h`
            <mwc-button
              slot="primaryAction"
              dialogAction="ok"
              label="Close"
            ></mwc-button>
          `:""}
    `}_renderAskESPHomeWeb(){return["New device",h`
      <div>
        A device needs to be connected to a computer using a USB cable to be
        added to ESPHome. Once added, ESPHome will interact with the device
        wirelessly.
      </div>
      <div>
        ${T?"Your browser does not support WebSerial.":"You are not browsing the dashboard over a secure connection (HTTPS)."}
        This prevents ESPHome from being able to install this on devices
        connected to this computer.
      </div>
      <div>
        You will still be able to install ESPHome by connecting the device to
        the computer that runs the ESPHome dashboard.
      </div>
      <div>
        Alternatively, you can use ESPHome Web to prepare a device for being
        used with ESPHome using this computer.
      </div>

      <mwc-button
        slot="primaryAction"
        label="Continue"
        @click=${()=>{this._state="basic_config"}}
      ></mwc-button>

      <a
        slot="secondaryAction"
        href=${"https://web.esphome.io/?dashboard_wizard"}
        target="_blank"
        rel="noopener"
      >
        <mwc-button
          no-attention
          dialogAction="close"
          label="Open ESPHome Web"
        ></mwc-button>
      </a>
    `,!1]}_renderBasicConfig(){if(void 0===this._hasWifiSecrets)return[void 0,this._renderProgress("Initializing"),!0];return[A?"New device":"Create configuration",h`
      ${this._error?h`<div class="error">${this._error}</div>`:""}

      <mwc-textfield
        label="Name"
        name="name"
        required
        pattern="^[a-z0-9-]+$"
        helper="Lowercase letters (a-z), numbers (0-9) or dash (-)"
        @input=${this._cleanNameInput}
        @blur=${this._cleanNameBlur}
      ></mwc-textfield>

      ${this._hasWifiSecrets?h`
            <div>
              This device will be configured to connect to the Wi-Fi network
              stored in your secrets.
            </div>
          `:h`
            <div>
              Enter the credentials of the Wi-Fi network that you want your
              device to connect to.
            </div>
            <div>
              This information will be stored in your secrets and used for this
              and future devices. You can edit the information later by editing
              your secrets at the top of the page.
            </div>

            <mwc-textfield
              label="Network name"
              name="ssid"
              required
              @blur=${this._cleanSSIDBlur}
            ></mwc-textfield>

            <mwc-textfield
              label="Password"
              name="password"
              type="password"
              helper="Leave blank if no password"
            ></mwc-textfield>
          `}

      <mwc-button
        slot="primaryAction"
        label="Next"
        @click=${this._handleBasicConfigSubmit}
      ></mwc-button>

      <mwc-button
        no-attention
        slot="secondaryAction"
        dialogAction="close"
        label="Cancel"
      ></mwc-button>
    `,!1]}_renderPickBoard(){return h`
      ${this._error?h`<div class="error">${this._error}</div>`:""}

      <div>
        Select the type of device that this configuration will be installed on.
      </div>
      <mwc-formfield label="ESP32" checked>
        <mwc-radio
          name="board"
          .value=${"esp32dev"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"esp32dev"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="ESP32-S2">
        <mwc-radio
          name="board"
          .value=${"esp32-s2-saola-1"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"esp32-s2-saola-1"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="ESP32-S3">
        <mwc-radio
          name="board"
          .value=${"esp32-s3-devkitc-1"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"esp32-s3-devkitc-1"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="ESP32-C3">
        <mwc-radio
          name="board"
          .value=${"esp32-c3-devkitm-1"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"esp32-c3-devkitm-1"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="ESP8266">
        <mwc-radio
          name="board"
          .value=${"esp01_1m"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"esp01_1m"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="Raspberry Pi Pico W">
        <mwc-radio
          name="board"
          .value=${"rpipicow"}
          @click=${this._handlePickBoardRadio}
          ?checked=${"rpipicow"===this._board}
        ></mwc-radio>
      </mwc-formfield>

      <mwc-formfield label="Pick specific board">
        <mwc-radio
          name="board"
          value="CUSTOM"
          @click=${this._handlePickBoardRadio}
          ?checked=${"CUSTOM"===this._board}
        ></mwc-radio>
      </mwc-formfield>
      ${"CUSTOM"!==this._board?"":h`
            <div class="formfield-extra">
              <select @change=${this._handlePickBoardCustom}>
                ${e=this._supportedBoards,e&&h`
    <optgroup label="ESP32">
      ${Object.keys(e.esp32).map((t=>h`<option value="${t}">${e.esp32[t]}</option>`))}
    </optgroup>
    <optgroup label="ESP8266">
      ${Object.keys(e.esp8266).map((t=>h`<option value="${t}">${e.esp8266[t]}</option>`))}
    </optgroup>
    <optgroup label="Raspberry Pi">
      ${Object.keys(e.rp2040).map((t=>h`<option value="${t}">${e.rp2040[t]}</option>`))}
    </optgroup>
  `}
              </select>
            </div>
          `}
      <div>
        Pick a custom board if the default targets don't work or if you want to
        use the pin numbers printed on the device in your configuration.
      </div>

      <mwc-button
        slot="primaryAction"
        label="Next"
        @click=${this._handlePickBoardSubmit}
      ></mwc-button>
      <mwc-button
        no-attention
        slot="secondaryAction"
        dialogAction="close"
        label="Cancel"
      ></mwc-button>
    `;var e}_renderConnectSerial(){return h`
      ${this._error?h`<div class="error">${this._error}</div>`:""}

      <div>
        ESPHome will now create your configuration and install it on your
        device.
      </div>

      <div>
        Connect your ESP8266 or ESP32 with a USB cable to your computer and
        click on connect. You need to do this once. Later updates install
        wirelessly.
        <a
          href="https://esphome.io/guides/getting_started_hassio.html#webserial"
          target="_blank"
          >Learn more</a
        >
      </div>

      <div>
        Skip this step to install it on your device later or if you are using a
        Raspberry Pi Pico.
      </div>

      <mwc-button
        slot="primaryAction"
        label="Connect"
        .disabled=${this._busy}
        @click=${this._handleConnectSerialSubmit}
      ></mwc-button>
      <mwc-button
        no-attention
        slot="secondaryAction"
        label="Skip this step"
        .disabled=${this._busy}
        @click=${this._handleConnectSerialSkip}
      ></mwc-button>
    `}_renderDone(){return this._error?this._renderMessage("👀",this._error,!0):h`
      ${this._renderMessage("🎉","Configuration created!",this._installed)}
      ${this._installed?"":h`
            <div>
              You can now install the configuration to your device. The first
              time this requires a cable.
            </div>
            <div>
              Once the device is installed and connected to your network, you
              will be able to manage it wirelessly.
            </div>
            <mwc-button
              slot="primaryAction"
              dialogAction="ok"
              label="Install"
              @click=${()=>k(`${this._data.name}.yaml`)}
            ></mwc-button>
            <mwc-button
              no-attention
              slot="secondaryAction"
              dialogAction="close"
              label="Skip"
            ></mwc-button>
          `}
    `}firstUpdated(e){super.firstUpdated(e),Y().then((e=>{this._hasWifiSecrets=e})),y("./boards").then((e=>{this._supportedBoards=e}))}updated(e){if(super.updated(e),e.has("_state")||e.has("_hasWifiSecrets")){const e=this.shadowRoot.querySelector("mwc-textfield, mwc-radio, mwc-button");e&&e.updateComplete.then((()=>e.focus()))}e.has("_board")&&"CUSTOM"===this._board&&(this._customBoard=this.shadowRoot.querySelector("select").value)}async _handleBasicConfigSubmit(){const e=this._inputName,t=e.reportValidity(),i=!!this._hasWifiSecrets||this._inputSSID.reportValidity();if(!t||!i)return void(t?this._inputSSID.focus():e.focus());const r=e.value;try{return await L(`${r}.yaml`),void(this._error="Name already in use")}catch(e){}this._data.name=r,this._hasWifiSecrets||(this._wifi={ssid:this._inputSSID.value,password:this._inputPassword.value}),setTimeout((()=>{this._state=A&&T?"connect_webserial":"pick_board"}),0)}_handlePickBoardRadio(e){this._board=e.target.value}_handlePickBoardCustom(e){this._customBoard=e.target.value}async _handlePickBoardSubmit(){this._data.board="CUSTOM"===this._board?this._customBoard:this._board,this._busy=!0;try{this._wifi&&await V(this._wifi.ssid,this._wifi.password),await F(this._data),x(),this._state="done"}catch(e){this._error=e.message||e}finally{this._busy=!1}}_handleConnectSerialSkip(){this._error=void 0,this._state="pick_board"}async _handleConnectSerialSubmit(){let e;this._busy=!0,this._error=void 0;let t=!1;try{try{e=await R(console)}catch(e){return console.error(e),void("NotFoundError"===e.name?B():this._error=e.message||String(e))}this._state="connecting_webserial";try{await e.initialize()}catch(e){return console.error(e),this._state="connect_webserial",void(this._error="Failed to initialize. Try resetting your device or holding the BOOT button while selecting your serial port until it starts preparing the installation.")}if(this._state="prepare_flash",e.chipFamily===I)this._data.board="esp32dev";else if(e.chipFamily===z)this._data.board="esp01_1m";else if(e.chipFamily===O)this._data.board="esp32-s2-saola-1";else if(e.chipFamily===D)this._data.board="esp32-s3-devkitc-1";else{if(e.chipFamily!==H)return this._state="connect_webserial",void(this._error=`Unable to identify the connected device (${e.chipFamily}).`);this._data.board="esp32-c3-devkitm-1"}try{await F(this._data)}catch(e){return console.error(e),this._state="connect_webserial",void(this._error="Unable to create the configuration")}t=!0;try{await N(this._configFilename)}catch(e){return console.error(e),this._state="connect_webserial",void(this._error="Unable to compile the configuration")}this._state="flashing";try{const t=await U(this._configFilename);await M(e,t,!0,(e=>{this._writeProgress=e}))}catch(e){return console.error(e),this._state="connect_webserial",void(this._error="Error installing the configuration")}t=!1,this._installed=!0,await e.hardReset(),this._state="wait_come_online";try{await new Promise(((e,t)=>{const i=S((t=>{t[this._configFilename]&&(i(),clearTimeout(r),e(void 0))})),r=setTimeout((()=>{i(),t("Timeout")}),2e4)}))}catch(e){console.error(e),this._error="Configuration created but unable to detect the device on the network"}this._state="done"}finally{this._busy=!1,e&&(e.connected&&(console.log("Disconnecting esp"),await e.disconnect()),console.log("Closing port"),await e.port.close()),t&&await j(this._configFilename)}}get _configFilename(){return`${this._data.name}.yaml`}async _handleClose(){this.parentNode.removeChild(this)}};ne.styles=[$,_`
      :host {
        --mdc-dialog-max-width: 390px;
      }
      mwc-textfield[name="name"] + div {
        margin-top: 18px;
      }
      .center {
        text-align: center;
      }
      mwc-circular-progress {
        margin-bottom: 16px;
      }
      .progress-pct {
        position: absolute;
        top: 50px;
        left: 0;
        right: 0;
      }
      .icon {
        font-size: 50px;
        line-height: 80px;
        color: black;
      }
      .error {
        color: var(--alert-error-color);
        margin-bottom: 16px;
      }
    `],r([a()],ne.prototype,"_busy",void 0),r([a()],ne.prototype,"_board",void 0),r([a()],ne.prototype,"_hasWifiSecrets",void 0),r([a()],ne.prototype,"_writeProgress",void 0),r([a()],ne.prototype,"_state",void 0),r([a()],ne.prototype,"_error",void 0),r([o("mwc-textfield[name=name]")],ne.prototype,"_inputName",void 0),r([o("mwc-textfield[name=ssid]")],ne.prototype,"_inputSSID",void 0),r([o("mwc-textfield[name=password]")],ne.prototype,"_inputPassword",void 0),ne=r([f("esphome-wizard-dialog")],ne);export{ne as ESPHomeWizardDialog};
