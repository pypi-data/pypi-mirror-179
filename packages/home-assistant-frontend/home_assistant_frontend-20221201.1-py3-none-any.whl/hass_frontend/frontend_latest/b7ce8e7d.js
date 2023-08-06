"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[3143],{87789:(e,t,r)=>{r.d(t,{G:()=>l,H:()=>c});var a=r(24833);const i=new Set(["battery","carbon_monoxide","gas","heat","moisture","problem","safety","smoke","tamper"]),n=e=>{if("battery"===(null==e?void 0:e.attributes.device_class))return(e=>{const t=Number(e.state);return isNaN(t)?"sensor-battery-unknown":t>=70?"sensor-battery-high":t>=30?"sensor-battery-medium":"sensor-battery-low"})(e)};var o=r(58831),s=r(39197);const c=(e,t)=>{if(!e||!(0,s.v)(e,t))return"var(--rgb-disabled-color)";const r=l(e,t);return r?`var(--rgb-state-${r}-color)`:"var(--rgb-state-default-color)"},l=(e,t)=>{const r=void 0!==t?t:null==e?void 0:e.state;switch((0,o.M)(e.entity_id)){case"alarm_control_panel":return(e=>{switch(e){case"armed_away":case"armed_vacation":case"armed_home":case"armed_night":case"armed_custom_bypass":return"alarm-armed";case"pending":return"alarm-pending";case"arming":case"disarming":return"alarm-arming";case"triggered":return"alarm-triggered";default:return}})(r);case"binary_sensor":return(e=>{const t=null==e?void 0:e.attributes.device_class;return t&&i.has(t)?"binary-sensor-alerting":"binary-sensor"})(e);case"cover":return"cover";case"climate":return(e=>{switch(e){case"auto":return"climate-auto";case"cool":return"climate-cool";case"dry":return"climate-dry";case"fan_only":return"climate-fan-only";case"heat":return"climate-heat";case"heat_cool":return"climate-heat-cool";default:return}})(r);case"fan":return"fan";case"lock":return(e=>{switch(e){case"locked":return"lock-locked";case"jammed":return"lock-jammed";case"locking":case"unlocking":return"lock-pending";default:return}})(r);case"light":return"light";case"humidifier":return"humidifier";case"media_player":return"media-player";case"sensor":return n(e);case"vacuum":return"vacuum";case"siren":return"siren";case"sun":return"above_horizon"===r?"sun-day":"sun-night";case"switch":return"switch";case"update":return(0,a.Sk)(e)?"update-installing":"update"}}},52797:(e,t,r)=>{r.d(t,{N:()=>a});const a=r(37500).iv`
  ha-state-icon[data-active][data-domain="alert"],
  ha-state-icon[data-active][data-domain="automation"],
  ha-state-icon[data-active][data-domain="binary_sensor"],
  ha-state-icon[data-active][data-domain="calendar"],
  ha-state-icon[data-active][data-domain="camera"],
  ha-state-icon[data-active][data-domain="cover"],
  ha-state-icon[data-active][data-domain="device_tracker"],
  ha-state-icon[data-active][data-domain="fan"],
  ha-state-icon[data-active][data-domain="humidifier"],
  ha-state-icon[data-active][data-domain="light"],
  ha-state-icon[data-active][data-domain="input_boolean"],
  ha-state-icon[data-active][data-domain="lock"],
  ha-state-icon[data-active][data-domain="media_player"],
  ha-state-icon[data-active][data-domain="remote"],
  ha-state-icon[data-active][data-domain="script"],
  ha-state-icon[data-active][data-domain="sun"],
  ha-state-icon[data-active][data-domain="switch"],
  ha-state-icon[data-active][data-domain="timer"],
  ha-state-icon[data-active][data-domain="vacuum"],
  ha-state-icon[data-active][data-domain="group"] {
    color: var(--paper-item-icon-active-color, #fdd835);
  }

  ha-state-icon[data-active][data-domain="alarm_control_panel"][data-state="pending"],
  ha-state-icon[data-active][data-domain="alarm_control_panel"][data-state="arming"],
  ha-state-icon[data-active][data-domain="alarm_control_panel"][data-state="triggered"] {
    animation: pulse 1s infinite;
  }

  @keyframes pulse {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  /* Color the icon if unavailable */
  ha-state-icon[data-state="unavailable"] {
    color: var(--state-unavailable-color);
  }
`},43426:(e,t,r)=>{r.d(t,{U:()=>a});const a=async(e,t,r,a,i,...n)=>{let o=a[e];o||(o=a[e]={});const s=o[i];if(s)return s;const c=r(a,i,...n);return o[i]=c,c.then((()=>setTimeout((()=>{o[i]=void 0}),t)),(()=>{o[i]=void 0})),c}},3143:(e,t,r)=>{var a=r(37500),i=r(33310),n=r(51346),o=r(70483),s=r(58831),c=r(22311),l=r(39197),d=r(87789),u=r(52797),h=r(89439);r(87037);function f(){f=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(a){t.forEach((function(t){var i=t.placement;if(t.kind===a&&("static"===i||"prototype"===i)){var n="static"===i?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var a=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===a?void 0:a.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],a=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!v(e))return r.push(e);var t=this.decorateElement(e,i);r.push(t.element),r.push.apply(r,t.extras),a.push.apply(a,t.finishers)}),this),!t)return{elements:r,finishers:a};var n=this.decorateConstructor(r,t);return a.push.apply(a,n.finishers),n.finishers=a,n},addElementPlacement:function(e,t,r){var a=t[e.placement];if(!r&&-1!==a.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");a.push(e.key)},decorateElement:function(e,t){for(var r=[],a=[],i=e.decorators,n=i.length-1;n>=0;n--){var o=t[e.placement];o.splice(o.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,i[n])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&a.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:a,extras:r}},decorateConstructor:function(e,t){for(var r=[],a=t.length-1;a>=0;a--){var i=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[a])(i)||i);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var o=0;o<e.length-1;o++)for(var s=o+1;s<e.length;s++)if(e[o].key===e[s].key&&e[o].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[o].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return k(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?k(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=g(e.key),a=String(e.placement);if("static"!==a&&"prototype"!==a&&"own"!==a)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+a+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:a,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:b(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=b(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var a=(0,t[r])(e);if(void 0!==a){if("function"!=typeof a)throw new TypeError("Finishers must return a constructor.");e=a}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function p(e){var t,r=g(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var a={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(a.decorators=e.decorators),"field"===e.kind&&(a.initializer=e.value),a}function m(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function v(e){return e.decorators&&e.decorators.length}function y(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function b(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function g(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!=typeof a)return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}function w(){return w="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var a=_(e,t);if(a){var i=Object.getOwnPropertyDescriptor(a,t);return i.get?i.get.call(arguments.length<3?e:r):i.value}},w.apply(this,arguments)}function _(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=E(e)););return e}function E(e){return E=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},E(e)}let C=function(e,t,r,a){var i=f();if(a)for(var n=0;n<a.length;n++)i=a[n](i);var o=t((function(e){i.initializeInstanceElements(e,s.elements)}),r),s=i.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},a=0;a<e.length;a++){var i,n=e[a];if("method"===n.kind&&(i=t.find(r)))if(y(n.descriptor)||y(i.descriptor)){if(v(n)||v(i))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");i.descriptor=n.descriptor}else{if(v(n)){if(v(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");i.decorators=n.decorators}m(n,i)}else t.push(n)}return t}(o.d.map(p)),e);return i.initializeClassElements(o.F,s.elements),i.runClassFinishers(o.F,s.finishers)}(null,(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"stateObj",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"overrideIcon",value:void 0},{kind:"field",decorators:[(0,i.Cb)()],key:"overrideImage",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean})],key:"stateColor",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,reflect:!0,attribute:"icon"})],key:"_showIcon",value:()=>!0},{kind:"field",decorators:[(0,i.SB)()],key:"_iconStyle",value:()=>({})},{kind:"get",key:"_stateColor",value:function(){const e=this.stateObj?(0,c.N)(this.stateObj):void 0;return this.stateColor||"light"===e&&!1!==this.stateColor}},{kind:"method",key:"render",value:function(){const e=this.stateObj;if(!e&&!this.overrideIcon&&!this.overrideImage)return a.dy`<div class="missing">
        <ha-svg-icon .path=${"M13 14H11V9H13M13 18H11V16H13M1 21H23L12 2L1 21Z"}></ha-svg-icon>
      </div>`;if(!this._showIcon)return a.dy``;const t=e?(0,c.N)(e):void 0,r=!(!this._stateColor||!e)&&(0,l.v)(e);return a.dy`<ha-state-icon
      style=${(0,o.V)(this._iconStyle)}
      ?data-active=${r}
      data-domain=${(0,n.o)(t)}
      data-state=${(0,n.o)(null==e?void 0:e.state)}
      .icon=${this.overrideIcon}
      .state=${e}
    ></ha-state-icon>`}},{kind:"method",key:"willUpdate",value:function(e){if(w(E(r.prototype),"willUpdate",this).call(this,e),!(e.has("stateObj")||e.has("overrideImage")||e.has("overrideIcon")||e.has("stateColor")))return;const t=this.stateObj,a={},i={backgroundImage:""};if(this._showIcon=!0,t&&void 0===this.overrideImage)if(!t.attributes.entity_picture_local&&!t.attributes.entity_picture||this.overrideIcon){if((0,l.v)(t)&&this._stateColor){const e=(0,d.G)(t);if(t.attributes.rgb_color?a.color=`rgb(${t.attributes.rgb_color.join(",")})`:e&&(a.color=`rgb(var(--rgb-state-${e}-color))`),t.attributes.brightness){const e=t.attributes.brightness;if("number"!=typeof e){const r=`Type error: state-badge expected number, but type of ${t.entity_id}.attributes.brightness is ${typeof e} (${e})`;console.warn(r)}a.filter=`brightness(${(e+245)/5}%)`}}}else{let e=t.attributes.entity_picture_local||t.attributes.entity_picture;this.hass&&(e=this.hass.hassUrl(e)),"camera"===(0,s.M)(t.entity_id)&&(e=(0,h.Ch)(e,80,80)),i.backgroundImage=`url(${e})`,this._showIcon=!1}else if(this.overrideImage){let e=this.overrideImage;this.hass&&(e=this.hass.hassUrl(e)),i.backgroundImage=`url(${e})`,this._showIcon=!1}this._iconStyle=a,Object.assign(this.style,i)}},{kind:"get",static:!0,key:"styles",value:function(){return[u.N,a.iv`
        :host {
          position: relative;
          display: inline-block;
          width: 40px;
          color: var(--paper-item-icon-color, #44739e);
          border-radius: 50%;
          height: 40px;
          text-align: center;
          background-size: cover;
          line-height: 40px;
          vertical-align: middle;
          box-sizing: border-box;
        }
        :host(:focus) {
          outline: none;
        }
        :host(:not([icon]):focus) {
          border: 2px solid var(--divider-color);
        }
        :host([icon]:focus) {
          background: var(--divider-color);
        }
        ha-state-icon {
          transition: color 0.3s ease-in-out, filter 0.3s ease-in-out;
        }
        .missing {
          color: #fce588;
        }
      `]}}]}}),a.oi);customElements.define("state-badge",C)},89439:(e,t,r)=>{if(r.d(t,{sF:()=>n,qW:()=>o,kU:()=>s,jU:()=>c,Ch:()=>l,nk:()=>d,i4:()=>u,Lr:()=>f,tb:()=>p,Xn:()=>m,Mw:()=>v,B:()=>b,zj:()=>g}),98818!=r.j)var a=r(43426);var i=r(22814);const n=98818!=r.j?[1,2,3,4,6,8]:null,o=2,s="hls",c="web_rtc",l=(e,t,r)=>`${e}&width=${t}&height=${r}`,d=e=>`/api/camera_proxy_stream/${e.entity_id}?token=${e.attributes.access_token}`,u=async(e,t,r,i)=>{const n=await(0,a.U)("_cameraTmbUrl",9e3,h,e,t);return l(n,r,i)},h=async(e,t)=>{const r=await(0,i.iI)(e,`/api/camera_proxy/${t}`);return e.hassUrl(r.path)},f=async(e,t,r)=>{const a={type:"camera/stream",entity_id:t};r&&(a.format=r);const i=await e.callWS(a);return i.url=e.hassUrl(i.url),i},p=(e,t,r)=>e.callWS({type:"camera/web_rtc_offer",entity_id:t,offer:r}),m=(e,t)=>e.callWS({type:"camera/get_prefs",entity_id:t}),v=(e,t,r)=>e.callWS({type:"camera/update_prefs",entity_id:t,...r}),y="media-source://camera/",b=e=>e.startsWith(y),g=e=>e.substring(y.length)}}]);
//# sourceMappingURL=b7ce8e7d.js.map