# Yukawa couplings with spontaneous symmetry breaking (SSB)

![Python package](https://github.com/restrepo/DevOps/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/restrepo/DevOps/workflows/Upload%20Python%20Package/badge.svg)

Given a list of integers as the Abelian charges of fermions, check if there is a scalar which which can generate Yukawa couplings and non-zero masses for all them after the SSB-

## Install
```bash
$ pip install yukawa
```
## USAGE
```python
>>> from yukawa import yukawa
>>> yukawa.get_massive_fermions(l,s)
[(x,y),...]
```
Links:
* [Test pip page](https://pypi.org/project/yukawa/)
* Flake8 Tool For Style Guide Enforcement
