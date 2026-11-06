import time
text = """
Wkh vroxwlrq wr wkh pbvwhub zdv klgghq lq d sodfh wkdw qr rqh kdyg hyhu wkrxjkw wr vhdufk. Hyhub pruqlqj, wkh rog surihvvru zdonhg wkurxjk wkh txlhw vwuhhwv ri wkh flwb dqg ylvlwhg wkh vpdoo oleudub qhdu wkh ulyhu. Kh kdyg vshqw pdqb bhduv vwxgblqj dqflhqw errnv, irujrwwhq odqjxdjhv, dqg vwudqjh vberov wkdw dsshduhg lq wkh pdujlqv ri rog pdqxvfulswv.

Rqh udlqb diwhuqrrq, d brb qdphg Wkrpdv hqwhuhg wkh oleudub fduublqj d pbvwhulrxv ohwwhu. Wkh ohwwhu kdyg ehhq irxqg lq d zrrghq era exulhg ehqhdwk dq rog rdn wuhh. Lqvlgh wkh hqyhorsh zdv d slhfh ri sdshu fryhuhg zlwk vhhplqjob udqgrp ohwwhuv. Wkrpdv kdyg wulhg wr uhdg wkh phvvdjh, exw qrwklqj pdgh vhqvh.

Wkh surihvvru hadplqhg wkh sdshu fduhixoob. Kh qrwlfhg wkdw vrph ohwwhuv dsshduhg pruh riwhq wkdq rwkhuv, dqg wkdw wkh vsdfhv ehwzhhq zrugv vhhphg wr iroorz wkh sdwwhuqv ri ruglqdub Hqjolvk. Diwhu vhyhudo plqxwhv, kh vplohg dqg dvnhg Wkrpdv wr eulqj klp d shqflo.

Wrjhwkhu, wkhb ehjdq wr zrun wkurxjk wkh phvvdjh. Wkhb zurwh grzq wkh doskdehw dqg frpsduhg hdfk ohwwhu zlwk wkh rqh wkdw dsshduhg lq wkh whaw. Vrrq, wkh iluvw zrug ehjdq wr pdnh vhqvh, dqg wkh vhfrqg iroorzhg txlfnob. Wkrpdv frxog kdugob eholhyh krz vlpsoh wkh vhfuhw kdyg ehhq doo dorqj.

Exw wkh ghfrghg phvvdjh zdv rqob wkh ehjlqqlqj. Lw ghvfulehg d klgghq grru ehqhdwk wkh rog forfn wrzhu, d qduur z vwdufdvh, dqg d ur rp wkdw kdyg qrw ehhq rshqhg iru pruh wkdq d kxqguhg bhduv. Wkh surihvvru zd uqhg Wkrpdv wkdw vrph vhfuhwv zhuh ehwwhu ohiw xqglvfryhuhg, exw wkh brb zdv do uhdgb ghwhuplqhg wr ilqg rxw zkdw odl ehklqg wkh grru.

Wkdw hyhqlqj, dv wkh odvw vxqoljkw glvdsshduhg ehklqg wkh urriv, wkhb phw dw wkh edvh ri wkh forfn wrzhu. Wkh dlu zdv frog, dqg wkh vwuhhwv zhuh doprvw hpswb. Wkh surihvvru fduulhg d odqwhuq, zkl oh Wkrpdv khog wkh rog ohwwhu wljkwob lq klv kdqg. Wkhb irxqg d uxvwhg lurq grru klgghq ehklqg d khdyb fxuwdlq ri lyb.

Zlwk d orxg fuhdn, wkh grru rz hqhg. Ehbrqg lw vwuhwfkhg d orqj sdvvdjh il oohg zlwk gxvw dqg frezhev. Wkhlu irrwvwhsv hfkrhg djdlqvw wkh vwrqh zdoov dv wkhb pryhg g hhshu lqwr wkh g dunqhvv. Dw wkh hqg ri wkh sdvvdjh, wkhb glvfryhuhg d vpdoo fkdp ehu zlwk d vlqjoh zrrghq fkhvw lq wkh fhqwhu.

Wkh fkhvw zdv orfnhg, exw rq lwv olg zdv dqrwkhu hqfubswhg phvvdjh. Wkrpdv odxjkhg, iru kh qrz xqghuvwrrg wkh wulfn. Kh wrrn rxw klv qrwherrn dqg ehjdq wr ghfrgh wkh zrugv, rqh ohwwhu dw d wlph. Dv kh uhdg wkh ilqdo vhqwhqfh, klv hadlw hphu jhg lqwr d juld.

Wkh surihvvru orrnhg dw klp zlwk fxulrvlwb. Zkdw grhv lw vdb, kh dvnhg. Wkrpdv wxuqhg wkh sdshu durxqg dqg vkrzhg klp wkh dqvzhu. Wkh vhfuhw zdv qrw d wuhdvxuh ri jrog ru vl oyhu, exw vrphwklqj idu pruh ydoxdeoh. Lw zdv d froohfwlrq ri nqrzohgjh, sdwlhqwob suhvhuyhg iru ixwxuh jhqhudwlrqv.

Dqg vr, zkdw kdyg ehjxq dv d vlpsoh sxccoh ehfdph wkh iluvw fkd swhu ri d idu judqghu dgyhqwxuh.
"""

pocty = [0] * 26
abeceda = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(text)):
    if text[i] in abeceda:
        pozice = abeceda.index(text[i])
        pocty[pozice] += 1

print(pocty)