Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/abbyestep/Downloads/cryptanalysis-3.py ============
>>> ciphertext = "TAFM QGBPMU FXTPGKBQUM TAU HUPMHUQTFVUM DXK OUTAGKM GJ QGOHBTUP MQFUXQU. MZOLGCFQ FXJGPODTFGX FM PUHPUMUXTUK DM KDTD, WAUTAUP FT LU XBOLUPM, TUIT, GP FODNUM. DBTGODTUK HPGQUMMUM JGP GHUPDTFXN GX TAU KDTD DPU PUHPUMUXTUK LZ NUXUPDC HPGQUKBPUM YXGWX DM DCNGPFTAOM. TAGMU DCNGPFTAOM DPU WPFTTUX FX D HDPTFQBCDP XGTDTFGX, D HPGNPDOOFXN CDXNBDNU, DM HPGNPDOM. MTBKUXTM WFCC CUDPX AGW TG QDPPZ GBT TAUMU TDMYM DXK AGW TG TAFXY DLGBT QGOHBTDTFGX FX TUPOM GJ NUXUPDC HDTTUPXM, MBQA DM AFUPDPQAFQDC QGOHGMFTFGX GP TAU BMU GJ FXTUPQADXNUDLCU QGOHGXUXTM WFTA QGXMFMTUXT FXTUPJDQUM"
>>> 
============ RESTART: /Users/abbyestep/Downloads/cryptanalysis-3.py ============
>>> ciphertext = "TAFM QGBPMU FXTPGKBQUM TAU HUPMHUQTFVUM DXK OUTAGKM GJ QGOHBTUP MQFUXQU. MZOLGCFQ FXJGPODTFGX FM PUHPUMUXTUK DM KDTD, WAUTAUP FT LU XBOLUPM, TUIT, GP FODNUM. DBTGODTUK HPGQUMMUM JGP GHUPDTFXN GX TAU KDTD DPU PUHPUMUXTUK LZ NUXUPDC HPGQUKBPUM YXGWX DM DCNGPFTAOM. TAGMU DCNGPFTAOM DPU WPFTTUX FX D HDPTFQBCDP XGTDTFGX, D HPGNPDOOFXN CDXNBDNU, DM HPGNPDOM. MTBKUXTM WFCC CUDPX AGW TG QDPPZ GBT TAUMU TDMYM DXK AGW TG TAFXY DLGBT QGOHBTDTFGX FX TUPOM GJ NUXUPDC HDTTUPXM, MBQA DM AFUPDPQAFQDC QGOHGMFTFGX GP TAU BMU GJ FXTUPQADXNUDLCU QGOHGXUXTM WFTA QGXMFMTUXT FXTUPJDQUM"
>>> suggest_substitutions(ciphertext)
One letter words:
D
D
Suggestions for one letter words: a, i
Two letter words:
GJ
FM
DM
FT
LU
GP
GX
LZ
DM
FX
DM
TG
TG
FX
GJ
DM
GP
GJ
Suggestions for two letter words:  of, to, in, it, is, be, as, at, so, we, he, by, or, on, do, if, me, my, up, an, go, no, us, am
Three letter words:
TAU
DXK
JGP
TAU
DPU
DPU
AGW
GBT
DXK
AGW
TAU
BMU
Suggestions for three letter words: the, and, for, are, but, not, you, all, any, can, had, her, was, one, our, out, day, get, has, him, his, how, man, new, now, old, see, two, way, who, boy, did, its, let, put, say, she, too, use
>>> substitute(ciohertext, "D G", "a o")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    substitute(ciohertext, "D G", "a o")
NameError: name 'ciohertext' is not defined
>>> substitute(ciphertext, "D G", "a o")
'TAFM QoBPMU FXTPoKBQUM TAU HUPMHUQTFVUM aXK OUTAoKM oJ QoOHBTUP MQFUXQU. MZOLoCFQ FXJoPOaTFoX FM PUHPUMUXTUK aM KaTa, WAUTAUP FT LU XBOLUPM, TUIT, oP FOaNUM. aBToOaTUK HPoQUMMUM JoP oHUPaTFXN oX TAU KaTa aPU PUHPUMUXTUK LZ NUXUPaC HPoQUKBPUM YXoWX aM aCNoPFTAOM. TAoMU aCNoPFTAOM aPU WPFTTUX FX a HaPTFQBCaP XoTaTFoX, a HPoNPaOOFXN CaXNBaNU, aM HPoNPaOM. MTBKUXTM WFCC CUaPX AoW To QaPPZ oBT TAUMU TaMYM aXK AoW To TAFXY aLoBT QoOHBTaTFoX FX TUPOM oJ NUXUPaC HaTTUPXM, MBQA aM AFUPaPQAFQaC QoOHoMFTFoX oP TAU BMU oJ FXTUPQAaXNUaLCU QoOHoXUXTM WFTA QoXMFMTUXT FXTUPJaQUM'
>>>  substitute(ciphertext, "D", "i")
 
SyntaxError: unexpected indent
>>> substitute(ciphertext, "D", "i")
'TAFM QGBPMU FXTPGKBQUM TAU HUPMHUQTFVUM iXK OUTAGKM GJ QGOHBTUP MQFUXQU. MZOLGCFQ FXJGPOiTFGX FM PUHPUMUXTUK iM KiTi, WAUTAUP FT LU XBOLUPM, TUIT, GP FOiNUM. iBTGOiTUK HPGQUMMUM JGP GHUPiTFXN GX TAU KiTi iPU PUHPUMUXTUK LZ NUXUPiC HPGQUKBPUM YXGWX iM iCNGPFTAOM. TAGMU iCNGPFTAOM iPU WPFTTUX FX i HiPTFQBCiP XGTiTFGX, i HPGNPiOOFXN CiXNBiNU, iM HPGNPiOM. MTBKUXTM WFCC CUiPX AGW TG QiPPZ GBT TAUMU TiMYM iXK AGW TG TAFXY iLGBT QGOHBTiTFGX FX TUPOM GJ NUXUPiC HiTTUPXM, MBQA iM AFUPiPQAFQiC QGOHGMFTFGX GP TAU BMU GJ FXTUPQAiXNUiLCU QGOHGXUXTM WFTA QGXMFMTUXT FXTUPJiQUM'
>>> substitute(ciphertext, "D G", "i o")
'TAFM QoBPMU FXTPoKBQUM TAU HUPMHUQTFVUM iXK OUTAoKM oJ QoOHBTUP MQFUXQU. MZOLoCFQ FXJoPOiTFoX FM PUHPUMUXTUK iM KiTi, WAUTAUP FT LU XBOLUPM, TUIT, oP FOiNUM. iBToOiTUK HPoQUMMUM JoP oHUPiTFXN oX TAU KiTi iPU PUHPUMUXTUK LZ NUXUPiC HPoQUKBPUM YXoWX iM iCNoPFTAOM. TAoMU iCNoPFTAOM iPU WPFTTUX FX i HiPTFQBCiP XoTiTFoX, i HPoNPiOOFXN CiXNBiNU, iM HPoNPiOM. MTBKUXTM WFCC CUiPX AoW To QiPPZ oBT TAUMU TiMYM iXK AoW To TAFXY iLoBT QoOHBTiTFoX FX TUPOM oJ NUXUPiC HiTTUPXM, MBQA iM AFUPiPQAFQiC QoOHoMFTFoX oP TAU BMU oJ FXTUPQAiXNUiLCU QoOHoXUXTM WFTA QoXMFMTUXT FXTUPJiQUM'
>>> substitute(ciphertext, "D G X", "i o t")
'TAFM QoBPMU FtTPoKBQUM TAU HUPMHUQTFVUM itK OUTAoKM oJ QoOHBTUP MQFUtQU. MZOLoCFQ FtJoPOiTFot FM PUHPUMUtTUK iM KiTi, WAUTAUP FT LU tBOLUPM, TUIT, oP FOiNUM. iBToOiTUK HPoQUMMUM JoP oHUPiTFtN ot TAU KiTi iPU PUHPUMUtTUK LZ NUtUPiC HPoQUKBPUM YtoWt iM iCNoPFTAOM. TAoMU iCNoPFTAOM iPU WPFTTUt Ft i HiPTFQBCiP toTiTFot, i HPoNPiOOFtN CitNBiNU, iM HPoNPiOM. MTBKUtTM WFCC CUiPt AoW To QiPPZ oBT TAUMU TiMYM itK AoW To TAFtY iLoBT QoOHBTiTFot Ft TUPOM oJ NUtUPiC HiTTUPtM, MBQA iM AFUPiPQAFQiC QoOHoMFTFot oP TAU BMU oJ FtTUPQAitNUiLCU QoOHotUtTM WFTA QotMFMTUtT FtTUPJiQUM'
>>> substitute(ciphertext, "D G X K", "i o t s")
'TAFM QoBPMU FtTPosBQUM TAU HUPMHUQTFVUM its OUTAosM oJ QoOHBTUP MQFUtQU. MZOLoCFQ FtJoPOiTFot FM PUHPUMUtTUs iM siTi, WAUTAUP FT LU tBOLUPM, TUIT, oP FOiNUM. iBToOiTUs HPoQUMMUM JoP oHUPiTFtN ot TAU siTi iPU PUHPUMUtTUs LZ NUtUPiC HPoQUsBPUM YtoWt iM iCNoPFTAOM. TAoMU iCNoPFTAOM iPU WPFTTUt Ft i HiPTFQBCiP toTiTFot, i HPoNPiOOFtN CitNBiNU, iM HPoNPiOM. MTBsUtTM WFCC CUiPt AoW To QiPPZ oBT TAUMU TiMYM its AoW To TAFtY iLoBT QoOHBTiTFot Ft TUPOM oJ NUtUPiC HiTTUPtM, MBQA iM AFUPiPQAFQiC QoOHoMFTFot oP TAU BMU oJ FtTUPQAitNUiLCU QoOHotUtTM WFTA QotMFMTUtT FtTUPJiQUM'
>>> substitute(ciphertext, "GJ GP", "of or")
'TAFM QoBrMU FXTroKBQUM TAU HUrMHUQTFVUM DXK OUTAoKM of QoOHBTUr MQFUXQU. MZOLoCFQ FXforODTFoX FM rUHrUMUXTUK DM KDTD, WAUTAUr FT LU XBOLUrM, TUIT, or FODNUM. DBToODTUK HroQUMMUM for oHUrDTFXN oX TAU KDTD DrU rUHrUMUXTUK LZ NUXUrDC HroQUKBrUM YXoWX DM DCNorFTAOM. TAoMU DCNorFTAOM DrU WrFTTUX FX D HDrTFQBCDr XoTDTFoX, D HroNrDOOFXN CDXNBDNU, DM HroNrDOM. MTBKUXTM WFCC CUDrX AoW To QDrrZ oBT TAUMU TDMYM DXK AoW To TAFXY DLoBT QoOHBTDTFoX FX TUrOM of NUXUrDC HDTTUrXM, MBQA DM AFUrDrQAFQDC QoOHoMFTFoX or TAU BMU of FXTUrQADXNUDLCU QoOHoXUXTM WFTA QoXMFMTUXT FXTUrfDQUM'
>>> substitute(ciphertext, "GJ GP D U", "of or a e")
'TAFM QoBrMe FXTroKBQeM TAe HerMHeQTFVeM aXK OeTAoKM of QoOHBTer MQFeXQe. MZOLoCFQ FXforOaTFoX FM reHreMeXTeK aM KaTa, WAeTAer FT Le XBOLerM, TeIT, or FOaNeM. aBToOaTeK HroQeMMeM for oHeraTFXN oX TAe KaTa are reHreMeXTeK LZ NeXeraC HroQeKBreM YXoWX aM aCNorFTAOM. TAoMe aCNorFTAOM are WrFTTeX FX a HarTFQBCar XoTaTFoX, a HroNraOOFXN CaXNBaNe, aM HroNraOM. MTBKeXTM WFCC CearX AoW To QarrZ oBT TAeMe TaMYM aXK AoW To TAFXY aLoBT QoOHBTaTFoX FX TerOM of NeXeraC HaTTerXM, MBQA aM AFerarQAFQaC QoOHoMFTFoX or TAe BMe of FXTerQAaXNeaLCe QoOHoXeXTM WFTA QoXMFMTeXT FXTerfaQeM'
>>> substitute(ciphertext, "GJ GP D U X F", "of or a e n i")
'TAiM QoBrMe inTroKBQeM TAe HerMHeQTiVeM anK OeTAoKM of QoOHBTer MQienQe. MZOLoCiQ inforOaTion iM reHreMenTeK aM KaTa, WAeTAer iT Le nBOLerM, TeIT, or iOaNeM. aBToOaTeK HroQeMMeM for oHeraTinN on TAe KaTa are reHreMenTeK LZ NeneraC HroQeKBreM YnoWn aM aCNoriTAOM. TAoMe aCNoriTAOM are WriTTen in a HarTiQBCar noTaTion, a HroNraOOinN CanNBaNe, aM HroNraOM. MTBKenTM WiCC Cearn AoW To QarrZ oBT TAeMe TaMYM anK AoW To TAinY aLoBT QoOHBTaTion in TerOM of NeneraC HaTTernM, MBQA aM AierarQAiQaC QoOHoMiTion or TAe BMe of inTerQAanNeaLCe QoOHonenTM WiTA QonMiMTenT inTerfaQeM'
>>> substitute(ciphertext, "GJ GP D U X F C", "of or a e n i l")
'TAiM QoBrMe inTroKBQeM TAe HerMHeQTiVeM anK OeTAoKM of QoOHBTer MQienQe. MZOLoliQ inforOaTion iM reHreMenTeK aM KaTa, WAeTAer iT Le nBOLerM, TeIT, or iOaNeM. aBToOaTeK HroQeMMeM for oHeraTinN on TAe KaTa are reHreMenTeK LZ Neneral HroQeKBreM YnoWn aM alNoriTAOM. TAoMe alNoriTAOM are WriTTen in a HarTiQBlar noTaTion, a HroNraOOinN lanNBaNe, aM HroNraOM. MTBKenTM Will learn AoW To QarrZ oBT TAeMe TaMYM anK AoW To TAinY aLoBT QoOHBTaTion in TerOM of Neneral HaTTernM, MBQA aM AierarQAiQal QoOHoMiTion or TAe BMe of inTerQAanNeaLle QoOHonenTM WiTA QonMiMTenT inTerfaQeM'
>>> substitute(ciphertext, "GJ GP D U X F C L", "of or a e n i l u")
'TAiM QoBrMe inTroKBQeM TAe HerMHeQTiVeM anK OeTAoKM of QoOHBTer MQienQe. MZOuoliQ inforOaTion iM reHreMenTeK aM KaTa, WAeTAer iT ue nBOuerM, TeIT, or iOaNeM. aBToOaTeK HroQeMMeM for oHeraTinN on TAe KaTa are reHreMenTeK uZ Neneral HroQeKBreM YnoWn aM alNoriTAOM. TAoMe alNoriTAOM are WriTTen in a HarTiQBlar noTaTion, a HroNraOOinN lanNBaNe, aM HroNraOM. MTBKenTM Will learn AoW To QarrZ oBT TAeMe TaMYM anK AoW To TAinY auoBT QoOHBTaTion in TerOM of Neneral HaTTernM, MBQA aM AierarQAiQal QoOHoMiTion or TAe BMe of inTerQAanNeaule QoOHonenTM WiTA QonMiMTenT inTerfaQeM'
>>> substitute(ciphertext, "GJ GP D U X F C L T", "of or a e n i l u t")
'tAiM QoBrMe introKBQeM tAe HerMHeQtiVeM anK OetAoKM of QoOHBter MQienQe. MZOuoliQ inforOation iM reHreMenteK aM Kata, WAetAer it ue nBOuerM, teIt, or iOaNeM. aBtoOateK HroQeMMeM for oHeratinN on tAe Kata are reHreMenteK uZ Neneral HroQeKBreM YnoWn aM alNoritAOM. tAoMe alNoritAOM are Written in a HartiQBlar notation, a HroNraOOinN lanNBaNe, aM HroNraOM. MtBKentM Will learn AoW to QarrZ oBt tAeMe taMYM anK AoW to tAinY auoBt QoOHBtation in terOM of Neneral HatternM, MBQA aM AierarQAiQal QoOHoMition or tAe BMe of interQAanNeaule QoOHonentM WitA QonMiMtent interfaQeM'
>>> 
>>> substitute(ciphertext, "GJ GP D U X F C L T A M N", "of or a e n i l u t h s g")
'this QoBrse introKBQes the HersHeQtiVes anK OethoKs of QoOHBter sQienQe. sZOuoliQ inforOation is reHresenteK as Kata, Whether it ue nBOuers, teIt, or iOages. aBtoOateK HroQesses for oHerating on the Kata are reHresenteK uZ general HroQeKBres YnoWn as algorithOs. those algorithOs are Written in a HartiQBlar notation, a HrograOOing langBage, as HrograOs. stBKents Will learn hoW to QarrZ oBt these tasYs anK hoW to thinY auoBt QoOHBtation in terOs of general Hatterns, sBQh as hierarQhiQal QoOHosition or the Bse of interQhangeaule QoOHonents With Qonsistent interfaQes'
>>> substitute(ciphertext, "GJ GP D U X F C L T A M N Y", "of or a e n i l u t h s g k")
'this QoBrse introKBQes the HersHeQtiVes anK OethoKs of QoOHBter sQienQe. sZOuoliQ inforOation is reHresenteK as Kata, Whether it ue nBOuers, teIt, or iOages. aBtoOateK HroQesses for oHerating on the Kata are reHresenteK uZ general HroQeKBres knoWn as algorithOs. those algorithOs are Written in a HartiQBlar notation, a HrograOOing langBage, as HrograOs. stBKents Will learn hoW to QarrZ oBt these tasks anK hoW to think auoBt QoOHBtation in terOs of general Hatterns, sBQh as hierarQhiQal QoOHosition or the Bse of interQhangeaule QoOHonents With Qonsistent interfaQes'
>>> substitute(ciphertext, "GJ GP D U X F C L T A M N Y K", "of or a e n i l u t h s g k d")
'this QoBrse introdBQes the HersHeQtiVes and Oethods of QoOHBter sQienQe. sZOuoliQ inforOation is reHresented as data, Whether it ue nBOuers, teIt, or iOages. aBtoOated HroQesses for oHerating on the data are reHresented uZ general HroQedBres knoWn as algorithOs. those algorithOs are Written in a HartiQBlar notation, a HrograOOing langBage, as HrograOs. stBdents Will learn hoW to QarrZ oBt these tasks and hoW to think auoBt QoOHBtation in terOs of general Hatterns, sBQh as hierarQhiQal QoOHosition or the Bse of interQhangeaule QoOHonents With Qonsistent interfaQes'
>>> substitute(ciphertext, "GJ GP D U X F C L T A M N Y K Q", "of or a e n i l u t h s g k d c")
'this coBrse introdBces the HersHectiVes and Oethods of coOHBter science. sZOuolic inforOation is reHresented as data, Whether it ue nBOuers, teIt, or iOages. aBtoOated Hrocesses for oHerating on the data are reHresented uZ general HrocedBres knoWn as algorithOs. those algorithOs are Written in a HarticBlar notation, a HrograOOing langBage, as HrograOs. stBdents Will learn hoW to carrZ oBt these tasks and hoW to think auoBt coOHBtation in terOs of general Hatterns, sBch as hierarchical coOHosition or the Bse of interchangeaule coOHonents With consistent interfaces'
]
>>> substitute(ciphertext, "GJ GP D U X F C L T A M N Y K Q B H", "of or a e n i l u t h s g k d c u p")
'Substitution is invalid'
>>> substitute(ciphertext, "GJ GP D U X F C T A M N Y K Q B H O", "of or a e n i l t h s g k d c u p m")
'this course introduces the perspectiVes and methods of computer science. sZmLolic information is represented as data, Whether it Le numLers, teIt, or images. automated processes for operating on the data are represented LZ general procedures knoWn as algorithms. those algorithms are Written in a particular notation, a programming language, as programs. students Will learn hoW to carrZ out these tasks and hoW to think aLout computation in terms of general patterns, such as hierarchical composition or the use of interchangeaLle components With consistent interfaces'
>>> substitute(ciphertext, "GJ GP D U X F C T A M N Y K Q B H O V", "of or a e n i l t h s g k d c u p m v")
'this course introduces the perspectives and methods of computer science. sZmLolic information is represented as data, Whether it Le numLers, teIt, or images. automated processes for operating on the data are represented LZ general procedures knoWn as algorithms. those algorithms are Written in a particular notation, a programming language, as programs. students Will learn hoW to carrZ out these tasks and hoW to think aLout computation in terms of general patterns, such as hierarchical composition or the use of interchangeaLle components With consistent interfaces'
>>> substitute(ciphertext, "GJ GP D U X F C T A M N Y K Q B H O V L", "of or a e n i l t h s g k d c u p m v b")
'this course introduces the perspectives and methods of computer science. sZmbolic information is represented as data, Whether it be numbers, teIt, or images. automated processes for operating on the data are represented bZ general procedures knoWn as algorithms. those algorithms are Written in a particular notation, a programming language, as programs. students Will learn hoW to carrZ out these tasks and hoW to think about computation in terms of general patterns, such as hierarchical composition or the use of interchangeable components With consistent interfaces'
>>> substitute(ciphertext, "GJ GP D U X F C T A M N Y K Q B H O V L Z", "of or a e n i l t h s g k d c u p m v b y")
'this course introduces the perspectives and methods of computer science. symbolic information is represented as data, Whether it be numbers, teIt, or images. automated processes for operating on the data are represented by general procedures knoWn as algorithms. those algorithms are Written in a particular notation, a programming language, as programs. students Will learn hoW to carry out these tasks and hoW to think about computation in terms of general patterns, such as hierarchical composition or the use of interchangeable components With consistent interfaces'
>>> substitute(ciphertext, "GJ GP D U X F C T A M N Y K Q B H O V L Z I W", "of or a e n i l t h s g k d c u p m v b y x w")
'this course introduces the perspectives and methods of computer science. symbolic information is represented as data, whether it be numbers, text, or images. automated processes for operating on the data are represented by general procedures known as algorithms. those algorithms are written in a particular notation, a programming language, as programs. students will learn how to carry out these tasks and how to think about computation in terms of general patterns, such as hierarchical composition or the use of interchangeable components with consistent interfaces'
>>> 