# Breakthrough curves from a column experiment

**What is a breakthrough curve?**<br>
It's a plot of concentration at some point over time

**What is a column experiment?**<br>
A fluid with some solute concentration is injected at one end of a cilyndrical soil sample and its concentration is registered at the other end. 

**More details at:** <br>
[![DOI:10.1016/B978-0-12-420022-7.00014-8](https://zenodo.org/badge/DOI/10.1016/B978-0-12-420022-7.00014-8.svg)](https://linkinghub.elsevier.com/retrieve/pii/B9780124200227000148)

<p>&nbsp;</p>
***

## Description
<p align="center">
	<img src="./btCol_media/gifs/descriptionProblem.png" alt="Breakthrough curve" height=400>
</p>

<p>
An injection of some bioparticle (e.g. a virus) concentration is set at the inlet of a column experiment. The bioparticle can either attach to the solid matrix, dettach and reenter the aqueous phase, and decay into another species. After some time, the bioparticle injection is stopped and only clean water keeps runing through the column. 
</p>

|Column parameters | | Value | Unit |
|---|---|--:|:--|
|Lenght| *L* |50|cm|
|Diameter| *Ø* | 5|cm|
|Darcy flow| *q* |2.05|cm/h|
|Porosity| *φ* |0.37|-|
|Grain size| *d<sub>50</sub>*|0.44|mm|

<p>&nbsp;</p>

|Particle parameters | | Value | Unit |
|---|---|--:|:--|
|Size | *d<sub>p</sub>*| 62 | nm |
|Isoelectric point| *IEP*| ~ 3.5| - |
|Initial concentration| *C<sub>0</sub>*| 1.66 × 10<sup>-16</sup>|mol/L|

<p>&nbsp;</p>

***

## **Plug flow case**

|Parameter | | Value | Unit |
|---|---|--:|:--|
|Long. dispersion coefficient| *α<sub>L</sub>* |0 |cm|
|Attachment rate| *k<sub>att</sub>* |0|1/s|
|Detachment rate| *k<sub>det</sub>* |0|1/s|
|Decay while in aqueous phase| *λ<sub>aq</sub>* |0|1/s|
|Decay while adsorbed to solid phase| *λ<sub>im</sub>* |0|1/s|

<p>&nbsp;</p>

**Results**

<p align="left">
	<img src="./btCol_media/plots/bt_plugFlow.png" alt="Breakthrough curve" height=400>
</p>

***

## **With longitudinal dispersion**

|Parameter | | Value | Unit |
|---|---|--:|:--|
|Long. dispersion coefficient| *α<sub>L</sub>* |0.2 |cm|
|Attachment rate| *k<sub>att</sub>* |0|1/s|
|Detachment rate| *k<sub>det</sub>* |0|1/s|
|Decay while in aqueous phase| *λ<sub>aq</sub>* |0|1/s|
|Decay while adsorbed to solid phase| *λ<sub>im</sub>* |0|1/s|

<p>&nbsp;</p>

**Results**

<p align="left">
	<img src="./btCol_media/plots/bt_longDispersion.png" alt="Breakthrough curve" height=400><img src="./btCol_media/gifs/onlyDispersion.gif" alt="Breakthrough curve" height=400>
</p>

***

## **Only attachment (sink)**

|Parameter | | Value | Unit |
|---|---|--:|:--|
|Long. dispersion coefficient| *α<sub>L</sub>* |0.2 |cm|
|Attachment rate| *k<sub>att</sub>* |1.11 × 10<sup>-5</sup>|1/s|
|Detachment rate| *k<sub>det</sub>* |0|1/s|
|Decay while in aqueous phase| *λ<sub>aq</sub>* |0|1/s|
|Decay while adsorbed to solid phase| *λ<sub>im</sub>* |0|1/s|

<p>&nbsp;</p>

**Results**

<p align="left">
	<img src="./btCol_media/plots/bt_onlyAttachment.png" alt="Breakthrough curve" height=400><img src="./btCol_media/gifs/onlyAttachment.gif" alt="Breakthrough curve" height=400>
</p>

***

## **Attachment & detachment (source + sink)**

|Parameter | | Value | Unit |
|---|---|--:|:--|
|Long. dispersion coefficient| *α<sub>L</sub>* |0.2 |cm|
|Attachment rate| *k<sub>att</sub>* |1.11 × 10<sup>-5</sup>|1/s|
|Detachment rate| *k<sub>det</sub>* |7.22 × 10<sup>-7</sup>|1/s|
|Decay while in aqueous phase| *λ<sub>aq</sub>* |0|1/s|
|Decay while adsorbed to solid phase| *λ<sub>im</sub>* |0|1/s|

<p>&nbsp;</p>

**Results**

<p align="left">
	<img src="./btCol_media/plots/bt_attachDetachment.png" alt="Breakthrough curve" height=300><img src="./btCol_media/gifs/attachDetachment.gif" alt="Breakthrough curve" height=300>
</p>

***

## **Attachment, detachment & decay**

|Parameter | | Value | Unit |
|---|---|--:|:--|
|Long. dispersion coefficient| *α<sub>L</sub>* |0.2 |cm|
|Attachment rate| *k<sub>att</sub>* |1.11 × 10<sup>-5</sup>|1/s|
|Detachment rate| *k<sub>det</sub>* |7.22 × 10<sup>-7</sup>|1/s|
|Decay while in aqueous phase| *λ<sub>aq</sub>* |1.94 × 10<sup>-6</sup>|1/s|
|Decay while adsorbed to solid phase| *λ<sub>im</sub>* |9.72 × 10<sup>-6</sup>|1/s|

<p>&nbsp;</p>

**Results**

<p align="left">
	<img src="./btCol_media/plots/bt_allProcesses.png" alt="Breakthrough curve" height=400>
</p>

_______

[&#128281;](https://edsaac.github.io/bioparticle/) << Go back.

<p align="right">
	<img src="https://badges.frapsoft.com/os/v1/open-source.png?v=103" alt="OS<3">
</p>

