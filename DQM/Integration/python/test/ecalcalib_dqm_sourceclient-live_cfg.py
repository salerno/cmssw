### AUTO-GENERATED CMSRUN CONFIGURATION FOR ECAL DQM ###
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('runkey', default = 'pp_run', mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string, info = 'Run Keys of CMS')
options.register('runNumber', default = 194533, mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.int, info = "Run number.")
options.register('runInputDir', default = '/fff/BU0/test', mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string, info = "Directory where the DQM files will appear.")
options.register('skipFirstLumis', default = False, mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.bool, info = "Skip (and ignore the minEventsPerLumi parameter) for the files which have been available at the begining of the processing.")

options.parseArguments()


from DQM.Integration.test.dqmPythonTypes import *
runType = RunType(['pp_run','cosmic_run','hi_run','hpu_run'])
if not options.runkey.strip():
    options.runkey = 'pp_run'

runType.setRunType(options.runkey.strip())

process = cms.Process("process")

### Load cfis ###

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
process.load("RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi")
process.load("RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi")
process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")
process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")
process.load("DQM.EcalMonitorTasks.EcalCalibMonitorTasks_cfi")
process.load("DQM.EcalMonitorClient.EcalCalibMonitorClient_cfi")
process.load("DQM.Integration.test.environment_cfi")
process.load("FWCore.Modules.preScaler_cfi")
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

### Individual module setups ###

process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        threshold = cms.untracked.string('WARNING'),
        noTimeStamps = cms.untracked.bool(True),
        noLineBreaks = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('cerr')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.ecalLaserLedUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    alphaEB = cms.double(1.138),
    alphaEE = cms.double(1.89),
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    AlphaBetaFilename = cms.untracked.string('NOFILE'),
    betaEB = cms.double(1.655),
    MinAmplEndcap = cms.double(16.0),
    MinAmplBarrel = cms.double(12.0),
    algo = cms.string('EcalUncalibRecHitWorkerFixedAlphaBetaFit'),
    betaEE = cms.double(1.4),
    UseDynamicPedestal = cms.bool(True),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB')
)

process.ecalLaserLedFilter = cms.EDFilter("EcalMonitorPrescaler",
    laserPrescaleFactor = cms.untracked.int32(1),
    ledPrescaleFactor = cms.untracked.int32(1),
    EcalRawDataCollection = cms.InputTag("ecalDigis")
)

process.ecalPedestalFilter = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalDigis"),
    pedestalPrescaleFactor = cms.untracked.int32(1)
)

process.ecalTestPulseFilter = cms.EDFilter("EcalMonitorPrescaler",
    testpulsePrescaleFactor = cms.untracked.int32(1),
    EcalRawDataCollection = cms.InputTag("ecalDigis")
)

process.ecalDigis = cms.EDProducer("EcalRawToDigi",
    tccUnpacking = cms.bool(True),
    FedLabel = cms.InputTag("listfeds"),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    feIdCheck = cms.bool(True),
    silentMode = cms.untracked.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    eventPut = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54),
    FEDs = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    DoRegional = cms.bool(False),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True)
)

process.source = cms.Source("DQMStreamerReader",
    streamLabel = cms.untracked.string('_streamDQM_StorageManager'),
    delayMillis = cms.untracked.uint32(500),
    runNumber = cms.untracked.uint32(0),
    endOfRunKills = cms.untracked.bool(True),
    runInputDir = cms.untracked.string(''),
    minEventsPerLumi = cms.untracked.int32(1),
    deleteDatFiles = cms.untracked.bool(False),
    SelectEvents = cms.untracked.vstring('*'),
    skipFirstLumis = cms.untracked.bool(False)
)

process.ecalCalibrationFilter = cms.EDFilter("EcalMonitorPrescaler",
    laserPrescaleFactor = cms.untracked.int32(1),
    testpulsePrescaleFactor = cms.untracked.int32(1),
    ledPrescaleFactor = cms.untracked.int32(1),
    EcalRawDataCollection = cms.InputTag("ecalDigis"),
    pedestalPrescaleFactor = cms.untracked.int32(1)
)

process.ecalTestPulseUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    algo = cms.string('EcalUncalibRecHitWorkerMaxSample'),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB')
)

process.ecalCalibMonitorClient.verbosity = 0

process.preScaler.prescaleFactor = 1

process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/ecalcalib_reference.root"

process.ecalPNDiodeMonitorTask.verbosity = 0

process.GlobalTag.toGet = cms.VPSet(cms.PSet(
    record = cms.string('EcalDQMChannelStatusRcd'),
    tag = cms.string('EcalDQMChannelStatus_v1_hlt'),
    connect = cms.untracked.string('frontier://(proxyurl=http://frontier.cms:3128)(serverurl=http://frontier.cms:8000/FrontierOnProd)(serverurl=http://frontier.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)(failovertoserver=no)/CMS_COND_34X_ECAL')
), 
    cms.PSet(
        record = cms.string('EcalDQMTowerStatusRcd'),
        tag = cms.string('EcalDQMTowerStatus_v1_hlt'),
        connect = cms.untracked.string('frontier://(proxyurl=http://frontier.cms:3128)(serverurl=http://frontier.cms:8000/FrontierOnProd)(serverurl=http://frontier.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)(failovertoserver=no)/CMS_COND_34X_ECAL')
    ))

process.ecalLaserLedMonitorTask.verbosity = 0

process.ecalPedestalMonitorTask.verbosity = 0

process.ecalTestPulseMonitorTask.verbosity = 0

process.dqmEnv.subSystemFolder = cms.untracked.string('EcalCalibration')

### Sequences ###

process.ecalRecoSequence = cms.Sequence((process.ecalGlobalUncalibRecHit+process.ecalDetIdToBeRecovered+process.ecalRecHit))
process.ecalPreRecoSequence = cms.Sequence(process.ecalDigis)

### Paths ###

process.ecalLaserLedPath = cms.Path(process.preScaler+process.ecalPreRecoSequence+process.ecalLaserLedFilter+process.ecalRecoSequence+process.ecalLaserLedUncalibRecHit+process.ecalLaserLedMonitorTask+process.ecalPNDiodeMonitorTask)
process.ecalTestPulsePath = cms.Path(process.preScaler+process.ecalPreRecoSequence+process.ecalTestPulseFilter+process.ecalRecoSequence+process.ecalTestPulseUncalibRecHit+process.ecalTestPulseMonitorTask+process.ecalPNDiodeMonitorTask)
process.ecalPedestalPath = cms.Path(process.preScaler+process.ecalPreRecoSequence+process.ecalPedestalFilter+process.ecalPedestalFilter+process.ecalRecoSequence+process.ecalPedestalMonitorTask+process.ecalPNDiodeMonitorTask)
process.ecalClientPath = cms.Path(process.preScaler+process.ecalPreRecoSequence+process.ecalCalibrationFilter+process.ecalCalibrationFilter+process.ecalCalibMonitorClient)

process.dqmEndPath = cms.EndPath(process.dqmEnv)
process.dqmOutputPath = cms.EndPath(process.dqmSaver)

### Schedule ###

process.schedule = cms.Schedule(process.ecalLaserLedPath,process.ecalTestPulsePath,process.ecalPedestalPath,process.ecalClientPath,process.dqmEndPath,process.dqmOutputPath)

### Setup source ###
process.source.runNumber = options.runNumber
process.source.runInputDir = options.runInputDir
process.source.skipFirstLumis = options.skipFirstLumis
