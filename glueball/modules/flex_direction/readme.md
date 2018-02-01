# module: Flex direction

Establishes the main-axis, thus defining the direction flex items are placed
inside the flex container.








## Dynamic properties
The value of a dynamic property is determined by the provided values.

| Base selector | Dynamic props |
| ------------- | ------------- |
| `.fd` |`flex-direction`|





## Provided values
The following sets of values determine the dynamic properties and selectors.

### Directions

Selector  | Value
--------- | ---------
`row` | `row`
`col` | `row-reverse`
`rowr` | `column`
`colr` | `column-reverse`





## Media





| Prefix  |  >0 |  >36 |  >48 |  >62 |  >75 | 
| :------:  |  :---------: |  :---------: |  :---------: |  :---------: |  :---------: | 
|  (none)  |▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|▒▒▒▒▒|






## CSS rules
```css

.fd-row { flex-direction: row; }
.fd-col { flex-direction: row-reverse; }
.fd-rowr { flex-direction: column; }
.fd-colr { flex-direction: column-reverse; }

```

- - - - -
_**note: This documentation was auto-generated from the source files.**_
- - - - -