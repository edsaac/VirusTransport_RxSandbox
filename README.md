```
 _     _                        _   _      _
| |__ (_) ___  _ __   __ _ _ __| |_(_) ___| | ___
| '_ \| |/ _ \| '_ \ / _` | '__| __| |/ __| |/ _ \
| |_) | | (_) | |_) | (_| | |  | |_| | (__| |  __/
|_.__/|_|\___/| .__/ \__,_|_|   \__|_|\___|_|\___|
              |_|
```
## **a PFLOTRAN Reaction Sandbox for virus transport**

<img src="./images/virusBlob.gif" alt="gifBiopartcile" width="600"/>

***

## Conceptual Mode

<img src="./images/virusPath.png" alt="virusPaths" width="600"/>

**Mathematical description:**

<img src="./images/Eqn1.png" alt="Math framework" width="600"/>

***

## Tests

|Test|Link|
|---|---|
|Breakthrough curves from a column experiment | [![Badges](https://img.shields.io/badge/Test-PFLOTRAN-9cf.svg)](https://github.com/edsaac/VirusTransport_RxSandbox/tree/master/test/breakthroughCurves/)|


***

## Instructions

1. Add this new reaction sandbox (*BIOPARTICLE*) to PFLOTRAN's source folder.
```
cp src/reaction_sandbox_escPTr.F90  $PFLOTRAN_DIR/src/pflotran/reaction_sandbox_escPTr.F90
```
2. Replace the main reaction sandbox fortran file to include *BIOPARTICLE* as one of the options.
```
cp src/reaction_sandbox.F90  $PFLOTRAN_DIR/src/pflotran/reaction_sandbox.F90
```
3. Update dependencies.
```
python3 $PFLOTRAN_DIR/python/src/python/pflotran_depedencies.py
```
4. Compile PFLOTRAN code.
```
cd $PFLOTRAN_DIR/src/pflotran/
make pflotran
```

Details at https://bitbucket.org/pflotran/pflotran/wiki/Documentation/ReactionSandbox

***

## Doing right now?

>Trying to replicate results from this paper: 
>
>Sadeghi, G., Schijven, J.F., Behrends, T., Hassanizadeh, S.M., Gerritse, J. and Kleingeld, P.J. (2011), Systematic Study of Effects of pH and Ionic Strength on >Attachment of Phage PRD1. Groundwater, 49: 12-19. [![DOI:10.1111/j.1745-6584.2010.00767.x](https://zenodo.org/badge/DOI/10.1111/j.1745-6584.2010.00767.x.svg)](https://doi.org/10.1111/j.1745-6584.2010.00767.x)
>
_______

[![OS<3](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)