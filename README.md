# Merge svg-s to one pdf aligning them in grid

Two A5 svg can be printed on one 1 A4 paper. Or four A6 can be printed on A4. The script aligns images on one pdf file and draw lines to cut paper.

```
bash gen4.sh FILEs
```

Result is `out.pdf` file.

But default options is good only for A6 on A4 paper. There is some options which one can specify by environment variables

To print two A5 svg on A4:

```
ROWS=2 COLUMNS=1 ROTATE=1 SCALE=0.7 OPACITY=1 bash gen4.sh 1.svg 2.svg
```

To print two A4 svg on A4:

```
ROWS=2 COLUMNS=1 ROTATE=1 OPACITY=1 bash gen4.sh 1.svg 2.svg
```

To print four A6 svg on A4:

```
SCALE=0.5 OPACITY=1 bash gen4.sh 1.svg 2.svg 3.svg 4.svg
```
