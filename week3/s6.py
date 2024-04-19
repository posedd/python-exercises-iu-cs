# Aşağıdaki verilen cümlerdeki sesli harflerin sessiz harflere oranını bulan
# fonksiyon yazınız.
# “Yapay Zeka ile ilgili en yalın tanımlardan biri şöyle; yapay zeka, bilgisayar sistemlerinin
# insan zekasını taklit etme yeteneğidir.”
# “Yapay zekanın ve akıllı makinelerin tarihi, eski Yunan mitolojisine kadar gitmektedir. “
# “Fakat alana dair ilk teorik çalışmalar 1950’deki Alan Turing’in Computing Machinery
# and Inteligence makalesiyle başlamıştır. “


def sesli_sessiz_oran():
    sesli_harf = "aeuio"
    sessiz_harf = "bcdprstvyz"
    sesli_count=0
    sessiz_count=0
    makale = "Yapay Zeka ile ilgili en yalin tanimlardan biri şöyle; yapay zeka, bilgisayar sistemlerinin insan zekasini taklit etme yeteneğidir".lower()
    for i in makale:
        if i in sesli_harf:
            sesli_count += 1
        elif i in sessiz_harf:
            sessiz_count += 1
    oran = sesli_count/sessiz_count
    print(f"Cumledeki sesli harflerin sessiz harflere orani {oran}'dir.")
sesli_sessiz_oran()

