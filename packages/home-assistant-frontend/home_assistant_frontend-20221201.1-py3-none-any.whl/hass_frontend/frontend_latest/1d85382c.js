"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[79042],{59699:(e,t,i)=>{i.d(t,{Z:()=>o});var r=i(90394),a=i(39244),n=i(23682),s=36e5;function o(e,t){(0,n.Z)(2,arguments);var i=(0,r.Z)(t);return(0,a.Z)(e,i*s)}},39244:(e,t,i)=>{i.d(t,{Z:()=>s});var r=i(90394),a=i(34327),n=i(23682);function s(e,t){(0,n.Z)(2,arguments);var i=(0,a.Z)(e).getTime(),s=(0,r.Z)(t);return new Date(i+s)}},72949:(e,t,i)=>{i.d(t,{Z:()=>n});var r=i(34327),a=i(23682);function n(e){(0,a.Z)(1,arguments);var t=(0,r.Z)(e);return t.setMinutes(0,0,0),t}},79042:(e,t,i)=>{i.a(e,(async e=>{i.r(t);i(51187);var r=i(79021),a=i(72949),n=i(59699),s=i(37500),o=i(33310),l=i(14516),d=i(99137),c=i(94653),h=(i(85066),i(51144)),u=i(11654),m=i(91476),p=i(29152),f=i(89207),v=e([p,m,c]);function y(){y=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var a=t.placement;if(t.kind===r&&("static"===a||"prototype"===a)){var n="static"===a?e:i;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var r=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],r=[],a={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,a)}),this),e.forEach((function(e){if(!k(e))return i.push(e);var t=this.decorateElement(e,a);i.push(t.element),i.push.apply(i,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:i,finishers:r};var n=this.decorateConstructor(i,t);return r.push.apply(r,n.finishers),n.finishers=r,n},addElementPlacement:function(e,t,i){var r=t[e.placement];if(!i&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var i=[],r=[],a=e.decorators,n=a.length-1;n>=0;n--){var s=t[e.placement];s.splice(s.indexOf(e.key),1);var o=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,a[n])(o)||o);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var d=l.extras;if(d){for(var c=0;c<d.length;c++)this.addElementPlacement(d[c],t);i.push.apply(i,d)}}return{element:e,finishers:r,extras:i}},decorateConstructor:function(e,t){for(var i=[],r=t.length-1;r>=0;r--){var a=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[r])(a)||a);if(void 0!==n.finisher&&i.push(n.finisher),void 0!==n.elements){e=n.elements;for(var s=0;s<e.length-1;s++)for(var o=s+1;o<e.length;o++)if(e[s].key===e[o].key&&e[s].placement===e[o].placement)throw new TypeError("Duplicated element ("+e[s].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return $(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?$(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=D(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var a=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:i,placement:r,descriptor:Object.assign({},a)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(a,"get","The property descriptor of a field descriptor"),this.disallowProperty(a,"set","The property descriptor of a field descriptor"),this.disallowProperty(a,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:w(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=w(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var r=(0,t[i])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function _(e){var t,i=D(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function g(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function k(e){return e.decorators&&e.decorators.length}function b(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function w(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function D(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var r=i.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function $(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,r=new Array(t);i<t;i++)r[i]=e[i];return r}[p,m,c]=v.then?await v:v;const E=e=>s.dy`<mwc-list-item>
  <span>${e.name}</span>
</mwc-list-item>`;!function(e,t,i,r){var a=y();if(r)for(var n=0;n<r.length;n++)a=r[n](a);var s=t((function(e){a.initializeInstanceElements(e,o.elements)}),i),o=a.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},r=0;r<e.length;r++){var a,n=e[r];if("method"===n.kind&&(a=t.find(i)))if(b(n.descriptor)||b(a.descriptor)){if(k(n)||k(a))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");a.descriptor=n.descriptor}else{if(k(n)){if(k(a))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");a.decorators=n.decorators}g(n,a)}else t.push(n)}return t}(s.d.map(_)),e);a.initializeClassElements(s.F,o.elements),a.runClassFinishers(s.F,o.finishers)}([(0,o.Mo)("dialog-calendar-event-editor")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_calendars",value:()=>[]},{kind:"field",decorators:[(0,o.SB)()],key:"_calendarId",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_summary",value:()=>""},{kind:"field",decorators:[(0,o.SB)()],key:"_rrule",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_allDay",value:()=>!1},{kind:"field",decorators:[(0,o.SB)()],key:"_dtstart",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_dtend",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_submitting",value:()=>!1},{kind:"method",key:"showDialog",value:function(e){if(this._error=void 0,this._params=e,this._calendars=e.calendars,this._calendarId=e.calendarId||this._calendars[0].entity_id,e.entry){const t=e.entry;this._allDay=(0,d.J)(t.dtstart),this._summary=t.summary,this._rrule=t.rrule,this._allDay?(this._dtstart=new Date(t.dtstart),this._dtend=(0,r.Z)(new Date(t.dtend),-1)):(this._dtstart=new Date(t.dtstart),this._dtend=new Date(t.dtend))}else this._allDay=!1,this._dtstart=(0,a.Z)(new Date),this._dtend=(0,n.Z)(this._dtstart,1)}},{kind:"method",key:"render",value:function(){if(!this._params)return s.dy``;const e=void 0===this._params.entry,{startDate:t,startTime:i,endDate:r,endTime:a}=this._getLocaleStrings(this._dtstart,this._dtend);return s.dy`
      <ha-dialog
        open
        @closed=${this._close}
        scrimClickAction
        escapeKeyAction
        .heading=${s.dy`
          <div class="header_title">
            ${e?this.hass.localize("ui.components.calendar.event.add"):this._summary}
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
                .value=${t}
                .locale=${this.hass.locale}
                @value-changed=${this._startDateChanged}
              ></ha-date-input>
              ${this._allDay?"":s.dy`<ha-time-input
                    .value=${i}
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
                .value=${r}
                .min=${t}
                .locale=${this.hass.locale}
                @value-changed=${this._endDateChanged}
              ></ha-date-input>
              ${this._allDay?"":s.dy`<ha-time-input
                    .value=${a}
                    .locale=${this.hass.locale}
                    @value-changed=${this._endTimeChanged}
                  ></ha-time-input>`}
            </div>
          </div>
          <ha-recurrence-rule-editor
            .locale=${this.hass.locale}
            .value=${this._rrule||""}
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
    `}},{kind:"field",key:"_getLocaleStrings",value(){return(0,l.Z)(((e,t)=>{const i=this.hass.config.time_zone;return{startDate:null==e?void 0:e.toLocaleDateString("en-CA",{timeZone:i}),startTime:null==e?void 0:e.toLocaleTimeString("en-GB",{timeZone:i}),endDate:null==t?void 0:t.toLocaleDateString("en-CA",{timeZone:i}),endTime:null==t?void 0:t.toLocaleTimeString("en-GB",{timeZone:i})}}))}},{kind:"method",key:"_handleSummaryChanged",value:function(e){this._summary=e.target.value}},{kind:"method",key:"_handleRRuleChanged",value:function(e){this._rrule=e.detail.value}},{kind:"method",key:"_allDayToggleChanged",value:function(e){this._allDay=e.target.checked}},{kind:"method",key:"_startDateChanged",value:function(e){this._dtstart=new Date(e.detail.value+"T"+this._dtstart.toISOString().split("T")[1])}},{kind:"method",key:"_endDateChanged",value:function(e){this._dtend=new Date(e.detail.value+"T"+this._dtend.toISOString().split("T")[1])}},{kind:"method",key:"_startTimeChanged",value:function(e){this._dtstart=new Date(this._dtstart.toISOString().split("T")[0]+"T"+e.detail.value)}},{kind:"method",key:"_endTimeChanged",value:function(e){this._dtend=new Date(this._dtend.toISOString().split("T")[0]+"T"+e.detail.value)}},{kind:"method",key:"_calculateData",value:function(){const{startDate:e,startTime:t,endDate:i,endTime:a}=this._getLocaleStrings(this._dtstart,this._dtend),n={summary:this._summary,rrule:this._rrule,dtstart:"",dtend:""};return this._allDay?(n.dtstart=e,n.dtend=(0,r.Z)(new Date(this._dtend),1).toLocaleDateString("en-CA")):(n.dtstart=`${e}T${t}`,n.dtend=`${i}T${a}`),n}},{kind:"method",key:"_handleCalendarChanged",value:function(e){this._calendarId=e.detail.value}},{kind:"method",key:"_createEvent",value:async function(){this._submitting=!0;try{await(0,h.fE)(this.hass,this._calendarId,this._calculateData())}catch(e){this._error=e?e.message:"Unknown error"}finally{this._submitting=!1}await this._params.updated(),this._params=void 0}},{kind:"method",key:"_saveEvent",value:async function(){}},{kind:"method",key:"_deleteEvent",value:async function(){this._submitting=!0;const e=this._params.entry,t=await(0,f.Y)(this,{title:this.hass.localize("ui.components.calendar.event.confirm_delete.delete"),text:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.recurring_prompt"):this.hass.localize("ui.components.calendar.event.confirm_delete.prompt"),confirmText:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.delete_this"):this.hass.localize("ui.components.calendar.event.confirm_delete.delete"),confirmFutureText:e.recurrence_id?this.hass.localize("ui.components.calendar.event.confirm_delete.delete_future"):void 0});if(void 0!==t){try{await(0,h.d1)(this.hass,this._calendarId,e.uid,e.recurrence_id||"",t)}catch(e){return void(this._error=e?e.message:"Unknown error")}finally{this._submitting=!1}await this._params.updated(),this._close()}else this._submitting=!1}},{kind:"method",key:"_close",value:function(){this._calendars=[],this._calendarId=void 0,this._params=void 0,this._dtstart=void 0,this._dtend=void 0,this._summary="",this._rrule=void 0}},{kind:"get",static:!0,key:"styles",value:function(){return[u.yu,s.iv`
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
//# sourceMappingURL=1d85382c.js.map