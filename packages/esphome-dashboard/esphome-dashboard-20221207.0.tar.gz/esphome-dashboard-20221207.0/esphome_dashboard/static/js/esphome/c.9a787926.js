import{E as o,r as i,b as e,d as t,p as a,n,s,y as d,W as c,U as l}from"./index-b2b66d7f.js";import"./c.493fa92b.js";let r=class extends s{constructor(){super(...arguments),this._showCopied=!1}render(){return d`
      <mwc-dialog
        open
        heading=${`API key for ${this.configuration}`}
        scrimClickAction
        @closed=${this._handleClose}
      >
        ${void 0===this._apiKey?"Loading…":null===this._apiKey?d`Unable to automatically extract API key. Open the configuration
              and look for <code>api:</code>.`:d`
              <div class="key" @click=${this._copyApiKey}>
                <code>${this._apiKey}</code>
                <mwc-button ?disabled=${this._showCopied}
                  >${this._showCopied?"Copied!":"Copy"}</mwc-button
                >
              </div>
            `}
        ${null===this._apiKey?d`
              <mwc-button
                @click=${this._editConfig}
                no-attention
                slot="secondaryAction"
                dialogAction="close"
                label="Open configuration"
              ></mwc-button>
            `:""}

        <mwc-button
          no-attention
          slot="primaryAction"
          dialogAction="close"
          label="Close"
        ></mwc-button>
      </mwc-dialog>
    `}firstUpdated(o){super.firstUpdated(o),c(this.configuration).then((async o=>{var i,e;this._apiKey=null===(e=null===(i=null==o?void 0:o.api)||void 0===i?void 0:i.encryption)||void 0===e?void 0:e.key}))}_copyApiKey(){(async o=>{if(navigator.clipboard)try{return void await navigator.clipboard.writeText(o)}catch{}const i=document.createElement("textarea");i.value=o,document.body.appendChild(i),i.select(),document.execCommand("copy"),document.body.removeChild(i)})(this._apiKey),this._showCopied=!0,setTimeout((()=>this._showCopied=!1),2e3)}_editConfig(){l(this.configuration)}_handleClose(){this.parentNode.removeChild(this)}};r.styles=[o,i`
      .key {
        position: relative;
        display: flex;
        align-items: center;
      }
      code {
        word-break: break-all;
      }
      .key mwc-button {
        margin-left: 16px;
      }
      .copied {
        font-weight: bold;
        color: var(--alert-success-color);

        position: absolute;
        background-color: var(--mdc-theme-surface, #fff);
        padding: 10px;
        right: 0;
        font-size: 1.2em;
      }
    `],e([t()],r.prototype,"configuration",void 0),e([a()],r.prototype,"_apiKey",void 0),e([a()],r.prototype,"_showCopied",void 0),r=e([n("esphome-show-api-key-dialog")],r);
