"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[79042],{90394:(e,t,i)=>{function a(e){if(null===e||!0===e||!1===e)return NaN;var t=Number(e);return isNaN(t)?t:t<0?Math.ceil(t):Math.floor(t)}i.d(t,{Z:()=>a})},79021:(e,t,i)=>{i.d(t,{Z:()=>s});var a=i(90394),r=i(34327),n=i(23682);function s(e,t){(0,n.Z)(2,arguments);var i=(0,r.Z)(e),s=(0,a.Z)(t);return isNaN(s)?new Date(NaN):s?(i.setDate(i.getDate()+s),i):i}},59699:(e,t,i)=>{i.d(t,{Z:()=>o});var a=i(90394),r=i(39244),n=i(23682),s=36e5;function o(e,t){(0,n.Z)(2,arguments);var i=(0,a.Z)(t);return(0,r.Z)(e,i*s)}},39244:(e,t,i)=>{i.d(t,{Z:()=>s});var a=i(90394),r=i(34327),n=i(23682);function s(e,t){(0,n.Z)(2,arguments);var i=(0,r.Z)(e).getTime(),s=(0,a.Z)(t);return new Date(i+s)}},72949:(e,t,i)=>{i.d(t,{Z:()=>n});var a=i(34327),r=i(23682);function n(e){(0,r.Z)(1,arguments);var t=(0,a.Z)(e);return t.setMinutes(0,0,0),t}},79042:(e,t,i)=>{i.a(e,(async e=>{i.r(t);i(51187);var a=i(72949),r=i(59699),n=i(79021),s=i(37500),o=i(33310),l=i(99137),d=i(94653),c=(i(85066),i(51144)),h=i(11654),u=i(91476),p=i(29152),m=i(89207),f=e([p,u,d]);function v(){v=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(a){t.forEach((function(t){var r=t.placement;if(t.kind===a&&("static"===r||"prototype"===r)){var n="static"===r?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var a=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===a?void 0:a.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],a=[],r={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,r)}),this),e.forEach((function(e){if(!g(e))return i.push(e);var t=this.decorateElement(e,r);i.push(t.element),i.push.apply(i,t.extras),a.push.apply(a,t.finishers)}),this),!t)return{elements:i,finishers:a};var n=this.decorateConstructor(i,t);return a.push.apply(a,n.finishers),n.finishers=a,n},addElementPlacement:function(e,t,i){var a=t[e.placement];if(!i&&-1!==a.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");a.push(e.key)},decorateElement:function(e,t){for(var i=[],a=[],r=e.decorators,n=r.length-1;n>=0;n--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var o=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,r[n])(o)||o);e=l.element,this.addElementPlacement(e,t),l.finisher&&a.push(l.finisher);var d=l.extras;if(d){for(var c=0;c<d.length;c++)this.addElementPlacement(d[c],t);i.push.apply(i,d)}}return{element:e,finishers:a,extras:i}},decorateConstructor:function(e,t){for(var i=[],a=t.length-1;a>=0;a--){var r=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[a])(r)||r);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var s=0;s<e.length-1;s++)for(var o=s+1;o<e.length;o++)if(e[s].key===e[o].key&&e[s].placement===e[o].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return D(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?D(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=w(e.key),a=String(e.placement);if("static"!==a&&"prototype"!==a&&"own"!==a)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+a+'"');var r=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:a,descriptor:Object.assign({},r)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(r,"get","The property descriptor of a field descriptor"),this.disallowProperty(r,"set","The property descriptor of a field descriptor"),this.disallowProperty(r,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:b(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=b(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var a=(0,t[i])(e);if(void 0!==a){if("function"!=typeof a)throw new TypeError("Finishers must return a constructor.");e=a}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function y(e){var t,i=w(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var a={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(a.decorators=e.decorators),"field"===e.kind&&(a.initializer=e.value),a}function _(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function g(e){return e.decorators&&e.decorators.length}function k(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function b(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function w(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var a=i.call(e,t||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function D(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,a=new Array(t);i<t;i++)a[i]=e[i];return a}[p,u,d]=f.then?await f:f;const E=e=>s.dy`<mwc-list-item>
  <span>${e.name}</span>
</mwc-list-item>`;!function(e,t,i,a){var r=v();if(a)for(var n=0;n<a.length;n++)r=a[n](r);var s=t((function(e){r.initializeInstanceElements(e,o.elements)}),i),o=r.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},a=0;a<e.length;a++){var r,n=e[a];if("method"===n.kind&&(r=t.find(i)))if(k(n.descriptor)||k(r.descriptor)){if(g(n)||g(r))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");r.descriptor=n.descriptor}else{if(g(n)){if(g(r))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");r.decorators=n.decorators}_(n,r)}else t.push(n)}return t}(s.d.map(y)),e);r.initializeClassElements(s.F,o.elements),r.runClassFinishers(s.F,o.finishers)}([(0,o.Mo)("dialog-calendar-event-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_calendars",value:()=>[]},{kind:"field",decorators:[(0,o.SB)()],key:"_calendarId",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_data",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_allDay",value:()=>!1},{kind:"field",decorators:[(0,o.SB)()],key:"_dtstart",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_dtend",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_submitting",value:()=>!1},{kind:"method",key:"showDialog",value:async function(e){if(this._error=void 0,this._params=e,this._calendars=e.calendars,this._calendarId=e.calendarId||this._calendars[0].entity_id,e.entry){const t=e.entry;this._data=t,this._allDay=(0,l.J)(t.dtstart),this._allDay?(this._dtstart=new Date(t.dtstart),this._dtend=new Date(t.dtend),this._dtend.setDate(this._dtend.getDate()-1)):(this._dtstart=new Date(t.dtstart),this._dtend=new Date(t.dtend))}else this._data={summary:"",dtstart:"",dtend:""},this._allDay=!1,this._dtstart=(0,a.Z)(new Date),this._dtend=(0,r.Z)(this._dtstart,1),this._dateChanged();await this.updateComplete}},{kind:"method",key:"render",value:function(){if(!this._params)return s.dy``;const e=void 0===this._params.entry;return s.dy`
      <ha-dialog
        open
        @closed=${this._close}
        scrimClickAction
        escapeKeyAction
        .heading=${s.dy`
          <div class="header_title">
            ${e?this.hass.localize("ui.components.calendar.event.add"):this._data.summary}
          </div>
          <ha-icon-button
            .label=${this.hass.localize("ui.dialogs.generic.close")}
            .path=${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}
            dialogAction="close"
            class="header_button"
          ></ha-icon-button>
        `}
      >
        <div class="content">
          ${this._error?s.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}

          <ha-textfield
            class="summary"
            name="summary"
            .label=${this.hass.localize("ui.components.calendar.event.summary")}
            required
            @change=${this._handleSummaryChanged}
            error-message=${this.hass.localize("ui.common.error_required")}
            dialogInitialFocus
          ></ha-textfield>
          <ha-combo-box
            name="calendar"
            .hass=${this.hass}
            .label=${this.hass.localize("ui.components.calendar.label")}
            .value=${this._calendarId}
            .renderer=${E}
            .items=${this._calendars}
            item-id-path="entity_id"
            item-value-path="entity_id"
            item-label-path="name"
            required
            @value-changed=${this._handleCalendarChanged}
          ></ha-combo-box>
          <ha-formfield
            .label=${this.hass.localize("ui.components.calendar.event.all_day")}
          >
            <ha-switch
              id="all_day"
              .checked=${this._allDay}
              @change=${this._allDayToggleChanged}
            ></ha-switch>
          </ha-formfield>

          <div>
            <span class="label"
              >${this.hass.localize("ui.components.calendar.event.start")}:</span
            >
            <div class="flex">
              <ha-date-input
                .value=${this._data.dtstart}
                .locale=${this.hass.locale}
                @value-changed=${this._startDateChanged}
              ></ha-date-input>
              ${this._allDay?"":s.dy`<ha-time-input
                    .value=${this._data.dtstart.split("T")[1]}
                    .locale=${this.hass.locale}
                    @value-changed=${this._startTimeChanged}
                  ></ha-time-input>`}
            </div>
          </div>
          <div>
            <span class="label"
              >${this.hass.localize("ui.components.calendar.event.end")}:</span
            >
            <div class="flex">
              <ha-date-input
                .value=${this._data.dtend}
                .min=${this._data.dtstart}
                .locale=${this.hass.locale}
                @value-changed=${this._endDateChanged}
              ></ha-date-input>
              ${this._allDay?"":s.dy`<ha-time-input
                    .value=${this._data.dtend.split("T")[1]}
                    .locale=${this.hass.locale}
                    @value-changed=${this._endTimeChanged}
                  ></ha-time-input>`}
            </div>
          </div>
          <ha-recurrence-rule-editor
            .locale=${this.hass.locale}
            .value=${this._data.rrule||""}
            @value-changed=${this._handleRRuleChanged}
          >
          </ha-recurrence-rule-editor>
        </div>
        ${e?s.dy`
              <mwc-button
                slot="primaryAction"
                @click=${this._createEvent}
                .disabled=${this._submitting}
              >
                ${this.hass.localize("ui.components.calendar.event.add")}
              </mwc-button>
            `:s.dy` <mwc-button
                slot="primaryAction"
                @click=${this._saveEvent}
                .disabled=${this._submitting}
              >
                ${this.hass.localize("ui.components.calendar.event.save")}
              </mwc-button>
              ${this._params.canDelete?s.dy`
                    <mwc-button
                      slot="secondaryAction"
                      class="warning"
                      @click=${this._deleteEvent}
                      .disabled=${this._submitting}
                    >
                      ${this.hass.localize("ui.components.calendar.event.delete")}
                    </mwc-button>
                  `:""}`}
      </ha-dialog>
    `}},{kind:"method",key:"_handleSummaryChanged",value:function(e){this._data.summary=e.target.value}},{kind:"method",key:"_handleRRuleChanged",value:function(e){this._data.rrule=e.detail.value,this.requestUpdate()}},{kind:"method",key:"_allDayToggleChanged",value:function(e){this._allDay=e.target.checked,this._dateChanged()}},{kind:"method",key:"_startDateChanged",value:function(e){this._dtstart=new Date(e.detail.value+"T"+this._dtstart.toISOString().split("T")[1]),this._dateChanged()}},{kind:"method",key:"_endDateChanged",value:function(e){this._dtend=new Date(e.detail.value+"T"+this._dtend.toISOString().split("T")[1]),this._dateChanged()}},{kind:"method",key:"_startTimeChanged",value:function(e){this._dtstart=new Date(this._dtstart.toISOString().split("T")[0]+"T"+e.detail.value),this._dateChanged()}},{kind:"method",key:"_endTimeChanged",value:function(e){this._dtend=new Date(this._dtend.toISOString().split("T")[0]+"T"+e.detail.value),this._dateChanged()}},{kind:"method",key:"_dateChanged",value:function(){this._allDay?(this._data.dtstart=this._dtstart.toISOString(),this._data.dtend=(0,n.Z)(new Date(this._dtend),1).toISOString()):(this._data.dtstart=this._dtstart.toISOString(),this._data.dtend=this._dtend.toISOString())}},{kind:"method",key:"_handleCalendarChanged",value:function(e){this._calendarId=e.detail.value}},{kind:"method",key:"_createEvent",value:async function(){this._submitting=!0;try{await(0,c.fE)(this.hass,this._calendarId,this._data)}catch(e){this._error=e?e.message:"Unknown error"}finally{this._submitting=!1}await this._params.updated(),this._params=void 0}},{kind:"method",key:"_saveEvent",value:async function(){}},{kind:"method",key:"_deleteEvent",value:async function(){this._submitting=!0;const e=this._params.entry,t=await(0,m.Y)(this,{title:this.hass.localize("ui.components.calendar.event.confirm_delete.delete"),text:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.recurring_prompt"):this.hass.localize("ui.components.calendar.event.confirm_delete.prompt"),confirmText:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.delete_this"):this.hass.localize("ui.components.calendar.event.confirm_delete.delete"),confirmFutureText:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.delete_future"):void 0});if(void 0!==t){try{await(0,c.d1)(this.hass,this._calendarId,e.uid,e.recurrence_id||"",t)}catch(e){return void(this._error=e?e.message:"Unknown error")}finally{this._submitting=!1}await this._params.updated(),this._close()}else this._submitting=!1}},{kind:"method",key:"_close",value:function(){this._calendars=[],this._calendarId=void 0,this._params=void 0,this._data=void 0,this._dtstart=void 0,this._dtend=void 0}},{kind:"get",static:!0,key:"styles",value:function(){return[h.yu,s.iv`
        state-info {
          line-height: 40px;
        }
        ha-textfield {
          display: block;
          margin-bottom: 24px;
        }
        ha-formfield {
          display: block;
          padding: 16px 0;
        }
        ha-date-input {
          flex-grow: 1;
        }
        ha-time-input {
          margin-left: 16px;
        }
        ha-recurrence-rule-editor {
          display: block;
          margin-top: 16px;
        }
        .flex {
          display: flex;
          justify-content: space-between;
        }
        .label {
          font-size: 12px;
          font-weight: 500;
          color: var(--input-label-ink-color);
        }
        .date-range-details-content {
          display: inline-block;
        }
        ha-rrule {
          display: block;
        }
        ha-combo-box {
          display: block;
          margin-bottom: 24px;
        }
        ha-svg-icon {
          width: 40px;
          margin-right: 8px;
          margin-inline-end: 8px;
          margin-inline-start: initial;
          direction: var(--direction);
          vertical-align: top;
        }
        ha-rrule {
          display: inline-block;
        }
        .key {
          display: inline-block;
          vertical-align: top;
        }
        .value {
          display: inline-block;
          vertical-align: top;
        }
      `]}}]}}),s.oi)}))}}]);
//# sourceMappingURL=7ce15bdd.js.map