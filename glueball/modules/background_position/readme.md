# module: Background position

Sets the background position of images.
A static declaration of "no-repeat" is implicitly included.






## Static declarations
A static declaration is not altered by the provided values.


+ `background-repeat: no-repeat;`




## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.bgp` |`background-position`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Positions

Selector  | Value
--------- | ---------
`lt` | `left top`
`lc` | `left center`
`lb` | `left bottom`
`rt` | `right top`
`rc` | `right center`
`rb` | `right bottom`
`ct` | `center top`
`cc` | `center center`
`cb` | `center bottom`





## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|






## CSS rules
```css

.bgp-lt { background-position: left top; background-repeat: no-repeat; }
.bgp-lc { background-position: left center; background-repeat: no-repeat; }
.bgp-lb { background-position: left bottom; background-repeat: no-repeat; }
.bgp-rt { background-position: right top; background-repeat: no-repeat; }
.bgp-rc { background-position: right center; background-repeat: no-repeat; }
.bgp-rb { background-position: right bottom; background-repeat: no-repeat; }
.bgp-ct { background-position: center top; background-repeat: no-repeat; }
.bgp-cc { background-position: center center; background-repeat: no-repeat; }
.bgp-cb { background-position: center bottom; background-repeat: no-repeat; }


@media (min-width: 36em) {
.s_bgp-lt { background-position: left top; background-repeat: no-repeat; }
.s_bgp-lc { background-position: left center; background-repeat: no-repeat; }
.s_bgp-lb { background-position: left bottom; background-repeat: no-repeat; }
.s_bgp-rt { background-position: right top; background-repeat: no-repeat; }
.s_bgp-rc { background-position: right center; background-repeat: no-repeat; }
.s_bgp-rb { background-position: right bottom; background-repeat: no-repeat; }
.s_bgp-ct { background-position: center top; background-repeat: no-repeat; }
.s_bgp-cc { background-position: center center; background-repeat: no-repeat; }
.s_bgp-cb { background-position: center bottom; background-repeat: no-repeat; }
}


@media (min-width: 48em) {
.m_bgp-lt { background-position: left top; background-repeat: no-repeat; }
.m_bgp-lc { background-position: left center; background-repeat: no-repeat; }
.m_bgp-lb { background-position: left bottom; background-repeat: no-repeat; }
.m_bgp-rt { background-position: right top; background-repeat: no-repeat; }
.m_bgp-rc { background-position: right center; background-repeat: no-repeat; }
.m_bgp-rb { background-position: right bottom; background-repeat: no-repeat; }
.m_bgp-ct { background-position: center top; background-repeat: no-repeat; }
.m_bgp-cc { background-position: center center; background-repeat: no-repeat; }
.m_bgp-cb { background-position: center bottom; background-repeat: no-repeat; }
}


@media (min-width: 62em) {
.l_bgp-lt { background-position: left top; background-repeat: no-repeat; }
.l_bgp-lc { background-position: left center; background-repeat: no-repeat; }
.l_bgp-lb { background-position: left bottom; background-repeat: no-repeat; }
.l_bgp-rt { background-position: right top; background-repeat: no-repeat; }
.l_bgp-rc { background-position: right center; background-repeat: no-repeat; }
.l_bgp-rb { background-position: right bottom; background-repeat: no-repeat; }
.l_bgp-ct { background-position: center top; background-repeat: no-repeat; }
.l_bgp-cc { background-position: center center; background-repeat: no-repeat; }
.l_bgp-cb { background-position: center bottom; background-repeat: no-repeat; }
}


@media (min-width: 75em) {
.x_bgp-lt { background-position: left top; background-repeat: no-repeat; }
.x_bgp-lc { background-position: left center; background-repeat: no-repeat; }
.x_bgp-lb { background-position: left bottom; background-repeat: no-repeat; }
.x_bgp-rt { background-position: right top; background-repeat: no-repeat; }
.x_bgp-rc { background-position: right center; background-repeat: no-repeat; }
.x_bgp-rb { background-position: right bottom; background-repeat: no-repeat; }
.x_bgp-ct { background-position: center top; background-repeat: no-repeat; }
.x_bgp-cc { background-position: center center; background-repeat: no-repeat; }
.x_bgp-cb { background-position: center bottom; background-repeat: no-repeat; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -