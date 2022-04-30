# test1=input("Muellimsinizse 1 yazin!")  (QuizYarat)
# test2=input("Telebesinizse 2 yazin!") (QuizHellEt)
suallar=[
    {
        "sualinMetni":"Python öyrənə bilirsən mi?",
        "cavablar":[
        "Deyəsən",
        "Hə amma çox çətindi",
        "O nə olan şeydi",
        "Tam mənlikdir"
        ],
    "duzgunCavab":"C"
},
        {
        "sualinMetni":"5*2=?",
        "cavablar":[
        "11",
        "4",
        "8",
        "10"
        ],
    "duzgunCavab":"D"
},
        {
        "sualinMetni":"14+7=?",
        "cavablar":[
        "20",
        "21",
        "14",
        "22"
        ],
    "duzgunCavab":"B"
}
]
questionum=1
for sual in suallar:
    quiz=f"""
    {questionum}. {sual["sualinMetni"]}
            A) {sual["cavablar"][0]}
            B) {sual["cavablar"][1]}
            C) {sual["cavablar"][2]}
            D) {sual["cavablar"][3]}
    """
    print(quiz)
    cavab=input("Cavabinizi daxil edin: ")
    questionum+=1
    # if cavab==sual["duzgunCavab"]:
    #     print("Tebrikler!")
    # else:
    #     print("Yanlish cavab!")

# def QuizYarat():
#     # verilən sual formatına uyğun olaraq istifadəçidən sual detallarının alınması
#     # alinan detallara uyğun olaraq sual yaradılması
#     # yaradılan sualın suallar listinə əlavə edilməsi

#     pass
# def QuiziHellet():
#     # QuizYarat() funksiyası ilə yaradılmış sualların tək tək ekranda görünməsini təmin etmək
#     # Hər sualın cavabının daxil edilməsini təmin etmək
#     # Düzgün cavabın balı 10 Baldır
#     # Ümumi balın hesablanması tələb olunur
#     # Bütün suallar bitdikdən sonra quizin nəticələri aşağıdakı mətn formatında göstəriləcək
#     # "Sizin quiz nəticələri Düz Cavab Sayı : 10, Səhv Cavab Sayı : 3, Ümumi Əldə Edilən Nəticə : 100"
#     pass