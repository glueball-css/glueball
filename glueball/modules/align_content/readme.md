# module: Align content

Align a flex container's lines within it, when there is extra space in the cross-axis.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.ac` |`align-content`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Alignment options

Selector  | Value
--------- | ---------
`fs` | `flex-start`
`fe` | `flex-end`
`c` | `center`
`sb` | `space-between`
`sa` | `space-around`
`s` | `stretch`





## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.ac-fs { align-content: flex-start; }
.ac-fe { align-content: flex-end; }
.ac-c { align-content: center; }
.ac-sb { align-content: space-between; }
.ac-sa { align-content: space-around; }
.ac-s { align-content: stretch; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -