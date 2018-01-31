# module Coordinates

Top, right, bottom and left offsets.








## Dynamic properties
The value of a dynamic property is determined by the provided values.


+ base selector: `.top` - properties: `top`

+ base selector: `.right` - properties: `right`

+ base selector: `.bottom` - properties: `bottom`

+ base selector: `.left` - properties: `left`





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Offsets

Selector  | Value
--------- | ---------
`-2` | `-2rem`
`-1` | `-1rem`
`0` | `0`
`1` | `1rem`
`2` | `2rem`





## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|




## Pseudo selectors
The following pseudo selectors are available:

### hover
The pseudo selector `hover` has the following media queries available:




| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `s`  ||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `m`  |||▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|
|  `l`  ||||▒▒▒▒▒|▒▒▒▒▒|
|  `x`  |||||▒▒▒▒▒|
|  `tl`  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒||
|  `tm`  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|||
|  `ts`  |▒▒▒▒▒|▒▒▒▒▒||||
|  `tt`  |▒▒▒▒▒|||||





## CSS rules
```css

.top-2 { top: -2rem; }
.top-1 { top: -1rem; }
.top0 { top: 0; }
.top1 { top: 1rem; }
.top2 { top: 2rem; }
.right-2 { right: -2rem; }
.right-1 { right: -1rem; }
.right0 { right: 0; }
.right1 { right: 1rem; }
.right2 { right: 2rem; }
.bottom-2 { bottom: -2rem; }
.bottom-1 { bottom: -1rem; }
.bottom0 { bottom: 0; }
.bottom1 { bottom: 1rem; }
.bottom2 { bottom: 2rem; }
.left-2 { left: -2rem; }
.left-1 { left: -1rem; }
.left0 { left: 0; }
.left1 { left: 1rem; }
.left2 { left: 2rem; }


@media (min-width: 36em) {
.s_top-2 { top: -2rem; }
.s_top-1 { top: -1rem; }
.s_top0 { top: 0; }
.s_top1 { top: 1rem; }
.s_top2 { top: 2rem; }
.s_right-2 { right: -2rem; }
.s_right-1 { right: -1rem; }
.s_right0 { right: 0; }
.s_right1 { right: 1rem; }
.s_right2 { right: 2rem; }
.s_bottom-2 { bottom: -2rem; }
.s_bottom-1 { bottom: -1rem; }
.s_bottom0 { bottom: 0; }
.s_bottom1 { bottom: 1rem; }
.s_bottom2 { bottom: 2rem; }
.s_left-2 { left: -2rem; }
.s_left-1 { left: -1rem; }
.s_left0 { left: 0; }
.s_left1 { left: 1rem; }
.s_left2 { left: 2rem; }
}


@media (min-width: 48em) {
.m_top-2 { top: -2rem; }
.m_top-1 { top: -1rem; }
.m_top0 { top: 0; }
.m_top1 { top: 1rem; }
.m_top2 { top: 2rem; }
.m_right-2 { right: -2rem; }
.m_right-1 { right: -1rem; }
.m_right0 { right: 0; }
.m_right1 { right: 1rem; }
.m_right2 { right: 2rem; }
.m_bottom-2 { bottom: -2rem; }
.m_bottom-1 { bottom: -1rem; }
.m_bottom0 { bottom: 0; }
.m_bottom1 { bottom: 1rem; }
.m_bottom2 { bottom: 2rem; }
.m_left-2 { left: -2rem; }
.m_left-1 { left: -1rem; }
.m_left0 { left: 0; }
.m_left1 { left: 1rem; }
.m_left2 { left: 2rem; }
}


@media (min-width: 62em) {
.l_top-2 { top: -2rem; }
.l_top-1 { top: -1rem; }
.l_top0 { top: 0; }
.l_top1 { top: 1rem; }
.l_top2 { top: 2rem; }
.l_right-2 { right: -2rem; }
.l_right-1 { right: -1rem; }
.l_right0 { right: 0; }
.l_right1 { right: 1rem; }
.l_right2 { right: 2rem; }
.l_bottom-2 { bottom: -2rem; }
.l_bottom-1 { bottom: -1rem; }
.l_bottom0 { bottom: 0; }
.l_bottom1 { bottom: 1rem; }
.l_bottom2 { bottom: 2rem; }
.l_left-2 { left: -2rem; }
.l_left-1 { left: -1rem; }
.l_left0 { left: 0; }
.l_left1 { left: 1rem; }
.l_left2 { left: 2rem; }
}


@media (min-width: 75em) {
.x_top-2 { top: -2rem; }
.x_top-1 { top: -1rem; }
.x_top0 { top: 0; }
.x_top1 { top: 1rem; }
.x_top2 { top: 2rem; }
.x_right-2 { right: -2rem; }
.x_right-1 { right: -1rem; }
.x_right0 { right: 0; }
.x_right1 { right: 1rem; }
.x_right2 { right: 2rem; }
.x_bottom-2 { bottom: -2rem; }
.x_bottom-1 { bottom: -1rem; }
.x_bottom0 { bottom: 0; }
.x_bottom1 { bottom: 1rem; }
.x_bottom2 { bottom: 2rem; }
.x_left-2 { left: -2rem; }
.x_left-1 { left: -1rem; }
.x_left0 { left: 0; }
.x_left1 { left: 1rem; }
.x_left2 { left: 2rem; }
}

.hover_top-2:hover { top: -2rem; }
.hover_top-1:hover { top: -1rem; }
.hover_top0:hover { top: 0; }
.hover_top1:hover { top: 1rem; }
.hover_top2:hover { top: 2rem; }
.hover_right-2:hover { right: -2rem; }
.hover_right-1:hover { right: -1rem; }
.hover_right0:hover { right: 0; }
.hover_right1:hover { right: 1rem; }
.hover_right2:hover { right: 2rem; }
.hover_bottom-2:hover { bottom: -2rem; }
.hover_bottom-1:hover { bottom: -1rem; }
.hover_bottom0:hover { bottom: 0; }
.hover_bottom1:hover { bottom: 1rem; }
.hover_bottom2:hover { bottom: 2rem; }
.hover_left-2:hover { left: -2rem; }
.hover_left-1:hover { left: -1rem; }
.hover_left0:hover { left: 0; }
.hover_left1:hover { left: 1rem; }
.hover_left2:hover { left: 2rem; }


@media (min-width: 36em) {
.s_hover_top-2:hover { top: -2rem; }
.s_hover_top-1:hover { top: -1rem; }
.s_hover_top0:hover { top: 0; }
.s_hover_top1:hover { top: 1rem; }
.s_hover_top2:hover { top: 2rem; }
.s_hover_right-2:hover { right: -2rem; }
.s_hover_right-1:hover { right: -1rem; }
.s_hover_right0:hover { right: 0; }
.s_hover_right1:hover { right: 1rem; }
.s_hover_right2:hover { right: 2rem; }
.s_hover_bottom-2:hover { bottom: -2rem; }
.s_hover_bottom-1:hover { bottom: -1rem; }
.s_hover_bottom0:hover { bottom: 0; }
.s_hover_bottom1:hover { bottom: 1rem; }
.s_hover_bottom2:hover { bottom: 2rem; }
.s_hover_left-2:hover { left: -2rem; }
.s_hover_left-1:hover { left: -1rem; }
.s_hover_left0:hover { left: 0; }
.s_hover_left1:hover { left: 1rem; }
.s_hover_left2:hover { left: 2rem; }
}


@media (min-width: 48em) {
.m_hover_top-2:hover { top: -2rem; }
.m_hover_top-1:hover { top: -1rem; }
.m_hover_top0:hover { top: 0; }
.m_hover_top1:hover { top: 1rem; }
.m_hover_top2:hover { top: 2rem; }
.m_hover_right-2:hover { right: -2rem; }
.m_hover_right-1:hover { right: -1rem; }
.m_hover_right0:hover { right: 0; }
.m_hover_right1:hover { right: 1rem; }
.m_hover_right2:hover { right: 2rem; }
.m_hover_bottom-2:hover { bottom: -2rem; }
.m_hover_bottom-1:hover { bottom: -1rem; }
.m_hover_bottom0:hover { bottom: 0; }
.m_hover_bottom1:hover { bottom: 1rem; }
.m_hover_bottom2:hover { bottom: 2rem; }
.m_hover_left-2:hover { left: -2rem; }
.m_hover_left-1:hover { left: -1rem; }
.m_hover_left0:hover { left: 0; }
.m_hover_left1:hover { left: 1rem; }
.m_hover_left2:hover { left: 2rem; }
}


@media (min-width: 62em) {
.l_hover_top-2:hover { top: -2rem; }
.l_hover_top-1:hover { top: -1rem; }
.l_hover_top0:hover { top: 0; }
.l_hover_top1:hover { top: 1rem; }
.l_hover_top2:hover { top: 2rem; }
.l_hover_right-2:hover { right: -2rem; }
.l_hover_right-1:hover { right: -1rem; }
.l_hover_right0:hover { right: 0; }
.l_hover_right1:hover { right: 1rem; }
.l_hover_right2:hover { right: 2rem; }
.l_hover_bottom-2:hover { bottom: -2rem; }
.l_hover_bottom-1:hover { bottom: -1rem; }
.l_hover_bottom0:hover { bottom: 0; }
.l_hover_bottom1:hover { bottom: 1rem; }
.l_hover_bottom2:hover { bottom: 2rem; }
.l_hover_left-2:hover { left: -2rem; }
.l_hover_left-1:hover { left: -1rem; }
.l_hover_left0:hover { left: 0; }
.l_hover_left1:hover { left: 1rem; }
.l_hover_left2:hover { left: 2rem; }
}


@media (min-width: 75em) {
.x_hover_top-2:hover { top: -2rem; }
.x_hover_top-1:hover { top: -1rem; }
.x_hover_top0:hover { top: 0; }
.x_hover_top1:hover { top: 1rem; }
.x_hover_top2:hover { top: 2rem; }
.x_hover_right-2:hover { right: -2rem; }
.x_hover_right-1:hover { right: -1rem; }
.x_hover_right0:hover { right: 0; }
.x_hover_right1:hover { right: 1rem; }
.x_hover_right2:hover { right: 2rem; }
.x_hover_bottom-2:hover { bottom: -2rem; }
.x_hover_bottom-1:hover { bottom: -1rem; }
.x_hover_bottom0:hover { bottom: 0; }
.x_hover_bottom1:hover { bottom: 1rem; }
.x_hover_bottom2:hover { bottom: 2rem; }
.x_hover_left-2:hover { left: -2rem; }
.x_hover_left-1:hover { left: -1rem; }
.x_hover_left0:hover { left: 0; }
.x_hover_left1:hover { left: 1rem; }
.x_hover_left2:hover { left: 2rem; }
}


@media (max-width: 74.99em) {
.tl_hover_top-2:hover { top: -2rem; }
.tl_hover_top-1:hover { top: -1rem; }
.tl_hover_top0:hover { top: 0; }
.tl_hover_top1:hover { top: 1rem; }
.tl_hover_top2:hover { top: 2rem; }
.tl_hover_right-2:hover { right: -2rem; }
.tl_hover_right-1:hover { right: -1rem; }
.tl_hover_right0:hover { right: 0; }
.tl_hover_right1:hover { right: 1rem; }
.tl_hover_right2:hover { right: 2rem; }
.tl_hover_bottom-2:hover { bottom: -2rem; }
.tl_hover_bottom-1:hover { bottom: -1rem; }
.tl_hover_bottom0:hover { bottom: 0; }
.tl_hover_bottom1:hover { bottom: 1rem; }
.tl_hover_bottom2:hover { bottom: 2rem; }
.tl_hover_left-2:hover { left: -2rem; }
.tl_hover_left-1:hover { left: -1rem; }
.tl_hover_left0:hover { left: 0; }
.tl_hover_left1:hover { left: 1rem; }
.tl_hover_left2:hover { left: 2rem; }
}


@media (max-width: 61.99em) {
.tm_hover_top-2:hover { top: -2rem; }
.tm_hover_top-1:hover { top: -1rem; }
.tm_hover_top0:hover { top: 0; }
.tm_hover_top1:hover { top: 1rem; }
.tm_hover_top2:hover { top: 2rem; }
.tm_hover_right-2:hover { right: -2rem; }
.tm_hover_right-1:hover { right: -1rem; }
.tm_hover_right0:hover { right: 0; }
.tm_hover_right1:hover { right: 1rem; }
.tm_hover_right2:hover { right: 2rem; }
.tm_hover_bottom-2:hover { bottom: -2rem; }
.tm_hover_bottom-1:hover { bottom: -1rem; }
.tm_hover_bottom0:hover { bottom: 0; }
.tm_hover_bottom1:hover { bottom: 1rem; }
.tm_hover_bottom2:hover { bottom: 2rem; }
.tm_hover_left-2:hover { left: -2rem; }
.tm_hover_left-1:hover { left: -1rem; }
.tm_hover_left0:hover { left: 0; }
.tm_hover_left1:hover { left: 1rem; }
.tm_hover_left2:hover { left: 2rem; }
}


@media (max-width: 47.99em) {
.ts_hover_top-2:hover { top: -2rem; }
.ts_hover_top-1:hover { top: -1rem; }
.ts_hover_top0:hover { top: 0; }
.ts_hover_top1:hover { top: 1rem; }
.ts_hover_top2:hover { top: 2rem; }
.ts_hover_right-2:hover { right: -2rem; }
.ts_hover_right-1:hover { right: -1rem; }
.ts_hover_right0:hover { right: 0; }
.ts_hover_right1:hover { right: 1rem; }
.ts_hover_right2:hover { right: 2rem; }
.ts_hover_bottom-2:hover { bottom: -2rem; }
.ts_hover_bottom-1:hover { bottom: -1rem; }
.ts_hover_bottom0:hover { bottom: 0; }
.ts_hover_bottom1:hover { bottom: 1rem; }
.ts_hover_bottom2:hover { bottom: 2rem; }
.ts_hover_left-2:hover { left: -2rem; }
.ts_hover_left-1:hover { left: -1rem; }
.ts_hover_left0:hover { left: 0; }
.ts_hover_left1:hover { left: 1rem; }
.ts_hover_left2:hover { left: 2rem; }
}


@media (max-width: 35.99em) {
.tt_hover_top-2:hover { top: -2rem; }
.tt_hover_top-1:hover { top: -1rem; }
.tt_hover_top0:hover { top: 0; }
.tt_hover_top1:hover { top: 1rem; }
.tt_hover_top2:hover { top: 2rem; }
.tt_hover_right-2:hover { right: -2rem; }
.tt_hover_right-1:hover { right: -1rem; }
.tt_hover_right0:hover { right: 0; }
.tt_hover_right1:hover { right: 1rem; }
.tt_hover_right2:hover { right: 2rem; }
.tt_hover_bottom-2:hover { bottom: -2rem; }
.tt_hover_bottom-1:hover { bottom: -1rem; }
.tt_hover_bottom0:hover { bottom: 0; }
.tt_hover_bottom1:hover { bottom: 1rem; }
.tt_hover_bottom2:hover { bottom: 2rem; }
.tt_hover_left-2:hover { left: -2rem; }
.tt_hover_left-1:hover { left: -1rem; }
.tt_hover_left0:hover { left: 0; }
.tt_hover_left1:hover { left: 1rem; }
.tt_hover_left2:hover { left: 2rem; }
}

```

- - - - -
- - - - -
>This documentation was auto-generated from the source files.
