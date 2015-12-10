# pileUpCorrector
pileUp filter for Run2 pp analysis

- pileUp filter candidates
	- <strong> pileUpFilter_baseCut </strong>, apply a Ntrk cut (number of tracks associated with second primary vertex) as function of dz values
	- <strong> pileUpFilter_baseCut_dz </strong>, on top of baseCut, accept events that dz > 1cm (distance between first primary vertex and second primary vertex in z direction)
	- <strong> pileUpFilter_only1Vertex </strong>, the extreme cut, accept events with only 1 vertex exsit

## Instructions to add pileUp filter

- go to CMSSW_versions/src directory
- type <pre><code> git clone https://github.com/KongTu/pileUpCorrector.git </pre></code>
- <pre><code>scram b -j4 </pre></code>
- go to your config file that runs, add the following line where you load includes 
<pre><code> process.load("pileUpCorrector.pileUpFilter.pileUpFilter_cff") </pre></code>
- add your filter candidate process in the <strong> cms.Path() </strong>, for example: <pre><code> process.pileUpFilter_baseCut </pre></code>

Enjoy!

HI Tracking team


