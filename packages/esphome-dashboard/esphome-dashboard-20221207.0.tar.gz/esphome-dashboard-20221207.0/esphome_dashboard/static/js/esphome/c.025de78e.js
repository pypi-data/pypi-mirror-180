import{r as o,b as t,d as e,p as i,n as r,s,y as a}from"./index-b2b66d7f.js";import"./c.e36b571b.js";import{o as n}from"./c.0c8eb282.js";import{e as c}from"./c.5644905a.js";import"./c.493fa92b.js";import"./c.c6160864.js";import"./c.9302e097.js";import"./c.0b38eff0.js";import"./c.b2354a5a.js";let d=class extends s{constructor(){super(...arguments),this.downloadFactoryFirmware=!0}render(){return a`
      <esphome-process-dialog
        .heading=${`Download ${this.configuration}`}
        .type=${"compile"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        ${void 0===this._result?"":0===this._result?a`
              <a
                slot="secondaryAction"
                href="${c(this.configuration,this.downloadFactoryFirmware)}"
              >
                <mwc-button label="Download"></mwc-button>
              </a>
            `:a`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_handleProcessDone(o){if(this._result=o.detail,0!==o.detail)return;const t=document.createElement("a");t.download=this.configuration+".bin",t.href=c(this.configuration,this.downloadFactoryFirmware),document.body.appendChild(t),t.click(),t.remove()}_handleRetry(){n(this.configuration,this.downloadFactoryFirmware)}_handleClose(){this.parentNode.removeChild(this)}};d.styles=o`
    a {
      text-decoration: none;
    }
  `,t([e()],d.prototype,"configuration",void 0),t([e()],d.prototype,"downloadFactoryFirmware",void 0),t([i()],d.prototype,"_result",void 0),d=t([r("esphome-compile-dialog")],d);
