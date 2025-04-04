# skywater-std-cell-char
Standard Cell characterization for the Skywater 130nm PDK using open-source tools

# RC Extraction with magic

```
extract all
ext2sim labels on
ext2sim
extresist all
ext2spice lvs
ext2spice cthresh 0.1
ext2spice extresist on
ext2spice
```

See also [Github](https://github.com/RTimothyEdwards/magic/issues/174)
