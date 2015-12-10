import FWCore.ParameterSet.Config as cms

import pileUpCorrector.pileUpFilter.pileUpFilter_cfi

pileUpFilter_default = pileUpCorrector.pileUpFilter.pileUpFilter_cfi.pileupVertexFilter.clone() 

### define your own filter ###

pileUpFilter_baseCut = pileUpFilter_default.clone(
## add cuts ##
)

pileUpFilter_baseCut_dz = pileUpFilter_default.clone(
## add cuts ##
)

pileUpFilter_only1Vertex = pileUpFilter_default.clone(
 			   dzCutByNtrk = cms.vdouble( 999., 0.0, 0.0, 0.0, 0.0),
                           dzTolerance = cms.double(9999.),)

