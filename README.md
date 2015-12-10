# pileUpCorrector
pileUp filter for Run2 pp analysis

- pileUp filter candidates
	- pileUpFilter_baseCut, to apply a Ntrk cut (number of tracks associated with second primary vertex) as function of dz values
	- pileUpFilter_baseCut_dz, on top of baseCut, accept events that dz > 1cm (distance between first primary vertex and second primary vertex in z direction)
	- pileUpFilter_only1Vertex, the extreme cut, accept events with only 1 vertex exsit

## Instructions to add pileUp filter

- click on <dfn> copy to clipboard </dfn>
- go to CMSSW_versions/src directory
- type <pre><code> git clone https://github.com/KongTu/pileUpCorrector.git </pre></code>
- scram b -j4
- go to your config file that runs, add the following line where you load includes 
<pre><code> process.load("pileUpCorrector.pileUpFilter.pileUpFilter_cff") </pre></code>
- add your filter candidate process in the cms.Path() <pre><code> process.pileUpFilter_baseCut </pre></code>

Enjoy!

HI Tracking team


