# parametr olaraq daxil edilən list içərisində təkrarlanan ədədləri və hər ədəddən neçə ədəd olduğunu ekrana çap edin
# ededler=[23,56,890,12,45,123,67,23,34,12]
# ls={}
# def tekralananEdedleriTap(ls):
#     for i in ededler:
#         if ededler.count(i)>1:
#             ls[i]=ededler.count(i)
#     print(ls)
# tekralananEdedleriTap(ls)

# ededler=[23,56,890,12,45,123,67,23,34,12]
# def xususiEdedlerinCemi(ls,reqemSayi):
#     # parametr olaraq daxil edilən list içərisində yenə parametr olaraq verilən rəqəm sayına uyğun ədədlərin cəmini ekrana çap edin
#     # reqemSayi=2 daxil edilirsə 2 rəqəmli ədədlərin cəmini tapmalıdır
#     pass


#ededler=[23,56,890,12,45,123,67,23,34,12]
# def ədədDaxilindəkiRəqəmiTap(ls,reqem):
#     # parametr olaraq daxil edilən list içərisindəki elementlərin içərisində yenə parametr olaraq verilən rəqəm olan ədədləri ekrana çap edin
#     pass

#ededler=[23,56,890,12,45,123,67,23,34,12]
# def enBoyukNEded(ls,n):
#     # parametr olaraq daxil edilən list içərisindəki elementlərin daxil edilən n parametri qədər olan ən böyük ədədləri ekrana çap edin
#     pass

def sum_of_list(l,n):
    if n == 0:
        return l[n]
    return l[n] + sum_of_list(l,n-1)

my_list = [1,3,5,2,4]
print("The sum of my_list is", sum_of_list(my_list,len(my_list)-1))