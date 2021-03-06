# module: Padding

Various padding properties:

* padding top, right, bottom and left
* padding (shorthand for all margins)
* padding horizontal and vertical (x & y)








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.p` |`padding`|
| `.pt` |`padding-top`|
| `.pr` |`padding-right`|
| `.pb` |`padding-bottom`|
| `.pl` |`padding-left`|
| `.px` |`padding-left`, |`padding-right`|
| `.py` |`padding-top`, |`padding-bottom`|





## Provided values
The following values determine the dynamic properties and selectors.

Suffix  | Value
--------- | ---------
`0` | `0`
`1` | `0.0625rem`
`2` | `0.125rem`
`3` | `0.25rem`
`4` | `0.5rem`
`5` | `1rem`
`6` | `2rem`
`7` | `4rem`
`8` | `8rem`
`9` | `999rem`




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

.p0 { padding: 0; }
.p1 { padding: 0.0625rem; }
.p2 { padding: 0.125rem; }
.p3 { padding: 0.25rem; }
.p4 { padding: 0.5rem; }
.p5 { padding: 1rem; }
.p6 { padding: 2rem; }
.p7 { padding: 4rem; }
.p8 { padding: 8rem; }
.p9 { padding: 999rem; }
.pt0 { padding-top: 0; }
.pt1 { padding-top: 0.0625rem; }
.pt2 { padding-top: 0.125rem; }
.pt3 { padding-top: 0.25rem; }
.pt4 { padding-top: 0.5rem; }
.pt5 { padding-top: 1rem; }
.pt6 { padding-top: 2rem; }
.pt7 { padding-top: 4rem; }
.pt8 { padding-top: 8rem; }
.pt9 { padding-top: 999rem; }
.pr0 { padding-right: 0; }
.pr1 { padding-right: 0.0625rem; }
.pr2 { padding-right: 0.125rem; }
.pr3 { padding-right: 0.25rem; }
.pr4 { padding-right: 0.5rem; }
.pr5 { padding-right: 1rem; }
.pr6 { padding-right: 2rem; }
.pr7 { padding-right: 4rem; }
.pr8 { padding-right: 8rem; }
.pr9 { padding-right: 999rem; }
.pb0 { padding-bottom: 0; }
.pb1 { padding-bottom: 0.0625rem; }
.pb2 { padding-bottom: 0.125rem; }
.pb3 { padding-bottom: 0.25rem; }
.pb4 { padding-bottom: 0.5rem; }
.pb5 { padding-bottom: 1rem; }
.pb6 { padding-bottom: 2rem; }
.pb7 { padding-bottom: 4rem; }
.pb8 { padding-bottom: 8rem; }
.pb9 { padding-bottom: 999rem; }
.pl0 { padding-left: 0; }
.pl1 { padding-left: 0.0625rem; }
.pl2 { padding-left: 0.125rem; }
.pl3 { padding-left: 0.25rem; }
.pl4 { padding-left: 0.5rem; }
.pl5 { padding-left: 1rem; }
.pl6 { padding-left: 2rem; }
.pl7 { padding-left: 4rem; }
.pl8 { padding-left: 8rem; }
.pl9 { padding-left: 999rem; }
.px0 { padding-left: 0; padding-right: 0; }
.px1 { padding-left: 0.0625rem; padding-right: 0.0625rem; }
.px2 { padding-left: 0.125rem; padding-right: 0.125rem; }
.px3 { padding-left: 0.25rem; padding-right: 0.25rem; }
.px4 { padding-left: 0.5rem; padding-right: 0.5rem; }
.px5 { padding-left: 1rem; padding-right: 1rem; }
.px6 { padding-left: 2rem; padding-right: 2rem; }
.px7 { padding-left: 4rem; padding-right: 4rem; }
.px8 { padding-left: 8rem; padding-right: 8rem; }
.px9 { padding-left: 999rem; padding-right: 999rem; }
.py0 { padding-top: 0; padding-bottom: 0; }
.py1 { padding-top: 0.0625rem; padding-bottom: 0.0625rem; }
.py2 { padding-top: 0.125rem; padding-bottom: 0.125rem; }
.py3 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
.py4 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.py5 { padding-top: 1rem; padding-bottom: 1rem; }
.py6 { padding-top: 2rem; padding-bottom: 2rem; }
.py7 { padding-top: 4rem; padding-bottom: 4rem; }
.py8 { padding-top: 8rem; padding-bottom: 8rem; }
.py9 { padding-top: 999rem; padding-bottom: 999rem; }


@media (min-width: 36em) {
.s_p0 { padding: 0; }
.s_p1 { padding: 0.0625rem; }
.s_p2 { padding: 0.125rem; }
.s_p3 { padding: 0.25rem; }
.s_p4 { padding: 0.5rem; }
.s_p5 { padding: 1rem; }
.s_p6 { padding: 2rem; }
.s_p7 { padding: 4rem; }
.s_p8 { padding: 8rem; }
.s_p9 { padding: 999rem; }
.s_pt0 { padding-top: 0; }
.s_pt1 { padding-top: 0.0625rem; }
.s_pt2 { padding-top: 0.125rem; }
.s_pt3 { padding-top: 0.25rem; }
.s_pt4 { padding-top: 0.5rem; }
.s_pt5 { padding-top: 1rem; }
.s_pt6 { padding-top: 2rem; }
.s_pt7 { padding-top: 4rem; }
.s_pt8 { padding-top: 8rem; }
.s_pt9 { padding-top: 999rem; }
.s_pr0 { padding-right: 0; }
.s_pr1 { padding-right: 0.0625rem; }
.s_pr2 { padding-right: 0.125rem; }
.s_pr3 { padding-right: 0.25rem; }
.s_pr4 { padding-right: 0.5rem; }
.s_pr5 { padding-right: 1rem; }
.s_pr6 { padding-right: 2rem; }
.s_pr7 { padding-right: 4rem; }
.s_pr8 { padding-right: 8rem; }
.s_pr9 { padding-right: 999rem; }
.s_pb0 { padding-bottom: 0; }
.s_pb1 { padding-bottom: 0.0625rem; }
.s_pb2 { padding-bottom: 0.125rem; }
.s_pb3 { padding-bottom: 0.25rem; }
.s_pb4 { padding-bottom: 0.5rem; }
.s_pb5 { padding-bottom: 1rem; }
.s_pb6 { padding-bottom: 2rem; }
.s_pb7 { padding-bottom: 4rem; }
.s_pb8 { padding-bottom: 8rem; }
.s_pb9 { padding-bottom: 999rem; }
.s_pl0 { padding-left: 0; }
.s_pl1 { padding-left: 0.0625rem; }
.s_pl2 { padding-left: 0.125rem; }
.s_pl3 { padding-left: 0.25rem; }
.s_pl4 { padding-left: 0.5rem; }
.s_pl5 { padding-left: 1rem; }
.s_pl6 { padding-left: 2rem; }
.s_pl7 { padding-left: 4rem; }
.s_pl8 { padding-left: 8rem; }
.s_pl9 { padding-left: 999rem; }
.s_px0 { padding-left: 0; padding-right: 0; }
.s_px1 { padding-left: 0.0625rem; padding-right: 0.0625rem; }
.s_px2 { padding-left: 0.125rem; padding-right: 0.125rem; }
.s_px3 { padding-left: 0.25rem; padding-right: 0.25rem; }
.s_px4 { padding-left: 0.5rem; padding-right: 0.5rem; }
.s_px5 { padding-left: 1rem; padding-right: 1rem; }
.s_px6 { padding-left: 2rem; padding-right: 2rem; }
.s_px7 { padding-left: 4rem; padding-right: 4rem; }
.s_px8 { padding-left: 8rem; padding-right: 8rem; }
.s_px9 { padding-left: 999rem; padding-right: 999rem; }
.s_py0 { padding-top: 0; padding-bottom: 0; }
.s_py1 { padding-top: 0.0625rem; padding-bottom: 0.0625rem; }
.s_py2 { padding-top: 0.125rem; padding-bottom: 0.125rem; }
.s_py3 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
.s_py4 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.s_py5 { padding-top: 1rem; padding-bottom: 1rem; }
.s_py6 { padding-top: 2rem; padding-bottom: 2rem; }
.s_py7 { padding-top: 4rem; padding-bottom: 4rem; }
.s_py8 { padding-top: 8rem; padding-bottom: 8rem; }
.s_py9 { padding-top: 999rem; padding-bottom: 999rem; }
}


@media (min-width: 48em) {
.m_p0 { padding: 0; }
.m_p1 { padding: 0.0625rem; }
.m_p2 { padding: 0.125rem; }
.m_p3 { padding: 0.25rem; }
.m_p4 { padding: 0.5rem; }
.m_p5 { padding: 1rem; }
.m_p6 { padding: 2rem; }
.m_p7 { padding: 4rem; }
.m_p8 { padding: 8rem; }
.m_p9 { padding: 999rem; }
.m_pt0 { padding-top: 0; }
.m_pt1 { padding-top: 0.0625rem; }
.m_pt2 { padding-top: 0.125rem; }
.m_pt3 { padding-top: 0.25rem; }
.m_pt4 { padding-top: 0.5rem; }
.m_pt5 { padding-top: 1rem; }
.m_pt6 { padding-top: 2rem; }
.m_pt7 { padding-top: 4rem; }
.m_pt8 { padding-top: 8rem; }
.m_pt9 { padding-top: 999rem; }
.m_pr0 { padding-right: 0; }
.m_pr1 { padding-right: 0.0625rem; }
.m_pr2 { padding-right: 0.125rem; }
.m_pr3 { padding-right: 0.25rem; }
.m_pr4 { padding-right: 0.5rem; }
.m_pr5 { padding-right: 1rem; }
.m_pr6 { padding-right: 2rem; }
.m_pr7 { padding-right: 4rem; }
.m_pr8 { padding-right: 8rem; }
.m_pr9 { padding-right: 999rem; }
.m_pb0 { padding-bottom: 0; }
.m_pb1 { padding-bottom: 0.0625rem; }
.m_pb2 { padding-bottom: 0.125rem; }
.m_pb3 { padding-bottom: 0.25rem; }
.m_pb4 { padding-bottom: 0.5rem; }
.m_pb5 { padding-bottom: 1rem; }
.m_pb6 { padding-bottom: 2rem; }
.m_pb7 { padding-bottom: 4rem; }
.m_pb8 { padding-bottom: 8rem; }
.m_pb9 { padding-bottom: 999rem; }
.m_pl0 { padding-left: 0; }
.m_pl1 { padding-left: 0.0625rem; }
.m_pl2 { padding-left: 0.125rem; }
.m_pl3 { padding-left: 0.25rem; }
.m_pl4 { padding-left: 0.5rem; }
.m_pl5 { padding-left: 1rem; }
.m_pl6 { padding-left: 2rem; }
.m_pl7 { padding-left: 4rem; }
.m_pl8 { padding-left: 8rem; }
.m_pl9 { padding-left: 999rem; }
.m_px0 { padding-left: 0; padding-right: 0; }
.m_px1 { padding-left: 0.0625rem; padding-right: 0.0625rem; }
.m_px2 { padding-left: 0.125rem; padding-right: 0.125rem; }
.m_px3 { padding-left: 0.25rem; padding-right: 0.25rem; }
.m_px4 { padding-left: 0.5rem; padding-right: 0.5rem; }
.m_px5 { padding-left: 1rem; padding-right: 1rem; }
.m_px6 { padding-left: 2rem; padding-right: 2rem; }
.m_px7 { padding-left: 4rem; padding-right: 4rem; }
.m_px8 { padding-left: 8rem; padding-right: 8rem; }
.m_px9 { padding-left: 999rem; padding-right: 999rem; }
.m_py0 { padding-top: 0; padding-bottom: 0; }
.m_py1 { padding-top: 0.0625rem; padding-bottom: 0.0625rem; }
.m_py2 { padding-top: 0.125rem; padding-bottom: 0.125rem; }
.m_py3 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
.m_py4 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.m_py5 { padding-top: 1rem; padding-bottom: 1rem; }
.m_py6 { padding-top: 2rem; padding-bottom: 2rem; }
.m_py7 { padding-top: 4rem; padding-bottom: 4rem; }
.m_py8 { padding-top: 8rem; padding-bottom: 8rem; }
.m_py9 { padding-top: 999rem; padding-bottom: 999rem; }
}


@media (min-width: 62em) {
.l_p0 { padding: 0; }
.l_p1 { padding: 0.0625rem; }
.l_p2 { padding: 0.125rem; }
.l_p3 { padding: 0.25rem; }
.l_p4 { padding: 0.5rem; }
.l_p5 { padding: 1rem; }
.l_p6 { padding: 2rem; }
.l_p7 { padding: 4rem; }
.l_p8 { padding: 8rem; }
.l_p9 { padding: 999rem; }
.l_pt0 { padding-top: 0; }
.l_pt1 { padding-top: 0.0625rem; }
.l_pt2 { padding-top: 0.125rem; }
.l_pt3 { padding-top: 0.25rem; }
.l_pt4 { padding-top: 0.5rem; }
.l_pt5 { padding-top: 1rem; }
.l_pt6 { padding-top: 2rem; }
.l_pt7 { padding-top: 4rem; }
.l_pt8 { padding-top: 8rem; }
.l_pt9 { padding-top: 999rem; }
.l_pr0 { padding-right: 0; }
.l_pr1 { padding-right: 0.0625rem; }
.l_pr2 { padding-right: 0.125rem; }
.l_pr3 { padding-right: 0.25rem; }
.l_pr4 { padding-right: 0.5rem; }
.l_pr5 { padding-right: 1rem; }
.l_pr6 { padding-right: 2rem; }
.l_pr7 { padding-right: 4rem; }
.l_pr8 { padding-right: 8rem; }
.l_pr9 { padding-right: 999rem; }
.l_pb0 { padding-bottom: 0; }
.l_pb1 { padding-bottom: 0.0625rem; }
.l_pb2 { padding-bottom: 0.125rem; }
.l_pb3 { padding-bottom: 0.25rem; }
.l_pb4 { padding-bottom: 0.5rem; }
.l_pb5 { padding-bottom: 1rem; }
.l_pb6 { padding-bottom: 2rem; }
.l_pb7 { padding-bottom: 4rem; }
.l_pb8 { padding-bottom: 8rem; }
.l_pb9 { padding-bottom: 999rem; }
.l_pl0 { padding-left: 0; }
.l_pl1 { padding-left: 0.0625rem; }
.l_pl2 { padding-left: 0.125rem; }
.l_pl3 { padding-left: 0.25rem; }
.l_pl4 { padding-left: 0.5rem; }
.l_pl5 { padding-left: 1rem; }
.l_pl6 { padding-left: 2rem; }
.l_pl7 { padding-left: 4rem; }
.l_pl8 { padding-left: 8rem; }
.l_pl9 { padding-left: 999rem; }
.l_px0 { padding-left: 0; padding-right: 0; }
.l_px1 { padding-left: 0.0625rem; padding-right: 0.0625rem; }
.l_px2 { padding-left: 0.125rem; padding-right: 0.125rem; }
.l_px3 { padding-left: 0.25rem; padding-right: 0.25rem; }
.l_px4 { padding-left: 0.5rem; padding-right: 0.5rem; }
.l_px5 { padding-left: 1rem; padding-right: 1rem; }
.l_px6 { padding-left: 2rem; padding-right: 2rem; }
.l_px7 { padding-left: 4rem; padding-right: 4rem; }
.l_px8 { padding-left: 8rem; padding-right: 8rem; }
.l_px9 { padding-left: 999rem; padding-right: 999rem; }
.l_py0 { padding-top: 0; padding-bottom: 0; }
.l_py1 { padding-top: 0.0625rem; padding-bottom: 0.0625rem; }
.l_py2 { padding-top: 0.125rem; padding-bottom: 0.125rem; }
.l_py3 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
.l_py4 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.l_py5 { padding-top: 1rem; padding-bottom: 1rem; }
.l_py6 { padding-top: 2rem; padding-bottom: 2rem; }
.l_py7 { padding-top: 4rem; padding-bottom: 4rem; }
.l_py8 { padding-top: 8rem; padding-bottom: 8rem; }
.l_py9 { padding-top: 999rem; padding-bottom: 999rem; }
}


@media (min-width: 75em) {
.x_p0 { padding: 0; }
.x_p1 { padding: 0.0625rem; }
.x_p2 { padding: 0.125rem; }
.x_p3 { padding: 0.25rem; }
.x_p4 { padding: 0.5rem; }
.x_p5 { padding: 1rem; }
.x_p6 { padding: 2rem; }
.x_p7 { padding: 4rem; }
.x_p8 { padding: 8rem; }
.x_p9 { padding: 999rem; }
.x_pt0 { padding-top: 0; }
.x_pt1 { padding-top: 0.0625rem; }
.x_pt2 { padding-top: 0.125rem; }
.x_pt3 { padding-top: 0.25rem; }
.x_pt4 { padding-top: 0.5rem; }
.x_pt5 { padding-top: 1rem; }
.x_pt6 { padding-top: 2rem; }
.x_pt7 { padding-top: 4rem; }
.x_pt8 { padding-top: 8rem; }
.x_pt9 { padding-top: 999rem; }
.x_pr0 { padding-right: 0; }
.x_pr1 { padding-right: 0.0625rem; }
.x_pr2 { padding-right: 0.125rem; }
.x_pr3 { padding-right: 0.25rem; }
.x_pr4 { padding-right: 0.5rem; }
.x_pr5 { padding-right: 1rem; }
.x_pr6 { padding-right: 2rem; }
.x_pr7 { padding-right: 4rem; }
.x_pr8 { padding-right: 8rem; }
.x_pr9 { padding-right: 999rem; }
.x_pb0 { padding-bottom: 0; }
.x_pb1 { padding-bottom: 0.0625rem; }
.x_pb2 { padding-bottom: 0.125rem; }
.x_pb3 { padding-bottom: 0.25rem; }
.x_pb4 { padding-bottom: 0.5rem; }
.x_pb5 { padding-bottom: 1rem; }
.x_pb6 { padding-bottom: 2rem; }
.x_pb7 { padding-bottom: 4rem; }
.x_pb8 { padding-bottom: 8rem; }
.x_pb9 { padding-bottom: 999rem; }
.x_pl0 { padding-left: 0; }
.x_pl1 { padding-left: 0.0625rem; }
.x_pl2 { padding-left: 0.125rem; }
.x_pl3 { padding-left: 0.25rem; }
.x_pl4 { padding-left: 0.5rem; }
.x_pl5 { padding-left: 1rem; }
.x_pl6 { padding-left: 2rem; }
.x_pl7 { padding-left: 4rem; }
.x_pl8 { padding-left: 8rem; }
.x_pl9 { padding-left: 999rem; }
.x_px0 { padding-left: 0; padding-right: 0; }
.x_px1 { padding-left: 0.0625rem; padding-right: 0.0625rem; }
.x_px2 { padding-left: 0.125rem; padding-right: 0.125rem; }
.x_px3 { padding-left: 0.25rem; padding-right: 0.25rem; }
.x_px4 { padding-left: 0.5rem; padding-right: 0.5rem; }
.x_px5 { padding-left: 1rem; padding-right: 1rem; }
.x_px6 { padding-left: 2rem; padding-right: 2rem; }
.x_px7 { padding-left: 4rem; padding-right: 4rem; }
.x_px8 { padding-left: 8rem; padding-right: 8rem; }
.x_px9 { padding-left: 999rem; padding-right: 999rem; }
.x_py0 { padding-top: 0; padding-bottom: 0; }
.x_py1 { padding-top: 0.0625rem; padding-bottom: 0.0625rem; }
.x_py2 { padding-top: 0.125rem; padding-bottom: 0.125rem; }
.x_py3 { padding-top: 0.25rem; padding-bottom: 0.25rem; }
.x_py4 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.x_py5 { padding-top: 1rem; padding-bottom: 1rem; }
.x_py6 { padding-top: 2rem; padding-bottom: 2rem; }
.x_py7 { padding-top: 4rem; padding-bottom: 4rem; }
.x_py8 { padding-top: 8rem; padding-bottom: 8rem; }
.x_py9 { padding-top: 999rem; padding-bottom: 999rem; }
}

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -