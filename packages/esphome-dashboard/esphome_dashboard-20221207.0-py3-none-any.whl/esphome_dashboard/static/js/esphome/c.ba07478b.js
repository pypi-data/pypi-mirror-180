import{b as o,d as i,p as t,n as s,s as e,y as a,U as n,j as l}from"./index-b2b66d7f.js";import"./c.e36b571b.js";import"./c.493fa92b.js";let d=class extends e{render(){const o=void 0===this._valid?"":this._valid?"✅":"❌";return a`
      <esphome-process-dialog
        .heading=${`Validate ${this.configuration} ${o}`}
        .type=${"validate"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Edit"
          @click=${this._openEdit}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Install"
          @click=${this._openInstall}
        ></mwc-button>
      </esphome-process-dialog>
    `}_openEdit(){n(this.configuration)}_openInstall(){l(this.configuration)}_handleProcessDone(o){this._valid=0==o.detail}_handleClose(){this.parentNode.removeChild(this)}};o([i()],d.prototype,"configuration",void 0),o([t()],d.prototype,"_valid",void 0),d=o([s("esphome-validate-dialog")],d);
