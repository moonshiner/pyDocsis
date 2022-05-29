from pydocsis.cmConfig import CmConfig
from pydocsis.configFile import ConfigFile


def test_generate_string_from_file():
    file = "DCTR3.cfg"
    this_config = CmConfig()
    this_config.generate_string_from_file(file)
    assert this_config.tlv_string == "2b080803002040a101000301012b0d0803ffffff09060404000000051d0101113601040000000a02040000000a03040000025804040000000105040000000106040000025807040000003c08040000000109040000000412010321fe30820311308201f9a00302010202101d573e6f32c65aa07534bc0f8d04abd2300d06092a864886f70d0101050500308197310b300906035504061302555331393037060355040a133044617461204f766572204361626c65205365727669636520496e746572666163652053706563696669636174696f6e7331153013060355040b130c4361626c65204d6f64656d73313630340603550403132d444f43534953204361626c65204d6f64656d20526f6f7420436572746966696361746520417574686f72697479301e170d3033303231343030303030305a170d3133303231333233353935395a3059310b30090603550406130255533111300f06035521fe040a13083830303030303033310f300d060355040b1306444f43534953312630240603550403131d436f646520566572696669636174696f6e20436572746966696361746530819f300d06092a864886f70d010101050003818d0030818902818100df4187864c8ab6249f20b3cd1792604de5886f78f8d754129a2d6e881fd2eaf1657d45fb0387bd68b7b4b252d2921130d7b26e1254dd400568721077fd6c044d2fcf00e844e1b1b1bf5ba08dfe61d035abf0c53856c470005eee23e431c6aa0255e23b1e1fbc8d222ef09216817e33dd487e00aeb1578f29d17a8bd3e5c06dcb0203010001a31a301830160603551d250101ff040c300a06082b060121fe0505070303300d06092a864886f70d010105050003820101000d387e45f458291d36bb3c4b953a956361c86d03ca6f8fa9d2df3669c9f3cde8d9dafb3352ddf61f73fce3405394714937449a9f7f16ff4c559b02a70a6ed2b2740222f5924833ba08e104288c30b6305d153170bdf760d6c876875aff42b7634a0fc958214918737e826973437468382987556b72285eeeb4513a3e740f55adc5afbc07981807bc0608a40cfc4622ba3d190793fff99a1c4ef2aeb8af73dc0ceb0e1a1f1cd4ea46156baf6062ae07ffabd3ebfd4885eac2764e23c8dd587fea4cef77f0c623b5bfb615af5f540435868adcdbec9c223bacb9dd2c8fe01b0df9678de9688e211beb096fc2e034bc40de985f92d89fedc4af493d817db6784b3d97cd0b133011060c2b0601020145010604010b040201060b133011060c2b06010201450106040103040201020b163014060c2b06010201450106040109044004440100000b133011060c2b06010201450106040102040201040b133011060c2b0601020145010604010e040201190b133011060c2b0601020145010604010f040201190b133011060c2b06010201450106040104040201020b163014060c2b0601020145010604010a044004ffff80000b133011060c2b06010201450106040105040201020b133011060c2b0601020145010604010b050201060b133011060c2b06010201450106040103050201020b163014060c2b06010201450106040109054004440600000b133011060c2b06010201450106040102050201040b133011060c2b0601020145010604010e050201190b133011060c2b0601020145010604010f050201190b133011060c2b06010201450106040104050201020b163014060c2b0601020145010604010a054004fffe00000b133011060c2b06010201450106040105050201020b133011060c2b0601020145010604010b060201060b133011060c2b06010201450106040103060201020b163014060c2b0601020145010604010906400446a82f000b133011060c2b06010201450106040102060201040b133011060c2b0601020145010604010e060201190b133011060c2b0601020145010604010f060201190b133011060c2b06010201450106040104060201020b163014060c2b0601020145010604010a064004ffffff000b133011060c2b06010201450106040105060201020b133011060c2b0601020145010604010b070201060b133011060c2b06010201450106040103070201020b163014060c2b06010201450106040109074004446378000b133011060c2b06010201450106040102070201040b133011060c2b0601020145010604010e070201190b133011060c2b0601020145010604010f070201190b133011060c2b06010201450106040104070201020b163014060c2b0601020145010604010a074004fffffc000b133011060c2b06010201450106040105070201020b133011060c2b0601020145010604010b090201060b133011060c2b06010201450106040103090201010b133011060c2b06010201450106040102090201040b133011060c2b0601020145010604010e090201190b133011060c2b0601020145010604010f090201190b133011060c2b06010201450106040104090201020b133011060c2b06010201450106040105090201030b133011060c2b0601020145010604010b0b0201110b133011060c2b060102014501060401030b0201010b133011060c2b060102014501060401020b0201040b143012060c2b0601020145010604010e0b020200870b143012060c2b0601020145010604010f0b0202008b0b133011060c2b060102014501060401040b0201000b133011060c2b060102014501060401050b0201030b133011060c2b0601020145010604010b150201060b133011060c2b06010201450106040103150201010b133011060c2b06010201450106040102150201040b143012060c2b0601020145010604010e15020200870b143012060c2b0601020145010604010f150202008b0b133011060c2b06010201450106040104150201000b133011060c2b06010201450106040105150201030b133011060c2b0601020145010604010b1e0201060b133011060c2b060102014501060401031e0201010b133011060c2b060102014501060401021e0201040b133011060c2b0601020145010604010e1e0201500b133011060c2b0601020145010604010f1e0201500b133011060c2b060102014501060401041e0201020b133011060c2b060102014501060401051e0201010b133011060c2b0601020145010604010b280201060b133011060c2b06010201450106040103280201010b133011060c2b06010201450106040102280201040b143012060c2b0601020145010604010e28020201bd0b143012060c2b0601020145010604010f28020201bd0b133011060c2b06010201450106040104280201000b133011060c2b06010201450106040105280201030b133011060c2b0601020145010604010b5a0201110b133011060c2b060102014501060401035a0201010b133011060c2b060102014501060401025a0201040b143012060c2b0601020145010604010e5a0202076c0b143012060c2b0601020145010604010f5a0202076c0b133011060c2b060102014501060401045a0201020b133011060c2b060102014501060401055a0201030b133011060c2b0601020145010604010b640201060b133011060c2b06010201450106040103640201010b133011060c2b06010201450106040102640201040b143012060c2b0601020145010604010e64020205990b143012060c2b0601020145010604010f64020205990b133011060c2b06010201450106040104640201020b133011060c2b06010201450106040105640201010b133011060c2b0601020145010604010b650201110b133011060c2b06010201450106040103650201010b133011060c2b06010201450106040102650201040b143012060c2b0601020145010604010e650202059a0b143012060c2b0601020145010604010f650202059a0b133011060c2b06010201450106040104650201000b133011060c2b06010201450106040105650201010b153013060b2b060102014501020102014004ac1000000b153013060b2b060102014501020103014004fff000000b21301f060b2b0601020145010201040104107969576a6f61626379644c6f675641730b123010060b2b060102014501020105010201030b123010060b2b060102014501020106010401400b123010060b2b060102014501020107010201040b153013060b2b060102014501020102024004ac1000000b153013060b2b060102014501020103024004fff000000b21301f060b2b060102014501020104020410626f524b616c69636e6f7769445641740b123010060b2b060102014501020105020201020b123010060b2b060102014501020106020401400b123010060b2b060102014501020107020201040b153013060b2b060102014501020102034004647e00000b153013060b2b060102014501020103034004fff000000b21301f060b2b0601020145010201040304107969576a6f61626379644c6f675641730b123010060b2b060102014501020105030201030b123010060b2b060102014501020106030401400b123010060b2b060102014501020107030201040b153013060b2b060102014501020102044004647e00000b153013060b2b060102014501020103044004fff000000b21301f060b2b060102014501020104040410626f524b616c69636e6f7769445641740b123010060b2b060102014501020105040201020b123010060b2b060102014501020106040401400b123010060b2b060102014501020107040201040b163014060f2b06010401a01301030101020319000201010b133011060c2b060104018b154d01042c000201000b163014060f2b06010401a013010301010203120042010c0b153013060e2b06010401a013010301010101000201030b193017060f2b06010401a0130103010102030f000404020000000b123010060b2b06010401a0130a0118000201030b133011060c2b06010401890e01814802240401160b163014060d2b06010401890e011303050800020300a8c00b143012060d2b06010401890e0113030507000201010b233021060d2b060104018b154e01876904000410272a73bdb4945eddc88f6a66198c10560b123010060b2b060104018b154e0108000201000b1c301a060e2b06010401a013010304010203000408efe7e7480de641660b1d301b060f2b06010401a01301030101020305050408efe7e7480de641660b173015060d2b0601040190220501010101004004647ef94b0b233021060d2b0601040190220501010103000410626f524b616c69636e6f7769445641740b383036060c2b060104019022040201020004265c5c3130302e3132362e3234392e373520746c6764766f69702e6c696e63656e736566696c650b363034060c2b060104019022040201030004245c5c3130302e3132362e3234392e373520203c4d41433e2e656e64706f696e7466696c650b153013060e2b060104a23d02020201010104000201010b153013060e2b060104a23d02020201010404000201010b183016060e2b060104a23d02020201010402000404726f6f740b1a3018060e2b060104a23d02020201010403000406723066346a790b133011060c2b06010201450106040102010201040b133011060c2b06010201450106040103010201010b133011060c2b06010201450106040104010201020b133011060c2b06010201450106040105010201030b163014060c2b06010201450106040109014004647ef94b0b163014060c2b0601020145010604010a014004ffffffff0b143012060c2b0601020145010604010b01020201000b133011060c2b0601020145010604010e010201000b143012060c2b0601020145010604010f01020200a00b133011060c2b06010201450106040102020201040b133011060c2b06010201450106040103020201010b133011060c2b06010201450106040104020201020b133011060c2b06010201450106040105020201030b163014060c2b06010201450106040109024004000000000b163014060c2b0601020145010604010a024004000000000b143012060c2b0601020145010604010b02020201000b143012060c2b0601020145010604010e02020200a30b153013060c2b0601020145010604010f02020300ffff0b153013060b2b0601020145010201020f4004647ef94b0b153013060b2b0601020145010201030f4004ffffffff0b21301f060b2b0601020145010201040f0410626f524b616c69636e6f7769445641740b123010060b2b0601020145010201050f0201050b123010060b2b0601020145010201060f0401400b123010060b2b0601020145010201070f02010418230102069a060107070100080400040f10090400001f400a04000000000e021f400f0102191601021644060107070100080400040f100a040000000006106c2c2b5e3ebc5c927d638e125e6f45fa0710872540e0f06b0ae7a0d2abda0bc9e208ff0000"
    # assert False


def test_parse():
    file = "DCTR3.cfg"
    this_config = CmConfig()
    this_config.generate_string_from_file(file)
    this_config.parse()
    assert len(this_config.tlvs) == 177


def test_encode():
    file = "DCTR3.cfg"
    this_config = CmConfig()
    this_config.generate_string_from_file(file)
    this_config.parse()
    file += ".new"
    this_config.configFilePath = file
    this_config.encode()
    this_config.generate_string_from_file(file)
    assert this_config.tlv_string == "2b080803002040a101000301012b0d0803ffffff09060404000000051d0101113601040000000a02040000000a03040000025804040000000105040000000106040000025807040000003c08040000000109040000000412010321fe30820311308201f9a00302010202101d573e6f32c65aa07534bc0f8d04abd2300d06092a864886f70d0101050500308197310b300906035504061302555331393037060355040a133044617461204f766572204361626c65205365727669636520496e746572666163652053706563696669636174696f6e7331153013060355040b130c4361626c65204d6f64656d73313630340603550403132d444f43534953204361626c65204d6f64656d20526f6f7420436572746966696361746520417574686f72697479301e170d3033303231343030303030305a170d3133303231333233353935395a3059310b30090603550406130255533111300f06035521fe040a13083830303030303033310f300d060355040b1306444f43534953312630240603550403131d436f646520566572696669636174696f6e20436572746966696361746530819f300d06092a864886f70d010101050003818d0030818902818100df4187864c8ab6249f20b3cd1792604de5886f78f8d754129a2d6e881fd2eaf1657d45fb0387bd68b7b4b252d2921130d7b26e1254dd400568721077fd6c044d2fcf00e844e1b1b1bf5ba08dfe61d035abf0c53856c470005eee23e431c6aa0255e23b1e1fbc8d222ef09216817e33dd487e00aeb1578f29d17a8bd3e5c06dcb0203010001a31a301830160603551d250101ff040c300a06082b060121fe0505070303300d06092a864886f70d010105050003820101000d387e45f458291d36bb3c4b953a956361c86d03ca6f8fa9d2df3669c9f3cde8d9dafb3352ddf61f73fce3405394714937449a9f7f16ff4c559b02a70a6ed2b2740222f5924833ba08e104288c30b6305d153170bdf760d6c876875aff42b7634a0fc958214918737e826973437468382987556b72285eeeb4513a3e740f55adc5afbc07981807bc0608a40cfc4622ba3d190793fff99a1c4ef2aeb8af73dc0ceb0e1a1f1cd4ea46156baf6062ae07ffabd3ebfd4885eac2764e23c8dd587fea4cef77f0c623b5bfb615af5f540435868adcdbec9c223bacb9dd2c8fe01b0df9678de9688e211beb096fc2e034bc40de985f92d89fedc4af493d817db6784b3d97cd0b133011060c2b0601020145010604010b040201060b133011060c2b06010201450106040103040201020b163014060c2b06010201450106040109044004440100000b133011060c2b06010201450106040102040201040b133011060c2b0601020145010604010e040201190b133011060c2b0601020145010604010f040201190b133011060c2b06010201450106040104040201020b163014060c2b0601020145010604010a044004ffff80000b133011060c2b06010201450106040105040201020b133011060c2b0601020145010604010b050201060b133011060c2b06010201450106040103050201020b163014060c2b06010201450106040109054004440600000b133011060c2b06010201450106040102050201040b133011060c2b0601020145010604010e050201190b133011060c2b0601020145010604010f050201190b133011060c2b06010201450106040104050201020b163014060c2b0601020145010604010a054004fffe00000b133011060c2b06010201450106040105050201020b133011060c2b0601020145010604010b060201060b133011060c2b06010201450106040103060201020b163014060c2b0601020145010604010906400446a82f000b133011060c2b06010201450106040102060201040b133011060c2b0601020145010604010e060201190b133011060c2b0601020145010604010f060201190b133011060c2b06010201450106040104060201020b163014060c2b0601020145010604010a064004ffffff000b133011060c2b06010201450106040105060201020b133011060c2b0601020145010604010b070201060b133011060c2b06010201450106040103070201020b163014060c2b06010201450106040109074004446378000b133011060c2b06010201450106040102070201040b133011060c2b0601020145010604010e070201190b133011060c2b0601020145010604010f070201190b133011060c2b06010201450106040104070201020b163014060c2b0601020145010604010a074004fffffc000b133011060c2b06010201450106040105070201020b133011060c2b0601020145010604010b090201060b133011060c2b06010201450106040103090201010b133011060c2b06010201450106040102090201040b133011060c2b0601020145010604010e090201190b133011060c2b0601020145010604010f090201190b133011060c2b06010201450106040104090201020b133011060c2b06010201450106040105090201030b133011060c2b0601020145010604010b0b0201110b133011060c2b060102014501060401030b0201010b133011060c2b060102014501060401020b0201040b143012060c2b0601020145010604010e0b020200870b143012060c2b0601020145010604010f0b0202008b0b133011060c2b060102014501060401040b0201000b133011060c2b060102014501060401050b0201030b133011060c2b0601020145010604010b150201060b133011060c2b06010201450106040103150201010b133011060c2b06010201450106040102150201040b143012060c2b0601020145010604010e15020200870b143012060c2b0601020145010604010f150202008b0b133011060c2b06010201450106040104150201000b133011060c2b06010201450106040105150201030b133011060c2b0601020145010604010b1e0201060b133011060c2b060102014501060401031e0201010b133011060c2b060102014501060401021e0201040b133011060c2b0601020145010604010e1e0201500b133011060c2b0601020145010604010f1e0201500b133011060c2b060102014501060401041e0201020b133011060c2b060102014501060401051e0201010b133011060c2b0601020145010604010b280201060b133011060c2b06010201450106040103280201010b133011060c2b06010201450106040102280201040b143012060c2b0601020145010604010e28020201bd0b143012060c2b0601020145010604010f28020201bd0b133011060c2b06010201450106040104280201000b133011060c2b06010201450106040105280201030b133011060c2b0601020145010604010b5a0201110b133011060c2b060102014501060401035a0201010b133011060c2b060102014501060401025a0201040b143012060c2b0601020145010604010e5a0202076c0b143012060c2b0601020145010604010f5a0202076c0b133011060c2b060102014501060401045a0201020b133011060c2b060102014501060401055a0201030b133011060c2b0601020145010604010b640201060b133011060c2b06010201450106040103640201010b133011060c2b06010201450106040102640201040b143012060c2b0601020145010604010e64020205990b143012060c2b0601020145010604010f64020205990b133011060c2b06010201450106040104640201020b133011060c2b06010201450106040105640201010b133011060c2b0601020145010604010b650201110b133011060c2b06010201450106040103650201010b133011060c2b06010201450106040102650201040b143012060c2b0601020145010604010e650202059a0b143012060c2b0601020145010604010f650202059a0b133011060c2b06010201450106040104650201000b133011060c2b06010201450106040105650201010b153013060b2b060102014501020102014004ac1000000b153013060b2b060102014501020103014004fff000000b21301f060b2b0601020145010201040104107969576a6f61626379644c6f675641730b123010060b2b060102014501020105010201030b123010060b2b060102014501020106010401400b123010060b2b060102014501020107010201040b153013060b2b060102014501020102024004ac1000000b153013060b2b060102014501020103024004fff000000b21301f060b2b060102014501020104020410626f524b616c69636e6f7769445641740b123010060b2b060102014501020105020201020b123010060b2b060102014501020106020401400b123010060b2b060102014501020107020201040b153013060b2b060102014501020102034004647e00000b153013060b2b060102014501020103034004fff000000b21301f060b2b0601020145010201040304107969576a6f61626379644c6f675641730b123010060b2b060102014501020105030201030b123010060b2b060102014501020106030401400b123010060b2b060102014501020107030201040b153013060b2b060102014501020102044004647e00000b153013060b2b060102014501020103044004fff000000b21301f060b2b060102014501020104040410626f524b616c69636e6f7769445641740b123010060b2b060102014501020105040201020b123010060b2b060102014501020106040401400b123010060b2b060102014501020107040201040b163014060f2b06010401a01301030101020319000201010b133011060c2b060104018b154d01042c000201000b163014060f2b06010401a013010301010203120042010c0b153013060e2b06010401a013010301010101000201030b193017060f2b06010401a0130103010102030f000404020000000b123010060b2b06010401a0130a0118000201030b133011060c2b06010401890e01814802240401160b163014060d2b06010401890e011303050800020300a8c00b143012060d2b06010401890e0113030507000201010b233021060d2b060104018b154e01876904000410272a73bdb4945eddc88f6a66198c10560b123010060b2b060104018b154e0108000201000b1c301a060e2b06010401a013010304010203000408efe7e7480de641660b1d301b060f2b06010401a01301030101020305050408efe7e7480de641660b173015060d2b0601040190220501010101004004647ef94b0b233021060d2b0601040190220501010103000410626f524b616c69636e6f7769445641740b383036060c2b060104019022040201020004265c5c3130302e3132362e3234392e373520746c6764766f69702e6c696e63656e736566696c650b363034060c2b060104019022040201030004245c5c3130302e3132362e3234392e373520203c4d41433e2e656e64706f696e7466696c650b153013060e2b060104a23d02020201010104000201010b153013060e2b060104a23d02020201010404000201010b183016060e2b060104a23d02020201010402000404726f6f740b1a3018060e2b060104a23d02020201010403000406723066346a790b133011060c2b06010201450106040102010201040b133011060c2b06010201450106040103010201010b133011060c2b06010201450106040104010201020b133011060c2b06010201450106040105010201030b163014060c2b06010201450106040109014004647ef94b0b163014060c2b0601020145010604010a014004ffffffff0b143012060c2b0601020145010604010b01020201000b133011060c2b0601020145010604010e010201000b143012060c2b0601020145010604010f01020200a00b133011060c2b06010201450106040102020201040b133011060c2b06010201450106040103020201010b133011060c2b06010201450106040104020201020b133011060c2b06010201450106040105020201030b163014060c2b06010201450106040109024004000000000b163014060c2b0601020145010604010a024004000000000b143012060c2b0601020145010604010b02020201000b143012060c2b0601020145010604010e02020200a30b153013060c2b0601020145010604010f02020300ffff0b153013060b2b0601020145010201020f4004647ef94b0b153013060b2b0601020145010201030f4004ffffffff0b21301f060b2b0601020145010201040f0410626f524b616c69636e6f7769445641740b123010060b2b0601020145010201050f0201050b123010060b2b0601020145010201060f0401400b123010060b2b0601020145010201070f02010418230102069a060107070100080400040f10090400001f400a04000000000e021f400f0102191601021644060107070100080400040f100a040000000006106c2c2b5e3ebc5c927d638e125e6f45fa0710872540e0f06b0ae7a0d2abda0bc9e208ff0000"
    # assert False
