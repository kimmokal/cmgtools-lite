#!/usr/bin/env python
#import re, sys, os, os.path

import glob, os, sys, math


### ./makeBinYields.py --mca ../systs/PDFUnc-RMS/mca-Summer16_Moriond17.txt -P ../systs/PDFUnc-RMS/links -F sf/t ../systs/PDFUnc-RMS/links/Friends/DileptonPreapproval/evVarFriend_{cname}.root -l 2.2 --grid -v 2 --od lumi22fb_DlMakeBinYields/PDFUnc-RMS --syst -b
#Following recipe from
#https://indico.cern.ch/event/459797/contribution/2/attachments/1181555/1710844/mcaod-Nov4-2015.pdf
#i.e.:
#MC Replicas: Make a distribution of the observable under the (eg 100) MC replicas and either take the RMS as the uncertainty or propagate the full distribution for non-gaussian cases


#PDFUnc-RMS

firstPart = """
### ./makeBinYields.py --mca ../systs/PDFUnc-RMS/mca-Summer16_Moriond17.txt -P ../systs/PDFUnc-RMS/links -F sf/t ../systs/PDFUnc-RMS/links/Friends/DileptonPreapproval/evVarFriend_{cname}.root -l 2.2 --grid -v 2 --od lumi22fb_DlMakeBinYields/PDFUnc-RMS --syst -b
#Following recipe from
#https://indico.cern.ch/event/459797/contribution/2/attachments/1181555/1710844/mcaod-Nov4-2015.pdf
#i.e.:
#MC Replicas: Make a distribution of the observable under the (eg 100) MC replicas and either take the RMS as the uncertainty or propagate the full distribution for non-gaussian cases

# MCA file for Summer16 samples

# Dileptonic ttbar
TTdiLep            : TTJets_DiLepton             : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : lheHTIncoming <= 600;
TTdiLep            : TTJets_LO_HT600to800        : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2 ;
TTdiLep            : TTJets_LO_HT800to1200       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;
TTdiLep            : TTJets_LO_HT1200to2500      : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;
TTdiLep            : TTJets_LO_HT2500toInf       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;

# Semileptonic ttbar
TTsemiLep          : TTJets_SingleLeptonFromT    : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : lheHTIncoming <= 600;
TTsemiLep          : TTJets_SingleLeptonFromTbar : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : lheHTIncoming <= 600;
TTsemiLep          : TTJets_LO_HT600to800        : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2  ;
TTsemiLep          : TTJets_LO_HT800to1200       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;
TTsemiLep          : TTJets_LO_HT1200to2500      : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;
TTsemiLep          : TTJets_LO_HT2500toInf       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;

# W+Jets
#WJets    : WJetsToLNu_HT100to200   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
#WJets    : WJetsToLNu_HT200to400   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
WJets    : WJetsToLNu_HT400to600   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
WJets    : WJetsToLNu_HT600to800   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
WJets    : WJetsToLNu_HT800to1200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
WJets    : WJetsToLNu_HT1200to2500 : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;
WJets    : WJetsToLNu_HT2500toInf  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr  ;

# QCD
QCD      : QCD_HT300to500          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
QCD      : QCD_HT500to700          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
QCD      : QCD_HT700to1000         : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
QCD      : QCD_HT1000to1500        : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
QCD      : QCD_HT1500to2000        : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
QCD      : QCD_HT2000toInf         : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;

# Single Top
SingleT : TToLeptons_sch           : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
SingleT : T_tch_powheg             : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
SingleT : TBar_tch_powheg          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
SingleT : TBar_tWch                : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
SingleT : T_tWch                   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;

# Drell-Yan
#DY      : DYJetsToLL_M50_HT100to200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
#DY      : DYJetsToLL_M50_HT200to400  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
DY      : DYJetsToLL_M50_HT400to600   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
DY      : DYJetsToLL_M50_HT600to800   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
DY      : DYJetsToLL_M50_HT800to1200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
DY      : DYJetsToLL_M50_HT1200to2500 : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
DY      : DYJetsToLL_M50_HT2500toInf  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;

# TTV
TTV : TTWToLNu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
TTV : TTWToQQ       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
TTV : TTZToLLNuNu   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
TTV : TTZToQQ       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;

# DiBoson
VV : WWTo2L2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
VV : WWToLNuQQ      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
VV : WZTo1L1Nu2Q    : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
VV : WZTo1L3Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
VV : WZTo2L2Q       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
VV : ZZTo2L2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;
#VV : ZZTo2Q2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr ;

"""




def returnWeightSnippe(index):
    temp = """
### PDF variation

# Dileptonic ttbar
TTdiLep_PDFUnc-RMS{0}            : TTJets_DiLepton             : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : lheHTIncoming <= 600;
TTdiLep_PDFUnc-RMS{0}            : TTJets_LO_HT600to800        : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2 ;
TTdiLep_PDFUnc-RMS{0}            : TTJets_LO_HT800to1200       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;
TTdiLep_PDFUnc-RMS{0}            : TTJets_LO_HT1200to2500      : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;
TTdiLep_PDFUnc-RMS{0}            : TTJets_LO_HT2500toInf       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24)==2;

# Semileptonic ttbar
TTsemiLep_PDFUnc-RMS{0}          : TTJets_SingleLeptonFromT    : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : lheHTIncoming <= 600;
TTsemiLep_PDFUnc-RMS{0}          : TTJets_SingleLeptonFromTbar : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : lheHTIncoming <= 600;
TTsemiLep_PDFUnc-RMS{0}          : TTJets_LO_HT600to800        : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2  ;
TTsemiLep_PDFUnc-RMS{0}          : TTJets_LO_HT800to1200       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;
TTsemiLep_PDFUnc-RMS{0}          : TTJets_LO_HT1200to2500      : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;
TTsemiLep_PDFUnc-RMS{0}          : TTJets_LO_HT2500toInf       : Xsec*1*btagSF*nISRttweight*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] : Sum$(abs(genTau_grandmotherId)==6&&abs(genTau_motherId)==24)+Sum$(abs(genLep_grandmotherId)==6&&abs(genLep_motherId)==24) <2 ;

# W+Jets
#WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT100to200   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
#WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT200to400   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT400to600   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT600to800   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT800to1200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT1200to2500 : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;
WJets_PDFUnc-RMS{0}    : WJetsToLNu_HT2500toInf  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0]  ;

# QCD
QCD_PDFUnc-RMS{0}      : QCD_HT300to500          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
QCD_PDFUnc-RMS{0}      : QCD_HT500to700          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
QCD_PDFUnc-RMS{0}      : QCD_HT700to1000         : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
QCD_PDFUnc-RMS{0}      : QCD_HT1000to1500        : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
QCD_PDFUnc-RMS{0}      : QCD_HT1500to2000        : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
QCD_PDFUnc-RMS{0}      : QCD_HT2000toInf         : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;

# Single Top
SingleT_PDFUnc-RMS{0} : TToLeptons_sch           : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
SingleT_PDFUnc-RMS{0} : T_tch_powheg             : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
SingleT_PDFUnc-RMS{0} : TBar_tch_powheg          : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
SingleT_PDFUnc-RMS{0} : TBar_tWch                : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
SingleT_PDFUnc-RMS{0} : T_tWch                   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;

# Drell-Yan
#DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT100to200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
#DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT200to400  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT400to600   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT600to800   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT800to1200  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT1200to2500 : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
DY_PDFUnc-RMS{0}      : DYJetsToLL_M50_HT2500toInf  : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;

# TTV
TTV_PDFUnc-RMS{0} : TTWToLNu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
TTV_PDFUnc-RMS{0} : TTWToQQ       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
TTV_PDFUnc-RMS{0} : TTZToLLNuNu   : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
TTV_PDFUnc-RMS{0} : TTZToQQ       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;

# DiBoson
VV_PDFUnc-RMS{0} : WWTo2L2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
VV_PDFUnc-RMS{0} : WWToLNuQQ      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
VV_PDFUnc-RMS{0} : WZTo1L1Nu2Q    : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
VV_PDFUnc-RMS{0} : WZTo1L3Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
VV_PDFUnc-RMS{0} : WZTo2L2Q       : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
VV_PDFUnc-RMS{0} : ZZTo2L2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;
#VV_PDFUnc-RMS{0} : ZZTo2Q2Nu      : Xsec*1*btagSF*puRatio*lepSF*DilepNJetCorr*LHEweight_wgt[{0}]/LHEweight_wgt[0] ;


""".format(index)
    return temp

f = open('mca-Summer16_Moriond17.txt', 'w')
f.write(firstPart)
for i in range (9,110):
    f.write(returnWeightSnippe(i))
f.close()


split = 0
f = open('mca-Summer16_Moriond17_{0}.txt'.format(split), 'w')
f.write(firstPart)
for i in range (9,110):
    if i%10==0:
        f.close()
        split += 1
        f = open('mca-Summer16_Moriond17_{0}.txt'.format(split), 'w')
        f.write(firstPart)
    f.write(returnWeightSnippe(i))
f.close()


for i in range (0,split+1):
    print "./makeBinYields.py --mca ../systs/PDFUnc-RMS/mca-Summer16_Moriond17_{split}.txt -P ../systs/PDFUnc-RMS/links -F sf/t ../systs/PDFUnc-RMS/links/Friends/DileptonPreapproval/evVarFriend_{cname}.root -l 2.2 --grid -v 2 --od lumi22fb_DlMakeBinYields/PDFUnc-RMS_{split} --syst -b".format(cname="{cname}",split=i)
