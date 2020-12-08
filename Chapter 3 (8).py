n = 18
saus_pack = 10
bun_pack = 8
saus_pack_need = n//saus_pack
bun_pack_need = n//bun_pack
saus_packs_rest = float(n%10)
bun_packs_rest = float(n%8)
if saus_packs_rest !=0:
    saus_pack_need +=1
else: saus_pack_need = n//10
if bun_packs_rest !=0:
    bun_pack_need +=1
else: bun_pack_need = n//8
rest_saus = (saus_pack_need*saus_pack)-n
rest_bun = (bun_pack_need*bun_pack)-n
print("Необходимое количество упаковок сосисок: ", saus_pack_need)
print("Необходимое количество упаковок булочек: ", bun_pack_need)
print("Остаток сосисок, шт: ", rest_saus)
print("Остаток булочек, шт: ", rest_bun)