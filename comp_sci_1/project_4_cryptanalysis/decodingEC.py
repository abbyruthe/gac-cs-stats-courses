Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /Users/abbyestep/Downloads/extraCredit.py ==============
>>> ciphertext = "CZCXYGIJJDANLYPUEGCXLUNAXCSDFULNIAEUAOLXUONLNIAEHPNGPCUGPJCJVCXNECRTCGLCOLIUVNOCVYUAODTPIFOUGIFFCSCGIJJDANLYCZCAJIXCLPUAILPCXEOCTCAOEDTIALPCNALCSXNLYECFBONEGNTFNACUAOJULDXCQDOSJCALIBCUGPIBNLEJCJVCXEIAFYNAEDGPUGIJJDANLYIBXCETIAENVFCGNLNMCAEGUAUAULJIETPCXCVCCELUVFNEPCOHPNGPHNFFEDTTIXLFNVCXUFUXLECODGULNIAUEUGIJJDANLYIBQDELNGCBUNLPUAOFCUXANASLPCGIFFCSCELXNZCELIJCCLLPCPNSPCELGFUNJEIBLXDLPUAOGIJJNLJCAL"
>>> print_frequencies(ciphertext)
A:29
B:7
C:49
D:14
E:25
F:17
G:20
H:3
I:25
J:21
K:0
L:36
M:1
N:33
O:15
P:20
Q:2
R:1
S:7
T:9
U:28
V:8
W:0
X:18
Y:8
Z:3
>>> substitute(ciphertext, "C Z L X A P T Y", "e v t r n h w y")
'everyGIJJDnNtyhUEGertUNnreSDFUtNInEUnOtrUONtNInEHhNGheUGhJeJVerNEeRweGteOtIUVNOeVyUnODwhIFOUGIFFeSeGIJJDnNtyevenJIrethUnItherEOewenOEDwIntheNnteSrNtyEeFBONEGNwFNneUnOJUtDreQDOSJentIBeUGhIBNtEJeJVerEInFyNnEDGhUGIJJDnNtyIBreEwInENVFeGNtNMenEGUnUnUtJIEwhereVeeEtUVFNEheOHhNGhHNFFEDwwIrtFNVerUFUrtEeODGUtNInUEUGIJJDnNtyIBQDEtNGeBUNthUnOFeUrnNnStheGIFFeSeEtrNveEtIJeetthehNSheEtGFUNJEIBtrDthUnOGIJJNtJent'
>>> substitute(ciphertext, "C Z L X A P T Y I", "e v t r n h w y o")
'everyGoJJDnNtyhUEGertUNnreSDFUtNonEUnOtrUONtNonEHhNGheUGhJeJVerNEeRweGteOtoUVNOeVyUnODwhoFOUGoFFeSeGoJJDnNtyevenJorethUnotherEOewenOEDwontheNnteSrNtyEeFBONEGNwFNneUnOJUtDreQDOSJentoBeUGhoBNtEJeJVerEonFyNnEDGhUGoJJDnNtyoBreEwonENVFeGNtNMenEGUnUnUtJoEwhereVeeEtUVFNEheOHhNGhHNFFEDwwortFNVerUFUrtEeODGUtNonUEUGoJJDnNtyoBQDEtNGeBUNthUnOFeUrnNnStheGoFFeSeEtrNveEtoJeetthehNSheEtGFUNJEoBtrDthUnOGoJJNtJent'
>>> substitute(ciphertext, "C Z L X A P T Y I N", "e v t r n h w y o a")
'everyGoJJDnatyhUEGertUanreSDFUtaonEUnOtrUOataonEHhaGheUGhJeJVeraEeRweGteOtoUVaOeVyUnODwhoFOUGoFFeSeGoJJDnatyevenJorethUnotherEOewenOEDwontheanteSratyEeFBOaEGawFaneUnOJUtDreQDOSJentoBeUGhoBatEJeJVerEonFyanEDGhUGoJJDnatyoBreEwonEaVFeGataMenEGUnUnUtJoEwhereVeeEtUVFaEheOHhaGhHaFFEDwwortFaVerUFUrtEeODGUtaonUEUGoJJDnatyoBQDEtaGeBUathUnOFeUrnanStheGoFFeSeEtraveEtoJeetthehaSheEtGFUaJEoBtrDthUnOGoJJatJent'
>>> substitute(ciphertext, "C Z L X A P T Y I N U", "e v t r n h w y o a u")
'everyGoJJDnatyhuEGertuanreSDFutaonEunOtruOataonEHhaGheuGhJeJVeraEeRweGteOtouVaOeVyunODwhoFOuGoFFeSeGoJJDnatyevenJorethunotherEOewenOEDwontheanteSratyEeFBOaEGawFaneunOJutDreQDOSJentoBeuGhoBatEJeJVerEonFyanEDGhuGoJJDnatyoBreEwonEaVFeGataMenEGununutJoEwhereVeeEtuVFaEheOHhaGhHaFFEDwwortFaVeruFurtEeODGutaonuEuGoJJDnatyoBQDEtaGeBuathunOFeurnanStheGoFFeSeEtraveEtoJeetthehaSheEtGFuaJEoBtrDthunOGoJJatJent'
>>> substitute(ciphertext, "C Z L X A P T Y I N U E", "e v t r n h w y o a u l")
'everyGoJJDnatyhulGertuanreSDFutaonlunOtruOataonlHhaGheuGhJeJVeraleRweGteOtouVaOeVyunODwhoFOuGoFFeSeGoJJDnatyevenJorethunotherlOewenOlDwontheanteSratyleFBOalGawFaneunOJutDreQDOSJentoBeuGhoBatlJeJVerlonFyanlDGhuGoJJDnatyoBrelwonlaVFeGataMenlGununutJolwhereVeeltuVFalheOHhaGhHaFFlDwwortFaVeruFurtleODGutaonuluGoJJDnatyoBQDltaGeBuathunOFeurnanStheGoFFeSeltraveltoJeetthehaSheltGFuaJloBtrDthunOGoJJatJent'
>>> substitute(ciphertext, "C Z L X A P T Y I N E", "e v t r n h w y o a l")
'everyGoJJDnatyhUlGertUanreSDFUtaonlUnOtrUOataonlHhaGheUGhJeJVeraleRweGteOtoUVaOeVyUnODwhoFOUGoFFeSeGoJJDnatyevenJorethUnotherlOewenOlDwontheanteSratyleFBOalGawFaneUnOJUtDreQDOSJentoBeUGhoBatlJeJVerlonFyanlDGhUGoJJDnatyoBrelwonlaVFeGataMenlGUnUnUtJolwhereVeeltUVFalheOHhaGhHaFFlDwwortFaVerUFUrtleODGUtaonUlUGoJJDnatyoBQDltaGeBUathUnOFeUrnanStheGoFFeSeltraveltoJeetthehaSheltGFUaJloBtrDthUnOGoJJatJent'
>>> substitute(ciphertext, "C Z L X A P T Y I U E", "e v t r n h w y o a l")
'everyGoJJDnNtyhalGertaNnreSDFatNonlanOtraONtNonlHhNGheaGhJeJVerNleRweGteOtoaVNOeVyanODwhoFOaGoFFeSeGoJJDnNtyevenJorethanotherlOewenOlDwontheNnteSrNtyleFBONlGNwFNneanOJatDreQDOSJentoBeaGhoBNtlJeJVerlonFyNnlDGhaGoJJDnNtyoBrelwonlNVFeGNtNMenlGananatJolwhereVeeltaVFNlheOHhNGhHNFFlDwwortFNVeraFartleODGatNonalaGoJJDnNtyoBQDltNGeBaNthanOFearnNnStheGoFFeSeltrNveltoJeetthehNSheltGFaNJloBtrDthanOGoJJNtJent'
>>> substitute(ciphertext, "C Z L X A P T Y I U E J", "e v t r n h w y o a l m")
'everyGommDnNtyhalGertaNnreSDFatNonlanOtraONtNonlHhNGheaGhmemVerNleRweGteOtoaVNOeVyanODwhoFOaGoFFeSeGommDnNtyevenmorethanotherlOewenOlDwontheNnteSrNtyleFBONlGNwFNneanOmatDreQDOSmentoBeaGhoBNtlmemVerlonFyNnlDGhaGommDnNtyoBrelwonlNVFeGNtNMenlGananatmolwhereVeeltaVFNlheOHhNGhHNFFlDwwortFNVeraFartleODGatNonalaGommDnNtyoBQDltNGeBaNthanOFearnNnStheGoFFeSeltrNveltomeetthehNSheltGFaNmloBtrDthanOGommNtment'
>>> substitute(ciphertext, "C Z L X A P T Y I U E J N", "e v t r n h w y o a l m i")
'everyGommDnityhalGertainreSDFationlanOtraOitionlHhiGheaGhmemVerileRweGteOtoaViOeVyanODwhoFOaGoFFeSeGommDnityevenmorethanotherlOewenOlDwontheinteSrityleFBOilGiwFineanOmatDreQDOSmentoBeaGhoBitlmemVerlonFyinlDGhaGommDnityoBrelwonliVFeGitiMenlGananatmolwhereVeeltaVFilheOHhiGhHiFFlDwwortFiVeraFartleODGationalaGommDnityoBQDltiGeBaithanOFearninStheGoFFeSeltriveltomeetthehiSheltGFaimloBtrDthanOGommitment'
>>> substitute(ciphertext, "C Z L X A P T Y I U E J N G", "e v t r n h w y o a l m i c")
'everycommDnityhalcertainreSDFationlanOtraOitionlHhicheachmemVerileRwecteOtoaViOeVyanODwhoFOacoFFeSecommDnityevenmorethanotherlOewenOlDwontheinteSrityleFBOilciwFineanOmatDreQDOSmentoBeachoBitlmemVerlonFyinlDchacommDnityoBrelwonliVFecitiMenlcananatmolwhereVeeltaVFilheOHhichHiFFlDwwortFiVeraFartleODcationalacommDnityoBQDlticeBaithanOFearninSthecoFFeSeltriveltomeetthehiSheltcFaimloBtrDthanOcommitment'
>>> substitute(ciphertext, "C Z L X A P T Y I U E J N G O D", "e v t r n h w y o a l m i c d u")
'everycommunityhalcertainreSuFationlandtraditionlHhicheachmemVerileRwectedtoaVideVyanduwhoFdacoFFeSecommunityevenmorethanotherldewendluwontheinteSrityleFBdilciwFineandmatureQudSmentoBeachoBitlmemVerlonFyinluchacommunityoBrelwonliVFecitiMenlcananatmolwhereVeeltaVFilhedHhichHiFFluwwortFiVeraFartleducationalacommunityoBQulticeBaithandFearninSthecoFFeSeltriveltomeetthehiSheltcFaimloBtruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P T Y I U E J N G O D E", "e v t r n h w y o a l m i c d u s")
'Substitution is invalid'
>>> substitute(ciphertext, "C Z L X A P T Y I U J N G O D E", "e v t r n h w y o a m i c d u s")
'everycommunityhascertainreSuFationsandtraditionsHhicheachmemVeriseRwectedtoaVideVyanduwhoFdacoFFeSecommunityevenmorethanothersdewendsuwontheinteSrityseFBdisciwFineandmatureQudSmentoBeachoBitsmemVersonFyinsuchacommunityoBreswonsiVFecitiMenscananatmoswhereVeestaVFishedHhichHiFFsuwwortFiVeraFartseducationasacommunityoBQusticeBaithandFearninSthecoFFeSestrivestomeetthehiShestcFaimsoBtruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P T Y I U J N G O D E", "e v t r n h w y o a m i c d u s")
'everycommunityhascertainreSuFationsandtraditionsHhicheachmemVeriseRwectedtoaVideVyanduwhoFdacoFFeSecommunityevenmorethanothersdewendsuwontheinteSrityseFBdisciwFineandmatureQudSmentoBeachoBitsmemVersonFyinsuchacommunityoBreswonsiVFecitiMenscananatmoswhereVeestaVFishedHhichHiFFsuwwortFiVeraFartseducationasacommunityoBQusticeBaithandFearninSthecoFFeSestrivestomeetthehiShestcFaimsoBtruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H", "e v t r n h y o a m i c d u s w")
'everycommunityhascertainreSuFationsandtraditionswhicheachmemVeriseRTectedtoaVideVyanduThoFdacoFFeSecommunityevenmorethanothersdeTendsuTontheinteSrityseFBdisciTFineandmatureQudSmentoBeachoBitsmemVersonFyinsuchacommunityoBresTonsiVFecitiMenscananatmosThereVeestaVFishedwhichwiFFsuTTortFiVeraFartseducationasacommunityoBQusticeBaithandFearninSthecoFFeSestrivestomeetthehiShestcFaimsoBtruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H V D Q B F", "e v t r n h y o a m i c d u s w b n j f l")
'everycommunityhascertainreSulationsandtraditionswhicheachmemberiseRTectedtoabidebyanduTholdacolleSecommunityevenmorethanothersdeTendsuTontheinteSrityselfdisciTlineandmaturejudSmentofeachofitsmembersonlyinsuchacommunityofresTonsiblecitiMenscananatmosTherebeestablishedwhichwillsuTTortliberalartseducationasacommunityofjusticefaithandlearninSthecolleSestrivestomeetthehiShestclaimsoftruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H V D Q B F S", "e v t r n h y o a m i c d u s w b n j f l j")
'Substitution is invalid'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H V D Q B F S", "e v t r n h y o a m i c d u s w b n j f l g")
'everycommunityhascertainregulationsandtraditionswhicheachmemberiseRTectedtoabidebyanduTholdacollegecommunityevenmorethanothersdeTendsuTontheintegrityselfdisciTlineandmaturejudgmentofeachofitsmembersonlyinsuchacommunityofresTonsiblecitiMenscananatmosTherebeestablishedwhichwillsuTTortliberalartseducationasacommunityofjusticefaithandlearningthecollegestrivestomeetthehighestclaimsoftruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H V D Q B F S R T", "e v t r n h y o a m i c d u s w b n j f l g x p")
'everycommunityhascertainregulationsandtraditionswhicheachmemberisexpectedtoabidebyandupholdacollegecommunityevenmorethanothersdependsupontheintegrityselfdisciplineandmaturejudgmentofeachofitsmembersonlyinsuchacommunityofresponsiblecitiMenscananatmospherebeestablishedwhichwillsupportliberalartseducationasacommunityofjusticefaithandlearningthecollegestrivestomeetthehighestclaimsoftruthandcommitment'
>>> substitute(ciphertext, "C Z L X A P Y I U J N G O D E H V D Q B F S R T M", "e v t r n h y o a m i c d u s w b n j f l g x p z")
'everycommunityhascertainregulationsandtraditionswhicheachmemberisexpectedtoabidebyandupholdacollegecommunityevenmorethanothersdependsupontheintegrityselfdisciplineandmaturejudgmentofeachofitsmembersonlyinsuchacommunityofresponsiblecitizenscananatmospherebeestablishedwhichwillsupportliberalartseducationasacommunityofjusticefaithandlearningthecollegestrivestomeetthehighestclaimsoftruthandcommitment'
>>> 