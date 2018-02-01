# module: Justify content

Defines the alignment along the main axis.
It distributes extra free space leftover when the flex items on a line are inflexible,
or have reached their maximum size.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.jc` |`justify-content`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Distributions

Selector  | Value
--------- | ---------
`fs` | `flex-start`
`fe` | `flex-end`
`c` | `center`
`sb` | `space-between`
`sa` | `space-around`
`se` | `space-evenly`





## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.jc-fs { justify-content: flex-start; }
.jc-fe { justify-content: flex-end; }
.jc-c { justify-content: center; }
.jc-sb { justify-content: space-between; }
.jc-sa { justify-content: space-around; }
.jc-se { justify-content: space-evenly; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -